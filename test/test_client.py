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


def test_vectorize_file_text(test_client):
    """
    Test the vectorization of a text file.
    """
    with open("test/data/document.txt", "rb") as file:
        vector = test_client.vectorize(file.read(), "test.txt")
        assert vector is not None and len(vector) == 512


def test_vectorize_pdf_file(test_client):
    """
    Test the vectorization of a PDF file.
    """
    with open("test/data/lab.pdf", "rb") as file:
        vector = test_client.vectorize(file.read(), "test.pdf")
        assert vector is not None and len(vector) == 512
