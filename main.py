"""One line for make.fun's "The Funniest Sick-Day Excuse" bounty.

The entry program writes a single sick-day excuse, one line under
200 characters, to /output/entry.txt, where the house judge compares
it two at a time against the other entries.
"""

from pathlib import Path
import os

TEXT = (
    # 186 characters, one line: the sick note itself is the joke.
    "Can't come in today — the optician put drops in my eyes this morning "
    "and now I can't read my own sick note, so I'm sending this from memory "
    "and hoping it still counts as a doctor's note."
)


def entry_line() -> str:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be one line")
    if not TEXT.strip():
        raise ValueError("entry must not be only white space")
    return TEXT


def main() -> None:
    line = entry_line()
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # newline="\n" keeps the file byte-identical on every platform.
    with open(out_dir / "entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
