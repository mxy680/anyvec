import os

from .document.doc_mime_maps import document_mime_types, document_can_store_images
from .document import extract_text_simple_doc
from .image.image_mime_maps import image_extensions
from .utils import resolve_file_to_bytes
from anyvec.processing.image.image_ocr_and_vectorize import (
    ocr_and_vectorize_image_bytes,
)
from anyvec.processing.document.document_pdf_to_vec import pdf_document_to_vectors


class Processor:
    def __init__(self, client):
        self.client = client

    def process(
        self, file: str | bytes, file_name: str, ocr: bool, ocr_url: str
    ) -> tuple[str, list[str], str | None]:
        try:
            ext = os.path.splitext(file_name)[1].lower()
        except Exception as e:
            raise RuntimeError(f"Failed to extract extension from file name '{file_name}': {e}")

        # Always resolve file to bytes (handles str/bytes/url/path)
        try:
            file = resolve_file_to_bytes(file)
        except Exception as e:
            raise RuntimeError(f"Failed to resolve file to bytes for '{file_name}': {e}")

        if ext in image_extensions:
            try:
                return ocr_and_vectorize_image_bytes(file, file_name, ocr_url)
            except Exception as e:
                raise RuntimeError(f"Image processing failed for '{file_name}': {e}")

        if ext in document_mime_types:
            can_images = document_can_store_images.get(ext, False)
            if can_images:
                try:
                    return pdf_document_to_vectors(file, ext, ocr, ocr_url)
                except Exception as e:
                    raise RuntimeError(f"Document-to-PDF processing failed for '{file_name}': {e}")
            else:
                try:
                    text = extract_text_simple_doc(file, ext)
                    return (text, [], None)
                except Exception as e:
                    raise RuntimeError(f"Simple document text extraction failed for '{file_name}': {e}")
        else:
            raise RuntimeError(f"Unsupported file type: {ext} for file '{file_name}'")
