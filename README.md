# File Organizer 📁

A beginner-friendly Python utility that sorts the files in a folder
into subfolders by file type — Images, Documents, Videos, and more.

## Features

- Organizes files by extension into named folders
- Supports images, documents, videos, audio, archives, code, and more
- `--dry-run` mode previews the changes without moving anything
- Skips folders and files that are already in the right place
- Uses only the Python standard library — no third-party packages

## Requirements

- Python 3.8 or newer
- No third-party packages are required

## How to run

Preview what would happen first:

```bash
python file_organizer.py ~/Downloads --dry-run
```

Then organize the folder for real:

```bash
python file_organizer.py ~/Downloads
```

On some systems, use `python3 file_organizer.py ~/Downloads`.

## Categories

| Folder | File types |
| --- | --- |
| Images | .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg |
| Documents | .pdf, .doc, .docx, .txt, .md, .odt, .rtf |
| Videos | .mp4, .mkv, .mov, .avi, .webm |
| Audio | .mp3, .wav, .flac, .ogg, .m4a |
| Archives | .zip, .tar, .gz, .rar, .7z |
| Code | .py, .js, .html, .css, .json, .java, .cpp, .c |
| Spreadsheets | .csv, .xls, .xlsx, .ods |
| Presentations | .ppt, .pptx, .key |
| Others | anything else |

## Project structure

```text
file-organizer/
├── file_organizer.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Learning outcomes

- Working with files and folders using `pathlib`
- Moving files with `shutil`
- Command-line arguments with `argparse`
- Mapping file extensions to categories

## Author

SHANMUKHA SREE LALITHA VENKAT SHYAM PYNA ([@1shyam253](https://github.com/1shyam253))
