from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.parser import parse_python_file

router = APIRouter()

UPLOAD_DIR = "app/data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed_data = parse_python_file(file_path)

    return {
        "filename": file.filename,
        "parsed_data": parsed_data
    }