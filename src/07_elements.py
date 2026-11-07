from pathlib import Path
import pymupdf

from utils import save_json


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "data" / "sample.pdf"


pdf = pymupdf.open(str(PDF))

output = []


for page_number, page in enumerate(pdf, start=1):

    # --------------------------------------------------
    # TEXT BLOCKS
    # --------------------------------------------------

    blocks = page.get_text("blocks")

    for block_number, block in enumerate(blocks):

        x0, y0, x1, y1, text, *_ = block

        text = text.strip()

        if not text:
            continue

        output.append({
            "element_id":
                f"page_{page_number}_text_{block_number}",

            "type":
                "text",

            "page":
                page_number,

            "bbox": {
                "x0": round(x0, 2),
                "y0": round(y0, 2),
                "x1": round(x1, 2),
                "y1": round(y1, 2)
            },

            "text":
                text
        })


    # --------------------------------------------------
    # IMAGES
    # --------------------------------------------------

    images = page.get_images(full=True)

    for image_number, image in enumerate(images):

        xref = image[0]

        image_info = pdf.extract_image(xref)

        output.append({
            "element_id":
                f"page_{page_number}_image_{image_number}",

            "type":
                "image",

            "page":
                page_number,

            "xref":
                xref,

            "width":
                image_info["width"],

            "height":
                image_info["height"],

            "extension":
                image_info["ext"]
        })


    # --------------------------------------------------
    # DRAWINGS
    # --------------------------------------------------

    drawings = page.get_drawings()

    if drawings:

        output.append({
            "element_id":
                f"page_{page_number}_drawings",

            "type":
                "drawing",

            "page":
                page_number,

            "count":
                len(drawings)
        })


pdf.close()


save_json(
    "07_elements",
    "output.json",
    output
)