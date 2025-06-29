import os
from pathlib import Path
from dotenv import load_dotenv
from agno.knowledge.csv import CSVKnowledgeBase, CSVReader
from agno.vectordb.qdrant import Qdrant
from agno.document.chunking.recursive import RecursiveChunking

load_dotenv()

vector_db = Qdrant(
    collection="testingcsv",
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

chunking = RecursiveChunking(chunk_size=250, overlap=20)
reader = CSVReader(chunk=True)

csv_path = Path(r"C:\Users\touse\OneDrive\Desktop\RAG\University List for Different Courses 1.csv")
if not csv_path.exists():
    raise FileNotFoundError(f"{csv_path} not found!")

kb_csv = CSVKnowledgeBase(
    path=str(csv_path),
    reader=reader,
    vector_db=vector_db,
    chunking_strategy=chunking,
    num_documents=5,
)

print("📂 Loading CSV into knowledge base...")
kb_csv.load(recreate=True, upsert=True)
print("[✅] CSV ingestion complete!")
