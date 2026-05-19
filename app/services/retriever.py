from langchain_community.vectorstores import Chroma

from app.services.embedding_service import embedding_model

CHROMA_PATH = "chroma_db"


vector_store = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)


def retrieve_context(query: str, k: int = 3):

    results = vector_store.similarity_search(query, k=k)

    contexts = []

    for result in results:
        contexts.append(result.page_content)

    return "\n".join(contexts)