import requests
import mimetypes
from typing import Union
import base64

from anyvec.processing.document import extract_text_plain, extract_text_pdf
from anyvec.processing.image import extract_images_pdf


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
        
        match mime_type:
            case "text/plain":
                return extract_text_plain(file_bytes), []

            case "application/pdf":
                return extract_text_pdf(file_bytes), extract_images_pdf(file_bytes)
            
            case "image/png":
                return "", [base64.b64encode(file_bytes).decode("utf-8")]

        return "", []
