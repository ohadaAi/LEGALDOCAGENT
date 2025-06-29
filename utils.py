from ingest import kb

from fastapi import UploadFile
import shutil
from pathlib import Path
UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)

def handle_file_upload(file: UploadFile):
    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Prepare metadata
    new_doc = [{
        "path": str(file_path),
        "metadata": {
            "category": "uploaded_docs",
            "source": file.filename
        }
    }]
    
    # Load the new document into the vector DB
    kb.path = new_doc
    kb.load(recreate=False, upsert=True)
    return {"status": "success", "filename": file.filename}
