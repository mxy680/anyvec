import base64
import os
from anyvec.processing.processor import Processor


def test_vectorize_png_image():
    png_path = "test/assets/images/1721257650_animate_o_sample.png"
    assert os.path.exists(png_path), f"Test image not found: {png_path}"
    with open(png_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "1721257650_animate_o_sample.png")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_avif_image():
    avif_path = "test/assets/images/1718924786_hato.profile0.8bpc.yuv420.monochrome.no-cdef.avif"
    assert os.path.exists(avif_path), f"Test image not found: {avif_path}"
    with open(avif_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(
        file_bytes, "1718924786_hato.profile0.8bpc.yuv420.monochrome.no-cdef.avif"
    )
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_bmp_image():
    bmp_path = "test/assets/images/1718889054_sample_640×426.bmp"
    assert os.path.exists(bmp_path), f"Test image not found: {bmp_path}"
    with open(bmp_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "1718889054_sample_640×426.bmp")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_gif_image():
    gif_path = "test/assets/images/bird-wings-flying-feature.gif"
    assert os.path.exists(gif_path), f"Test image not found: {gif_path}"
    with open(gif_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "bird-wings-flying-feature.gif")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_heif_image():
    heif_path = "test/assets/images/1718889539_sample1.heif"
    assert os.path.exists(heif_path), f"Test image not found: {heif_path}"
    with open(heif_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "1718889539_sample1.heif")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_heic_image():
    heic_path = "test/assets/images/1718889515_sample1.heic"
    assert os.path.exists(heic_path), f"Test image not found: {heic_path}"
    with open(heic_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "1718889515_sample1.heic")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1


def test_vectorize_ico_image():
    ico_path = "test/assets/images/1718880897_941pL.ico"
    assert os.path.exists(ico_path), f"Test image not found: {ico_path}"
    with open(ico_path, "rb") as f:
        file_bytes = f.read()
    processor = Processor(client=object())
    text, images = processor.process(file_bytes, "sample.ico")
    assert text == ""
    assert isinstance(images, list)
    assert len(images) == 1
