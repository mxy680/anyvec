import os
import pytest
from anyvec.models import VectorizationPayload
from anyvec.client import AnyVecClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CODE_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets", "code")

def list_code_files():
    return [
        f for f in os.listdir(CODE_ASSETS_DIR)
        if os.path.isfile(os.path.join(CODE_ASSETS_DIR, f))
    ]

@pytest.fixture(scope="module")
def test_client():
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client is not None
    return client

@pytest.mark.parametrize("code_file", list_code_files())
def test_vectorize_code_file(test_client, code_file):
    file_path = os.path.join(CODE_ASSETS_DIR, code_file)
    assert os.path.exists(file_path), f"Test code file not found: {file_path}"
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name=code_file)
    result = test_client.vectorize(payload)
    assert result is not None
