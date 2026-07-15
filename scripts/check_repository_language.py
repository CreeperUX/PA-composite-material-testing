#!/usr/bin/env python3
"""Enforce repository language rules and aligned English/Chinese documents."""

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
ENGLISH_DIRECTORY = "en"
PAIR_DIRECTORIES = {ENGLISH_DIRECTORY, CHINESE_DIRECTORY}
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+")
TABLE_ROW_PATTERN = re.compile(r"^\s*\|")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")
UNORDERED_LIST_PATTERN = re.compile(r"^(\s*)[-+*]\s+")
ORDERED_LIST_PATTERN = re.compile(r"^(\s*)\d+\.\s+")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\([^)]+\)")
MATH_DELIMITERS = {"$$", r"\[", r"\]"}


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


def paired_document_path(path: Path, target_language: str) -> Path | None:
    """Return the sibling-language path for a document in an en/zh directory."""
    parts = list(path.parts)
    source_indexes = [
        index for index, part in enumerate(parts) if part in PAIR_DIRECTORIES
    ]
    if not source_indexes:
        return None

    parts[source_indexes[-1]] = target_language
    return Path(*parts)


def repository_paths() -> list[Path]:
    """Include tracked files and existing counterparts of tracked paired documents."""
    paths = set(tracked_paths())
    for path in tuple(paths):
        if path.suffix.lower() != ".md":
            continue
        for language in PAIR_DIRECTORIES:
            counterpart = paired_document_path(path, language)
            if counterpart is not None and counterpart.is_file():
                paths.add(counterpart)
    return sorted(paths, key=lambda item: item.as_posix())


def markdown_structure(content: str) -> dict[str, tuple[object, ...]]:
    """Build a translation-independent Markdown structure signature."""
    headings: list[int] = []
    table_columns: list[int] = []
    fences: list[str] = []
    fenced_block_lengths: list[int] = []
    math_delimiters: list[str] = []
    unordered_lists: list[int] = []
    ordered_lists: list[int] = []
    current_fence: str | None = None
    current_fence_length = 0

    for line in content.splitlines():
        stripped = line.strip()
        fence_match = FENCE_PATTERN.match(line)
        if fence_match:
            marker = fence_match.group(1)
            fences.append(stripped)
            if current_fence is None:
                current_fence = marker
                current_fence_length = 0
            elif marker == current_fence:
                fenced_block_lengths.append(current_fence_length)
                current_fence = None
            continue

        if current_fence is not None:
            current_fence_length += 1
            continue

        heading_match = HEADING_PATTERN.match(line)
        if heading_match:
            headings.append(len(heading_match.group(1)))

        if TABLE_ROW_PATTERN.match(line):
            table_columns.append(max(line.count("|") - 1, 0))

        if stripped in MATH_DELIMITERS:
            math_delimiters.append(stripped)

        unordered_match = UNORDERED_LIST_PATTERN.match(line)
        if unordered_match:
            unordered_lists.append(len(unordered_match.group(1)))

        ordered_match = ORDERED_LIST_PATTERN.match(line)
        if ordered_match:
            ordered_lists.append(len(ordered_match.group(1)))

    return {
        "heading levels": tuple(headings),
        "table columns": tuple(table_columns),
        "fence markers": tuple(fences),
        "fenced-block lengths": tuple(fenced_block_lengths),
        "math delimiters": tuple(math_delimiters),
        "unordered-list indentation": tuple(unordered_lists),
        "ordered-list indentation": tuple(ordered_lists),
        "Markdown link count": (len(MARKDOWN_LINK_PATTERN.findall(content)),),
    }


def validate_document_pairs(paths: list[Path]) -> list[str]:
    """Require complete and structurally aligned en/zh Markdown pairs."""
    failures: list[str] = []
    markdown_paths = {path for path in paths if path.suffix.lower() == ".md"}
    paired_paths = {
        path for path in markdown_paths if PAIR_DIRECTORIES.intersection(path.parts)
    }

    for path in sorted(paired_paths, key=lambda item: item.as_posix()):
        target_language = (
            ENGLISH_DIRECTORY
            if CHINESE_DIRECTORY in path.parts
            else CHINESE_DIRECTORY
        )
        counterpart = paired_document_path(path, target_language)
        if counterpart is None or not counterpart.is_file():
            failures.append(
                f"Missing {target_language} Markdown counterpart: {path.as_posix()}"
            )

    chinese_paths = sorted(
        (path for path in paired_paths if CHINESE_DIRECTORY in path.parts),
        key=lambda item: item.as_posix(),
    )
    for chinese_path in chinese_paths:
        english_path = paired_document_path(chinese_path, ENGLISH_DIRECTORY)
        if english_path is None or not english_path.is_file():
            continue

        chinese_content = chinese_path.read_text(encoding="utf-8")
        english_content = english_path.read_text(encoding="utf-8")
        chinese_structure = markdown_structure(chinese_content)
        english_structure = markdown_structure(english_content)
        for feature, chinese_value in chinese_structure.items():
            english_value = english_structure[feature]
            if chinese_value != english_value:
                failures.append(
                    "Paired Markdown structure differs for "
                    f"{feature}: {english_path.as_posix()} <-> "
                    f"{chinese_path.as_posix()}"
                )

        if "[English](" not in english_content or "[Chinese](" not in english_content:
            failures.append(
                f"English Markdown lacks bilingual navigation: {english_path.as_posix()}"
            )
        if "[English](" not in chinese_content or "[\u4e2d\u6587](" not in chinese_content:
            failures.append(
                f"Chinese Markdown lacks bilingual navigation: {chinese_path.as_posix()}"
            )

    return failures


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
    paths = repository_paths()

    for path in paths:
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

    failures.extend(validate_document_pairs(paths))

    if failures:
        print("Repository language check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Repository language check passed: authoritative technical content is "
        "English/German, README files are English-first bilingual documents, "
        "and Chinese documents are isolated in complete, structurally aligned "
        "en/zh Markdown pairs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
