import os
import requests
from anyvec.exceptions import InvalidFileInputError, InvalidFileURLError

import base64


def b64encode_bytes(data_bytes: bytes) -> str:
    """Base64-encode bytes and return as utf-8 string."""
    return base64.b64encode(data_bytes).decode("utf-8")


def resolve_file_to_bytes(file: str | bytes) -> bytes:
    """
    Given a file as a path/URL (str) or bytes, return the file as bytes.
    Raises InvalidFileInputError if not a valid URL or file path,
    and InvalidFileURLError if the URL is unreachable.
    """
    if isinstance(file, bytes):
        return file
    if isinstance(file, str):
        if file.startswith("http://") or file.startswith("https://"):
            try:
                response = requests.get(file)
                response.raise_for_status()
                return response.content
            except requests.exceptions.RequestException as e:
                raise InvalidFileURLError(file, str(e))
        else:
            if os.path.isfile(file):
                with open(file, "rb") as f:
                    return f.read()
            else:
                raise InvalidFileInputError(file)
    else:
        raise InvalidFileInputError(file)
