#!/usr/bin/env python3
"""
File Organizer - Automatically organize files by type
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import argparse
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FileOrganizer:
    """Organize files in a directory by their extensions"""

    FILE_TYPES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt', '.rtf'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go'],
        'Executables': ['.exe', '.msi', '.dmg', '.deb', '.rpm', '.app'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
        'Books': ['.epub', '.mobi', '.azw', '.azw3'],
        'Presentations': ['.ppt', '.pptx', '.key', '.odp']
    }

    def __init__(self, directory: str, create_folders: bool = True):
        """
        Initialize FileOrganizer with target directory

        Args:
            directory: Path to directory to organize
            create_folders: Create category folders if they don't exist
        """
        self.directory = Path(directory).resolve()
        self.create_folders = create_folders

        if not self.directory.exists():
            raise ValueError(f"Directory {directory} does not exist")

        if not self.directory.is_dir():
            raise ValueError(f"{directory} is not a directory")

    def get_file_category(self, file_path: Path) -> Optional[str]:
        """
        Get category for a file based on its extension

        Args:
            file_path: Path to file

        Returns:
            Category name or None if no match
        """
        extension = file_path.suffix.lower()

        for category, extensions in self.FILE_TYPES.items():
            if extension in extensions:
                return category

        return 'Others' if extension else None

    def organize(self, dry_run: bool = False) -> Dict[str, int]:
        """
        Organize files in the directory

        Args:
            dry_run: If True, only show what would be done without moving files

        Returns:
            Dictionary with statistics: {category: count}
        """
        stats = {}
        moved_count = 0
        error_count = 0

        logger.info(f"Starting file organization in: {self.directory}")
        logger.info(f"Dry run mode: {dry_run}")

        # Get all files in directory (not recursive)
        files = [f for f in self.directory.iterdir() if f.is_file()]

        if not files:
            logger.warning("No files found to organize")
            return stats

        logger.info(f"Found {len(files)} files to process")

        for file_path in files:
            try:
                # Skip hidden files
                if file_path.name.startswith('.'):
                    logger.debug(f"Skipping hidden file: {file_path.name}")
                    continue

                # Get category
                category = self.get_file_category(file_path)

                if category is None:
                    logger.debug(f"Skipping file without extension: {file_path.name}")
                    continue

                # Update statistics
                stats[category] = stats.get(category, 0) + 1

                # Create category folder
                category_folder = self.directory / category

                if not dry_run and self.create_folders:
                    category_folder.mkdir(exist_ok=True)

                # Target path
                target_path = category_folder / file_path.name

                # Handle name conflicts
                if target_path.exists():
                    base_name = file_path.stem
                    extension = file_path.suffix
                    counter = 1

                    while target_path.exists():
                        new_name = f"{base_name}_{counter}{extension}"
                        target_path = category_folder / new_name
                        counter += 1

                    logger.info(f"Renamed to avoid conflict: {target_path.name}")

                # Move file
                if dry_run:
                    logger.info(f"[DRY RUN] Would move: {file_path.name} → {category}/")
                else:
                    shutil.move(str(file_path), str(target_path))
                    logger.info(f"Moved: {file_path.name} → {category}/")
                    moved_count += 1

            except Exception as e:
                logger.error(f"Error processing {file_path.name}: {e}")
                error_count += 1
                continue

        # Print summary
        logger.info("\n" + "=" * 50)
        logger.info("ORGANIZATION SUMMARY")
        logger.info("=" * 50)

        for category, count in sorted(stats.items()):
            logger.info(f"{category:.<30} {count:>3} files")

        logger.info("=" * 50)
        logger.info(f"Total files processed: {sum(stats.values())}")

        if not dry_run:
            logger.info(f"Successfully moved: {moved_count}")

        if error_count > 0:
            logger.warning(f"Errors encountered: {error_count}")

        return stats

    def undo(self) -> bool:
        """
        Undo organization by moving files back to main directory

        Returns:
            True if successful, False otherwise
        """
        logger.info("Starting undo operation...")

        moved_count = 0
        error_count = 0

        # Get all category folders
        category_folders = [f for f in self.directory.iterdir()
                            if f.is_dir() and f.name in self.FILE_TYPES.keys()]

        for folder in category_folders:
            try:
                files = list(folder.iterdir())

                for file_path in files:
                    if file_path.is_file():
                        target_path = self.directory / file_path.name

                        # Handle name conflicts
                        if target_path.exists():
                            base_name = file_path.stem
                            extension = file_path.suffix
                            counter = 1

                            while target_path.exists():
                                new_name = f"{base_name}_restored_{counter}{extension}"
                                target_path = self.directory / new_name
                                counter += 1

                        shutil.move(str(file_path), str(target_path))
                        logger.info(f"Restored: {file_path.name}")
                        moved_count += 1

                # Remove empty folder
                if not list(folder.iterdir()):
                    folder.rmdir()
                    logger.info(f"Removed empty folder: {folder.name}")

            except Exception as e:
                logger.error(f"Error during undo for {folder.name}: {e}")
                error_count += 1
                continue

        logger.info(f"\nUndo complete. Restored {moved_count} files")

        if error_count > 0:
            logger.warning(f"Errors encountered: {error_count}")
            return False

        return True


def main():
    """Main function with CLI interface"""
    parser = argparse.ArgumentParser(
        description='Organize files in a directory by type',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --path ~/Downloads
  %(prog)s --path ~/Documents --dry-run
  %(prog)s --path ~/Desktop --undo
        """
    )

    parser.add_argument(
        '--path',
        type=str,
        required=True,
        help='Path to directory to organize'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without actually moving files'
    )

    parser.add_argument(
        '--undo',
        action='store_true',
        help='Undo previous organization'
    )

    parser.add_argument(
        '--no-create-folders',
        action='store_true',
        help='Do not create category folders (they must exist)'
    )

    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        # Initialize organizer
        organizer = FileOrganizer(
            args.path,
            create_folders=not args.no_create_folders
        )

        # Perform action
        if args.undo:
            success = organizer.undo()
            if success:
                logger.info("✅ Undo completed successfully!")
            else:
                logger.error("❌ Undo completed with errors")
                return 1
        else:
            stats = organizer.organize(dry_run=args.dry_run)

            if args.dry_run:
                logger.info("\n✅ Dry run completed! Run without --dry-run to actually move files.")
            else:
                logger.info("\n✅ Organization completed successfully!")

        return 0

    except KeyboardInterrupt:
        logger.warning("\n⚠️ Operation cancelled by user")
        return 130

    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())

# Modify configuration in core system - 2025-10-21 17:20:20
# Modified: 2025-10-21 17:20:20
CONFIG_VALUE = 'new_value'

# Adjust memory leak in auth service - 2025-10-24 20:04:29
# Enhanced: 2025-10-24 20:04:29
"""Documentation updated"""

# Develop performance bottleneck feature - 2025-10-31 17:27:10
# Improved: 2025-10-31 17:27:10
# Additional configuration

# Remove data processing in payment module - 2025-11-13 12:24:08
# Updated: 2025-11-13 12:24:08
def updated_function():
    pass