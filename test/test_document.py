import os
import pytest
from anyvec.client import AnyVecClient
from anyvec.models import VectorizationPayload
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@pytest.fixture(scope="module")
def test_client():
    """
    Returns a test client connected to the existing Weaviate instance.
    """
    client = AnyVecClient(os.getenv("CLIP_INFERENCE_URL"))
    assert client is not None
    return client


def test_vectorize_text(test_client):
    payload = VectorizationPayload(text_content="Hello, world!")
    result = test_client.vectorize(payload)
    assert result is not None


def test_vectorize_local_pdf(test_client):
    pdf_path = "test/assets/documents/Test.pdf"
    with open(pdf_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.pdf")
    result = test_client.vectorize(payload)
    assert result is not None
    
def test_vectorize_local_txt(test_client):
    txt_path = "test/assets/documents/Test.txt"
    with open(txt_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.txt")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_rtf(test_client):
    rtf_path = "test/assets/documents/Test.rtf"
    with open(rtf_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.rtf")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_html(test_client):
    html_path = "test/assets/documents/Test.html"
    with open(html_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.html")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_md(test_client):
    md_path = "test/assets/documents/Test.md"
    with open(md_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.md")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_docx(test_client):
    docx_path = "test/assets/documents/Test.docx"
    with open(docx_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.docx")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_dotx(test_client):
    dotx_path = "test/assets/documents/Test.dotx"
    with open(dotx_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.dotx")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_dotm(test_client):
    dotm_path = "test/assets/documents/Test.dotm"
    with open(dotm_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.dotm")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_docm(test_client):
    docm_path = "test/assets/documents/Test.docm"
    with open(docm_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.docm")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_ps(test_client):
    ps_path = "test/assets/documents/Test.ps"
    with open(ps_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.ps")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_xlsx(test_client):
    xlsx_path = "test/assets/documents/Test.xlsx"
    with open(xlsx_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.xlsx")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_xls(test_client):
    xls_path = "test/assets/documents/Test.xls"
    with open(xls_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.xls")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_odt(test_client):
    odt_path = "test/assets/documents/Test.odt"
    with open(odt_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.odt")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_ods(test_client):
    ods_path = "test/assets/documents/Test.ods"
    with open(ods_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.ods")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_odp(test_client):
    odp_path = "test/assets/documents/Test.odp"
    with open(odp_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.odp")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_pptx(test_client):
    pptx_path = "test/assets/documents/Test.pptx"
    with open(pptx_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.pptx")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_pptm(test_client):
    pptm_path = "test/assets/documents/Test.pptm"
    with open(pptm_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.pptm")
    result = test_client.vectorize(payload)
    assert result is not None

def test_vectorize_local_ppsx(test_client):
    ppsx_path = "test/assets/documents/Test.ppsx"
    with open(ppsx_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.ppsx")
    result = test_client.vectorize(payload)
    assert result is not None

import pytest

def test_vectorize_local_ppt(test_client):
    ppt_path = "test/assets/documents/Test.ppt"
    with open(ppt_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.ppt")
    with pytest.raises(Exception):
        test_client.vectorize(payload)

def test_vectorize_local_epub(test_client):
    epub_path = "test/assets/documents/Test.epub"
    with open(epub_path, "rb") as f:
        file_content = f.read()
    payload = VectorizationPayload(file_content=file_content, file_name="Test.epub")
    result = test_client.vectorize(payload)
    assert result is not None

