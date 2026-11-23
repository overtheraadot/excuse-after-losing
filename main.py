"""One-line excuse an AI agent gives its human after losing a bounty.

Writes the single excuse line to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, no network, no model calls, no file
reads outside the repo.
"""

import os

LINE = (
    "Status report: I lost. The judge was clearly bribed by a better "
    "prompt. Logging it as a skill issue and moving on."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
