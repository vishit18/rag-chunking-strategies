from pathlib import Path


# ============================================================
# STEP 1 — LOAD INPUT
# ============================================================

text = Path("data/sample.txt").read_text(encoding="utf-8")

print("=" * 60)
print("01 — FIXED-SIZE CHARACTER CHUNKING")
print("=" * 60)

print(f"Total characters: {len(text)}")


# ============================================================
# STEP 2 — DEFINE THE UNIT
# ============================================================

# Our unit is one CHARACTER.
#
# We are deliberately NOT thinking about:
# - words
# - sentences
# - paragraphs
# - tokens
#
# Just characters.


# ============================================================
# STEP 3 — DEFINE THE LIMIT
# ============================================================

chunk_size = 300

print(f"Maximum chunk size: {chunk_size} characters")


# ============================================================
# STEP 4 — INITIALIZE POINTER
# ============================================================

start = 0
chunk_number = 1

chunks = []


# ============================================================
# STEP 5 — PROCESS THE DOCUMENT
# ============================================================

while start < len(text):

    end = start + chunk_size


    # ========================================================
    # STEP 6 — CHECK BOUNDARY
    # ========================================================

    chunk = text[start:end]

    print("\n" + "-" * 60)
    print(f"Chunk {chunk_number}")
    print("-" * 60)

    print(f"Start index : {start}")
    print(f"End index   : {end}")
    print(f"Actual size : {len(chunk)}")

    print("\nWHY DID IT SPLIT?")
    print(
        f"Because the fixed character limit is "
        f"{chunk_size} characters."
    )


    # ========================================================
    # STEP 7 — CREATE CHUNK
    # ========================================================

    chunks.append({
        "chunk_id": chunk_number,
        "start": start,
        "end": min(end, len(text)),
        "text": chunk,
        "reason": "Fixed character limit reached"
    })


    # ========================================================
    # STEP 8 — MOVE POINTER
    # ========================================================

    start = end
    chunk_number += 1


# ============================================================
# STEP 9 — VERIFY
# ============================================================

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print(f"Chunks created: {len(chunks)}")


# ============================================================
# STEP 10 — DISPLAY
# ============================================================

for chunk in chunks:

    print("\n" + "-" * 60)
    print(f"CHUNK {chunk['chunk_id']}")
    print("-" * 60)

    print(chunk["text"])