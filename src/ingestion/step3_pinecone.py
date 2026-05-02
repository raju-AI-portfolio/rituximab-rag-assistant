
import os,json,time,pickle,re,math
from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()
PROC_DIR=Path.home()/"Documents/rituximab_rag/data/processed"
DB_DIR=Path.home()/"Documents/rituximab_rag/data/chroma_db"
DB_DIR.mkdir(parents=True,exist_ok=True)
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY","")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","")
EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL","text-embedding-3-small")
EMBEDDING_DIM=1536
INDEX_NAME=os.getenv("PINECONE_INDEX_NAME","rituximab-rag")
NAMESPACE=os.getenv("PINECONE_NAMESPACE","rituximab")
BATCH_SIZE=50

def load_chunks():
    with open(PROC_DIR/"rituximab_chunks.json",encoding="utf-8") as f:
        return json.load(f)

def get_embeddings(texts):
    from openai import OpenAI
    r=OpenAI(api_key=OPENAI_API_KEY).embeddings.create(model=EMBEDDING_MODEL,input=texts)
    return [item.embedding for item in r.data]

def get_or_create_index(pc):
    from pinecone import ServerlessSpec
    existing=[idx.name for idx in pc.list_indexes()]
    if INDEX_NAME in existing:
        print(f"  Index '{INDEX_NAME}' exists - connecting...")
        return pc.Index(INDEX_NAME)
    print(f"  Creating index '{INDEX_NAME}' (dim=1536, AWS us-east-1)...")
    pc.create_index(name=INDEX_NAME,dimension=EMBEDDING_DIM,metric="cosine",
                    spec=ServerlessSpec(cloud="aws",region="us-east-1"))
    print("  Waiting",end="",flush=True)
    for _ in range(30):
        if pc.describe_index(INDEX_NAME).status.get("ready",False): break
        print(".",end="",flush=True); time.sleep(2)
    print(" ready!")
    return pc.Index(INDEX_NAME)

def upsert_chunks(index,chunks):
    total,added=len(chunks),0
    for i in range(0,total,BATCH_SIZE):
        batch=chunks[i:i+BATCH_SIZE]
        embs=get_embeddings([c["text"] for c in batch])
        vecs=[{"id":c["chunk_id"],"values":e,
               "metadata":{"text":c["text"][:1000],"source":c["source"],
                           "category":c["category"],"chunk_index":c["chunk_index"]}}
              for c,e in zip(batch,embs)]
        index.upsert(vectors=vecs,namespace=NAMESPACE)
        added+=len(batch)
        bar="\u2588"*(added*20//total)+"\u2591"*(20-added*20//total)
        print(f"\r  Upserting [{bar}] {added}/{total}",end="",flush=True)
        time.sleep(0.3)
    print(f"\n\n  Upserted {added} vectors to '{INDEX_NAME}'")

def verify(index):
    stats=index.describe_index_stats()
    print(f"\n  Vectors: {stats.get('total_vector_count',0)}")
    qs=["What are the side effects of Rituximab?",
        "Can I get a flu vaccine while on Rituximab?",
        "What is the dose for rheumatoid arthritis?"]
    print("\n  Test retrieval:\n")
    for q in qs:
        res=index.query(vector=get_embeddings([q])[0],top_k=2,
                       include_metadata=True,namespace=NAMESPACE)
        print(f"  Q: {q}")
        for m in res.matches:
            print(f"     [score={m.score:.3f}] [{m.metadata.get('category','')}] {m.metadata.get('text','')[:80]}...")
        print()

def build_tfidf(chunks):
    print("Building TF-IDF fallback...")
    N,df,tfs=len(chunks),defaultdict(int),[]
    for c in chunks:
        tokens=re.findall(r'\b[a-z]{3,}\b',c["text"].lower())
        tf=defaultdict(int)
        for t in tokens: tf[t]+=1
        tfs.append(dict(tf))
        for t in set(tokens): df[t]+=1
    idf={t:math.log((N+1)/(df[t]+1))+1 for t in df}
    vectors=[]
    for tf in tfs:
        vec={t:tf[t]*idf.get(t,1) for t in tf}
        norm=math.sqrt(sum(v*v for v in vec.values())) or 1
        vectors.append({t:v/norm for t,v in vec.items()})
    db={"chunks":chunks,"vectors":vectors,"idf":idf,"type":"tfidf"}
    out=DB_DIR/"rituximab_index.pkl"
    with open(out,"wb") as f: pickle.dump(db,f)
    print(f"  TF-IDF saved ({out.stat().st_size//1024} KB)")

if __name__=="__main__":
    print("="*56)
    print("  Step 3: Pinecone Vector DB Builder")
    print("="*56+"\n")
    chunks=load_chunks()
    has_pc=bool(PINECONE_API_KEY and "your_" not in PINECONE_API_KEY)
    has_oai=bool(OPENAI_API_KEY and "your_" not in OPENAI_API_KEY)
    print(f"Loaded {len(chunks)} chunks")
    print(f"Pinecone : {'OK' if has_pc else 'MISSING - add to .env'}")
    print(f"OpenAI   : {'OK' if has_oai else 'MISSING - add to .env'}\n")
    if has_pc and has_oai:
        from pinecone import Pinecone
        pc=Pinecone(api_key=PINECONE_API_KEY)
        index=get_or_create_index(pc)
        t0=time.time()
        upsert_chunks(index,chunks)
        verify(index)
        print(f"\n  Done in {time.time()-t0:.1f}s | Index: {INDEX_NAME}")
    else:
        print("Missing keys - building TF-IDF fallback\n")
        build_tfidf(chunks)
