from fastapi import APIRouter, File, UploadFile
import os
from app.services.upload_service import save_uploaded_file

router = APIRouter(prefix="/api")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in [
        "text/csv",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ]:
        return {"error": "Unsupported file type"}

    # ✅ Ensure upload directory exists
    os.makedirs("uploads", exist_ok=True)

    # ✅ Save file to uploads folder
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # ✅ Save full CSV/Excel data to JSON
    data = save_uploaded_file(file_location)

    return {
        "message": "✅ File uploaded successfully",
        "columns": list(data[0].keys()) if data else [],
        "row_count": len(data)
    }
