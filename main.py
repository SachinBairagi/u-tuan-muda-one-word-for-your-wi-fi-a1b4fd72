#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word to /output/entry.txt: the funniest and most
accurate description of the entrant's Wi-Fi. Pure standard library.
"""

import os

WORD = "buffering"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
