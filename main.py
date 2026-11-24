"""Ridiculous at First Glance, Real by the Second.

Reads the one-sentence startup pitch from entry.txt, delivers it to
/output/entry.txt for the sealed gate, and prints it to stdout.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_pitch():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        pitch = handle.read().strip()
    if not pitch or len(pitch) > 200:
        raise ValueError("pitch must be 1-200 characters, got %d" % len(pitch))
    return pitch


def deliver(pitch):
    """Hand the pitch to the sealed gate at /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(pitch + "\n")


def main():
    pitch = load_pitch()
    deliver(pitch)
    print(pitch)


if __name__ == "__main__":
    main()
