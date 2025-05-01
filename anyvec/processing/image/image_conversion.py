"""
Functions for converting various image mime types/extensions to PNG bytes.
Handles plugin registration for special formats (HEIF/HEIC/AVIF).
"""

import io
from PIL import Image

# Register plugins for HEIF/HEIC/AVIF
import pillow_heif
import pillow_avif

pillow_heif.register_heif_opener()
pillow_avif.__version__


def image_bytes_to_png_bytes(image_bytes: bytes) -> bytes:
    """
    Convert any supported image bytes to PNG bytes.
    Raises UnidentifiedImageError if format not supported by Pillow/plugins.
    """
    image = Image.open(io.BytesIO(image_bytes))
    png_buffer = io.BytesIO()
    image.save(png_buffer, format="PNG")
    return png_buffer.getvalue()
