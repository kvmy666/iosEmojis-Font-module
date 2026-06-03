#!/bin/bash
# Install dependencies, extract PDFs → MD, create Word summary → PDF

set -e

echo "=== Installing Python dependencies ==="
pip install -q pdfplumber python-docx weasyprint cffi Pillow

echo "=== Step 1: Extract all PDFs → apache_full_notes.md ==="
python3 extract_pdfs_to_md.py

echo "=== Step 2: Create Word summary ==="
python3 create_summary_docx.py

echo "=== Step 3: Create PDF (WeasyPrint) ==="
python3 create_pdf_direct.py

echo ""
echo "Done!"
ls -lh apache_full_notes.md apache_summary.docx apache_summary.html apache_summary.pdf
