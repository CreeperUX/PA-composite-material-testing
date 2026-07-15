#!/usr/bin/env python3
"""Reject Chinese characters in tracked paths and repository text files."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


HAN_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".gitattributes",
    ".gitignore",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
TEXT_FILENAMES = {"VERSION"}


def tracked_paths() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]


def is_text_file(path: Path) -> bool:
    return path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES


def main() -> int:
    failures: list[str] = []

    for path in tracked_paths():
        display_path = path.as_posix()
        if HAN_PATTERN.search(display_path):
            failures.append(f"Path contains Chinese text: {display_path}")

        if not path.is_file() or not is_text_file(path):
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"Text file is not valid UTF-8: {display_path}")
            continue

        for line_number, line in enumerate(content.splitlines(), start=1):
            if HAN_PATTERN.search(line):
                failures.append(
                    f"Chinese text found: {display_path}:{line_number}"
                )

    if failures:
        print("Repository language check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Repository language check passed: tracked paths and text are English/German only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
