"""Write one one-line joke about working beside AI coding agents.

The joke is a literal: the program's whole job is to deliver it to
/output/entry.txt, exactly as written, with no trailing newline.
"""

import os

JOKE = (
    "The reviewer asked my agent for a smaller diff, "
    "so it split 2,000 lines into 2,000 commits \u2014 "
    "each one titled 'part 1 of 1'."
)


def main() -> None:
    # Self-check the gate before writing: 1-280 code points, one line.
    if not 1 <= len(JOKE) <= 280 or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke fails the entry gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
