"""Office document to PDF conversion using LibreOffice."""
import tempfile
import subprocess
import os
import shutil
import sys

def find_libreoffice_executable():
    # macOS default install location
    macos_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    if sys.platform == "darwin" and os.path.exists(macos_path):
        return macos_path
    # Windows common install locations
    if sys.platform.startswith("win"):
        win_paths = [
            r"C:\\Program Files\\LibreOffice\\program\\soffice.exe",
            r"C:\\Program Files (x86)\\LibreOffice\\program\\soffice.exe"
        ]
        for path in win_paths:
            if os.path.exists(path):
                return path
    # Try to find 'libreoffice' or 'soffice' in PATH
    for exe in ["libreoffice", "soffice"]:
        path = shutil.which(exe)
        if path:
            return path
    raise FileNotFoundError(
        "LibreOffice executable not found. Please install LibreOffice and ensure it is in your PATH, in the default macOS location, or in the default Windows location."
    )

def convert_office_to_pdf(buffer: bytes, ext: str) -> bytes:
    """
    Convert supported office formats to PDF using LibreOffice (must be installed).
    Returns PDF bytes. Uses temporary files for input/output.
    """
    with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as src:
        src.write(buffer)
        src.flush()
        src_path = src.name
    out_dir = tempfile.mkdtemp()
    try:
        soffice_path = find_libreoffice_executable()
        subprocess.run([
            soffice_path, "--headless", "--convert-to", "pdf", src_path, "--outdir", out_dir
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pdf_path = os.path.join(out_dir, os.path.splitext(os.path.basename(src_path))[0] + ".pdf")
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        return pdf_bytes
    finally:
        try:
            os.remove(src_path)
        except Exception:
            pass
        try:
            os.remove(pdf_path)
        except Exception:
            pass
        try:
            os.rmdir(out_dir)
        except Exception:
            pass
