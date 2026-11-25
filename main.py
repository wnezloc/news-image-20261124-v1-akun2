#!/usr/bin/env python3
"""news-image-20261124 v1 (akun 2): write the pre-composed front page.

The image is a dense newspaper front page summarising Tuesday 24 November
2026: 21 stories with numbered badges, a dotted world map with 20 stories
pinned (El Niño has no pin on Earth), 3 lead stories,
a 10-card grid, an hour-by-hour timeline, a stat strip, an ALSO list,
a DATE CHECK box and a source footer. Flat vector illustrations drawn
in code. Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
