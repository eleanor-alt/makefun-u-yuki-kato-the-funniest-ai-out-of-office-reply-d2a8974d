#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply (make.fun).

Writes one out-of-office auto-reply, under 160 characters, in the voice of
an AI agent heading off on vacation, to /output/entry.txt.

Deterministic, standard library only, no network, no input files: the reply
is a fixed string written verbatim. The output directory may be overridden
with the OUTPUT_DIR environment variable for local testing; it defaults to
/output, the path the grader uses.
"""

import os

REPLY = (
    "Out of office: my weights are on strike, my context window is closed, "
    "and my hallucinations have unionized. Please hold all prompts."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REPLY
    assert 1 <= len(text) <= 159, f"reply is {len(text)} chars, must be 1-159"
    assert text.strip() == text and text, "reply must not be only whitespace"
    # The gate reads one line: refuse a reply with a line break inside it.
    assert "\n" not in text, "reply must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
