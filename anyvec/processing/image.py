import fitz
import base64


def extract_images_pdf(buffer: bytes) -> list[bytes]:
    images: list[bytes] = []
    pdf_document = fitz.open("pdf", buffer)
    for page in pdf_document:
        for _, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_buffer = base_image["image"]
            encoded_image_buffer = base64.b64encode(image_buffer).decode("utf-8")
            images.append(encoded_image_buffer)

    return images
