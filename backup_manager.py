#!/usr/bin/env python3
"""
Backup Manager - Create and manage backups
"""

import os
import shutil
import datetime
from pathlib import Path
from typing import Optional
import argparse


class BackupManager:
    """Manage file and directory backups"""

    def __init__(self, source: str, destination: str):
        """Initialize BackupManager"""
        self.source = Path(source)
        self.destination = Path(destination)

        if not self.source.exists():
            raise ValueError(f"Source path {source} does not exist")

        self.destination.mkdir(parents=True, exist_ok=True)

    def create_backup(self, incremental: bool = False) -> str:
        """
        Create a backup

        Args:
            incremental: If True, only backup changed files

        Returns:
            Path to backup directory
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}"
        backup_path = self.destination / backup_name

        print(f"Creating backup: {backup_name}")

        if self.source.is_file():
            self._backup_file(self.source, backup_path)
        else:
            self._backup_directory(self.source, backup_path, incremental)

        print(f"Backup completed: {backup_path}")
        return str(backup_path)

    def _backup_file(self, source: Path, destination: Path) -> None:
        """Backup a single file"""
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    def _backup_directory(self, source: Path, destination: Path, incremental: bool) -> None:
        """Backup a directory"""
        if not incremental:
            shutil.copytree(source, destination)
        else:
            # Incremental backup logic
            self._incremental_backup(source, destination)

    def _incremental_backup(self, source: Path, destination: Path) -> None:
        """Perform incremental backup"""
        destination.mkdir(parents=True, exist_ok=True)

        for item in source.rglob('*'):
            if item.is_file():
                relative_path = item.relative_to(source)
                dest_file = destination / relative_path

                # Copy if file doesn't exist or is newer
                if not dest_file.exists() or item.stat().st_mtime > dest_file.stat().st_mtime:
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest_file)
                    print(f"  Backed up: {relative_path}")

    def list_backups(self) -> list:
        """List all available backups"""
        backups = [d for d in self.destination.iterdir() if d.is_dir() and d.name.startswith('backup_')]
        return sorted(backups, reverse=True)

    def restore_backup(self, backup_name: str, restore_path: Optional[str] = None) -> None:
        """Restore a backup"""
        backup_path = self.destination / backup_name

        if not backup_path.exists():
            raise ValueError(f"Backup {backup_name} does not exist")

        target_path = Path(restore_path) if restore_path else self.source

        print(f"Restoring backup {backup_name} to {target_path}")

        if backup_path.is_file():
            shutil.copy2(backup_path, target_path)
        else:
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(backup_path, target_path)

        print("Restore completed")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Backup Manager')
    parser.add_argument('--source', required=True, help='Source path')
    parser.add_argument('--dest', required=True, help='Destination path')
    parser.add_argument('--incremental', action='store_true', help='Incremental backup')
    parser.add_argument('--list', action='store_true', help='List backups')

    args = parser.parse_args()

    try:
        manager = BackupManager(args.source, args.dest)

        if args.list:
            backups = manager.list_backups()
            print("Available backups:")
            for backup in backups:
                print(f"  - {backup.name}")
        else:
            manager.create_backup(incremental=args.incremental)

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

# Resolve memory leak in database layer - 2025-10-14 13:50:50
try:
    result = process_data()
except Exception as e:
    logger.error(f'Processing failed: {e}')
    result = None

# Repair error handling in cache layer - 2025-10-30 10:14:37
# Modified: 2025-10-30 10:14:37
CONFIG_VALUE = 'new_value'

# Repair code structure in router - 2025-11-07 08:35:27
# Modified: 2025-11-07 08:35:27
CONFIG_VALUE = 'new_value'