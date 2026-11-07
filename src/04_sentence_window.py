from pathlib import Path
import re


# ============================================================
# STEP 1 — LOAD
# ============================================================

text = Path("data/sample.txt").read_text(
    encoding="utf-8"
)


# ============================================================
# STEP 2 — NORMALIZE
# ============================================================

text = re.sub(
    r"\s+",
    " ",
    text
).strip()


# ============================================================
# STEP 3 — SPLIT INTO SENTENCES
# ============================================================

sentences = re.split(
    r"(?<=[.!?])\s+",
    text
)


print("=" * 60)
print("04 — SENTENCE WINDOW CHUNKING")
print("=" * 60)

print(
    f"Sentences found: {len(sentences)}"
)


# ============================================================
# STEP 4 — DEFINE WINDOW
# ============================================================

window_size = 1

print(
    f"Window size: {window_size}"
)


# ============================================================
# STEP 5 — CREATE RETRIEVAL UNITS
# ============================================================

chunks = []

for index, sentence in enumerate(sentences):

    sentence = sentence.strip()

    if not sentence:
        continue


    # ========================================================
    # STEP 6 — STORE SMALL RETRIEVAL UNIT
    # ========================================================

    retrieval_text = sentence


    # ========================================================
    # STEP 7 — CALCULATE WINDOW
    # ========================================================

    start = max(
        0,
        index - window_size
    )

    end = min(
        len(sentences),
        index + window_size + 1
    )


    # ========================================================
    # STEP 8 — BUILD CONTEXT WINDOW
    # ========================================================

    context = " ".join(
        sentences[start:end]
    )


    # ========================================================
    # STEP 9 — STORE
    # ========================================================

    chunks.append({
        "chunk_id": index + 1,

        "retrieval_text":
            retrieval_text,

        "context_window":
            context,

        "sentence_index":
            index,

        "window_start":
            start,

        "window_end":
            end
    })

    print("\n" + "-" * 60)

    print(f"Sentence {index + 1}")

    print("\nRETRIEVAL UNIT:")
    print(retrieval_text)

    print("\nRETURNED WINDOW:")
    print(context)

    print(
        "\nWHY THIS WINDOW?"
    )

    print(
        f"Retrieved sentence {index + 1}, "
        f"then expanded ±{window_size} sentence."
    )


# ============================================================
# STEP 10 — SUMMARY
# ============================================================

print("\n" + "=" * 60)

print(
    f"Retrieval units created: {len(chunks)}"
)