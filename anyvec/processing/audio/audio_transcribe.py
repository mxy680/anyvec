"""
Audio transcription logic using the /transcribe API endpoint.
"""

import requests


def transcribe_audio_bytes(audio_bytes: bytes, ext: str, api_url: str) -> str:
    """
    Transcribe audio bytes by POSTing to the /transcribe endpoint of the API.
    Returns the transcribed text.
    :param audio_bytes: The raw audio bytes
    :param ext: The file extension (e.g., '.mp3')
    :param api_url: The base URL of the API (should not end with a slash)
    """
    files = {"file": (f"audio{ext}", audio_bytes)}
    endpoint = api_url.rstrip("/") + "/transcribe"
    resp = requests.post(endpoint, files=files, timeout=60)
    resp.raise_for_status()
    text = resp.json()["text"]
    return text
