from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.parser import parse_python_file
from app.services.reviewer import review_code
from app.graph.workflow import graph

router = APIRouter()

UPLOAD_DIR = "app/data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed_data = parse_python_file(file_path)
    initial_state = {
    "code": parsed_data["raw_code"],
    "context": "",
    "security_review": "",
    "performance_review": "",
    "style_review": "",
    "final_review": ""
}

    result = graph.invoke(initial_state)
    return {
        "filename": file.filename,
        "parsed_data": parsed_data,
        "final_review": result["final_review"]
    }