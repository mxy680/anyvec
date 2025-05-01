# Maps for document mime types and whether they can store images

# Map: extension (with dot) -> mime type (string)
document_mime_types = {
    ".txt": "text/plain",
    ".rtf": "application/rtf",
    ".md": "text/markdown",
    ".doc": "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".odt": "application/vnd.oasis.opendocument.text",
    ".pdf": "application/pdf",
    ".ppt": "application/vnd.ms-powerpoint",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".xls": "application/vnd.ms-excel",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".odp": "application/vnd.oasis.opendocument.presentation",
    ".ods": "application/vnd.oasis.opendocument.spreadsheet",
    ".epub": "application/epub+zip",
    ".ppsx": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
    ".dotm": "application/vnd.ms-word.template.macroEnabled.12",
    ".dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
    ".docm": "application/vnd.ms-word.document.macroEnabled.12",
    ".pptm": "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
}

# Map: extension (with dot) -> whether the document type can store images
# (True = can store images, False = cannot)
document_can_store_images = {
    ".txt": False,
    ".rtf": False,
    ".md": True,
    ".doc": True,
    ".docx": True,
    ".odt": True,
    ".pdf": True,
    ".ppt": True,
    ".pptx": True,
    ".xls": True,
    ".xlsx": True,
    ".odp": True,
    ".ods": True,
    ".epub": True,
    ".ppsx": True,
    ".dotm": True,
    ".dotx": True,
    ".docm": True,
    ".pptm": True,
}
