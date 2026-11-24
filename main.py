#!/usr/bin/env python3
"""Write one bizarre-but-sellable startup pitch to entry.txt.

The program honours the harness output directory (MAKEFUN_OUTPUT_DIR)
with /output as the fallback, and writes exactly one sentence of
1-200 characters: the odd thing sold, who pays for it, and why the
business holds together.
"""

import os
import sys

# One sentence: names the odd thing, the buyer, and the money logic.
PITCH = (
    "We sell the right to name a pothole after your ex: jilted lovers "
    "pay £25 a pothole, and councils finally fix the roads with the "
    "spite money."
)


def main() -> int:
    text = PITCH.strip()
    if not (1 <= len(text) <= 200):
        print(f"pitch is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or text != text.strip():
        print("pitch must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("pitch must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
