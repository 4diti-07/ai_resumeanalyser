"""
embeddings.py

Creates the embedding model used for RAG.
"""

from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Returns the embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )