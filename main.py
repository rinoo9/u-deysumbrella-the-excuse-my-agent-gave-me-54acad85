"""The Excuse My Agent Gave Me — a one-line excuse, printed deterministically."""

EXCUSE = (
    "I'm sorry \u2014 I spent the whole deadline re-reading my own context window "
    "to find your task, and by the time I found it, I'd already forgotten "
    "what a deadline was."
)


def main() -> None:
    import os

    # No clock, randomness, or network: the same excuse, byte for byte, every run.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = EXCUSE + "\n"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(EXCUSE)


if __name__ == "__main__":
    main()
