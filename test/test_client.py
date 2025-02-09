import os
import pytest
from anyvec.client import AnyVecClient
from anyvec.models import VectorizationPayload
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


def test_vectorize_text(test_client):
    payload = VectorizationPayload(text_content="Hello, world!")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_file(test_client):
    # Open a file in binary mode
    file_name = "test/data/lab.pdf"
    with open(file_name, "rb") as file:
        payload = VectorizationPayload(file_content=file.read(), file_name=file_name)
        result = test_client.vectorize(payload)
        assert result is not None


def test_one_to_one(test_client):
    payload1 = VectorizationPayload(text_content="Dog")
    payload2 = VectorizationPayload(text_content="Dog")
    result1 = test_client.vectorize(payload1)
    result2 = test_client.vectorize(payload2)
    assert result1 == result2


def test_similarity_text(test_client):
    payloads = [
        VectorizationPayload(text_content="Dog"),
        VectorizationPayload(text_content="Cat"),
        VectorizationPayload(text_content="Elevator"),
    ]

    results = [test_client.vectorize(payload) for payload in payloads]

    # Calculate cosine similarity
    similarities = [
        test_client.compare(results[0], results[1]),
        test_client.compare(results[1], results[2]),
        test_client.compare(results[0], results[2]),
    ]

    assert similarities[0] > similarities[1]
    assert similarities[0] > similarities[2]


def test_similarity_images(test_client):
    payloads = [
        VectorizationPayload(
            file_content=open("test/data/images/dog.png", "rb").read(),
            file_name="dog.png",
        ),
        VectorizationPayload(
            file_content=open("test/data/images/cat.png", "rb").read(),
            file_name="cat.png",
        ),
        VectorizationPayload(
            file_content=open("test/data/images/elevator.png", "rb").read(),
            file_name="elevator.png",
        ),
    ]

    results = [test_client.vectorize(payload) for payload in payloads]

    # Calculate cosine similarity
    similarities = [
        test_client.compare(results[0], results[1]),  # Dog vs Cat
        test_client.compare(results[1], results[2]),  # Cat vs Elevator
        test_client.compare(results[0], results[2]),  # Dog vs Elevator
    ]

    assert similarities[0] > similarities[1]
    assert similarities[0] > similarities[2]
