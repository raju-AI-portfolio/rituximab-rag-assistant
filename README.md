<div align="center">

# 🧬 Rituximab Patient Knowledge Assistant

### Phase 1 — Production Release

**AI-powered RAG system for Rituximab therapy patient education**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render.com-28a745?style=for-the-badge&logo=render&logoColor=white)](https://rituximab-rag-assistant.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pinecone](https://img.shields.io/badge/Pinecone-Serverless-000000?style=for-the-badge&logo=pinecone&logoColor=white)](https://pinecone.io)
[![OpenAI](https://img.shields.io/badge/GPT--4o--mini-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*Helping patients understand their Rituximab therapy — 24/7, grounded in FDA, NIH, NCCN and PubMed*

</div>

**Deployed on Render- live Demo: https://rituximab-rag-assistant.onrender.com/**
---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Phase 1 Upgrades](#-phase-1-upgrades)
- [How It Helps Patients](#-how-it-helps-patients)
- [Benefits to Organisations](#-benefits-to-organisations)
- [Architecture](#-architecture)
- [Knowledge Base](#-knowledge-base)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Deployment](#-deployment)
- [Test Results](#-test-results)
- [Roadmap](#-roadmap)
- [Resume Summary](#-resume-summary)

---

## 🔬 About the Project

Rituximab (Rituxan) is a biologic therapy prescribed to over **3 million patients worldwide** across:

| Condition | Global Patients |
|-----------|----------------|
| Non-Hodgkin Lymphoma (NHL) | ~500,000 active |
| Chronic Lymphocytic Leukemia (CLL) | ~200,000 active |
| Rheumatoid Arthritis (RA) | ~1.3M (US alone) |
| Multiple Sclerosis (MS) | ~200,000 active |
| Lupus / GPA / MPA | ~300,000 combined |

Despite its widespread use, patients face a critical information gap — complex therapy, lengthy infusions, serious safety warnings, and limited access to their care team after hours. This project solves that with a production-grade **RAG (Retrieval-Augmented Generation)** assistant that answers patient questions grounded exclusively in verified medical sources.

---

## 🚀 Phase 1 Upgrades

Phase 1 is a complete architectural upgrade from the original prototype:

| Component | Before (Prototype) | After (Phase 1) |
|-----------|-------------------|-----------------|
| Vector DB | TF-IDF pickle file (1.2MB local) | **Pinecone Serverless** cloud index |
| Embeddings | Bag-of-words keyword matching | **OpenAI text-embedding-3-small** (1536-dim) |
| Storage | Local `.pkl` file on disk | **Pinecone AWS us-east-1** — fully managed |
| LLM generation | Rule-based text extraction | **GPT-4o-mini** natural language generation |
| Answer quality | Fragment extraction | Structured, cited, patient-friendly answers |
| Web UI | Desktop-only fixed layout | **Mobile-responsive** with slide-out drawer |
| Model switcher | Not available | GPT-4 / Claude / Local toggle in browser UI |
| Retrieval | Lexical keyword overlap | **Semantic cosine similarity** (dense vectors) |
| Scalability | RAM-limited local | **Serverless auto-scaling** in Pinecone cloud |

---

## 💊 How It Helps Patients

### The problem

Patients on Rituximab therapy face real daily challenges:

| Challenge | Impact |
|-----------|--------|
| ❌ Can't reach care team after hours | Anxiety, delayed reporting of serious symptoms |
| ❌ Unreliable internet health information | Risk of dangerous misinformation |
| ❌ Complex medical jargon in package inserts | Patients cannot understand their own treatment |
| ❌ Fear of infusion reactions | Treatment avoidance, non-adherence |
| ❌ Uncertainty about drug interactions and vaccines | Potentially dangerous decisions |

### How this assistant solves it

✅ **24/7 availability** — answers from any device, any time, day or night

✅ **Source-verified answers** — every response retrieved from FDA labels, NIH, and clinical guidelines — never generated from AI memory

✅ **Plain language** — GPT-4o-mini rewrites complex medical text into clear patient-friendly answers

✅ **Covers 75+ patient questions** across 8 categories:

```
💊 Treatment basics       ⚠️  Side effects
🏥 Infusion process       🛡️  Safety & risks
📊 Monitoring             🌿 Lifestyle
🔄 Alternatives           💙 Emotional & practical
```

✅ **Scope filtering** — only answers Rituximab-related questions, blocking off-topic medical advice

✅ **Source citations** — every answer shows exactly which document it came from

✅ **Medical disclaimer** — every response includes a reminder to consult their doctor

### Real patient questions it answers

```
What are the side effects of Rituximab?
How long does my infusion take?
Can I get a flu vaccine while on Rituximab?
Is Rituximab safe during pregnancy?
What is PML and should I be worried?
What should I do if I get a fever?
Can I drink alcohol during treatment?
How will I know if it is working?
What is the dose for rheumatoid arthritis?
```

---

## 🏥 Benefits to Organisations

### Hospitals and cancer centres

| Benefit | Detail |
|---------|--------|
| 📉 Reduced call volume | Routine patient questions handled automatically 24/7 |
| 📈 Improved patient satisfaction | Patients feel supported between appointments |
| 🔒 Reduced liability | All answers from FDA-approved labeling with mandatory disclaimers |
| ⏱️ Clinical staff efficiency | Frees nurses from routine information queries |

### Pharmaceutical companies

| Benefit | Detail |
|---------|--------|
| 💊 Medication adherence | Informed patients complete full treatment courses |
| 📊 Real-world evidence | Query analytics reveal patient education gaps |
| 🤝 Patient support programs | White-label licensing for medication assistance programs |
| 📋 Label compliance | Information consistent with approved prescribing info |

### Health insurers and payers

| Benefit | Detail |
|---------|--------|
| 💰 Cost reduction | Improved adherence reduces hospitalisations |
| 🏨 Fewer ER visits | Patients seek care at the right level |
| 📱 Scalable education | Serves thousands of patients at near-zero marginal cost |

### Healthcare technology companies

| Benefit | Detail |
|---------|--------|
| 🔧 Extendable platform | RAG architecture extends to any biologic therapy |
| ⚖️ Regulatory pathway | Informational classification simplifies FDA SaMD approach |
| 🔗 EHR integration ready | FastAPI backend built for Epic/Cerner REST API integration |

---

## 🏗️ Architecture

<img width="468" height="541" alt="image" src="https://github.com/user-attachments/assets/d741ecce-4a12-4510-aca1-86085d5207ce" />


```
┌──────────────────────────────────────────────────────────────┐
│                    1 · DATA SOURCES                          │
│   FDA Label · PubMed (50 papers) · NCCN · MedlinePlus       │
│                    ClinicalTrials.gov · OpenFDA              │
└────────────────────────┬─────────────────────────────────────┘
                         │  7 documents → 1,019 chunks
┌────────────────────────▼─────────────────────────────────────┐
│                  2 · INGESTION PIPELINE                      │
│   PDF loader → Text chunker (512 chars) → OpenAI embeddings  │
│         → Pinecone upsert (1536-dim, 50 per batch)           │
└────────────────────────┬─────────────────────────────────────┘
                         │  1,019 dense vectors
┌────────────────────────▼─────────────────────────────────────┐
│              3 · PINECONE VECTOR DATABASE                    │
│   Index: rituximab-rag · Serverless · AWS us-east-1          │
│   Dimension: 1536 · Metric: cosine · Namespace: rituximab    │
└────────────────────────┬─────────────────────────────────────┘
                         │  query-time retrieval
┌────────────────────────▼─────────────────────────────────────┐
│                  4 · RAG PIPELINE                            │
│   Query → scope guard → embed → Pinecone top-5 → GPT-4      │
│         prompt builder → answer generation                   │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────────┐
│                  5 · SAFETY LAYER                            │
│   30-keyword scope filter · Medical disclaimer               │
│           Source citations · Confidence score                │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────────┐
│                6 · PATIENT INTERFACE                         │
│   Mobile-responsive HTML5 chat · FastAPI / Uvicorn           │
│       Model switcher (GPT-4 / Claude / Local)                │
│              Deployed live on Render.com                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 Knowledge Base

All documents sourced from **free, publicly available** official medical databases:

| Document | Source | Category | Chunks | Pinecone Scores |
|----------|--------|----------|--------|-----------------|
| FDA Rituxan Prescribing Label (PDF) | accessdata.fda.gov | fda_label | 410 | 0.55 – 0.75 |
| PubMed Research Abstracts (50 papers) | NCBI E-utilities API | research_abstracts | 551 | 0.60 – 0.78 |
| NCCN Clinical Guidelines | nccn.org | clinical_guidelines | 5 | 0.52 – 0.68 |
| MedlinePlus Patient Education | medlineplus.gov | patient_education | 5 | 0.60 – 0.72 |
| ClinicalTrials.gov Summaries | clinicaltrials.gov | clinical_trials | 45 | 0.48 – 0.65 |
| OpenFDA Adverse Events | api.fda.gov | adverse_events | 3 | 0.50 – 0.62 |
| **Total** | | **6 categories** | **1,019** | |

---

## 🛠️ Tech Stack

```
Language          Python 3.9  ·  JavaScript ES6
Vector DB         Pinecone Serverless  ·  rituximab-rag index
Embeddings        OpenAI text-embedding-3-small  ·  1536 dimensions
LLM               GPT-4o-mini  (Anthropic Claude as alternative)
Document          PyPDF  ·  JSON parser  ·  Text chunker
Web Framework     FastAPI  ·  Uvicorn ASGI
Frontend          HTML5  ·  CSS3  ·  Vanilla JS  ·  Mobile-responsive
Deployment        Render.com  ·  GitHub CI/CD
Version control   Git  ·  GitHub
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Pinecone account — free at [app.pinecone.io](https://app.pinecone.io)
- OpenAI API key — [platform.openai.com](https://platform.openai.com)

### 1 — Clone the repository

```bash
git clone https://github.com/raju-AI-portfolio/rituximab-rag-assistant.git
cd rituximab-rag-assistant
```

### 2 — Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3 — Configure environment variables

```bash
cp .env.example .env
nano .env
```

Fill in your keys:

```env
PINECONE_API_KEY=your_pinecone_key_here
OPENAI_API_KEY=your_openai_key_here
AI_PROVIDER=openai
OPENAI_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
PINECONE_INDEX_NAME=rituximab-rag
PINECONE_NAMESPACE=rituximab
TOP_K_RESULTS=5
```

### 4 — Set up data folders

```bash
mkdir -p data/raw data/processed data/chroma_db
```

### 5 — Download source documents

```bash
python3 src/ingestion/step1_download.py
```

### 6 — Process and chunk documents

```bash
python3 src/ingestion/step2_process.py
```

Expected output: `1,019 chunks saved`

### 7 — Build the Pinecone index (one-time setup, ~60 seconds)

```bash
python3 src/ingestion/step3_pinecone.py
```

Expected output:
```
Pinecone : OK
OpenAI   : OK
Creating index 'rituximab-rag' (dim=1536, AWS us-east-1)...
Waiting......... ready!
Upserting [████████████████████] 1019/1019
Upserted 1019 vectors to 'rituximab-rag'
Vectors: 1019
```

### 8 — Test the RAG pipeline

```bash
python3 src/retrieval/step4_rag_pinecone.py
```

### 9 — Launch the web app

```bash
python3 -m uvicorn app:app --reload
```

Open your browser at `http://localhost:8000`

---

## 📁 Project Structure

```
rituximab_rag/
│
├── app.py                              # FastAPI web server
├── web_ui_v2.html                      # Mobile-responsive chat UI (Phase 1)
├── web_ui.html                         # Original chat UI (Phase 0)
├── requirements.txt                    # Python dependencies
├── render.yaml                         # Render deployment config
├── .env.example                        # Environment variable template
├── .gitignore                          # Excludes .env, data/, .DS_Store
│
├── src/
│   ├── ingestion/
│   │   ├── step1_download.py           # Download documents from APIs
│   │   ├── step2_process.py            # Clean, chunk, categorise docs
│   │   ├── step3_pinecone.py           # Build Pinecone dense index (Phase 1)
│   │   └── step3_vectordb.py           # TF-IDF fallback index (Phase 0)
│   │
│   ├── retrieval/
│   │   ├── step4_rag_pinecone.py       # RAG pipeline — Pinecone edition (Phase 1)
│   │   └── step4_rag_pipeline.py       # RAG pipeline — TF-IDF edition (Phase 0)
│   │
│   └── interface/
│       └── chat.py                     # Terminal chat interface
│
└── data/
    ├── raw/                            # Source documents (PDF, TXT, JSON)
    │   ├── FDA Rituxan Label.pdf
    │   ├── fda_label_rituxan.txt
    │   ├── medlineplus_rituximab.txt
    │   ├── nccn_guidelines_rituximab.txt
    │   ├── pubmed_abstracts.txt
    │   ├── clinical_trials.json
    │   └── adverse_events.json
    ├── processed/
    │   └── rituximab_chunks.json       # 1,019 processed chunks
    └── chroma_db/
        └── rituximab_index.pkl         # TF-IDF fallback index
```

---

## 📡 API Reference

### `GET /`

Returns the HTML5 chat interface.

### `GET /health`

Returns system status and configuration.

**Response:**
```json
{
  "status": "ok",
  "version": "pinecone-edition",
  "db": "pinecone",
  "index": "rituximab-rag",
  "embedding": "text-embedding-3-small",
  "model": "gpt-4o-mini"
}
```

### `POST /ask`

Accepts a patient query and returns a RAG-generated answer.

**Request:**
```json
{
  "query": "What are the side effects of Rituximab?"
}
```

**Response:**
```json
{
  "query": "What are the side effects of Rituximab?",
  "in_scope": true,
  "answer": "According to the FDA prescribing label, the most common side effects of Rituximab include infusion-related reactions (fever, chills, nausea), increased risk of infections, fatigue, headache, and low blood cell counts...",
  "sources": ["FDA Rituxan Label.pdf", "medlineplus_rituximab.txt"],
  "model": "gpt-4o-mini",
  "score": 0.752,
  "db_type": "pinecone"
}
```

---

## 🌐 Deployment

### Deploy to Render (free)

1. Fork this repository on GitHub
2. Go to [render.com](https://render.com) and sign up with GitHub
3. Click **New +** → **Web Service** → connect your fork
4. Render auto-detects settings from `render.yaml`
5. Add environment variables in the **Environment** tab:

| Key | Value |
|-----|-------|
| `PINECONE_API_KEY` | your Pinecone key |
| `OPENAI_API_KEY` | your OpenAI key |
| `PINECONE_INDEX_NAME` | `rituximab-rag` |
| `PINECONE_NAMESPACE` | `rituximab` |
| `EMBEDDING_MODEL` | `text-embedding-3-small` |
| `AI_PROVIDER` | `openai` |
| `OPENAI_MODEL` | `gpt-4o-mini` |

6. Click **Save Changes** — Render auto-redeploys in 2–3 minutes

### render.yaml

```yaml
services:
  - type: web
    name: rituximab-rag-assistant
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    plan: free
```

---

## 🧪 Test Results

Live test results from the deployed Pinecone + GPT-4 pipeline:

| Patient Question | Top Source | Score | Model | Result |
|-----------------|------------|-------|-------|--------|
| What are the side effects of Rituximab? | FDA Label | 0.752 | gpt-4o-mini | ✅ Relevant |
| How long does a Rituximab infusion take? | MedlinePlus | 0.718 | gpt-4o-mini | ✅ Relevant |
| Can I get a flu vaccine while on Rituximab? | FDA Label | 0.622 | gpt-4o-mini | ✅ Relevant |
| Is Rituximab safe during pregnancy? | FDA Label | 0.694 | gpt-4o-mini | ✅ Relevant |
| What is the dose for rheumatoid arthritis? | FDA Label | 0.560 | gpt-4o-mini | ✅ Relevant |
| What is PML and should I be worried? | FDA Label | 0.731 | gpt-4o-mini | ✅ Relevant |
| Can I eat pizza? *(out-of-scope)* | N/A | N/A | scope-filter | ✅ Blocked |

---

## 🗺️ Roadmap

### ✅ Phase 1 — Complete
- [x] Pinecone Serverless vector database
- [x] OpenAI text-embedding-3-small dense embeddings
- [x] GPT-4o-mini answer generation
- [x] Mobile-responsive web UI with model switcher
- [x] Live deployment on Render.com with CI/CD

### Phase 2 — Near Term
- [ ] Multilingual support (Hindi, Telugu)
- [ ] EHR integration (Epic, Cerner) via FHIR REST API
- [ ] Voice interface for elderly patients
- [ ] Automated knowledge base refresh from FDA RSS feeds

### Phase 3 — Long Term
- [ ] Expand to all biologic therapies (Humira, Keytruda, Herceptin)
- [ ] FDA Software as a Medical Device (SaMD) regulatory pathway
- [ ] Clinical validation study with a patient cohort
- [ ] Hospital white-label licensing model

---


## ⚠️ Medical Disclaimer

This application is for **educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor or healthcare provider before making any medical decisions. In case of emergency call your local emergency services immediately.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Raju Kumar**

- Live app: [rituximab-rag-assistant.onrender.com](https://rituximab-rag-assistant.onrender.com)
- GitHub: [github.com/raju-AI-portfolio/rituximab-rag-assistant](https://github.com/raju-AI-portfolio/rituximab-rag-assistant)

---

<div align="center">

Built with ❤️ using **Pinecone · OpenAI GPT-4 · FastAPI · Render · FDA · NIH · NCCN · PubMed**

*Helping patients understand their therapy — one question at a time* 🧬

</div>
