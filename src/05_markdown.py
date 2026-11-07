from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter
from utils import save_json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "sample.md"

markdown = SOURCE.read_text(encoding="utf-8")

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "title"),
        ("##", "section"),
    ],
    strip_headers=False,
)

documents = splitter.split_text(markdown)

output = [
    {
        "chunk_id": i,
        "text": doc.page_content,
        "metadata": doc.metadata,
    }
    for i, doc in enumerate(documents)
]

save_json("05_markdown", "output.json", output)
