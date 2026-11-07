from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils import read_pdf_text, save_json

PDF = Path(__file__).resolve().parents[1] / "data" / "sample.pdf"

pages = read_pdf_text(PDF)

parents = [
    {
        "parent_id": f"page_{p['page']}",
        "page": p["page"],
        "text": p["text"],
    }
    for p in pages
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
)

children = []

for parent in parents:
    chunks = splitter.split_text(parent["text"])
    for i, chunk in enumerate(chunks):
        children.append({
            "child_id": f"{parent['parent_id']}_{i}",
            "parent_id": parent["parent_id"],
            "page": parent["page"],
            "text": chunk,
        })

save_json("08_parent_child", "parents.json", parents)
save_json("08_parent_child", "children.json", children)
