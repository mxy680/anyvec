from anyvec.tests import test_all


class AnyVecClient:
    def __init__(self, url: str, **kwargs):
        """
        Initialize the AnyVec client for Weaviate.

        Args:

        """
        self.url = url

        # Run tests on clip-inference endpoint
        test_all(url)
