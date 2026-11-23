"""News-image entry: deterministically writes the bundled image to /output/entry.png.

The image (entry.png, 1024x1024) sums up the world news of Tuesday 24 November 2026.
No network, no randomness: every run writes the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
