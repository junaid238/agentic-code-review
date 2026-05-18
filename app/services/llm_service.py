import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def generate_review(prompt: str):

    response = llm.invoke(prompt)

    return response.content