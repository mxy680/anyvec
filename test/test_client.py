import os
from anyvec.client import AnyVecClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_client():
    """
    Returns a test client connected to the existing Weaviate instance.
    """
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client is not None
