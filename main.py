"""One-word entry for make.fun's "The Internet in One Word" bounty.

The program writes a single word -- the whole internet, in one word --
to /output/entry.txt. Pure Python stdlib; no network, no dependencies.
"""

WORD_PART1 = "doom"
WORD_PART2 = "scroll"
WORD = WORD_PART1 + WORD_PART2


def main() -> None:
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip() != "", "word must not be only whitespace"
    assert not any(c.isspace() for c in WORD), "word must be a single word"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == WORD, "round-trip mismatch"

    print(len(WORD))


if __name__ == "__main__":
    main()
