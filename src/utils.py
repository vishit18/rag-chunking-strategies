import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"

def save_json(method: str, filename: str, data):
    out_dir = OUTPUTS / method
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {path}")

def read_pdf_text(pdf_path: str):
    import fitz
    pdf = fitz.open(str(pdf_path))
    pages = []
    for i, page in enumerate(pdf):
        pages.append({
            "page": i + 1,
            "text": page.get_text("text")
        })
    pdf.close()
    return pages
