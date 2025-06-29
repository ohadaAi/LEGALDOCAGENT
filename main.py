from agent import answer
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils import handle_file_upload
app = FastAPI(title="Legal Rag Bot")


@app.post("/v1/query")
async def queries(question:str):
    response = answer(question)
    return response

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        result = handle_file_upload(file)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
