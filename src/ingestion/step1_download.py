import os, json, time, requests
from pathlib import Path
from tqdm import tqdm

RAW = Path.home() / "Documents/rituximab_rag/data/raw"
RAW.mkdir(parents=True, exist_ok=True)

def download_pubmed(n=50):
    print("\n[1/3] PubMed abstracts...")
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    query = "rituximab[MeSH] AND (clinical trial[pt] OR adverse effects[sh] OR patient education[MeSH])"
    r = requests.get(base+"esearch.fcgi", params={"db":"pubmed","term":query,"retmax":n,"retmode":"json"})
    pmids = r.json()["esearchresult"]["idlist"]
    print(f"  Found {len(pmids)} papers")
    time.sleep(0.5)
    r2 = requests.get(base+"efetch.fcgi", params={"db":"pubmed","id":",".join(pmids),"rettype":"abstract","retmode":"text"})
    (RAW/"pubmed_abstracts.txt").write_text(r2.text, encoding="utf-8")
    print(f"  Saved pubmed_abstracts.txt ({len(r2.text)//1024} KB)")

def download_trials(n=25):
    print("\n[2/3] ClinicalTrials.gov...")
    r = requests.get("https://clinicaltrials.gov/api/v2/studies", params={
        "query.term":"rituximab","filter.overallStatus":"COMPLETED","pageSize":n})
    data = r.json()
    (RAW/"clinical_trials.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"  Saved clinical_trials.json ({len(data.get('studies',[]))} trials)")

def download_openfda():
    print("\n[3/3] OpenFDA adverse events...")
    r = requests.get("https://api.fda.gov/drug/event.json", params={
        "search":'patient.drug.openfda.generic_name:"RITUXIMAB"',
        "count":"patient.reaction.reactionmeddrapt.exact","limit":30})
    data = r.json()
    (RAW/"adverse_events.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"  Saved adverse_events.json ({len(data.get('results',[]))} reactions)")

print("="*50)
print("  Rituximab RAG — Step 1: Downloading Data")
print("="*50)
download_pubmed()
download_trials()
download_openfda()

files = list(RAW.glob("*"))
print(f"\n{'='*50}")
print(f"  Done! {len(files)} files in data/raw/")
for f in files:
    print(f"  {f.name}  ({f.stat().st_size//1024} KB)")
print("="*50)
