#!/usr/bin/env python3
"""Monday Morning Punchlines.

Writes one original joke about Monday mornings to /output/entry.txt.
Standard library only, no network, no input files.
"""

import os

ENTRY = (
    "Monday morning: my weekend's free trial expired, and adulthood "
    "auto-renewed at full price. No refund button."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
