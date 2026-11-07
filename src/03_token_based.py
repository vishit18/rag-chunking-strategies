from pathlib import Path
import tiktoken


# ============================================================
# STEP 1 — LOAD
# ============================================================

text = Path("data/sample.txt").read_text(
    encoding="utf-8"
)


# ============================================================
# STEP 2 — LOAD TOKENIZER
# ============================================================

encoding = tiktoken.get_encoding("cl100k_base")


# ============================================================
# STEP 3 — TOKENIZE
# ============================================================

tokens = encoding.encode(text)

print("=" * 60)
print("03 — TOKEN-BASED CHUNKING")
print("=" * 60)

print(f"Characters: {len(text)}")
print(f"Tokens:     {len(tokens)}")


# ============================================================
# STEP 4 — DEFINE LIMIT
# ============================================================

max_tokens = 100

print(f"Max tokens per chunk: {max_tokens}")


# ============================================================
# STEP 5 — INITIALIZE
# ============================================================

chunks = []

start = 0
chunk_number = 1


# ============================================================
# STEP 6 — SELECT TOKENS
# ============================================================

while start < len(tokens):

    end = min(
        start + max_tokens,
        len(tokens)
    )

    chunk_tokens = tokens[start:end]


    # ========================================================
    # STEP 7 — DECODE TOKENS
    # ========================================================

    chunk_text = encoding.decode(chunk_tokens)


    # ========================================================
    # STEP 8 — CREATE CHUNK
    # ========================================================

    chunks.append({
        "chunk_id": chunk_number,
        "token_start": start,
        "token_end": end,
        "token_count": len(chunk_tokens),
        "text": chunk_text,
        "reason": "Token limit reached"
    })

    print("\n" + "-" * 60)

    print(f"Chunk {chunk_number}")

    print(
        f"Tokens: {start} → {end}"
    )

    print(
        f"Token count: {len(chunk_tokens)}"
    )

    print(
        "\nWHY DID IT SPLIT?\n"
        f"The chunk reached the {max_tokens}-token limit."
    )

    print("\nTEXT:")
    print(chunk_text)


    # ========================================================
    # STEP 9 — MOVE POINTER
    # ========================================================

    start = end
    chunk_number += 1


# ============================================================
# STEP 10 — SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print(f"Total chunks: {len(chunks)}")