"""Text extraction for simple documents (txt, rtf, etc.)."""
from striprtf.striprtf import rtf_to_text

def extract_text_simple_doc(buffer: bytes, ext: str) -> str:
    """
    Extract text from documents that cannot store images (like .txt or .rtf).
    Accepts file as bytes and the file extension.
    """
    if ext == ".txt":
        return buffer.decode("utf-8", errors="ignore")
    elif ext == ".rtf":
        rtf_content = buffer.decode("utf-8", errors="ignore")
        return rtf_to_text(rtf_content)
    else:
        return ""
