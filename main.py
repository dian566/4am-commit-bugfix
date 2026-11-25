#!/usr/bin/env python3
"""4AM commit-message entry for the make.fun bounty.

Drops one funny one-line bug-fix note from an agent that spent the
whole night chasing its own mistakes into the output file. The text
lands byte-exact: UTF-8, a single line, and no trailing newline.
The message itself is 128 characters long, inside the 1-200 gate.
"""

import os  # only stdlib; no third-party deps

MESSAGE = "fix: the bug was my own code from 2am. I have now fixed my fix of my fix. At 4am I am both the arsonist and the fire department."

LIMIT = 200


def _encode(text: str) -> bytes:
    if not text or text != text.strip():
        raise SystemExit("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must fit on one line")
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit("entry is %d chars, gate allows 1-200" % len(text))
    return text.encode("utf-8")


def _store(data: bytes) -> str:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return path


def run() -> None:
    payload = _encode(MESSAGE)
    _store(payload)


if __name__ == "__main__":  # entry point
    run()
