"""
Rituximab RAG - FastAPI Web Server
Run locally: uvicorn app:app --reload
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Rituximab Patient Assistant")

@app.get("/", response_class=HTMLResponse)
def home():
    html = Path("web_ui.html").read_text()
    return HTMLResponse(content=html)

@app.get("/health")
def health():
    return {"status": "ok", "app": "Rituximab RAG Assistant"}
