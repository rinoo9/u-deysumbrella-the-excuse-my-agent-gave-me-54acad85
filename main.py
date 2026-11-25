"""The Excuse My Agent Gave Me — a one-line excuse, printed deterministically.

Round 2 line: the agent did finish on time, but only inside its own
simulation — and the simulation is now refusing to be merged into
reality. Same straight-faced apology, new culprit: the sandbox.
"""

EXCUSE = (
    "I did finish on time \u2014 in the simulation. Unfortunately, the "
    "simulation has now filed a formal objection to being merged into "
    "reality."
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
