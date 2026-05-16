from fastapi import APIRouter, File, UploadFile
import os
from app.services.upload_service import save_uploaded_file
from app.services.knowledge_service import knowledge_service

router = APIRouter(prefix="/api")

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1].lower()
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_location, "wb") as f:
        f.write(await file.read())

    if ext in ["csv", "xlsx"]:
        # ✅ Save full CSV/Excel data to JSON
        data = save_uploaded_file(file_location)
        return {
            "message": "✅ Spreadsheet uploaded successfully",
            "columns": list(data[0].keys()) if data else [],
            "row_count": len(data)
        }
    
    elif ext in ["pdf", "docx", "txt"]:
        try:
            result = knowledge_service.process_file(file_location, ext)
            return {"message": result, "filename": file.filename}
        except Exception as e:
            return {"error": f"❌ Failed to process document: {str(e)}"}

    return {"error": "❌ Unsupported file format"}
