import os
import pytest
from anyvec.client import AnyVecClient
from anyvec.models import VectorizationPayload
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

video_files = os.listdir("test/assets/videos")


@pytest.fixture(scope="module")
def test_client():
    url = os.getenv("CLIP_INFERENCE_URL")
    client = AnyVecClient(url)
    return client

@pytest.mark.parametrize("filename", video_files)
def test_vectorize_video_formats(test_client, filename):
    path = os.path.join("test/assets/videos", filename)
    assert os.path.exists(path), f"Test video not found: {path}"
    with open(path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name=filename)
    result = test_client.vectorize(payload)
    assert result is not None
