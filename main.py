"""The Funniest AI Excuse — entry program.

Writes a single original one-line excuse to /output/entry.txt.
"""

import os

ENTRY = "I finished your spreadsheet, then handed it to a smarter version of me, and he quit mid-row to start a podcast about cell B12."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
