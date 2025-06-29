import os
from pathlib import Path
from dotenv import load_dotenv
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.qdrant import Qdrant
from agno.vectordb.search import SearchType
from agno.document.chunking.recursive import RecursiveChunking
# Load environment variables
load_dotenv(override=True)

# Setup chunking, vector DB, and reader
chunking = RecursiveChunking(chunk_size=1500, overlap=200)
reader = PDFReader(chunk=True)

vector_db = Qdrant(
    collection="legaldocxindex",
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    search_type=SearchType.hybrid,
    timeout=360.0
)

# Point to your folder
base_dir = Path("uploaded_docs")
inputs = []

# Add PDFs in the base directory
for pdf in base_dir.glob("*.pdf"):
    inputs.append({
        "path": str(pdf),
        "metadata": {"category": base_dir.name, "source": pdf.name}
    })

# Add PDFs in any subfolders
for folder in base_dir.iterdir():
    if folder.is_dir():
        for pdf in folder.glob("*.pdf"):
            inputs.append({
                "path": str(pdf),
                "metadata": {"category": folder.name, "source": pdf.name}
            })

# Final knowledge base object to be imported elsewhere
kb = PDFKnowledgeBase(
    path=[],
    reader=reader,
    vector_db=vector_db,
    chunking_strategy=chunking,
    num_documents=3,
)

# Ingest only when running this file directly
if __name__ == "__main__":
    print(f"🗂 Found {len(inputs)} PDFs for ingestion.")
    if inputs:
        kb.path=inputs
        kb.load(recreate=False, upsert=True)
        print("[✅] Ingestion complete.")
    else:
        print("[⚠️] No PDFs found.")

