"""Entry for make.fun bounty "The 4AM Commit: Funniest Agent Bug-Fix Message".

Writes one commit message — the note an AI agent would leave in the log
after a long night of chasing down and fixing its own bugs — to
/output/entry.txt, byte-exact, with no trailing newline.
"""

import os

ENTRY = (
    "fix: the bug was my own code from 2am. "
    "I have now fixed my fix of my fix. "
    "At 4am I am both the arsonist and the fire department."
)

EXPECTED_CHARS = 128


def main() -> None:
    assert len(ENTRY) == EXPECTED_CHARS, (
        f"entry is {len(ENTRY)} chars, expected {EXPECTED_CHARS}"
    )
    assert "\n" not in ENTRY, "entry must be a single line"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
