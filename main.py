import os
from pathlib import Path

ENTRY_TEXT = "ctrlaltdefeat\n"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    (path / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
