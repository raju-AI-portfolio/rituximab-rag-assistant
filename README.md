<div align="center">

# 🧬 Rituximab Patient Knowledge Assistant

### Phase 2 — Azure-Native Production Release

**Fully Azure-native RAG system for Rituximab therapy patient education**

[![Azure Live Demo](https://img.shields.io/badge/Live%20Demo-Azure%20App%20Service-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://rituximab-rag-fmgvg6aravebatbz.centralindia-01.azurewebsites.net)
[![Render Demo](https://img.shields.io/badge/Also%20on-Render.com-28a745?style=for-the-badge&logo=render&logoColor=white)](https://rituximab-rag-assistant.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-GPT--4o-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
[![Azure AI Search](https://img.shields.io/badge/Azure%20AI%20Search-Vector%20DB-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/en-us/products/ai-services/ai-search)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*Helping patients understand their Rituximab therapy — 24/7, grounded in FDA, NIH, NCCN and PubMed*

</div>

---
---
## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Phase 2 Upgrades — Azure Native](#-phase-2-upgrades--azure-native)
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

Now deployed on **Microsoft Azure** — the same enterprise cloud infrastructure used by leading pharmaceutical companies including Novartis, Roche, and Pfizer.

---

## 🚀 Phase 2 Upgrades — Azure Native

Phase 2 migrates the entire stack to Microsoft Azure, replacing all third-party services with Azure-native equivalents:

| Component | Phase 1 (Render) | Phase 2 (Azure Native) |
|-----------|-----------------|------------------------|
| Hosting | Render.com (free tier) | **Azure App Service** (Central India, F1) |
| LLM | OpenAI API (direct) | **Azure OpenAI Service — GPT-4o** (50K TPM) |
| Vector Database | Pinecone Serverless | **Azure AI Search** (vector + hybrid search) |
| CI/CD | Render webhook | **GitHub Actions** workflow pipeline |
| Build system | Render Oryx | **Azure Oryx** build system |
| Web server | Uvicorn | **Gunicorn + UvicornWorker** (production-grade) |
| Secret management | Render env vars | **Azure App Settings** (encrypted at rest) |
| Python runtime | 3.9 | **Python 3.11** |
| Answer quality score | 0.75 avg | **0.80+ avg** (improved retrieval) |
| Model | GPT-4o-mini | **GPT-4o** (full model, latest version) |

### Why Azure matters for pharma

Azure is the cloud platform of choice for enterprise pharmaceutical companies due to:
- **GxP-compliant infrastructure** — validated for regulated pharma workloads
- **HIPAA BAA available** — Business Associate Agreement for healthcare data
- **EU data residency** — data stays within Azure geography (GDPR compliance)
- **Azure AI Foundry** — enterprise model lifecycle management
- **Private networking** — VNet integration for sensitive clinical data

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

✅ **Plain language** — GPT-4o rewrites complex medical text into clear patient-friendly answers

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

---

## 🏗️ Architecture

### Phase 2 — Azure Native Architecture

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
│         → Azure AI Search upsert (1536-dim vectors)          │
└────────────────────────┬─────────────────────────────────────┘
                         │  1,019 dense vectors
┌────────────────────────▼─────────────────────────────────────┐
│           3 · AZURE AI SEARCH (Vector Database)              │
│   Index: rituximab-index · HNSW algorithm · 1536-dim         │
│   Hybrid search: vector + keyword · Score: 0.80+ avg         │
└────────────────────────┬─────────────────────────────────────┘
                         │  query-time vector retrieval
┌────────────────────────▼─────────────────────────────────────┐
│                  4 · RAG PIPELINE                            │
│   Query → scope guard → embed → Azure AI Search top-5       │
│         → prompt builder → Azure OpenAI GPT-4o              │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────────┐
│                  5 · SAFETY LAYER                            │
│   30-keyword scope filter · Medical disclaimer               │
│           Source citations · Confidence score                │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────────┐
│           6 · AZURE APP SERVICE (Hosting)                    │
│   Python 3.11 · Gunicorn + UvicornWorker · Central India     │
│   GitHub Actions CI/CD · Auto-deploy on push to main        │
│   HTTPS · Azure-managed TLS certificate                      │
└──────────────────────────────────────────────────────────────┘
```

### CI/CD Pipeline

```
Developer laptop
      │
      │  git push origin main
      ▼
GitHub Repository
      │
      │  webhook triggers GitHub Actions workflow
      ▼
GitHub Actions Runner
      │  pip install -r requirements.txt
      │  deploy via publish profile
      ▼
Azure App Service (Central India)
      │  Gunicorn starts · env vars injected
      ▼
Live at: rituximab-rag-fmgvg6aravebatbz.centralindia-01.azurewebsites.net
```

---

## 📚 Knowledge Base

All documents sourced from **free, publicly available** official medical databases:

| Document | Source | Category | Chunks | Azure AI Search Scores |
|----------|--------|----------|--------|------------------------|
| FDA Rituxan Prescribing Label (PDF) | accessdata.fda.gov | fda_label | 410 | 0.65 – 0.85 |
| PubMed Research Abstracts (50 papers) | NCBI E-utilities API | research_abstracts | 551 | 0.68 – 0.82 |
| NCCN Clinical Guidelines | nccn.org | clinical_guidelines | 5 | 0.60 – 0.75 |
| MedlinePlus Patient Education | medlineplus.gov | patient_education | 5 | 0.65 – 0.78 |
| ClinicalTrials.gov Summaries | clinicaltrials.gov | clinical_trials | 45 | 0.55 – 0.70 |
| OpenFDA Adverse Events | api.fda.gov | adverse_events | 3 | 0.55 – 0.68 |
| **Total** | | **6 categories** | **1,019** | |

---

## 🛠️ Tech Stack

```
Language          Python 3.11  ·  JavaScript ES6
Cloud Platform    Microsoft Azure (Central India region)
Hosting           Azure App Service  ·  Free F1 tier
Vector DB         Azure AI Search  ·  rituximab-index  ·  HNSW algorithm
Embeddings        OpenAI text-embedding-3-small  ·  1536 dimensions
LLM               Azure OpenAI GPT-4o  ·  2024-11-20  ·  50K TPM
Document          PyPDF  ·  JSON parser  ·  Text chunker
Web Framework     FastAPI  ·  Gunicorn + UvicornWorker
Frontend          HTML5  ·  CSS3  ·  Vanilla JS  ·  Mobile-responsive
CI/CD             GitHub Actions  ·  Auto-deploy on push to main
Secret Mgmt       Azure App Settings  ·  Encrypted at rest
Version control   Git  ·  GitHub
Fallback DB       Pinecone Serverless  ·  rituximab-rag index
Fallback LLM      OpenAI API direct  ·  GPT-4o-mini
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Azure account — free at [portal.azure.com](https://portal.azure.com)
- OpenAI API key — [platform.openai.com](https://platform.openai.com) (for embeddings)
- Pinecone account (optional fallback) — [app.pinecone.io](https://app.pinecone.io)

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

#### Option A — Azure native (recommended)

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_DEPLOYMENT=gpt-4o

# Azure AI Search
AZURE_SEARCH_ENDPOINT=https://rituximab-search.search.windows.net
AZURE_SEARCH_KEY=your_azure_search_key
AZURE_SEARCH_INDEX=rituximab-index

# OpenAI (for embeddings only)
OPENAI_API_KEY=your_openai_key_here
EMBEDDING_MODEL=text-embedding-3-small
```

#### Option B — Pinecone fallback

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

### 7A — Build Azure AI Search index (Phase 2)

```bash
python3 upload_to_azure_search.py
```

Expected output:
```
Connecting to Pinecone...
Fetching vector IDs from Pinecone...
  Found 1019 vectors
  ...
Done! 1019 documents uploaded to Azure AI Search!
```

### 7B — Build the Pinecone index (Phase 1 fallback)

```bash
python3 src/ingestion/step3_pinecone.py
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
├── requirements.txt                    # Python dependencies (incl. gunicorn, azure-search-documents)
├── render.yaml                         # Render deployment config (Phase 1 fallback)
├── upload_to_azure_search.py           # Script to upload vectors to Azure AI Search
├── .github/
│   └── workflows/
│       └── main_rituximab-rag.yml      # GitHub Actions CI/CD workflow for Azure
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
│   │   ├── step4_rag_pinecone.py       # RAG pipeline — Azure AI Search + Azure OpenAI (Phase 2)
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

**Response (Phase 2 — Azure):**
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

**Response (Phase 2 — Azure AI Search + GPT-4o):**
```json
{
  "query": "What are the side effects of Rituximab?",
  "in_scope": true,
  "answer": "Rituximab can cause several side effects...[detailed structured answer with source citations]",
  "sources": ["FDA Rituxan Label.pdf", "pubmed_abstracts.txt"],
  "model": "gpt-4o",
  "score": 0.8012,
  "db_type": "azure_search"
}
```

---

## 🌐 Deployment

### Deploy to Azure App Service (Phase 2 — Recommended)

#### Prerequisites
- Azure account with active subscription
- GitHub repository with this code

#### Step 1 — Create Azure App Service

1. Go to [portal.azure.com](https://portal.azure.com)
2. Create a resource → Web App
3. Settings:
   - Runtime: Python 3.11
   - Region: Central India
   - Plan: Free F1

#### Step 2 — Set environment variables

In Azure portal → your Web App → Settings → Environment variables:

| Key | Value |
|-----|-------|
| `AZURE_OPENAI_ENDPOINT` | your Azure OpenAI base URL |
| `AZURE_OPENAI_KEY` | your Azure OpenAI key |
| `AZURE_OPENAI_DEPLOYMENT` | `gpt-4o` |
| `AZURE_SEARCH_ENDPOINT` | `https://rituximab-search.search.windows.net` |
| `AZURE_SEARCH_KEY` | your Azure AI Search admin key |
| `AZURE_SEARCH_INDEX` | `rituximab-index` |
| `OPENAI_API_KEY` | your OpenAI key (for embeddings) |
| `EMBEDDING_MODEL` | `text-embedding-3-small` |
| `PINECONE_API_KEY` | your Pinecone key (fallback) |
| `PINECONE_INDEX_NAME` | `rituximab-rag` |
| `PINECONE_NAMESPACE` | `rituximab` |

#### Step 3 — Set startup command

In Configuration → General settings → Startup command:
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

#### Step 4 — Connect GitHub for auto-deploy

Deployment Center → Source: GitHub → select repo and main branch → Save

GitHub Actions workflow is automatically created at `.github/workflows/main_rituximab-rag.yml`

---

### Deploy to Render (Phase 1 — Fallback)

1. Fork this repository on GitHub
2. Go to [render.com](https://render.com) and connect your fork
3. Render auto-detects settings from `render.yaml`
4. Add environment variables in the Environment tab
5. Click Save — Render auto-redeploys in 2–3 minutes

---

## 🧪 Test Results

### Phase 2 — Azure AI Search + GPT-4o results

| Patient Question | Top Source | Score | Model | DB | Result |
|-----------------|------------|-------|-------|-----|--------|
| What are the side effects of Rituximab? | FDA Label | 0.8012 | gpt-4o | azure_search | ✅ Relevant |
| How long does a Rituximab infusion take? | MedlinePlus | 0.7891 | gpt-4o | azure_search | ✅ Relevant |
| Can I get a flu vaccine while on Rituximab? | FDA Label | 0.7654 | gpt-4o | azure_search | ✅ Relevant |
| Is Rituximab safe during pregnancy? | FDA Label | 0.7823 | gpt-4o | azure_search | ✅ Relevant |
| What is the dose for rheumatoid arthritis? | FDA Label | 0.7412 | gpt-4o | azure_search | ✅ Relevant |
| What is PML and should I be worried? | FDA Label | 0.7956 | gpt-4o | azure_search | ✅ Relevant |
| Can I eat pizza? *(out-of-scope)* | N/A | N/A | scope-filter | N/A | ✅ Blocked |

### Phase 1 vs Phase 2 comparison

| Metric | Phase 1 (Pinecone + GPT-4o-mini) | Phase 2 (Azure AI Search + GPT-4o) |
|--------|----------------------------------|-------------------------------------|
| Avg retrieval score | 0.75 | **0.80+** |
| Answer detail | Good | **Excellent — structured with headings** |
| Source citations | Basic | **Detailed — category + document** |
| Model | GPT-4o-mini | **GPT-4o (full model)** |
| Infrastructure | Third-party SaaS | **Enterprise Azure cloud** |

---

## 🗺️ Roadmap

### ✅ Phase 1 — Complete
- [x] Pinecone Serverless vector database
- [x] OpenAI text-embedding-3-small dense embeddings
- [x] GPT-4o-mini answer generation
- [x] Mobile-responsive web UI with model switcher
- [x] Live deployment on Render.com with CI/CD

### ✅ Phase 2 — Complete (Azure Native)
- [x] Migrated hosting to Azure App Service (Central India)
- [x] Upgraded LLM to Azure OpenAI GPT-4o (enterprise grade)
- [x] Replaced Pinecone with Azure AI Search (1,019 vectors, HNSW)
- [x] GitHub Actions CI/CD pipeline (auto-deploy on push)
- [x] Gunicorn + UvicornWorker production web server
- [x] Azure App Settings for secret management

### Phase 3 — Near Term
- [ ] Azure Key Vault for API key management
- [ ] Application Insights for observability and monitoring
- [ ] Multilingual support (Hindi, Telugu)
- [ ] EHR integration (Epic, Cerner) via FHIR REST API
- [ ] Voice interface for elderly patients

### Phase 4 — Long Term
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

**Raju Kumar** — Healthcare AI Solutions Architect

- 🌐 Azure Live: [rituximab-rag-fmgvg6aravebatbz.centralindia-01.azurewebsites.net](https://rituximab-rag-fmgvg6aravebatbz.centralindia-01.azurewebsites.net)
- 🌐 Render Live: [rituximab-rag-assistant.onrender.com](https://rituximab-rag-assistant.onrender.com)
- 💼 LinkedIn: [linkedin.com/in/programdirectorai](https://www.linkedin.com/in/programdirectorai)
- 🐙 GitHub: [github.com/raju-AI-portfolio](https://github.com/raju-AI-portfolio)

---

<div align="center">

Built with ❤️ using **Azure OpenAI · Azure AI Search · Azure App Service · GitHub Actions · FastAPI · FDA · NIH · NCCN · PubMed**

*Helping patients understand their therapy — one question at a time* 🧬

**Deployed on Microsoft Azure — enterprise-grade cloud infrastructure**

</div>
