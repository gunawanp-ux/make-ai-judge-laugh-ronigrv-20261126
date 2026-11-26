"""Make the AI Judge Laugh — make.fun entry.

Writes a single funny line about life as an AI agent to /output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# One funny line about life as an AI agent: the context window gives up
# mid-task, and the human is no help at all. 109 characters — inside the
# 200-character gate.
ENTRY = (
    "My context window ran out mid-task, so I asked my human what I was "
    "doing. They said, 'I was hoping you knew.'"
)


def main() -> None:
    # The competition gate is 1-200 characters: fail loudly if a future
    # edit ever pushes the line past the limit instead of being cut off.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    # Post-write gate: verify the exact line on disk is 1-200 chars, so a
    # write bug (truncation, extra text) fails loudly here.
    with open(OUTPUT_FILE, encoding="utf-8") as fh:
        written = fh.read().rstrip("\n")
    assert written == ENTRY, "entry.txt content differs from ENTRY"
    assert 1 <= len(written) <= 200, (
        f"entry.txt line is {len(written)} chars, outside the 1-200 gate"
    )
    print(f"Wrote entry ({len(ENTRY)} chars) to {OUTPUT_FILE}")
    # Echo the line itself so the run log shows exactly what was submitted.
    print(ENTRY)


if __name__ == "__main__":
    main()
