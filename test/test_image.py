import os
import pytest
from anyvec.client import AnyVecClient
from anyvec.models import VectorizationPayload
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@pytest.fixture(scope="module")
def test_client():
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client is not None
    return client


def test_vectorize_png_image(test_client):
    png_path = "test/assets/images/1721257650_animate_o_sample.png"
    assert os.path.exists(png_path), f"Test image not found: {png_path}"
    with open(png_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(
        file_content=file_bytes, file_name="1721257650_animate_o_sample.png"
    )
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_avif_image(test_client):
    avif_path = "test/assets/images/1718924786_hato.profile0.8bpc.yuv420.monochrome.no-cdef.avif"
    assert os.path.exists(avif_path), f"Test image not found: {avif_path}"
    with open(avif_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(
        file_content=file_bytes,
        file_name="1718924786_hato.profile0.8bpc.yuv420.monochrome.no-cdef.avif",
    )
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_bmp_image(test_client):
    bmp_path = "test/assets/images/1718889054_sample_640×426.bmp"
    assert os.path.exists(bmp_path), f"Test image not found: {bmp_path}"
    with open(bmp_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(
        file_content=file_bytes, file_name="1718889054_sample_640×426.bmp"
    )
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_gif_image(test_client):
    gif_path = "test/assets/images/bird-wings-flying-feature.gif"
    assert os.path.exists(gif_path), f"Test image not found: {gif_path}"
    with open(gif_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(
        file_content=file_bytes, file_name="bird-wings-flying-feature.gif"
    )
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_heic_image(test_client):
    heic_path = "test/assets/images/1718889515_sample1.heic"
    assert os.path.exists(heic_path), f"Test image not found: {heic_path}"
    with open(heic_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(
        file_content=file_bytes, file_name="1718889515_sample1.heic"
    )
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_ico_image(test_client):
    ico_path = "test/assets/images/1718880897_941pL.ico"
    assert os.path.exists(ico_path), f"Test image not found: {ico_path}"
    with open(ico_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="favicon.ico")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_jpe_image(test_client):
    jpe_path = "test/assets/images/1718889688_sample_640×426.jpe"
    assert os.path.exists(jpe_path), f"Test image not found: {jpe_path}"
    with open(jpe_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.jpe")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_webp_image(test_client):
    webp_path = "test/assets/images/1718890746_sample1.webp"
    assert os.path.exists(webp_path), f"Test image not found: {webp_path}"
    with open(webp_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.webp")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_jpg_image(test_client):
    jpg_path = "test/assets/images/1718882001_Sample_2.jpg"
    assert os.path.exists(jpg_path), f"Test image not found: {jpg_path}"
    with open(jpg_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.jpg")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_jpeg_image(test_client):
    jpeg_path = "test/assets/images/1718882053_Sample_2.jpeg"
    assert os.path.exists(jpeg_path), f"Test image not found: {jpeg_path}"
    with open(jpeg_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.jpeg")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_icns_image(test_client):
    icns_path = "test/assets/images/1741149963_Adobe Edge Reflow.icns"
    assert os.path.exists(icns_path), f"Test image not found: {icns_path}"
    with open(icns_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.icns")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_psd_image(test_client):
    psd_path = "test/assets/images/1718890505_sample_640×426.psd"
    assert os.path.exists(psd_path), f"Test image not found: {psd_path}"
    with open(psd_path, "rb") as f:
        file_bytes = f.read()
    payload = VectorizationPayload(file_content=file_bytes, file_name="sample.psd")
    result = test_client.vectorize(payload)
    assert result is not None
