"""
build_db.py

Indexes all PDF documents inside
knowledge_base/
"""

import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from embeddings import get_embedding_model


KNOWLEDGE_BASE = "knowledge_base"

DB_PATH = "chroma_db"


documents = []

for file in os.listdir(KNOWLEDGE_BASE):

    if file.endswith(".pdf"):

        loader = PyPDFLoader(
            os.path.join(
                KNOWLEDGE_BASE,
                file
            )
        )

        documents.extend(loader.load())


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

Chroma.from_documents(
    documents=chunks,
    embedding=get_embedding_model(),
    persist_directory=DB_PATH
)

print()

print("=" * 50)

print("Knowledge Base Created Successfully!")

print("=" * 50)

print(f"Documents Indexed : {len(chunks)}")