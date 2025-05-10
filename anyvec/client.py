from anyvec.tests import test_all
from anyvec.processing.processor import Processor
from anyvec.vectorization import Vectorizer
from anyvec.vectorization import cosine_similarity
from anyvec.models import VectorizationPayload
from anyvec.exceptions import (
    MissingFileNameError,
    InsufficientInputError,
    EmptyFileError,
)


class AnyVecClient:
    """
    A client for interacting with the AnyVec API.

    Args:
        url (str): The base URL of the AnyVec server.
        **kwargs: Additional parameters for future extensions.
    """

    def __init__(self, url: str, **kwargs):
        self.url = url
        self._run_tests()
        self.processor = Processor(self, url=self.url)
        self.vectorizer = Vectorizer(self)

    def _run_tests(self):
        """Run tests on the clip-inference endpoint."""
        test_all(self.url)

    def vectorize(self, request: VectorizationPayload, ocr: bool = True):
        """
        Vectorizes a file or text and stores it in Weaviate.

        Args:
            request (VectorizationRequest): The vectorization request object.

        Returns:
            dict: Success status and collection name.

        Raises:
            InsufficientInputError: If no valid input is provided.
            MissingFileNameError: If file_name is required but missing.
        """

        # Validate input
        try:
            request.validate()
        except ValueError as e:
            if "file_name" in str(e):
                raise MissingFileNameError()
            else:
                raise InsufficientInputError()

        # Process text directly if provided
        if request.text_content:
            text = request.text_content
            images = []  # No image processing needed
        else:
            # Infer OCR URL from self.url
            text, images = self.processor.process(
                request.file_content or request.file_url,
                file_name=request.file_name,
                ocr=ocr,
            )


        if not text and not images:
            raise EmptyFileError()

        # Vectorize and store in Weaviate
        return self.vectorizer.vectorize(text, images)

    def compare(self, vector1: list[float], vector2: list[float]):
        """
        Compares two vectors and returns the similarity score.

        Args:
            vector1 (list[float]): The first vector.
            vector2 (list[float]): The second vector.

        Returns:
            float: The similarity score.
        """
        return cosine_similarity(vector1, vector2)
