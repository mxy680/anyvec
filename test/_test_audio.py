import os
from anyvec.processing.processor import Processor


import pytest

from anyvec.processing.processor import Processor
import os

audio_files = os.listdir("test/assets/audio")


@pytest.mark.parametrize("filename", audio_files)
def test_vectorize_audio_formats(filename):
    path = os.path.join("test/assets/audio", filename)
    assert os.path.exists(path), f"Test audio not found: {path}"
    with open(path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, filename)
    assert isinstance(text, str)
    assert text.strip() != ""
    assert images == []
