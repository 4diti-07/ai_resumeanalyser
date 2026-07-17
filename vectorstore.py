"""
vectorstore.py

Loads the Chroma vector database.
"""

from langchain_chroma import Chroma

from embeddings import get_embedding_model


DB_PATH = "chroma_db"


def load_vectorstore():
    """
    Loads the Chroma vector database.
    """

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embedding_model()
    )