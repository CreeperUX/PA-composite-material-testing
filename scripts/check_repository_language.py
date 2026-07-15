#!/usr/bin/env python3
"""Enforce English/German content with structured bilingual README files."""

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
README_NAME = "README.md"
ENGLISH_HEADING = "## English"
CHINESE_HEADING = "## \u4e2d\u6587"
CHINESE_DIRECTORY = "zh"


def tracked_paths() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]


def is_text_file(path: Path) -> bool:
    return path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES


def is_chinese_document(path: Path) -> bool:
    """Return whether a document is intentionally stored in a Chinese directory."""
    return CHINESE_DIRECTORY in path.parts


def validate_bilingual_readme(path: Path, content: str) -> list[str]:
    """Validate the required English-first, Chinese-second README structure."""
    failures: list[str] = []
    display_path = path.as_posix()
    english_index = content.find(ENGLISH_HEADING)
    chinese_index = content.find(CHINESE_HEADING)

    if english_index < 0:
        failures.append(f"README is missing {ENGLISH_HEADING!r}: {display_path}")
    if chinese_index < 0:
        failures.append(f"README is missing {CHINESE_HEADING!r}: {display_path}")
    if failures:
        return failures

    if english_index >= chinese_index:
        failures.append(
            f"README must place English before Chinese: {display_path}"
        )
        return failures

    english_section = content[english_index + len(ENGLISH_HEADING):chinese_index]
    chinese_section = content[chinese_index + len(CHINESE_HEADING):]
    if not english_section.strip():
        failures.append(f"README English section is empty: {display_path}")
    if HAN_PATTERN.search(english_section):
        failures.append(
            f"README English section contains Chinese text: {display_path}"
        )
    if not HAN_PATTERN.search(chinese_section):
        failures.append(
            f"README Chinese section has no Chinese reading-support text: {display_path}"
        )

    return failures


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

        if path.name == README_NAME:
            failures.extend(validate_bilingual_readme(path, content))
            continue

        if is_chinese_document(path):
            if path.suffix.lower() == ".md" and not HAN_PATTERN.search(content):
                failures.append(
                    f"Chinese Markdown document contains no Chinese text: {display_path}"
                )
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

    print(
        "Repository language check passed: authoritative technical content is "
        "English/German, README files are English-first bilingual documents, "
        "and Chinese documents are isolated under zh directories."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
