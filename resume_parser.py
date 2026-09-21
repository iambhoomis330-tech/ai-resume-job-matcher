import io
from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file):
    """Extract text from a PDF resume."""
    text = ""

    pdf_reader = PdfReader(file)

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_text_from_docx(file):
    """Extract text from a DOCX resume."""
    document = Document(file)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text).strip()


def extract_resume_text(uploaded_file):
    """Extract resume text based on file type."""

    if uploaded_file is None:
        raise ValueError("No resume file was uploaded.")

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )