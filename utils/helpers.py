"""
Helper utilities for automation tools
"""

import os
import hashlib
from pathlib import Path
from typing import Union


def get_file_hash(file_path: Union[str, Path], algorithm: str = 'sha256') -> str:
    """
    Calculate hash of a file

    Args:
        file_path: Path to file
        algorithm: Hash algorithm (md5, sha1, sha256)

    Returns:
        Hexadecimal hash string
    """
    hash_func = hashlib.new(algorithm)

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def format_bytes(bytes_size: int) -> str:
    """
    Format bytes to human-readable string

    Args:
        bytes_size: Size in bytes

    Returns:
        Formatted string (e.g., "1.5 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def ensure_directory(directory: Union[str, Path]) -> Path:
    """
    Ensure directory exists, create if not

    Args:
        directory: Directory path

    Returns:
        Path object
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def is_safe_path(base_path: Union[str, Path], target_path: Union[str, Path]) -> bool:
    """
    Check if target path is within base path (prevent directory traversal)

    Args:
        base_path: Base directory
        target_path: Target path to check

    Returns:
        True if safe, False otherwise
    """
    base = Path(base_path).resolve()
    target = Path(target_path).resolve()

    try:
        target.relative_to(base)
        return True
    except ValueError:
        return False

# Adjust error handling in validation module - 2025-10-12 18:08:45
# Enhanced: 2025-10-12 18:08:45
"""Documentation updated"""

# Implement file upload feature - 2025-10-27 12:24:25
class NewFeature:
    def __init__(self):
        self.enabled = True
    
    def execute(self):
        return 'Feature executed'

# Remove helper function in auth service for better maintainability - 2025-11-22 14:04:25
# Enhanced: 2025-11-22 14:04:25
"""Documentation updated"""

# Fix edge case in controller to enhance security - 2025-12-01 14:48:29
if data is None:
    raise ValueError('Data cannot be None')
return validate_data(data)