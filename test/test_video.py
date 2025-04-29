import os
import pytest
from anyvec.processing.processor import Processor

video_files = os.listdir("test/assets/videos")


@pytest.mark.parametrize("filename", video_files)
def test_vectorize_video_formats(filename):
    path = os.path.join("test/assets/videos", filename)
    assert os.path.exists(path), f"Test video not found: {path}"
    with open(path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, filename)
    # Text: should be a string (possibly empty if no audio)
    assert isinstance(text, str)
    # Images: should be a non-empty list of base64 PNG strings
    assert isinstance(images, list)
    assert len(images) > 0
    for img in images:
        assert isinstance(img, str)
        assert len(img) > 0
