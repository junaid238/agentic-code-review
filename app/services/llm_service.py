import os
from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI # commenting since limit is exceeded for open ai 
from langchain_groq import ChatGroq

load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def generate_review(prompt: str):

    response = llm.invoke(prompt)

    return response.content