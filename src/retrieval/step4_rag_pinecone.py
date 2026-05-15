
import os,re,math,pickle
from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()
DB_DIR=Path.home()/"Documents/rituximab_rag/data/chroma_db"
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY","")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","")
ANTHROPIC_KEY=os.getenv("ANTHROPIC_API_KEY","")
AI_PROVIDER=os.getenv("AI_PROVIDER","openai")
OPENAI_MODEL=os.getenv("OPENAI_MODEL","gpt-4o-mini")
ANTHROPIC_MODEL=os.getenv("ANTHROPIC_MODEL","claude-haiku-4-5-20251001")
EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL","text-embedding-3-small")
INDEX_NAME=os.getenv("PINECONE_INDEX_NAME","rituximab-rag")
NAMESPACE=os.getenv("PINECONE_NAMESPACE","rituximab")
TOP_K=int(os.getenv("TOP_K_RESULTS","5"))
DISCLAIMER="\n\n Educational only. Always consult your doctor."
SCOPE_KEYWORDS=["rituximab","rituxan","infusion","cd20","lymphoma","leukemia",
    "rheumatoid","arthritis","side effect","dose","dosage","vaccine","pregnancy",
    "hepatitis","pml","nhl","cll","treatment","therapy","biologic","monoclonal",
    "cancer","autoimmune","immune","reaction","fever","infection","fatigue","swelling"]
SYSTEM_PROMPT=("You are a compassionate medical assistant specialising in Rituximab therapy.\n"
    "Answer ONLY using the sources below. Use plain patient-friendly language.\n"
    "Never diagnose. Cite your source. For serious symptoms advise contacting doctor.")

def load_index():
    has_pc=bool(PINECONE_API_KEY and "your_" not in PINECONE_API_KEY)
    has_oai=bool(OPENAI_API_KEY and "your_" not in OPENAI_API_KEY)
    if has_pc and has_oai:
        try:
            from pinecone import Pinecone
            pc=Pinecone(api_key=PINECONE_API_KEY)
            index=pc.Index(INDEX_NAME)
            count=index.describe_index_stats().get("total_vector_count",0)
            print(f"  Pinecone connected - {count} vectors in '{INDEX_NAME}'")
            return {"type":"pinecone","index":index}
        except Exception as e:
            print(f"  Pinecone failed: {e} - using TF-IDF")
    pkl=DB_DIR/"rituximab_index.pkl"
    if pkl.exists():
        import pickle
        with open(pkl,"rb") as f: db=pickle.load(f)
        print(f"  TF-IDF loaded - {len(db['chunks'])} chunks")
        return db
    raise FileNotFoundError("No index found. Run step3_pinecone.py first.")

def is_in_scope(q): return any(kw in q.lower() for kw in SCOPE_KEYWORDS)

def process_query(q):
    q=re.sub(r'\bra\b','rheumatoid arthritis',q,flags=re.I)
    q=re.sub(r'\bnhl\b','non hodgkin lymphoma',q,flags=re.I)
    q=re.sub(r'\bcll\b','chronic lymphocytic leukemia',q,flags=re.I)
    return q.strip()

def embed_query(text):
    from openai import OpenAI
    return OpenAI(api_key=OPENAI_API_KEY).embeddings.create(
        model=EMBEDDING_MODEL,input=[text]).data[0].embedding

def retrieve(query,idx_obj):
    results=[]
    if idx_obj["type"]=="pinecone":
        q_vec=embed_query(query)
        res=idx_obj["index"].query(vector=q_vec,top_k=TOP_K+3,
                                    include_metadata=True,namespace=NAMESPACE)
        seen=defaultdict(int)
        for m in res.matches:
            src=m.metadata.get("source","")
            if seen[src]<2:
                results.append({"text":m.metadata.get("text",""),"source":src,
                                 "category":m.metadata.get("category",""),"score":round(m.score,4)})
                seen[src]+=1
            if len(results)>=TOP_K: break
    else:
        chunks,vectors,idf=idx_obj["chunks"],idx_obj["vectors"],idx_obj["idf"]
        tokens=re.findall(r'\b[a-z]{3,}\b',query.lower())
        qtf=defaultdict(int)
        for t in tokens: qtf[t]+=1
        qvec={t:qtf[t]*idf.get(t,1) for t in qtf}
        norm=math.sqrt(sum(v*v for v in qvec.values())) or 1
        qvec={t:v/norm for t,v in qvec.items()}
        scores=sorted([(sum(qvec.get(t,0)*vec.get(t,0) for t in qvec),i)
                       for i,vec in enumerate(vectors)],reverse=True)
        seen=defaultdict(int)
        for score,idx in scores:
            c=chunks[idx]
            if seen[c["source"]]<2:
                results.append({"text":c["text"],"source":c["source"],
                                 "category":c["category"],"score":round(score,4)})
                seen[c["source"]]+=1
            if len(results)>=TOP_K: break
    return results

