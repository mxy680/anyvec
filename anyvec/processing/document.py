import pdfplumber
import io


def extract_text_plain(buffer: bytes) -> str:
    return buffer.decode("utf-8")


def extract_text_pdf(buffer: bytes) -> str:
    with pdfplumber.open(io.BytesIO(buffer)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text
