# Maps for image mime types and extensions

image_mime_types = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".jpe": "image/jpeg",
    ".bmp": "image/bmp",
    ".gif": "image/gif",
    ".tiff": "image/tiff",
    ".ico": "image/x-icon",
    ".icns": "image/icns",
    ".heic": "image/heic",
    ".avif": "image/avif",
    ".webp": "image/webp",
    ".psd": "image/vnd.adobe.photoshop",
}

image_extensions = set(image_mime_types.keys())
