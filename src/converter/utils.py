"""Utility functions for the converter."""

import logging
import os
import uuid
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")


def check_if_directory_exists(dir_path: Path) -> bool:
    """Check if the directory exists."""
    if not Path.is_dir(dir_path):
        logging.error("Directory %s does not exist.", dir_path)
        return False
    return True


def create_directory_for_conversion(dir_path: Path) -> str:
    """Create a directory for the converted files."""
    jpg_dir = os.path.join(dir_path, f"{uuid.uuid4()!s}_ConvertedFiles")
    os.makedirs(jpg_dir, exist_ok=True)
    return jpg_dir


def get_all_files_with_format(dir_path: Path, file_suffix: str = ".heic") -> list[str]:
    """Get all files with the specified suffix."""
    return [file for file in os.listdir(dir_path) if file.lower().endswith(file_suffix)]
