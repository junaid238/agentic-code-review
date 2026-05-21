import os
from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI # commenting since limit is exceeded for open ai 
from langchain_groq import ChatGroq

load_dotenv(override=True)

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0
)
print(os.getenv("GROQ_API_KEY"))

def generate_review(prompt: str):

    response = llm.invoke(prompt)

    return response.content