# Repository language policy

English is the canonical language for repository-authored technical content.

German is also accepted for original laboratory exports, supplier reports, standards-related terms, and other source material that should not be rewritten. Repository-authored filenames, directory names, technical documentation, code, user-interface text, and data schemas must use English or German and must not contain Chinese text.

Every `README.md` is an intentional bilingual exception for reading support. Each README must contain a complete English section first and a corresponding Chinese section second. The English section remains authoritative when the two sections differ.

When English and Chinese versions are maintained as separate files, they must use the same filename in sibling `en/` and `zh/` directories. English files remain authoritative. Chinese-only historical or supplemental notes may be stored under `zh/` with an English path name so original project knowledge is preserved without introducing Chinese characters into repository paths.

Native CAD assets are local-only. Controlled English or German STEP export copies may be published under `cad/step/` after filename, metadata, and integrity review. Preparing the publication copy must not rename, move, or rewrite the native CAD working files. Formatted workbooks that cannot be converted without risking formulas or layout also remain in local archival storage until a controlled conversion is available.

Run the repository language check before committing:

```bash
python scripts/check_repository_language.py
```

The check rejects Chinese characters in tracked paths and in supported text files outside README documents and `zh/` directories. It validates that every README places the English heading before the Chinese heading, that the English section contains no Chinese text, and that the Chinese section contains Chinese reading-support text. It also requires Markdown documents under `zh/` to contain Chinese text. Binary English or German source documents are reviewed separately before they enter Git.
