import requests
import mimetypes
from typing import Union
import base64

from anyvec.processing.document import extract_text_plain
from anyvec.exceptions import UnsupportedFileTypeError
from anyvec.processing.filetype_maps import (
    mime_handlers,
    image_mime_types,
    code_file_exts,
)


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

        if mime_type in mime_handlers.keys():
            text_extractor, image_extractor = mime_handlers[mime_type]
            return text_extractor(file_bytes), image_extractor(file_bytes)
        elif mime_type in image_mime_types:
            # For standard image formats, the image is the file itself. Return as base64.
            return "", [base64.b64encode(file_bytes).decode("utf-8")]
        elif file_name.lower().endswith(code_file_exts):
            return extract_text_plain(file_bytes), []
        else:
            raise UnsupportedFileTypeError(mime_type)
