from anyvec.tests import test_all
from anyvec.processing.processor import Processor
from anyvec.vectorization.vectorizer import Vectorizer


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
        self.processor = Processor(self)
        self.vectorizer = Vectorizer(self)

    def _run_tests(self):
        """Run tests on the clip-inference endpoint."""
        test_all(self.url)

    def vectorize(self, file: str | bytes, file_name: str, **kwargs):
        """
        Vectorizes a file and stores it in Weaviate.

        Args:
            file (bytes | str): File buffer or https URL.
            fileName (str): Full file name (e.g., "document.pdf").
            **kwargs: Additional parameters.
        Returns:
            dict: Success status and collection name.
        """
        text, images = self.processor.process(file, file_name)
        vector = self.vectorizer.vectorize(text, images, file_name, **kwargs)
        return vector
