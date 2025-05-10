from anyvec.processing.document.document_pdf import (
    convert_to_pdf,
    extract_images_from_pdf_buffer,
    extract_text_from_pdf_buffer,
)
from anyvec.processing.utils import b64encode_bytes


def pdf_document_to_vectors(file: bytes, ext: str, ocr: bool, ocr_url: str):
    """
    Convert a document to PDF (with optional OCR), extract images and text, and return for vectorization.
    Returns: (extracted_text, image_bytes_list, ocr_text). Most callers only use the first two values.
    """
    # Convert to PDF (with optional OCR)
    pdf_result = convert_to_pdf(file, ext, ocr=ocr, ocr_url=ocr_url)
    pdf_bytes = pdf_result["pdf_bytes"]
    ocr_text = pdf_result.get("ocr_text")
    # Extract images from PDF
    images = extract_images_from_pdf_buffer(pdf_bytes)
    image_bytes_list = [b64encode_bytes(img["image_bytes"]) for img in images]
    # Extract text from PDF
    extracted_text = extract_text_from_pdf_buffer(pdf_bytes)
    return (extracted_text, image_bytes_list, ocr_text)
