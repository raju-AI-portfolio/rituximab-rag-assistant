"""
Step 2: Document Processor & Chunker
Loads all raw documents, cleans them, splits into chunks,
and saves processed chunks ready for the vector database.
Run: python3 src/ingestion/step2_process.py
"""

import json, re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

RAW_DIR  = Path.home() / "Documents/rituximab_rag/data/raw"
PROC_DIR = Path.home() / "Documents/rituximab_rag/data/processed"
PROC_DIR.mkdir(parents=True, exist_ok=True)

CHUNK_SIZE    = 500   # characters per chunk
CHUNK_OVERLAP = 80    # overlap between chunks

@dataclass
class Chunk:
    chunk_id:    str
    source:      str
    category:    str
    text:        str
    char_count:  int
    chunk_index: int

def clean_text(text: str) -> str:
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = text.strip()
    return text

def chunk_text(text: str) -> List[str]:
    chunks, start = [], 0
    while start < len(text):
        end = start + CHUNK_SIZE
        if end >= len(text):
            chunks.append(text[start:].strip())
            break
        # Find clean break point
        for sep in ['\n\n', '.\n', '. ']:
            pos = text.rfind(sep, start + CHUNK_SIZE // 2, end)
            if pos != -1:
                end = pos + len(sep)
                break
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - CHUNK_OVERLAP
    return chunks

def detect_category(fname: str) -> str:
    f = fname.lower()
    if 'fda' in f or 'label' in f or 'rituxan' in f:  return 'fda_label'
    if 'nccn' in f or 'guideline' in f:                return 'clinical_guidelines'
    if 'pubmed' in f or 'abstract' in f:               return 'research_abstracts'
    if 'medline' in f or 'patient' in f:               return 'patient_education'
    if 'trial' in f or 'clinical' in f:                return 'clinical_trials'
    if 'adverse' in f or 'event' in f:                 return 'adverse_events'
    return 'general'

def load_file(fpath: Path) -> str:
    suffix = fpath.suffix.lower()
    if suffix == '.pdf':
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(fpath))
            return '\n'.join(page.extract_text() or '' for page in reader.pages)
        except Exception as e:
            print(f"  PDF error: {e}")
            return ''
    elif suffix == '.json':
        try:
            data = json.loads(fpath.read_text(encoding='utf-8'))
            # Flatten JSON to readable text
            lines = []
            studies = data.get('studies', data.get('results', [data]))
            for item in (studies if isinstance(studies, list) else [studies]):
                for k, v in (item.items() if isinstance(item, dict) else []):
                    lines.append(f"{k}: {v}")
                lines.append('---')
            return '\n'.join(lines)
        except:
            return fpath.read_text(encoding='utf-8', errors='ignore')
    else:
        return fpath.read_text(encoding='utf-8', errors='ignore')

def process_all() -> List[Chunk]:
    all_chunks = []
    files = sorted(RAW_DIR.glob('*'))
    files = [f for f in files if f.suffix.lower() in ('.txt','.pdf','.json','.html')]

    print(f"Found {len(files)} documents in data/raw/\n")

    for fpath in files:
        print(f"Processing: {fpath.name}")
        raw = load_file(fpath)
        if not raw.strip():
            print(f"  Skipped (empty)\n")
            continue

        cleaned  = clean_text(raw)
        category = detect_category(fpath.name)
        chunks   = chunk_text(cleaned)

        print(f"  Category : {category}")
        print(f"  Length   : {len(cleaned):,} chars")
        print(f"  Chunks   : {len(chunks)}")

        for i, text in enumerate(chunks):
            all_chunks.append(Chunk(
                chunk_id    = f"{fpath.stem}_chunk_{i:04d}",
                source      = fpath.name,
                category    = category,
                text        = text,
                char_count  = len(text),
                chunk_index = i,
            ))
        print(f"  Done ✅\n")

    return all_chunks

def save(chunks: List[Chunk]):
    out = PROC_DIR / 'rituximab_chunks.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump([asdict(c) for c in chunks], f, indent=2, ensure_ascii=False)
    print(f"Saved {len(chunks)} chunks → {out}")

    # Summary
    from collections import Counter
    cats = Counter(c.category for c in chunks)
    print(f"\nChunks by category:")
    for cat, n in sorted(cats.items()):
        print(f"  {cat:<25} {n} chunks")

if __name__ == '__main__':
    print("="*50)
    print("  Rituximab RAG — Step 2: Processing")
    print("="*50 + "\n")
    chunks = process_all()
    save(chunks)
    avg = sum(c.char_count for c in chunks) / len(chunks)
    print(f"\n{'='*50}")
    print(f"  Total chunks : {len(chunks)}")
    print(f"  Avg size     : {avg:.0f} chars")
    print(f"  Output       : data/processed/")
    print("="*50)
