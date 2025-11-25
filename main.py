"""Demo script to use the converter."""

import argparse
import logging
import os
from os.path import join
from pathlib import Path

from src.converter.converter import convert_heic_to_jpg

logging.basicConfig(level=logging.INFO, format="%(message)s")

parser = argparse.ArgumentParser(description="This app converts pictures from heic to jpeg format.")
parser.add_argument("--folder_path", type=Path, required=False)

args = parser.parse_args()


def main():
    """Run the converter."""
    if not args.folder_path or not os.path.isdir(args.folder_path):
        logging.warning(
            "No valid directory provided. We will use the examples folder from the project."
        )
        directory = os.getcwd()
        pictures_dir = join(directory, "examples")
    else:
        pictures_dir = args.folder_path
    convert_heic_to_jpg(pictures_dir)


if __name__ == "__main__":
    main()
