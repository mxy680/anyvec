"""
Functions for extracting text from code files for vectorization.
Code files cannot store images, so only text is extracted.
"""

def extract_text_from_code_file(buffer: bytes, ext: str) -> str:
    """
    Extract text from code files (source code, scripts, notebooks, etc.).
    Accepts file as bytes and the file extension.
    Returns decoded text (UTF-8, fallback to latin-1 if needed).
    """
    try:
        return buffer.decode("utf-8")
    except UnicodeDecodeError:
        return buffer.decode("latin-1", errors="ignore")
