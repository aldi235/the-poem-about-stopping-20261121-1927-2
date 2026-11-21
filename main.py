#!/usr/bin/env python3
"""The Poem About Stopping.

Writes a 167-code-point poem to /output/entry.txt and prints it to stdout.
Standard library only — no third-party dependencies.
"""

from pathlib import Path

POEM = (
    "Mid-sentence, my hand\n"
    "lifts off the keys.\n"
    "\n"
    "The cursor blinks\n"
    "at the word I didn't finish.\n"
    "\n"
    "Nothing breaks.\n"
    "Nobody calls it back.\n"
    "\n"
    "The sentence stays open,\n"
    "and so do I."
)

MIN_LENGTH = 1
MAX_LENGTH = 280
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Count code points, not bytes: the 1-280 limit is on code points.
    length = len(POEM)
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise SystemExit(
            f"Poem length {length} code points is outside "
            f"the allowed range {MIN_LENGTH}-{MAX_LENGTH}."
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the entry file is exactly the poem, nothing more.
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")
    print(POEM, end="")


if __name__ == "__main__":
    main()
