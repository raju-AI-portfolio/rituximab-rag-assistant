# 🧬 Rituximab Patient Knowledge Assistant

> An AI-powered Retrieval-Augmented Generation (RAG) system that helps patients access accurate, source-verified information about Rituximab therapy — available 24/7, grounded in FDA, NIH, NCCN, and PubMed sources.
>
> **Deployed on Render- live Demo: https://rituximab-rag-assistant.onrender.com/**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render.com-28a745?style=for-the-badge&logo=render)](https://rituximab-rag-assistant.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [How It Helps Patients](#-how-it-helps-patients)
- [Benefits to Organisations](#-benefits-to-organisations)
- [System Architecture](#-system-architecture)
- [Knowledge Base & Data Sources](#-knowledge-base--data-sources)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [How It Works (RAG Pipeline)](#-how-it-works-rag-pipeline)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Resume Summary](#-resume-summary)
- [Author](#-author)

---

## 🔬 About the Project

Rituximab (Rituxan) is one of the world's most widely prescribed biologic therapies, used to treat:

| Condition | Patients Affected |
|-----------|------------------|
| Non-Hodgkin Lymphoma (NHL) | ~80,000 new cases/year (US) |
| Chronic Lymphocytic Leukemia (CLL) | ~21,000 new cases/year (US) |
| Rheumatoid Arthritis (RA) | ~1.3 million patients (US) |
| Multiple Sclerosis (MS) | ~1 million patients (US) |
| Lupus & Vasculitis | ~200,000 patients (US) |

Despite its widespread use, patients consistently struggle to access **timely, accurate, trustworthy information** about their therapy. This project solves that problem using **Retrieval-Augmented Generation (RAG)** — an AI architecture that retrieves answers exclusively from verified medical sources rather than generating them from memory, eliminating hallucination risk.

---

## 💊 How It Helps Patients

### The Problem Patients Face

> *"I got home from my infusion and had so many questions, but my oncologist's office was closed. I had no idea if what I was feeling was normal."*

Patients on Rituximab therapy face real, daily challenges:

| Challenge | Impact |
|-----------|--------|
| ❌ Can't reach care team after hours | Anxiety, delayed reporting of serious symptoms |
| ❌ Unreliable internet health information | Risk of dangerous misinformation |
| ❌ Complex medical jargon in package inserts | Patients can't understand their own treatment |
| ❌ Fear of infusion reactions | Avoidance of treatment, non-adherence |
| ❌ Uncertainty about drug interactions & vaccines | Potentially dangerous decisions |

### How This Assistant Solves It

✅ **24/7 Availability** — Patients can ask questions any time, day or night, from any device

✅ **Source-Verified Answers** — Every response is retrieved directly from FDA labels, NIH guidelines, and clinical research — not generated from AI memory

✅ **Plain Language** — Answers are written in patient-friendly language, not medical jargon

✅ **Covers All Key Topics** — 75+ patient questions across 8 categories:

```
💊 Treatment basics      ⚠️  Side effects
🏥 Infusion process      🛡️  Safety & risks
📊 Monitoring            🌿 Lifestyle
🔄 Alternatives          💙 Emotional support
```

✅ **Instant Scope Filtering** — The system only answers Rituximab-related questions, preventing dangerous off-topic medical advice

✅ **Always Cites Sources** — Every answer shows exactly which document it came from (FDA Label, MedlinePlus, NCCN Guidelines, PubMed)

✅ **Medical Disclaimer on Every Response** — Patients are always reminded to consult their doctor for personal medical decisions

### Real Patient Questions It Answers

```
"What are the side effects of Rituximab?"
"How long does my infusion take?"
"Can I get a flu vaccine while on treatment?"
"Is Rituximab safe during pregnancy?"
"What is PML and should I be worried?"
"What should I do if I get a fever?"
"Can I drink alcohol during treatment?"
"How will I know if it's working?"
```

---

## 🏥 Benefits to Organisations

### For Hospitals & Cancer Centres

| Benefit | Detail |
|---------|--------|
| 📉 **Reduced call volume** | Routine patient questions handled automatically, freeing nursing staff for clinical work |
| 📈 **Improved patient satisfaction** | Patients feel supported between appointments, reducing anxiety and improving trust |
| 🔒 **Reduced liability** | All answers sourced from FDA-approved labeling with mandatory disclaimers |
| ⏱️ **Nurse time savings** | Infusion centres report 30–50% of patient calls are routine information requests |
| 🌍 **Extended reach** | Serves patients who cannot easily phone the clinic (language barriers, time zones, disability) |

### For Pharmaceutical Companies

| Benefit | Detail |
|---------|--------|
| 💊 **Medication adherence** | Informed patients are significantly more likely to complete their treatment courses |
| 📊 **Real-world evidence** | Aggregated anonymised query data reveals gaps in patient education materials |
| 🤝 **Patient support programs** | Can be white-labelled as part of existing medication assistance programs |
| 🌐 **Digital companion** | Complements existing patient portals and medication reminder apps |
| 📋 **Label compliance** | Ensures patients receive information consistent with approved prescribing information |

### For Health Insurance & Payers

| Benefit | Detail |
|---------|--------|
| 💰 **Cost reduction** | Improved adherence reduces hospitalisation from treatment complications |
| 🏨 **Fewer emergency visits** | Patients who understand side effects seek care at the right level, not ER for minor symptoms |
| 📱 **Scalable education** | One system serves thousands of patients simultaneously at near-zero marginal cost |

### For Healthcare Technology Companies

| Benefit | Detail |
|---------|--------|
| 🔧 **Extendable platform** | RAG architecture easily adapts to any biologic therapy (Humira, Keytruda, Herceptin) |
| ⚖️ **Regulatory pathway** | Informational (not diagnostic) classification simplifies FDA SaMD regulatory approach |
| 🔗 **EHR integration ready** | FastAPI backend designed for integration with Epic, Cerner, and other EHR systems |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     PATIENT INTERFACE                        │
│              Web UI (HTML)  ·  Terminal Chat                │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                    SAFETY LAYER                              │
│         Scope Filter  ·  Disclaimer  ·  Citations           │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                    RAG PIPELINE                              │
│   Query Processor → Retriever → Prompt Builder → Generator  │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  KNOWLEDGE BASE                              │
│        TF-IDF Vector Index  ·  1,019 Chunks  ·  1.2 MB      │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  DATA SOURCES                                │
│   FDA Label  ·  PubMed  ·  NCCN  ·  MedlinePlus  ·  Trials │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 Knowledge Base & Data Sources

All documents are sourced from **free, publicly available** official medical databases.

| Source | Type | Chunks | Access |
|--------|------|--------|--------|
| FDA Rituxan Prescribing Label (PDF) | FDA Label | 410 | Free — accessdata.fda.gov |
| PubMed Research Abstracts (50 papers) | Research | 551 | Free — NCBI E-utilities API |
| NCCN Clinical Guidelines | Clinical Guidelines | 5 | Free with registration — nccn.org |
| MedlinePlus Patient Education | Patient Education | 5 | Free — medlineplus.gov |
| ClinicalTrials.gov Summaries | Clinical Trials | 45 | Free — clinicaltrials.gov API |
| OpenFDA Adverse Events | Safety Data | 3 | Free — api.fda.gov |
| **Total** | | **1,019 chunks** | |

---

## ✨ Features

- 🔍 **Semantic retrieval** — TF-IDF cosine similarity search across 1,019 medical document chunks
- 🛡️ **Scope guard** — Blocks non-Rituximab questions with 30+ keyword triggers
- 📚 **Source citations** — Every answer shows which official document it came from
- ⚠️ **Safety disclaimer** — Medical disclaimer attached to every response
- 💬 **Web chat UI** — Dark-themed, mobile-friendly browser interface
- 🖥️ **Terminal interface** — Coloured CLI chat with session history logging
- 🌐 **REST API** — FastAPI backend ready for EHR/portal integration
- 📊 **Confidence scoring** — Relevance score shown for every retrieved answer
- 🔄 **Session logging** — All conversations saved to JSON for analysis
- 🚀 **Free deployment** — Runs on Render.com free tier

---

## 🛠️ Tech Stack

```
Language        Python 3.9 · JavaScript (ES6)
RAG Engine      TF-IDF Vectorisation · Cosine Similarity · Top-K Retrieval
Document        PyPDF · JSON parser · Text chunker (512 chars, 80 overlap)
Storage         Pickle index · JSON chunks · Local filesystem
Web Framework   FastAPI · Uvicorn
Frontend        HTML5 · CSS3 · Vanilla JavaScript
Deployment      Render.com · GitHub Actions
Data Sources    FDA · NIH/PubMed · NCCN · MedlinePlus · ClinicalTrials.gov
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip3
- ~50 MB disk space

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rituximab-rag-assistant.git
cd rituximab-rag-assistant
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Set up data directories

```bash
mkdir -p data/raw data/processed data/chroma_db
```

### 4. Download source documents

```bash
python3 src/ingestion/step1_download.py
```

Or create documents manually — see [Data Sources](#-knowledge-base--data-sources).

### 5. Process and chunk documents

```bash
python3 src/ingestion/step2_process.py
```

### 6. Build the vector index

```bash
python3 src/ingestion/step3_vectordb.py
```

### 7. Test the RAG pipeline

```bash
python3 src/retrieval/step4_rag_pipeline.py
```

### 8. Launch the terminal chat

```bash
python3 src/interface/chat.py
```

### 9. Launch the web server

```bash
uvicorn app:app --reload
```

Open your browser at `http://localhost:8000`

---

## 📁 Project Structure

```
rituximab_rag/
│
├── app.py                          # FastAPI web server
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment config
├── web_ui.html                     # Browser chat interface
│
├── src/
│   ├── ingestion/
│   │   ├── step1_download.py       # Download documents from APIs
│   │   ├── step2_process.py        # Clean, chunk, categorise
│   │   └── step3_vectordb.py       # Build TF-IDF vector index
│   │
│   ├── retrieval/
│   │   └── step4_rag_pipeline.py   # Core RAG query engine
│   │
│   └── interface/
│       └── chat.py                 # Terminal chat UI
│
├── data/
│   ├── raw/                        # Source documents (PDF, TXT, JSON)
│   ├── processed/
│   │   └── rituximab_chunks.json   # 1,019 processed chunks
│   ├── chroma_db/
│   │   └── rituximab_index.pkl     # TF-IDF vector index (1.2 MB)
│   └── chat_history.json           # Session logs
│
└── config/
    └── .env.example                # Environment variables template
```

---

## ⚙️ How It Works (RAG Pipeline)

```
Patient Question
      │
      ▼
┌─────────────┐
│   Scope     │  Is this a Rituximab-related question?
│   Check     │  If NO → polite redirect to doctor
└──────┬──────┘
       │ YES
       ▼
┌─────────────┐
│   Query     │  Expand abbreviations (RA, NHL, CLL)
│  Processor  │  Normalise and clean input
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  TF-IDF     │  Compute cosine similarity against 1,019 chunks
│  Retrieval  │  Return top-5 most relevant (max 2 per source)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Prompt    │  Combine patient question + retrieved chunks
│   Builder   │  Apply source priority: FDA > Patient Ed > Guidelines
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Answer    │  Generate clear, structured response
│ Generation  │  Attach source citations + medical disclaimer
└──────┬──────┘
       │
       ▼
  Patient receives cited, safe, source-verified answer
```

---

## 🌐 Deployment

### Deploy to Render (Free)

1. Fork this repository
2. Go to [render.com](https://render.com) and sign up with GitHub
3. Click **New +** → **Web Service**
4. Connect your forked repository
5. Render auto-detects settings from `render.yaml`
6. Add environment variable: `PYTHON_VERSION` = `3.9.6`
7. Click **Create Web Service**

Your app will be live at:
```
https://rituximab-rag-assistant.onrender.com
```

### Deploy locally with Docker (optional)

```bash
docker build -t rituximab-rag .
docker run -p 8000:8000 rituximab-rag
```

---

## 🗺️ Roadmap

### Phase 1 — Near Term
- [ ] Integrate OpenAI GPT-4 for higher-quality answer generation
- [ ] Upgrade to dense embeddings (text-embedding-3-small) + ChromaDB
- [ ] Add Hindi and Telugu language support
- [ ] Improve mobile responsiveness

### Phase 2 — Mid Term
- [ ] EHR integration (Epic, Cerner)
- [ ] Voice interface for elderly patients
- [ ] Nurse analytics dashboard
- [ ] Automated FDA feed updates

### Phase 3 — Long Term
- [ ] Expand to all biologic therapies (Humira, Keytruda, Herceptin)
- [ ] FDA SaMD regulatory pathway
- [ ] Clinical validation study
- [ ] Hospital white-label licensing

---

## 📄 Resume Summary

**Technical:**
> Designed and developed an AI-powered Rituximab therapy knowledge assistant using Retrieval-Augmented Generation (RAG), integrating FDA labels, NIH, NCCN, and PubMed data sources into a 1,019-chunk vector knowledge base deployed live on Render.com.

**Impact:**
> Built a domain-specific RAG-based clinical assistant for Rituximab therapy, enabling patients to access structured, source-verified drug information across oncology, rheumatology, and neurology use cases.

---

## ⚠️ Medical Disclaimer

This application is for **educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor, pharmacist, or healthcare provider for medical decisions. In case of emergency, call your local emergency services immediately.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Raju Kumar**

- GitHub: [@rajukumar](https://github.com/rajukumar)
- Project: [Rituximab RAG Assistant](https://github.com/rajukumar/rituximab-rag-assistant)

---

<div align="center">

Built with ❤️ using **RAG · FDA · NIH · NCCN · PubMed · FastAPI · Render**

*Helping patients understand their therapy — one question at a time* 🧬

</div>
