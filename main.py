#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun bounty entry.

Reads the single one-liner from entry.txt (the entry's source of truth,
next to this file) and writes it, byte for byte, to /output/entry.txt
for the grader. Deterministic: no clock, no randomness, no network,
stdlib only. The line is 107 characters, inside the 1-140 gate.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_line() -> str:
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        text = f.read().strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"line is {len(text)} chars, must be 1-140")
    return text


def main() -> None:
    text = load_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    print(text)


if __name__ == "__main__":
    main()
