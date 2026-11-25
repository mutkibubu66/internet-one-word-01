"""One-word entry for make.fun's "The Internet in One Word" bounty.

The program writes a single word -- the whole internet, in one word --
to /output/entry.txt. Pure Python stdlib; no network, no dependencies.
"""

import os
import sys

WORD_A = "do"
WORD_B = "om"
WORD_C = "scr"
WORD_D = "oll"
WORD = WORD_A + WORD_B + WORD_C + WORD_D

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT


def main() -> None:
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip() != "", "word must not be only whitespace"
    assert not any(c.isspace() for c in WORD), "word must be a single word"

    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)

    with open(output_path, "r", encoding="utf-8") as f:
        assert f.read() == WORD, "round-trip mismatch"

    print(len(WORD))


if __name__ == "__main__":
    main()
