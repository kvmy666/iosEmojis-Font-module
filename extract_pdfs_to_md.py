import pdfplumber
import os

PDF_DIR = "/root/.claude/uploads/83193016-a359-4c13-a70f-6e9fec4d3dab/"

PDFS = [
    ("0fed5d8b-Lec1__Introduction_to_Apache_HTTP_Server.pdf",           "Chapter 1: Introduction to Apache HTTP Server"),
    ("1a25a545-Lec_2__Installing_Apache_on_Linux_and_Windows.pdf",      "Chapter 2: Installing Apache on Linux and Windows"),
    ("d3e51541-Lec_3__Configuration_files.pdf",                         "Chapter 3: Configuration Files"),
    ("45e5ca23-Lec_4__Virtual_Hosts.pdf",                               "Chapter 4: Virtual Hosts"),
    ("21c41277-Chapter_5_SSL_Configuration.pdf",                        "Chapter 5: SSL Configuration"),
    ("bf3d2f90-Chapter_6_Configure_Apache_as_forward_proxy_server.pdf", "Chapter 6: Forward Proxy Server"),
    ("549b5098-Chapter_7_Configure_Apache_as_backward_proxy_server.pdf","Chapter 7: Reverse Proxy Server"),
    ("6072c7c5-Chapter_8_display_server_statistics.pdf",                "Chapter 8: Display Server Statistics"),
]

output = []

for filename, title in PDFS:
    path = os.path.join(PDF_DIR, filename)
    print(f"Extracting: {title}")
    output.append(f"\n# {title}\n")
    try:
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text and text.strip():
                    output.append(text.strip())
                output.append("\n---\n")
        print(f"  -> OK ({len(pdf.pages)} pages)")
    except Exception as e:
        print(f"  -> ERROR: {e}")
        output.append(f"[Error extracting {filename}: {e}]\n")

out_path = "apache_full_notes.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"\nDone. Output: {out_path} ({os.path.getsize(out_path):,} bytes)")
