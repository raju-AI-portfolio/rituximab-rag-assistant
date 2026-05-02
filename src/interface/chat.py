import pickle, re, math, json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

DB_PATH  = Path.home() / "Documents/rituximab_rag/data/chroma_db/rituximab_index.pkl"
LOG_PATH = Path.home() / "Documents/rituximab_rag/data/chat_history.json"

DISCLAIMER = "\n⚠️  Educational only. Always consult your doctor."

SCOPE_KEYWORDS = [
    "rituximab","rituxan","infusion","cd20","lymphoma","leukemia",
    "rheumatoid","arthritis","side effect","dose","dosage","vaccine",
    "pregnancy","hepatitis","pml","nhl","cll","treatment","therapy",
    "cancer","autoimmune","immune","reaction","fever","infection",
    "fatigue","nausea","pain","swelling","biologic","monoclonal"
]

def load_index():
    with open(DB_PATH,"rb") as f:
        db = pickle.load(f)
    return db["chunks"], db["vectors"], db["idf"]

def tokenize(text):
    return re.findall(r'\b[a-z]{3,}\b', text.lower())

def cosine(a, b):
    return sum(a[t]*b[t] for t in set(a)&set(b))

def retrieve(query, chunks, vectors, idf, top_k=5):
    tokens = tokenize(query)
    qtf = defaultdict(int)
    for t in tokens: qtf[t] += 1
    qvec = {t: qtf[t]*idf.get(t,1) for t in qtf}
    norm = math.sqrt(sum(v*v for v in qvec.values())) or 1
    qvec = {t: v/norm for t, v in qvec.items()}
    scores = sorted([(cosine(qvec,vec),i) for i,vec in enumerate(vectors)], reverse=True)
    results, seen = [], defaultdict(int)
    for score, idx in scores:
        src = chunks[idx]["source"]
        if seen[src] < 2:
            results.append({"chunk": chunks[idx], "score": round(score,4)})
            seen[src] += 1
        if len(results) >= top_k: break
    return results

def is_in_scope(query):
    return any(kw in query.lower() for kw in SCOPE_KEYWORDS)

def process_query(q):
    q = re.sub(r'\bra\b',  'rheumatoid arthritis', q, flags=re.I)
    q = re.sub(r'\bnhl\b', 'non hodgkin lymphoma',  q, flags=re.I)
    q = re.sub(r'\bcll\b', 'chronic lymphocytic leukemia', q, flags=re.I)
    return q.strip()

def build_answer(query, retrieved):
    if not retrieved:
        return "No information found. Please consult your doctor."

    by_cat = defaultdict(list)
    for r in retrieved:
        by_cat[r["chunk"]["category"]].append(r["chunk"]["text"])

    priority = ["fda_label","patient_education","clinical_guidelines",
                "research_abstracts","clinical_trials","adverse_events"]
    parts = []
    for cat in priority:
        if cat in by_cat:
            text = by_cat[cat][0]
            sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.strip()) > 40]
            if sents:
                parts.append(" ".join(sents[:3]))
            if len(parts) >= 2: break

    answer = "\n\n".join(parts) if parts else retrieved[0]["chunk"]["text"][:400]

    sources = set()
    for r in retrieved:
        s = r["chunk"]["source"]
        if "FDA" in s or "fda" in s:     sources.add("FDA Label")
        elif "medline" in s.lower():      sources.add("MedlinePlus")
        elif "nccn" in s.lower():         sources.add("NCCN Guidelines")
        elif "pubmed" in s.lower():       sources.add("PubMed")
        elif "trial" in s.lower():        sources.add("ClinicalTrials.gov")
        elif "adverse" in s.lower():      sources.add("FDA Adverse Events")

    answer += f"\n\n📚 Sources: {', '.join(sources)}"
    answer += DISCLAIMER
    return answer

def save_log(history):
    with open(LOG_PATH,"w") as f:
        json.dump(history, f, indent=2)

def banner():
    print("\n" + "="*58)
    print("  🧬  Rituximab Patient Knowledge Assistant")
    print("  Powered by RAG  |  FDA · NIH · NCCN · PubMed")
    print("="*58)
    print("  Type your question and press Enter.")
    print("  Commands: help | history | quit")
    print("="*58 + "\n")

def chat():
    banner()
    print("  Loading knowledge base...", end="", flush=True)
    chunks, vectors, idf = load_index()
    print(f" done ({len(chunks)} chunks)\n")

    history = []

    while True:
        try:
            user = input("You: ").strip()
            if not user: continue

            if user.lower() in ("quit","exit","bye"):
                save_log(history)
                print("\n  Goodbye! Stay well 💙\n")
                break

            if user.lower() == "help":
                print("""
  Example questions:
  • What are the side effects of Rituximab?
  • How long does the infusion take?
  • Can I get a flu vaccine while on Rituximab?
  • Is Rituximab safe during pregnancy?
  • What is the dose for rheumatoid arthritis?
  • What should I do if I get a fever?
  • What is PML?
  • Can I drink alcohol on Rituximab?
""")
                continue

            if user.lower() == "history":
                if not history:
                    print("  No questions yet.\n")
                else:
                    print(f"\n  Last {min(5,len(history))} questions:")
                    for i,h in enumerate(history[-5:],1):
                        print(f"  {i}. [{h['time']}] {h['query']}")
                    print()
                continue

            if not is_in_scope(user):
                print("\n  I only answer questions about Rituximab therapy.")
                print("  For other topics please consult your doctor.\n")
                continue

            print("  Searching...", end="", flush=True)
            processed  = process_query(user)
            retrieved  = retrieve(processed, chunks, vectors, idf)
            answer     = build_answer(processed, retrieved)
            score      = retrieved[0]["score"] if retrieved else 0
            bar        = "█"*int(score*10) + "░"*(10-int(score*10))
            print(" done\n")

            print("┌─ Answer " + "─"*47)
            for line in answer.split("\n"):
                print("│ " + line)
            print("└" + "─"*56)
            print(f"  Confidence: [{bar}] {score:.0%}\n")

            history.append({
                "query": user,
                "time":  datetime.now().strftime("%H:%M"),
                "score": score
            })

        except KeyboardInterrupt:
            save_log(history)
            print("\n\n  Session saved. Goodbye! 💙\n")
            break

if __name__ == "__main__":
    chat()
