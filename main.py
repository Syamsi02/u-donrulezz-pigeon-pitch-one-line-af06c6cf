#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Prints one original one-line elevator pitch a city pigeon gives
investors for its startup, and writes it to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output).

Pure standard library, deterministic: the same line every run.
"""

import os

PITCH = (
    "I'm the coo-founder of Crumbd, raising seed to scale the only "
    "delivery fleet that works for breadcrumbs, never calls in sick, "
    "and already holds a five-star rating on every statue in the city."
)


def main() -> None:
    # The gate allows 1-200 characters of non-whitespace text on one line.
    assert 1 <= len(PITCH) <= 200, "pitch must fit in 200 characters"
    assert "\n" not in PITCH, "pitch must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print(PITCH)


if __name__ == "__main__":
    main()
