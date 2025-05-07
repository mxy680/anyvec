"""
Functions for converting various image mime types/extensions to PNG bytes.
Handles plugin registration for special formats (HEIF/HEIC/AVIF).
"""

import io
from PIL import Image, UnidentifiedImageError

import pillow_heif
import pillow_avif

pillow_heif.register_heif_opener()
pillow_avif.__version__


def image_bytes_to_png_bytes(image_bytes: bytes) -> bytes:
    """
    Convert any supported image bytes to PNG bytes using Pillow.
    Raises RuntimeError if format not supported by Pillow/plugins or conversion fails.
    """
    import logging

    try:
        image = Image.open(io.BytesIO(image_bytes))
    except UnidentifiedImageError as e:
        logging.error(f"Unidentified image format: {e}")
        raise RuntimeError(f"Unidentified image format: {e}")
    except Exception as e:
        logging.error(f"Error opening image: {e}")
        raise RuntimeError(f"Error opening image: {e}")
    # Convert to RGB if needed
    try:
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")
    except Exception as e:
        logging.error(f"Failed to convert image mode: {e}")
        raise RuntimeError(f"Failed to convert image mode: {e}")
    try:
        png_buffer = io.BytesIO()
        image.save(png_buffer, format="PNG")
        return png_buffer.getvalue()
    except Exception as e:
        logging.error(f"Failed to save image as PNG: {e}")
        raise RuntimeError(f"Failed to save image as PNG: {e}")
