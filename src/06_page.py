from pathlib import Path
from utils import read_pdf_text, save_json

PDF = Path(__file__).resolve().parents[1] / "data" / "sample.pdf"

pages = read_pdf_text(PDF)

output = [
    {
        "chunk_id": f"page_{p['page']}",
        "type": "page",
        "page": p["page"],
        "text": p["text"],
    }
    for p in pages
]

save_json("06_page", "output.json", output)
