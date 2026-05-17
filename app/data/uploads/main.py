from fastapi import FastAPI, UploadFile, File
from app.graph.workflow import workflow
import shutil
import os
import asyncio

from app.services.parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
# from app.services.gemini_service import extract_resume_data
from app.utils.json_parser import safe_json_parse # this is replaced by langchain output parser in lc_llm_service.py

#using langchain , replacing gemini llm with langchain below 
from app.services.lc_llm_service import extract_resume_data

api_key = os.getenv("GROC_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "the resume analyzer is ready with first API"}

# @app.get("/test")
# def test():
#     return {"status": "working"}


UPLOAD_DIR ="uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# @app.post("/analyze-resume")
# async def analyze_resume(file: UploadFile = File(...)):
#     file_path = f"{UPLOAD_DIR}/{file.filename}"

#     # Save file
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Extract text (run in thread)
#     raw_text = await asyncio.to_thread(extract_text_from_pdf, file_path)

#     # Clean text
#     cleaned_text = clean_text(raw_text)
#     '''
#     # Gemini extraction , Parse JSON safely
#     llm_output = extract_resume_data(cleaned_text)
#     parsed_output = safe_json_parse(llm_output)

#     return {
#         "filename": file.filename,
#         "data": parsed_output
#     }
#     '''
#     #using langchain instead of gemini LLM per line 11 ,12
#     parsed_output = extract_resume_data(cleaned_text)

#     return {
#         "filename": file.filename,
#         "data": parsed_output
#     }
@app.post("/analyze-with-agents")
async def analyze_with_agents(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text = await asyncio.to_thread(
        extract_text_from_pdf,
        file_path
    )

    cleaned_text = clean_text(raw_text)

    # Example JD
    jd_text = """
    Looking for Python, FastAPI, Docker, SQL skills
    """

    initial_state = {
        "resume_text": cleaned_text,
        "jd_text": jd_text
    }

    result = workflow.invoke(initial_state)

    return result