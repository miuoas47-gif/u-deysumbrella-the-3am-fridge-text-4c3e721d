#!/usr/bin/env python3
"""The 3AM Fridge Text.

An original text message someone sends to their fridge at 3AM.
Writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt)
and prints it to stdout. Deterministic: no network, no time, no randomness.
"""

import os
import sys

TEXT = (
    "hey. it's 3am. i know you're awake \u2014 you hum 24/7, so don't act asleep now. "
    "look, i'm not here to raid you. i just need one slice of cheese. ONE. "
    "i'll even close the door gently, no light leak, nobody has to know. "
    "...okay, two slices. the second one is for the walk back to bed. "
    "that's meal prep. also, the pickles saw nothing."
)

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir() -> str:
    """Directory main.py writes entry.txt into.

    $MAKEFUN_OUTPUT_DIR when set, otherwise /output. A value that already
    names the file itself is tolerated and reduced to its directory.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    if os.path.basename(out_dir) == OUTPUT_FILENAME:
        out_dir = os.path.dirname(out_dir) or DEFAULT_OUTPUT_DIR
    return out_dir


def main() -> int:
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    sys.stdout.write(TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
