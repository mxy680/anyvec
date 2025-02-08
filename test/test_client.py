import os
import pytest
from anyvec.client import AnyVecClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="module")
def test_client():
    """
    Returns a test client connected to the existing Weaviate instance.
    """
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client is not None
    return client


def test_vectorize(test_client):
    """
    Test the vectorize method of the AnyVecClient.
    """
    text, images = test_client.vectorize(
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "anyclip-inference-test.pdf"
    )
    print(text, images)