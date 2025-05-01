import io
import base64
import requests
from .image_conversion import image_bytes_to_png_bytes

def ocr_and_vectorize_image_bytes(file_bytes: bytes, file_name: str, ocr_url: str):
    """
    Converts image bytes to PNG, sends PNG to OCR endpoint, and returns OCR text and base64 PNG for vectorization.
    Returns: (ocr_text, [image_b64], ocr_text)
    """
    # Convert any image bytes to PNG bytes using the conversion utility
    png_bytes = image_bytes_to_png_bytes(file_bytes)

    # Send PNG to OCR endpoint
    files = {
        "file": (
            file_name if file_name.endswith(".png") else file_name + ".png",
            io.BytesIO(png_bytes),
            "image/png",
        )
    }
    response = requests.post(ocr_url, files=files)
    response.raise_for_status()
    ocr_text = response.text.strip()

    # Base64 encode the PNG image for vectorization
    image_b64 = base64.b64encode(png_bytes).decode("utf-8")
    return (ocr_text, [image_b64], ocr_text)
