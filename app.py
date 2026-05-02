from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Rituximab RAG — Pinecone Edition")

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content=Path("web_ui_v2.html").read_text()
                        if Path("web_ui_v2.html").exists()
                        else Path("web_ui.html").read_text())

@app.get("/health")
def health():
    return {
        "status":    "ok",
        "version":   "pinecone-edition",
        "db":        "pinecone",
        "index":     os.getenv("PINECONE_INDEX_NAME", "rituximab-rag"),
        "embedding": os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        "model":     os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    }

@app.post("/ask")
async def ask_endpoint(request: Request):
    try:
        from src.retrieval.step4_rag_pinecone import load_index, ask
        body  = await request.json()
        query = body.get("query", "").strip()
        if not query:
            return JSONResponse({"error": "No query provided"}, status_code=400)
        index  = load_index()
        result = ask(query, index)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
