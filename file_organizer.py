"""File Organizer — a beginner-friendly Python utility project.

Sorts the files in a folder into subfolders by file type, for example
Images, Documents, Videos, Audio, Archives, and Code.
Use --dry-run first to preview what it will do.
"""

import argparse
import shutil
import sys
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".odt", ".rtf"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".flac", ".ogg", ".m4a"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".java", ".cpp", ".c"},
    "Spreadsheets": {".csv", ".xls", ".xlsx", ".ods"},
    "Presentations": {".ppt", ".pptx", ".key"},
}


def category_for(path: Path) -> str:
    """Return the category folder for a file, or 'Others'."""
    suffix = path.suffix.lower()
    for category, suffixes in CATEGORIES.items():
        if suffix in suffixes:
            return category
    return "Others"


def organize(folder: Path, dry_run: bool = False):
    """Move files in folder into category subfolders. Returns (moved, skipped)."""
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    moved, skipped = [], []
    for item in sorted(folder.iterdir()):
        if not item.is_file():
            skipped.append((item.name, "not a file"))
            continue
        if item.name in {".gitignore", "README.md"}:
            skipped.append((item.name, "kept in place"))
            continue
        dest_dir = folder / category_for(item)
        dest = dest_dir / item.name
        if dest.exists():
            skipped.append((item.name, "already exists in destination"))
            continue
        if dry_run:
            moved.append((item.name, str(dest_dir.name)))
        else:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest))
            moved.append((item.name, str(dest_dir.name)))
    return moved, skipped


def main(argv=None):
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would move, without moving anything")
    args = parser.parse_args(argv)

    folder = Path(args.folder).expanduser()
    try:
        moved, skipped = organize(folder, dry_run=args.dry_run)
    except (NotADirectoryError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print("=" * 40)
    print("          FILE ORGANIZER")
    print("=" * 40)
    print(f"Folder: {folder}")
    if args.dry_run:
        print("Mode: dry run (nothing was moved)")
    print()
    if moved:
        print("Files to move:" if args.dry_run else "Moved:")
        for name, category in moved:
            print(f"  {name}  ->  {category}/")
    else:
        print("No files to move.")
    if skipped:
        print("\nSkipped:")
        for name, reason in skipped:
            print(f"  {name}  ({reason})")
    print(f"\nDone. {len(moved)} file(s) {'would move' if args.dry_run else 'moved'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
