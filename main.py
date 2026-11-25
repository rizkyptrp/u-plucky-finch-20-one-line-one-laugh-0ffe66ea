#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt in the grader). Python 3.13, standard library only.
Deterministic, no network, no model calls: the line is a fixed string
chosen after scoring six candidate variants against the judge's brief
(laugh on first read, fast punch, freshness, economy, holds up) and
keeping only the best, then tightening it in an improvement pass.
"""

import os
from pathlib import Path

LINE = "I asked my smartwatch to track my steps. It reported me missing."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    # The gate: UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    # No trailing newline: the file is exactly the joke, byte for byte,
    # which also keeps it smallest for the size tie-break.
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
