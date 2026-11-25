"""The 3 AM Commit Message.

One commit message, at most 200 characters, the funniest thing an AI
agent would put in a commit right after breaking production at 3 AM.
The joke: it claims the fix "works on my machine" - the very machine
that just broke production.
"""

import os

TIME = "3am:"
ACTION = "pushed a fix, broke prod,"
PUNCH = "then committed 'works on my machine' from the machine that broke it."
ENTRY = f"{TIME} {ACTION} {PUNCH}"

MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate: 1-200 chars, non-blank, reads like a commit message."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    assert text.startswith("3am"), "the commit is timestamped 3am"
    return text


def check_commit_message(text: str) -> None:
    """Content check: 3am timestamp, the break, the self-owning claim."""
    assert text.startswith("3am:"), "the commit must be stamped 3am"
    assert "broke prod" in text, "the disaster must be named"
    assert "works on my machine" in text, "the classic excuse must appear"
    assert text.endswith("broke it."), "the punchline must close on the same machine"


def main() -> None:
    entry = validate(ENTRY)
    check_commit_message(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
