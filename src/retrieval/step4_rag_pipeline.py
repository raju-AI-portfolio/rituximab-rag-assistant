"""
Step 4: RAG Pipeline
─────────────────────
Query processor → Retriever → Prompt builder → Answer generator
Uses OpenAI GPT for generation (or falls back to a rule-based answer).
Run: python3 src/retrieval/step4_rag_pipeline.py
"""

import pickle, re, math, json, os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

DB_PATH = Path.home() / "Documents/rituximab_rag/data/chroma_db/rituximab_index.pkl"

DISCLAIMER = (
    "\n\n⚠️  This information is for educational purposes only and is "
    "not a substitute for professional medical advice. Always consult "
    "your doctor or healthcare provider."
)

# Scope guard — only answer Rituximab-related questions
SCOPE_KEYWORDS = [
    "rituximab","rituxan","truxima","ruxience","riabni",
    "infusion","cd20","lymphoma","leukemia","rheumatoid",
    "arthritis","side effect","dose","dosage","vaccine",
    "pregnancy","hepatitis","pml","b-cell","nhl","cll",
    "treatment","therapy","injection","biologic","monoclonal"
]

# ── Load index ────────────────────────────────────────
def load_index():
    with open(DB_PATH, "rb") as f:
        db = pickle.load(f)
    return db["chunks"], db["vectors"], db["idf"]

# ── Scope check ───────────────────────────────────────
def is_in_scope(query: str) -> bool:
    q = query.lower()
    return any(kw in q for kw in SCOPE_KEYWORDS)

# ── Query processor ───────────────────────────────────
def process_query(query: str) -> str:
    # Lowercase, strip extra spaces
    query = query.strip()
    # Expand common abbreviations
    query = re.sub(r'\bra\b',  'rheumatoid arthritis', query, flags=re.I)
    query = re.sub(r'\bnhl\b', 'non hodgkin lymphoma',  query, flags=re.I)
    query = re.sub(r'\bcll\b', 'chronic lymphocytic leukemia', query, flags=re.I)
    return query

# ── TF-IDF retriever ──────────────────────────────────
def tokenize(text):
    return re.findall(r'\b[a-z]{3,}\b', text.lower())

def cosine(a, b):
    return sum(a[t]*b[t] for t in set(a)&set(b))

def retrieve(query, chunks, vectors, idf, top_k=5):
    tokens = tokenize(query)
    qtf    = defaultdict(int)
    for t in tokens:
        qtf[t] += 1
    qvec = {t: qtf[t]*idf.get(t,1) for t in qtf}
    norm = math.sqrt(sum(v*v for v in qvec.values())) or 1
    qvec = {t: v/norm for t, v in qvec.items()}

    scores = sorted(
        [(cosine(qvec, vec), i) for i, vec in enumerate(vectors)],
        reverse=True
    )
    results = []
    seen_sources = defaultdict(int)
    for score, idx in scores:
        src = chunks[idx]["source"]
        # Max 2 chunks per source to ensure diversity
        if seen_sources[src] < 2:
            results.append({"chunk": chunks[idx], "score": round(score, 4)})
            seen_sources[src] += 1
        if len(results) >= top_k:
            break
    return results

# ── Prompt builder ────────────────────────────────────
def build_prompt(query: str, retrieved: list) -> str:
    context_parts = []
    for i, r in enumerate(retrieved, 1):
        c = r["chunk"]
        context_parts.append(
            f"[Source {i}: {c['source']} | {c['category']}]\n{c['text']}"
        )
    context = "\n\n".join(context_parts)

    prompt = f"""You are a knowledgeable and caring medical information assistant 
specializing in Rituximab (Rituxan) therapy. Your role is to help patients 
understand their treatment clearly and accurately.

Use ONLY the information from the sources below to answer the question.
If the answer is not in the sources, say "I don't have enough information 
on that — please ask your doctor."
Always be clear, compassionate, and easy to understand.
Always cite which source your answer comes from.

SOURCES:
{context}

PATIENT QUESTION:
{query}

ANSWER:"""
    return prompt

# ── Rule-based fallback generator (no API key needed) ─
def generate_answer_local(query: str, retrieved: list) -> str:
    if not retrieved:
        return "I could not find relevant information about that in my knowledge base. Please consult your doctor."

    # Combine top retrieved chunks into a structured answer
    top = retrieved[0]["chunk"]
    others = retrieved[1:]

    # Extract key sentences from top chunk
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', top["text"]) if len(s.strip()) > 30]
    answer_sentences = sentences[:4]  # Take top 4 sentences

    answer = " ".join(answer_sentences)

    # Add supporting info from other sources if available
    if others:
        supporting = others[0]["chunk"]["text"][:200].strip()
        answer += f"\n\nAdditionally: {supporting}..."

    # Add source citation
    sources_used = list({r["chunk"]["source"] for r in retrieved})
    answer += f"\n\n📚 Sources: {', '.join(sources_used)}"

    return answer

# ── OpenAI generator (if API key available) ───────────
def generate_answer_openai(prompt: str) -> str:
    try:
        import openai
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return None

# ── Main RAG function ─────────────────────────────────
def ask(query: str, chunks, vectors, idf, use_openai=False) -> dict:
    result = {
        "query":     query,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "in_scope":  True,
        "retrieved": [],
        "answer":    "",
        "sources":   []
    }

    # 1. Scope check
    if not is_in_scope(query):
        result["in_scope"] = False
        result["answer"]   = (
            "I'm specialized in Rituximab therapy information only. "
            "For other medical questions, please consult your doctor."
        )
        return result

    # 2. Process query
    processed = process_query(query)

    # 3. Retrieve top chunks
    retrieved = retrieve(processed, chunks, vectors, idf, top_k=5)
    result["retrieved"] = retrieved
    result["sources"]   = list({r["chunk"]["source"] for r in retrieved})

    # 4. Generate answer
    if use_openai and os.getenv("OPENAI_API_KEY"):
        prompt = build_prompt(processed, retrieved)
        answer = generate_answer_openai(prompt)
        if not answer:
            answer = generate_answer_local(processed, retrieved)
    else:
        answer = generate_answer_local(processed, retrieved)

    result["answer"] = answer + DISCLAIMER
    return result

# ── CLI test ──────────────────────────────────────────
if __name__ == "__main__":
    print("="*55)
    print("  Rituximab RAG — Step 4: RAG Pipeline Test")
    print("="*55 + "\n")

    chunks, vectors, idf = load_index()
    print(f"Index loaded: {len(chunks)} chunks\n")

    test_questions = [
        "What are the common side effects of Rituximab?",
        "How long does a Rituximab infusion take?",
        "Can I get a flu vaccine while on Rituximab?",
        "Is Rituximab safe to take during pregnancy?",
        "What is the dose of Rituximab for rheumatoid arthritis?",
        "Can I eat pizza?",   # Out of scope test
    ]

    for q in test_questions:
        print(f"{'─'*55}")
        print(f"Q: {q}\n")
        result = ask(q, chunks, vectors, idf)

        if not result["in_scope"]:
            print(f"[OUT OF SCOPE] {result['answer']}\n")
            continue

        print(f"A: {result['answer']}\n")
        print(f"   Top sources: {', '.join(result['sources'])}")
        print(f"   Retrieved  : {len(result['retrieved'])} chunks\n")

    print("="*55)
    print("  RAG Pipeline working! ✅")
    print("="*55)
