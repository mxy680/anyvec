import requests
import fitz  # PyMuPDF
import io


def ocr_pdf_bytes(pdf_bytes: bytes, ocr_url: str) -> str:
    """
    Split PDF into images (one per page), send each image to the /ocr endpoint, concatenate results.
    """
    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    all_text = []
    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        pix = page.get_pixmap(dpi=300)
        img_bytes = pix.tobytes("png")
        files = {"file": (f"page_{page_num+1}.png", io.BytesIO(img_bytes), "image/png")}
        response = requests.post(ocr_url, files=files)
        response.raise_for_status()
        all_text.append(response.text.strip())
    return "\n".join(all_text)
