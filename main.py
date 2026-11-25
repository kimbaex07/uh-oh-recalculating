"""The Agent's Uh-Oh entry generator.

Writes the single-word entry to entry.txt inside MAKEFUN_OUTPUT_DIR.
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = "Recalculating"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
