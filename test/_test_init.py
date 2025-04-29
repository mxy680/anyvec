import os
import pytest
from anyvec.client import AnyVecClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_client_init():
    # This will initialize the client. It will raise if connection fails or on init error.
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client.url == os.getenv("CLIP_INFERENCE_URL")
