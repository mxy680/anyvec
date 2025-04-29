import os
from anyvec.processing.processor import Processor


def test_vectorize_mp3_audio():
    wav_path = "test/assets/audio/Hi there this is you.mp3"
    assert os.path.exists(wav_path), f"Test audio not found: {wav_path}"
    with open(wav_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "Hi there this is you.mp3")
    print(text)
    assert isinstance(text, str)
    assert text.strip() != ""
    assert images == []
