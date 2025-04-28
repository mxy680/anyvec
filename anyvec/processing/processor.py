import requests
import mimetypes
from typing import Union
import base64

from anyvec.processing.document import (
    extract_text_plain,
    extract_text_pdf,
    extract_text_docx_like,
    extract_text_ps,
    extract_text_epub,
    extract_text_xlsx,
    extract_text_xls,
    extract_text_ods,
    extract_text_odt,
    extract_text_odp,
    extract_text_pptx_like,
    extract_text_ppt,
    extract_text_mammoth,
    extract_images_pdf,
    extract_images_docx,
    extract_images_pptx_like,
    extract_images_odt,
    extract_images_odp,
    extract_images_ods,
    extract_images_epub,
    extract_images_xlsx,
)
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
        match mime_type:
            # Word processing
            case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # .docx
                return extract_text_docx_like(file_bytes), extract_images_docx(file_bytes)
            case ("application/vnd.openxmlformats-officedocument.wordprocessingml.template"  # .dotx
                  | "application/vnd.ms-word.template.macroenabled.12"  # .dotm
                  | "application/vnd.ms-word.document.macroenabled.12"):  # .docm
                return extract_text_mammoth(file_bytes), []  # TODO: add images for dotx/dotm/docm if needed

            # Plain text and similar
            case "text/plain" | "application/rtf" | "text/html" | "text/markdown":
                return extract_text_plain(file_bytes), []

            # PDF
            case "application/pdf":
                return extract_text_pdf(file_bytes), extract_images_pdf(file_bytes)

            # Spreadsheets
            case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":  # .xlsx
                return extract_text_xlsx(file_bytes), extract_images_xlsx(file_bytes)
            case "application/vnd.ms-excel":  # .xls
                return extract_text_xls(file_bytes), []  # TODO: add images for .xls if needed
            case "application/vnd.oasis.opendocument.spreadsheet":  # .ods
                return extract_text_ods(file_bytes), extract_images_ods(file_bytes)

            # Word processing
            case "application/vnd.oasis.opendocument.text":  # .odt
                return extract_text_odt(file_bytes), extract_images_odt(file_bytes)

            # Presentations
            case "application/vnd.oasis.opendocument.presentation":  # .odp
                return extract_text_odp(file_bytes), extract_images_odp(file_bytes)
            case ("application/vnd.openxmlformats-officedocument.presentationml.presentation"  # .pptx
                  | "application/vnd.openxmlformats-officedocument.presentationml.slideshow"  # .ppsx
                  | "application/vnd.ms-powerpoint.presentation.macroenabled.12"):  # .pptm
                return extract_text_pptx_like(file_bytes), extract_images_pptx_like(file_bytes)
            case "application/vnd.ms-powerpoint":  # .ppt
                try:
                    return extract_text_ppt(file_bytes), []  # TODO: images for .ppt not implemented
                except NotImplementedError:
                    raise UnsupportedFileTypeError(".ppt extraction is not supported. Consider converting to .pptx.")

            # eBook
            case "application/epub+zip":  # .epub
                return extract_text_epub(file_bytes), extract_images_epub(file_bytes)

            # PostScript
            case "application/postscript":  # .ps
                return extract_text_ps(file_bytes), []

            # Images
            case "image/png":
                return "", [base64.b64encode(file_bytes).decode("utf-8")]

            # Fallback
            case _:
                raise UnsupportedFileTypeError(mime_type)
