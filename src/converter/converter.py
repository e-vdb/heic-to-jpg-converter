"""Converter module."""

import logging
import os

import pyheif
from PIL import Image
from tqdm import tqdm

from src.converter.utils import (
    check_if_directory_exists,
    create_directory_for_conversion,
    get_all_files_with_format,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_heic_as_image(heic_path) -> Image.Image:
    """Get an image from a HEIC file."""
    with open(heic_path, "rb") as heic_file:
        heif_file = pyheif.read(heic_file)
        image = Image.frombytes(
            mode=heif_file.mode, size=heif_file.size, data=heif_file.data, decoder_name="raw"
        )
    return image


def save_image_to_jpeg(jpg_path, image) -> None:
    """Save an image to a JPEG file."""
    with open(jpg_path, "wb") as jpg_file:
        image.save(jpg_file, "JPEG", quality=100)


def convert_heic_to_jpg(heic_dir) -> None:
    """Convert HEIC files to JPG files."""
    if not check_if_directory_exists(dir_path=heic_dir):
        return

    # Create a directory to store the converted JPG files
    jpg_dir = create_directory_for_conversion(dir_path=heic_dir)

    # Get all HEIC files in the specified directory
    heic_files = get_all_files_with_format(dir_path=heic_dir)
    total_files = len(heic_files)

    if total_files == 0:
        logging.warning("No HEIC files found in the directory. Conversion aborted.")
        return

    # Convert each HEIC file to JPG
    num_converted = 0
    for file_index, file_name in enumerate(tqdm(heic_files, unit="file"), start=1):
        heic_path = os.path.join(heic_dir, file_name)
        jpg_path = os.path.join(jpg_dir, os.path.splitext(file_name)[0] + ".jpg")

        try:
            image = get_heic_as_image(heic_path)

            save_image_to_jpeg(jpg_path, image)
            num_converted += 1

        except Exception as e:
            logging.exception(f"Error converting {file_name}: {e!s}")

    if num_converted == total_files:
        logging.info("Conversion successfully completed. %s files converted.", total_files)
    else:
        logging.warning(
            "Errors encountered during conversion.%s over %s were converted.",
            num_converted,
            total_files,
        )
