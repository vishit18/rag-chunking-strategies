from pathlib import Path


# ============================================================
# STEP 1 — LOAD INPUT
# ============================================================

text = Path("data/sample.txt").read_text(encoding="utf-8")


# ============================================================
# STEP 2 — DEFINE UNIT
# ============================================================

# Unit = characters


# ============================================================
# STEP 3 — DEFINE PARAMETERS
# ============================================================

chunk_size = 300
overlap = 50

print("=" * 60)
print("02 — FIXED-SIZE CHUNKING WITH OVERLAP")
print("=" * 60)

print(f"Chunk size : {chunk_size}")
print(f"Overlap    : {overlap}")


# ============================================================
# STEP 4 — VALIDATE PARAMETERS
# ============================================================

if overlap >= chunk_size:
    raise ValueError(
        "Overlap must be smaller than chunk size."
    )


# ============================================================
# STEP 5 — INITIALIZE
# ============================================================

start = 0
chunk_number = 1

chunks = []


# ============================================================
# STEP 6 — PROCESS
# ============================================================

while start < len(text):

    end = min(
        start + chunk_size,
        len(text)
    )

    chunk = text[start:end]


    # ========================================================
    # STEP 7 — CREATE CHUNK
    # ========================================================

    chunks.append({
        "chunk_id": chunk_number,
        "start": start,
        "end": end,
        "text": chunk,
        "reason": "Fixed-size boundary"
    })

    print("\n" + "-" * 60)
    print(f"Chunk {chunk_number}")
    print("-" * 60)

    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Size: {len(chunk)}")

    print(
        "\nWHY DID IT SPLIT?\n"
        f"The chunk reached the {chunk_size}-character limit."
    )


    # ========================================================
    # STEP 8 — MOVE WITH OVERLAP
    # ========================================================

    next_start = end - overlap

    print(
        f"\nNEXT CHUNK STARTS AT: {next_start}"
    )

    print(
        f"Reason: retain {overlap} characters "
        "from the previous chunk."
    )

    if end == len(text):
        break

    start = next_start
    chunk_number += 1


# ============================================================
# STEP 9 — VERIFY
# ============================================================

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print(f"Chunks created: {len(chunks)}")


# ============================================================
# STEP 10 — SHOW
# ============================================================

for chunk in chunks:

    print("\n" + "-" * 60)

    print(
        f"Chunk {chunk['chunk_id']} "
        f"[{chunk['start']}:{chunk['end']}]"
    )

    print(chunk["text"])