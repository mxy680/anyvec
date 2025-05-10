import os
from .document.doc_mime_maps import document_mime_types, document_can_store_images
from .document.document_extract import extract_text_simple_doc
from .image.image_mime_maps import image_extensions
from .utils import resolve_file_to_bytes
from anyvec.processing.document.document_pdf_to_vec import pdf_document_to_vectors
from anyvec.processing.video.extract_video import (
    extract_audio_from_video,
    send_audio_to_transcription_server,
    extract_and_ocr_video_frames,
)

from .code.code_mime_maps import code_extensions
from .code.code_vectorize import extract_text_from_code_file
from .audio.audio_mime_maps import audio_extensions
from .audio.audio_transcribe import transcribe_audio_bytes
from anyvec.processing.video.video_mime_maps import video_extensions


class Processor:
    def __init__(self, client, url):
        """
        :param client: AnyVecClient or similar
        :param url: Base URL for the API (e.g., http://localhost:8000)
        """
        self.client = client
        self.url = url

    def process(
        self, file: str | bytes, file_name: str, ocr: bool
    ) -> tuple[str, list[bytes]]:
        try:
            ext = os.path.splitext(file_name)[1].lower()
        except Exception as e:
            raise RuntimeError(
                f"Failed to extract extension from file name '{file_name}': {e}"
            )

        # Always resolve file to bytes (handles str/bytes/url/path)
        try:
            file = resolve_file_to_bytes(file)
        except Exception as e:
            raise RuntimeError(
                f"Failed to resolve file to bytes for '{file_name}': {e}"
            )

        if ext in code_extensions:
            try:
                text = extract_text_from_code_file(file, ext)
                return (text, [])
            except Exception as e:
                raise RuntimeError(
                    f"Code file text extraction failed for '{file_name}': {e}"
                )

        if ext in audio_extensions:
            try:
                text = transcribe_audio_bytes(file, ext, self.url)
                return (text, [])
            except Exception as e:
                raise RuntimeError(f"Audio transcription failed for '{file_name}': {e}")

        if ext in video_extensions:
            try:
                # 1. Extract audio from video bytes and transcribe
                audio_bytes = extract_audio_from_video(file, ext)
                transcription_url = self.url.rstrip("/") + "/transcribe"
                transcript_response = send_audio_to_transcription_server(
                    audio_bytes, transcription_url
                )
                transcript = (
                    transcript_response.get("text")
                    or transcript_response.get("transcript")
                    or str(transcript_response)
                )
                # 2. Extract frames and OCR text using helper
                ocr_text, frames = extract_and_ocr_video_frames(file, ext)
                # 3. Combine transcript and OCR text
                if transcript and ocr_text:
                    combined_text = f"{transcript}\n{ocr_text}"
                else:
                    combined_text = transcript or ocr_text
                return (combined_text, frames)

            except Exception as e:
                raise RuntimeError(f"Video processing failed for '{file_name}': {e}")

        if ext in image_extensions:
            try:
                ocr_endpoint = self.url.rstrip("/") + "/ocr"
                from anyvec.processing.image.image_ocr_and_vectorize import (
                    ocr_and_vectorize_image_bytes,
                )

                ocr_text, image_b64_list, _ = ocr_and_vectorize_image_bytes(
                    file, file_name, ocr_endpoint
                )
                return (ocr_text, image_b64_list)
            except Exception as e:
                raise RuntimeError(f"Image processing failed for '{file_name}': {e}")

        if ext in document_mime_types:
            can_images = document_can_store_images.get(ext, False)
            if can_images:
                try:
                    ocr_endpoint = self.url.rstrip("/") + "/ocr"
                    text, images, _ = pdf_document_to_vectors(
                        file, ext, ocr, ocr_endpoint
                    )
                    return (text, images)
                except Exception as e:
                    raise RuntimeError(
                        f"Document-to-PDF processing failed for '{file_name}': {e}"
                    )
            else:
                try:
                    text = extract_text_simple_doc(file, ext)
                    return (text, [])
                except Exception as e:
                    raise RuntimeError(
                        f"Simple document text extraction failed for '{file_name}': {e}"
                    )
        else:
            raise RuntimeError(f"Unsupported file type: {ext} for file '{file_name}'")
