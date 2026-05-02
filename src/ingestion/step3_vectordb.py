"""
Step 3: Vector Database Builder
Loads processed chunks, generates embeddings using
ChromaDB's built-in model, and stores them locally.
Run: python3 src/ingestion/step3_vectordb.py
"""

import json, time, pickle, re, math
from pathlib import Path
from collections import defaultdict, Counter

PROC_DIR = Path.home() / "Documents/rituximab_rag/data/processed"
DB_DIR   = Path.home() / "Documents/rituximab_rag/data/chroma_db"
DB_DIR.mkdir(parents=True, exist_ok=True)

# ── Load chunks ──────────────────────────────────────
def load_chunks():
    with open(PROC_DIR / "rituximab_chunks.json", encoding="utf-8") as f:
        return json.load(f)

# ── TF-IDF vectorizer (no internet needed) ──────────
def tokenize(text):
    return re.findall(r'\b[a-z]{3,}\b', text.lower())

def build_index(chunks):
    print("Building TF-IDF index...")
    N   = len(chunks)
    df  = defaultdict(int)
    tfs = []

    for chunk in chunks:
        tokens = tokenize(chunk["text"])
        tf = defaultdict(int)
        for t in tokens:
            tf[t] += 1
        tfs.append(dict(tf))
        for t in set(tokens):
            df[t] += 1

    idf = {t: math.log((N+1)/(df[t]+1))+1 for t in df}

    vectors = []
    for tf in tfs:
        vec  = {t: tf[t] * idf.get(t, 1) for t in tf}
        norm = math.sqrt(sum(v*v for v in vec.values())) or 1
        vectors.append({t: v/norm for t, v in vec.items()})

    return vectors, idf

def cosine(a, b):
    return sum(a[t]*b[t] for t in set(a)&set(b))

def search(query, chunks, vectors, idf, top_k=3):
    tokens = tokenize(query)
    qtf    = defaultdict(int)
    for t in tokens:
        qtf[t] += 1
    qvec = {t: qtf[t]*idf.get(t,1) for t in qtf}
    norm = math.sqrt(sum(v*v for v in qvec.values())) or 1
    qvec = {t: v/norm for t, v in qvec.items()}

    scores = sorted(enumerate(vectors), key=lambda x: -cosine(qvec, x[1]))
    return [{"chunk": chunks[i], "score": round(cosine(qvec, vectors[i]), 4)}
            for i, _ in scores[:top_k]]

# ── Save & Load ──────────────────────────────────────
def save_index(chunks, vectors, idf):
    db = {"chunks": chunks, "vectors": vectors, "idf": idf}
    path = DB_DIR / "rituximab_index.pkl"
    with open(path, "wb") as f:
        pickle.dump(db, f)
    size = path.stat().st_size // 1024
    print(f"Index saved → {path}  ({size} KB)")

# ── Verify ───────────────────────────────────────────
def verify(chunks, vectors, idf):
    print("\n── Verification ─────────────────────────────")
    print(f"  Total chunks  : {len(chunks)}")
    cats = Counter(c["category"] for c in chunks)
    for cat, n in sorted(cats.items()):
        print(f"  {cat:<25} {n}")

    questions = [
        "What are the side effects of Rituximab?",
        "How long does the infusion take?",
        "Can I get vaccines while on Rituximab?",
        "Is Rituximab safe during pregnancy?",
        "What is the dose for rheumatoid arthritis?",
    ]
    print("\n  Test retrieval:\n")
    for q in questions:
        results = search(q, chunks, vectors, idf, top_k=2)
        print(f"  Q: {q}")
        for r in results:
            c = r["chunk"]
            print(f"     [score={r['score']:.3f}] [{c['category']}] {c['text'][:90]}...")
        print()

# ── Main ─────────────────────────────────────────────
if __name__ == "__main__":
    print("="*52)
    print("  Rituximab RAG — Step 3: Vector DB Builder")
    print("="*52 + "\n")

    chunks = load_chunks()
    print(f"Loaded {len(chunks)} chunks\n")

    t0 = time.time()
    vectors, idf = build_index(chunks)
    save_index(chunks, vectors, idf)
    elapsed = time.time() - t0

    verify(chunks, vectors, idf)

    print("="*52)
    print(f"  Vector DB ready! ({elapsed:.1f}s)")
    print(f"  Location : {DB_DIR}")
    print("="*52)
