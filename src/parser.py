import pdfplumber
from docx import Document
import re

def clean_text(text):
    """Cleans up raw text extracted from documents."""
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_text_from_pdf(file_or_bytes):
    text = ""
    with pdfplumber.open(file_or_bytes) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return clean_text(text)

def extract_text_from_docx(file_or_bytes):
    doc = Document(file_or_bytes)
    text = "\n".join([para.text for para in doc.paragraphs])
    return clean_text(text)