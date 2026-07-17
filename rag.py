"""
rag.py

Retrieves relevant context from the
knowledge base.
"""

from vectorstore import load_vectorstore


def retrieve_context(query, k=3):
    """
    Retrieves relevant chunks from ChromaDB.

    Args:
        query (str)
        k (int)

    Returns:
        str
    """

    db = load_vectorstore()

    docs = db.similarity_search(query, k=k)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context