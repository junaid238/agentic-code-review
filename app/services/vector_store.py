import os

from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.services.embedding_service import embedding_model


DATA_PATH = "app/data/standards"
CHROMA_PATH = "chroma_db"


def load_documents():

    documents = []

    for filename in os.listdir(DATA_PATH):

        file_path = os.path.join(DATA_PATH, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

            documents.append(text)

    return documents


def build_vector_store():

    documents = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.create_documents(documents)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    vector_store.persist()

    return vector_store