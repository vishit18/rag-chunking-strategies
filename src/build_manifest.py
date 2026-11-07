from pathlib import Path
import json
from utils import OUTPUTS, save_json

methods = [
    "01_fixed_size",
    "02_recursive",
    "03_sentence",
    "04_semantic",
    "05_markdown",
    "06_page",
    "07_elements",
    "08_parent_child",
    "09_multimodal",
]

manifest = []

for method in methods:
    directory = OUTPUTS / method
    if not directory.exists():
        continue

    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            count = len(data) if isinstance(data, list) else len(data)
        except Exception:
            count = None

        manifest.append({
            "method": method,
            "file": str(path.relative_to(OUTPUTS.parent)),
            "items_or_keys": count,
        })

save_json("comparison", "manifest.json", manifest)
print("\nGenerated comparison manifest.")
