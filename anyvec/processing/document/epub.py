"""EPUB to PDF conversion."""

def convert_epub_to_pdf(buffer: bytes) -> bytes:
    """
    Convert EPUB bytes to PDF using ebooklib, bs4, and pdfkit.
    """
    try:
        import tempfile
        import pdfkit
        from ebooklib import epub
        from bs4 import BeautifulSoup
        with tempfile.NamedTemporaryFile(delete=True, suffix=".epub") as tmp:
            tmp.write(buffer)
            tmp.flush()
            book = epub.read_epub(tmp.name)
            html = []
            for item in book.get_items():
                # 9 is ITEM_DOCUMENT
                if item.get_type() == 9:
                    soup = BeautifulSoup(item.get_content(), "html.parser")
                    html.append(soup.get_text(separator="<br>", strip=True))
            html_str = "<br>".join(html)
            pdf_bytes = pdfkit.from_string(html_str, False)
            return pdf_bytes
    except ImportError:
        raise RuntimeError("ebooklib, bs4, and pdfkit must be installed to convert .epub to PDF")
