class AnyVecError(Exception):
    """Base exception for AnyVec-related errors."""

    pass

class InvalidFileInputError(AnyVecError):
    """Raised when a string is neither a valid URL nor a file path."""
    def __init__(self, file):
        super().__init__(f"Provided string is neither a valid URL nor a file path: {file}")

class InvalidFileURLError(AnyVecError):
    """Raised when a file URL is not reachable or invalid."""
    def __init__(self, url, message=None):
        msg = message or f"Provided URL is not reachable or invalid: {url}"
        super().__init__(msg)
        self.url = url


class APIConnectionError(AnyVecError):
    """Raised when there is an issue connecting to the API."""

    def __init__(self, url, message="Failed to connect to API"):
        super().__init__(f"{message}: {url}")
        self.url = url


class APIVectorizationError(AnyVecError):
    """Raised when vectorization fails."""

    def __init__(self, url, response, message="Vectorization failed"):
        super().__init__(f"{message}: {url}, Response: {response}")
        self.url = url
        self.response = response


class APIResponseError(AnyVecError):
    """Raised when an API request returns an unexpected status code."""

    def __init__(
        self, url, status_code, response_body, message="Unexpected API response"
    ):
        super().__init__(
            f"{message}: {url}, Status: {status_code}, Response: {response_body}"
        )
        self.url = url
        self.status_code = status_code
        self.response_body = response_body


class APIMissingVectorError(AnyVecError):
    """Raised when expected vectors are missing from the API response."""

    def __init__(
        self, url, expected_texts, expected_images, actual_texts, actual_images
    ):
        message = (
            f"Vectorization mismatch at {url}.\n"
            f"Expected text vectors: {expected_texts}, got {actual_texts}\n"
            f"Expected image vectors: {expected_images}, got {actual_images}"
        )
        super().__init__(message)
        self.url = url
        self.expected_texts = expected_texts
        self.expected_images = expected_images
        self.actual_texts = actual_texts
        self.actual_images = actual_images


class VectorizationError(Exception):
    """Base exception for vectorization errors."""

    pass


class MissingFileNameError(VectorizationError):
    """Raised when file_name is missing for file-based processing."""

    def __init__(self):
        super().__init__("file_name is required when passing file_content or file_url.")


class InsufficientInputError(VectorizationError):
    """Raised when no valid input is provided."""

    def __init__(self):
        super().__init__(
            "Provide at least one of text_content, file_content, or file_url."
        )


class EmptyFileError(VectorizationError):
    """Raised when no valid input is provided."""

    def __init__(self):
        super().__init__("No valid input provided.")


class UnsupportedFileTypeError(VectorizationError):
    """Raised when an unsupported file type is provided."""

    def __init__(self, file_type):
        super().__init__(f"Unsupported file type: {file_type}")
