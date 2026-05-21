# from langchain_community.embeddings import HuggingFaceEmbeddings

# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# replacing with openAI embedding to resolve Docker install issues (package downloads failed)

# from langchain_openai import OpenAIEmbeddings

# embedding_model = OpenAIEmbeddings()

from langchain_community.embeddings import FastEmbedEmbeddings


embedding_model = FastEmbedEmbeddings()