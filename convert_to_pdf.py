import subprocess
import sys
import os


def convert_docx_to_pdf(docx_path, output_dir="."):
    abs_path = os.path.abspath(docx_path)
    abs_out  = os.path.abspath(output_dir)

    # Try docx2pdf first (uses LibreOffice under the hood on Linux)
    try:
        from docx2pdf import convert
        convert(abs_path, abs_out)
        print("Converted with docx2pdf")
        return
    except Exception as e:
        print(f"docx2pdf failed ({e}), trying LibreOffice directly...")

    # Fallback: direct LibreOffice call
    result = subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "pdf",
         "--outdir", abs_out, abs_path],
        capture_output=True,
        text=True,
        timeout=120
    )

    if result.returncode == 0:
        print("Converted with LibreOffice")
        print(result.stdout)
    else:
        print("LibreOffice error:", result.stderr)
        sys.exit(1)


convert_docx_to_pdf("apache_summary.docx", ".")
