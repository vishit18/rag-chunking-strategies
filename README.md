# RAG Chunking Strategies

Hands-on, runnable examples of nine chunking strategies for Retrieval-Augmented Generation (RAG). Each script reads a sample document from `data/`, chunks it, and writes JSON to `outputs/` so the strategies can be compared side by side.

## Strategies

| # | Script | Strategy |
|---|--------|----------|
| 1 | `src/01_fixed_size.py` | Fixed-size character chunks |
| 2 | `src/02_fixed_overlap.py` | Fixed-size chunks with overlap (recursive splitter) |
| 3 | `src/03_token_based.py` | Token-based chunking |
| 4 | `src/04_sentence_window.py` | Sentence / semantic-window chunking |
| 5 | `src/05_markdown.py` | Markdown header-aware chunking |
| 6 | `src/06_page.py` | Page-based chunking for PDFs |
| 7 | `src/07_elements.py` | Element-based chunking (titles, paragraphs, lists) |
| 8 | `src/08_parent_child.py` | Parent-child (small-to-big) chunking |
| 9 | `src/09_multimodal.py` | Multimodal extraction (images from PDFs) |

`src/build_manifest.py` summarizes every method into `outputs/comparison/manifest.json`, and `src/utils.py` holds shared helpers.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run scripts from the repository root:

```bash
python src/01_fixed_size.py
python src/05_markdown.py
# ...
python src/build_manifest.py   # compare all methods
```

## Project layout

```
data/       sample.txt, sample.md, sample.pdf
src/        one script per strategy + utilities
outputs/    generated chunks (JSON) per strategy
```

## Choosing a strategy

- **Fixed-size / overlap**: simplest baseline; overlap preserves boundary context.
- **Token-based**: matches the embedding model's context limits.
- **Sentence / semantic**: keeps ideas intact at some compute cost.
- **Markdown / elements**: use document structure when it exists.
- **Page**: preserves provenance for citations in PDFs.
- **Parent-child**: retrieve small chunks, return larger context.
- **Multimodal**: for documents where images carry information.

## License

MIT
