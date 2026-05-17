from fastapi import FastAPI

app = FastAPI(title="Agentic AI to review the code of any programming language ")

@app.get("/")
async def root():
    return {        
        "message": "Agentic AI Code Review API Running"
    }