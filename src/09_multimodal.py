from pathlib import Path
import fitz
from utils import save_json

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "data" / "sample.pdf"
OUT = ROOT / "outputs" / "09_multimodal" / "images"
OUT.mkdir(parents=True, exist_ok=True)

pdf = fitz.open(str(PDF))
results = []

for page_number, page in enumerate(pdf, start=1):
    for image_number, image in enumerate(page.get_images(full=True)):
        xref = image[0]
        data = pdf.extract_image(xref)
        extension = data["ext"]
        filename = f"page_{page_number}_image_{image_number}.{extension}"
        path = OUT / filename
        path.write_bytes(data["image"])

        results.append({
            "type": "image",
            "page": page_number,
            "image_path": str(path.relative_to(ROOT)),
            "vision_description": None,
            "note": "Pass this image to a vision model and store its description/caption here.",
        })

pdf.close()
save_json("09_multimodal", "images.json", results)