def build_prompt(query,retrieved):
    ctx="\n\n".join([f"[SOURCE {i+1}: {r['source']} | {r['category']}]\n{r['text']}"
                      for i,r in enumerate(retrieved)])
    return f"{SYSTEM_PROMPT}\n\nSOURCES:\n{ctx}\n\nPATIENT QUESTION:\n{query}\n\nANSWER:"

def generate_openai(prompt):
    try:
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT","")
        azure_key=os.getenv("AZURE_OPENAI_KEY","")
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT","gpt-4o")
        if azure_endpoint and azure_key:
            from openai import AzureOpenAI
            r=AzureOpenAI(
                azure_endpoint=azure_endpoint,
                api_key=azure_key,
                api_version="2024-08-01-preview"
            ).chat.completions.create(
                model=azure_deployment,
                messages=[{"role":"user","content":prompt}],
                temperature=0.3,max_tokens=600)
        else:
            from openai import OpenAI
            r=OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
                model=OPENAI_MODEL,messages=[{"role":"user","content":prompt}],
                temperature=0.3,max_tokens=600)
        return r.choices[0].message.content,azure_deployment if azure_endpoint else OPENAI_MODEL
    except Exception as e: return None,str(e)

def generate_anthropic(prompt):
    try:
        import anthropic
        r=anthropic.Anthropic(api_key=ANTHROPIC_KEY).messages.create(
            model=ANTHROPIC_MODEL,max_tokens=600,
            messages=[{"role":"user","content":prompt}])
        return r.content[0].text,ANTHROPIC_MODEL
    except Exception as e: return None,str(e)

def generate_fallback(retrieved):
    if not retrieved: return "No info found. Please consult your doctor.","local"
    priority=["fda_label","patient_education","clinical_guidelines","research_abstracts"]
    by_cat=defaultdict(list)
    for r in retrieved: by_cat[r["category"]].append(r["text"])
    parts=[]
    for cat in priority:
        if cat in by_cat:
            sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+',by_cat[cat][0]) if len(s.strip())>40]
            if sents: parts.append(" ".join(sents[:3]))
            if len(parts)>=2: break
    answer="\n\n".join(parts) if parts else retrieved[0]["text"][:400]
    sources=", ".join({r["source"] for r in retrieved})
    return answer+f"\n\n Sources: {sources}","local-tfidf"

def generate_answer(prompt,retrieved):
    answer=None
    if AI_PROVIDER=="anthropic" and ANTHROPIC_KEY and "your_" not in ANTHROPIC_KEY:
        answer,model=generate_anthropic(prompt)
    elif OPENAI_API_KEY and "your_" not in OPENAI_API_KEY:
        answer,model=generate_openai(prompt)
    else: model="local"
    if answer is None: answer,model=generate_fallback(retrieved)
    return answer,model

def ask(query,idx_obj):
    result={"query":query,"in_scope":True,"answer":"","sources":[],
            "model":"","score":0,"db_type":idx_obj.get("type","tfidf")}
    if not is_in_scope(query):
        result["in_scope"]=False
        result["answer"]="I specialise in Rituximab therapy only. Please consult your doctor."
        return result
    processed=process_query(query)
    retrieved=retrieve(processed,idx_obj)
    if not retrieved:
        result["answer"]="No relevant info found. Please ask your doctor."
        return result
    prompt=build_prompt(processed,retrieved)
    answer,model=generate_answer(prompt,retrieved)
    result["answer"]=answer+DISCLAIMER
    result["sources"]=list({r["source"] for r in retrieved})
    result["model"]=model
    result["score"]=retrieved[0]["score"] if retrieved else 0
    return result

if __name__=="__main__":
    print("="*56)
    print("  Step 4: RAG Pipeline (Pinecone Edition)")
    print("="*56+"\n")
    print("Loading index...",end="",flush=True)
    idx_obj=load_index()
    print()
    questions=["What are the side effects of Rituximab?",
               "How long does a Rituximab infusion take?",
               "Can I get a flu vaccine while on Rituximab?",
               "Is Rituximab safe during pregnancy?",
               "What is the RA dose?","Can I eat pizza?"]
    for q in questions:
        print(f"\n{'-'*56}\nQ: {q}\n")
        r=ask(q,idx_obj)
        if not r["in_scope"]:
            print(f"[OUT OF SCOPE] {r['answer']}")
        else:
            print(f"A: {r['answer'][:280]}...")
            print(f"\n   DB: {r['db_type']} | Model: {r['model']} | Score: {r['score']:.3f}")
    print(f"\n{'='*56}\n  Pinecone RAG Pipeline working!\n{'='*56}")
