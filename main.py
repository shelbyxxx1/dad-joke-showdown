#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR when it is set). Standard library only.
"""

import os

JOKE = "My smart fridge keeps suggesting recipes, but its meal plans are always half-baked."


def main():
    # Fail fast instead of writing an entry the gate would refuse.
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1-200 characters, got %d" % len(JOKE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
