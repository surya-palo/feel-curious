#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short, original text to /output/entry.txt.
Deterministic: the same bytes on every run. No network, stdlib only.
"""

from pathlib import Path

TEXT = (
    "The last lighthouse keeper left a kettle on, a chair pulled out, "
    "and a logbook open to a page that only says: tomorrow. "
    "I have been turning that page over ever since. "
    "What was he waiting for \u2014 "
    "and what are you still waiting to read?"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
