"""PDF conversion utilities for various document types."""

from .document_ocr import ocr_pdf_bytes
from .doc_mime_maps import document_can_store_images
from .document_office import convert_office_to_pdf
from weasyprint import HTML
import markdown
from ebooklib import epub
import fitz  # PyMuPDF


def extract_text_from_pdf_buffer(pdf_buffer: bytes) -> str:
    """
    Extract text from a PDF buffer (bytes).
    Returns all text from all pages as a single string.
    Requires PyMuPDF (fitz).
    """
    pdf = fitz.open(stream=pdf_buffer, filetype="pdf")
    text = []
    for page in pdf:
        text.append(page.get_text())
    return "\n".join(text)


def extract_images_from_pdf_buffer(pdf_buffer: bytes):
    """
    Extract images from a PDF buffer (bytes).
    Returns a list of dicts with keys: 'image_bytes', 'ext', 'page', 'xref'.
    Requires PyMuPDF (fitz).
    """
    images = []
    pdf = fitz.open(stream=pdf_buffer, filetype="pdf")
    for page_index in range(len(pdf)):
        page = pdf[page_index]
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            images.append(
                {
                    "image_bytes": image_bytes,
                    "ext": ext,
                    "page": page_index,
                    "xref": xref,
                }
            )
    return images


def convert_markdown_to_pdf(buffer: bytes) -> bytes:
    """
    Convert Markdown bytes to PDF bytes using WeasyPrint.
    """
    html = markdown.markdown(buffer.decode("utf-8"))
    pdf_bytes = HTML(string=html).write_pdf()
    return pdf_bytes


def convert_epub_to_pdf(buffer: bytes) -> bytes:
    """
    Convert EPUB bytes to PDF bytes using WeasyPrint.
    """
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".epub", delete=False) as tmp:
        tmp.write(buffer)
        tmp.flush()
        tmp_path = tmp.name
    try:
        book = epub.read_epub(tmp_path)
        html_content = ""
        from ebooklib import ITEM_DOCUMENT

        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                html_content += item.get_content().decode("utf-8")
        pdf_bytes = HTML(string=html_content).write_pdf()
        return pdf_bytes
    finally:
        import os

        os.remove(tmp_path)


def convert_to_pdf(buffer: bytes, ext: str, ocr: bool, ocr_url: str) -> dict:
    """
    Convert a document (buffer, ext) to PDF and optionally perform OCR.
    Returns a dict: {"pdf_bytes": ..., "ocr_text": ...} if ocr is True, else {"pdf_bytes": ...}
    Only for documents that CAN store images (per document_can_store_images).
    """
    if ext not in document_can_store_images:
        raise NotImplementedError(
            f"Conversion to PDF is only supported for documents that can store images. '{ext}' cannot store images."
        )
    if ext == ".pdf":
        pdf_bytes = buffer
    elif ext in {
        ".doc",
        ".docx",
        ".docm",
        ".dotx",
        ".dotm",
        ".ppt",
        ".pptx",
        ".ppsx",
        ".pptm",
        ".odt",
        ".odp",
        ".xls",
        ".xlsx",
        ".ods",
    }:
        pdf_bytes = convert_office_to_pdf(buffer, ext)
    elif ext == ".md":
        pdf_bytes = convert_markdown_to_pdf(buffer)
    elif ext == ".epub":
        pdf_bytes = convert_epub_to_pdf(buffer)
    else:
        raise NotImplementedError(f"Unsupported file type for PDF conversion: {ext}")

    result = {"pdf_bytes": pdf_bytes}
    if ocr:
        ocr_text = ocr_pdf_bytes(pdf_bytes, ocr_url=ocr_url)
        result["ocr_text"] = ocr_text
    return result
