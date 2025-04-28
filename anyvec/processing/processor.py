import requests
import mimetypes
from typing import Union
import base64

from anyvec.processing.document import (
    extract_text_plain,
    extract_text_pdf,
    extract_text_docx_like,
    extract_text_ps,
)
from anyvec.processing.image import extract_images_pdf
from anyvec.exceptions import UnsupportedFileTypeError


class Processor:
    def __init__(self, client):
        self.client = client

    def process(self, file: str | bytes, file_name: str) -> Union[str, bytes]:
        # Get the file file_bytes
        if isinstance(file, str):
            response = requests.get(file, stream=True)

            if response.status_code != 200:
                raise Exception(f"Failed to download file from {file}")

            file_bytes = response.content
        elif isinstance(file, bytes):
            file_bytes = file

        # Get the mime type
        mime_type = mimetypes.guess_type(file_name)[0]

        # Robust handling for Word formats (Python 3.13 workaround)
        if mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # .docx
            return extract_text_docx_like(file_bytes), []
        elif mime_type in (
            "application/vnd.openxmlformats-officedocument.wordprocessingml.template",  # .dotx
            "application/vnd.ms-word.template.macroenabled.12",  # .dotm
            "application/vnd.ms-word.document.macroenabled.12",  # .docm
        ):
            from anyvec.processing.document import extract_text_mammoth
            return extract_text_mammoth(file_bytes), []

        match mime_type:
            case "text/plain":
                return extract_text_plain(file_bytes), []

            case "application/pdf":
                return extract_text_pdf(file_bytes), extract_images_pdf(file_bytes)

            case "application/rtf":
                return extract_text_plain(file_bytes), []

            case "text/html":
                return extract_text_plain(file_bytes), []

            case "text/markdown":
                return extract_text_plain(file_bytes), []

            case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":  # .xlsx
                from anyvec.processing.document import extract_text_xlsx
                return extract_text_xlsx(file_bytes), []

            case "application/vnd.ms-excel":  # .xls
                from anyvec.processing.document import extract_text_xls
                return extract_text_xls(file_bytes), []

            case "application/vnd.oasis.opendocument.text":  # .odt
                from anyvec.processing.document import extract_text_odt
                return extract_text_odt(file_bytes), []

            case "application/vnd.oasis.opendocument.spreadsheet":  # .ods
                from anyvec.processing.document import extract_text_ods
                return extract_text_ods(file_bytes), []

            case "application/vnd.oasis.opendocument.presentation":  # .odp
                from anyvec.processing.document import extract_text_odp
                return extract_text_odp(file_bytes), []

            case ("application/vnd.openxmlformats-officedocument.presentationml.presentation"  # .pptx
                  | "application/vnd.openxmlformats-officedocument.presentationml.slideshow"  # .ppsx
                  | "application/vnd.ms-powerpoint.presentation.macroenabled.12"):  # .pptm
                from anyvec.processing.document import extract_text_pptx_like
                return extract_text_pptx_like(file_bytes), []

            case "application/vnd.ms-powerpoint":  # .ppt
                from anyvec.processing.document import extract_text_ppt
                try:
                    return extract_text_ppt(file_bytes), []
                except NotImplementedError:
                    raise UnsupportedFileTypeError(".ppt extraction is not supported. Consider converting to .pptx.")

            case "application/epub+zip":  # .epub
                from anyvec.processing.document import extract_text_epub
                return extract_text_epub(file_bytes), []

            case "application/postscript":  # .ps
                return extract_text_ps(file_bytes), []

            case "image/png":
                return "", [base64.b64encode(file_bytes).decode("utf-8")]

            case _:
                raise UnsupportedFileTypeError(mime_type)

