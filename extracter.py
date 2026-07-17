"""
extracter.py

Extracts text from PDF resumes using PyMuPDF.
"""

import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF.

    Returns:
        str: Extracted text.
    """

    text = ""

    document = fitz.open(pdf_path)

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()