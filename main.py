"""make.fun entry: write the one-word username to <output>/entry.txt.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. The directory is created if missing. The entry text
is immutable and written with a single trailing newline.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "ctrlaltdefeat\n"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = Path(output_dir)
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {path!r}: {exc}")
    (path / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
