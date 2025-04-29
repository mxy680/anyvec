import os
import pytest
from anyvec.processing.processor import Processor

CODE_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets", "code")

# List all files in the code assets directory
def list_code_files():
    return [
        f for f in os.listdir(CODE_ASSETS_DIR)
        if os.path.isfile(os.path.join(CODE_ASSETS_DIR, f))
    ]

@pytest.mark.parametrize("code_file", list_code_files())
def test_vectorize_code_file(code_file):
    file_path = os.path.join(CODE_ASSETS_DIR, code_file)
    assert os.path.exists(file_path), f"Test code file not found: {file_path}"
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, code_file)
    assert isinstance(text, str)
    assert text.strip() != ""  # Should extract some text
    assert isinstance(images, list)
    assert images == []  # Code files should not produce images
