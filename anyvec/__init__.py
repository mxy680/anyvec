# AnyVec package root

_registry = {}

def register(mime_type):
    """
    Decorator to register a new modality (MIME type) with a preprocessor and encoder endpoint.
    Usage:
        @register("model/obj")
        def my_preprocessor(file_bytes):
            ...
            return text, images
    """
    def decorator(preprocessor):
        _registry[mime_type] = preprocessor
        return preprocessor
    return decorator


def get_registered_handler(mime_type):
    return _registry.get(mime_type)

# Expose for downstream usage
__all__ = ["register", "get_registered_handler"]
