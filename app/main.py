from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agentic AI to review the code of any programming language ")
app.include_router(router)

@app.get("/")
async def root():
    return {        
        "message": "Agentic AI Code Review API Running"
    }
