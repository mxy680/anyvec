"""Markdown to PDF conversion."""

def convert_markdown_to_pdf(buffer: bytes) -> bytes:
    """
    Convert Markdown bytes to PDF using markdown and pdfkit.
    """
    try:
        import markdown
        import pdfkit
        html = markdown.markdown(buffer.decode("utf-8", errors="ignore"))
        pdf_bytes = pdfkit.from_string(html, False)
        return pdf_bytes
    except ImportError:
        raise RuntimeError("markdown and pdfkit must be installed to convert .md to PDF")
