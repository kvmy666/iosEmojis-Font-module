"""
Extract highlighted text from DS Chapter PDFs.
Colors: green (30), red (4), yellow (6) = 40 total.
Also extracts all plain text per chapter for full notes.
"""
import fitz  # PyMuPDF
import os
import json

PDF_DIR = "/root/.claude/uploads/ca553555-cd29-5783-b4d9-921ffa4bffcf/"

PDFS = [
    ("ae279915-DSChapter_1fin.pdf",  "Chapter 1"),
    ("b84e8f27-DSChapter_2fin.pdf",  "Chapter 2"),
    ("a39eaf45-DSChapter_3fin.pdf",  "Chapter 3"),
    ("5c520a14-DSChapter_4fin.pdf",  "Chapter 4"),
    ("f9bff6e6-DSChapter_5fin.pdf",  "Chapter 5"),
    ("9d392223-DSChapter_6fin.pdf",  "Chapter 6"),
    ("c65a1369-DSChapter_7fin.pdf",  "Chapter 7"),
    ("a050377f-DSChapter_8fin.pdf",  "Chapter 8"),
    ("3b2bc961-DSChapter_9fin.pdf",  "Chapter 9"),
    ("73ef2226-DSChapter_10fin.pdf", "Chapter 10"),
]

def classify_color(rgb):
    """Return 'green', 'red', 'yellow', or 'other' from a 0-1 float RGB tuple."""
    if rgb is None:
        return "other"
    r, g, b = rgb
    # Yellow: high R+G, low B
    if r > 0.7 and g > 0.7 and b < 0.4:
        return "yellow"
    # Green: high G, low R+B
    if g > 0.5 and r < 0.5 and b < 0.5:
        return "green"
    # Also handle lime/bright green
    if g > 0.7 and r < 0.7:
        return "green"
    # Red: high R, low G+B
    if r > 0.6 and g < 0.4 and b < 0.4:
        return "red"
    return "other"


highlights = {"green": [], "red": [], "yellow": [], "other": []}
full_text_by_chapter = {}

for filename, chap_name in PDFS:
    path = os.path.join(PDF_DIR, filename)
    print(f"\n{'='*50}")
    print(f"Processing: {chap_name} ({filename})")

    doc = fitz.open(path)
    chap_text_pages = []

    for page_num, page in enumerate(doc, 1):
        # Extract plain text
        text = page.get_text("text")
        chap_text_pages.append(f"--- Page {page_num} ---\n{text}")

        # Extract annotations (highlights)
        for annot in page.annots():
            if annot.type[0] not in (8, 9, 10, 11):  # highlight types
                continue

            color_rgb = annot.colors.get("stroke") or annot.colors.get("fill")
            color_name = classify_color(color_rgb)

            # Extract the highlighted text
            rect = annot.rect
            words = page.get_text("words")
            highlighted_words = []
            for w in words:
                wr = fitz.Rect(w[:4])
                if rect.intersects(wr):
                    highlighted_words.append(w[4])

            highlighted_text = " ".join(highlighted_words).strip()
            if not highlighted_text:
                # fallback: get text blocks in rect area
                blocks = page.get_text("blocks", clip=rect)
                highlighted_text = " ".join(b[4].strip() for b in blocks).strip()

            if highlighted_text:
                entry = {
                    "chapter": chap_name,
                    "page": page_num,
                    "color": color_name,
                    "color_rgb": color_rgb,
                    "text": highlighted_text
                }
                highlights[color_name].append(entry)
                print(f"  [{color_name}] p{page_num}: {highlighted_text[:80]}...")

    full_text_by_chapter[chap_name] = "\n".join(chap_text_pages)
    doc.close()
    print(f"  -> Annotations found: G={sum(1 for h in highlights['green'] if h['chapter']==chap_name)}, "
          f"R={sum(1 for h in highlights['red'] if h['chapter']==chap_name)}, "
          f"Y={sum(1 for h in highlights['yellow'] if h['chapter']==chap_name)}")

# Save results
with open("ds_highlights.json", "w", encoding="utf-8") as f:
    json.dump(highlights, f, indent=2, ensure_ascii=False)

# Save full text MD
with open("ds_full_notes.md", "w", encoding="utf-8") as f:
    for chap_name, text in full_text_by_chapter.items():
        f.write(f"\n# {chap_name}\n\n{text}\n\n---\n")

print("\n\n=== SUMMARY ===")
print(f"Green highlights : {len(highlights['green'])}")
print(f"Red highlights   : {len(highlights['red'])}")
print(f"Yellow highlights: {len(highlights['yellow'])}")
print(f"Other/unknown    : {len(highlights['other'])}")
print(f"Total annotated  : {sum(len(v) for v in highlights.values())}")
print(f"\nSaved: ds_highlights.json, ds_full_notes.md")
