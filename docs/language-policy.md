# Repository language policy

English is the canonical language for repository-authored content.

German is also accepted for original laboratory exports, supplier reports, standards-related terms, and other source material that should not be rewritten. Repository-authored filenames, directory names, documentation, code, user-interface text, and data schemas must use English or German and must not contain Chinese text.

Native CAD assets are local-only. Controlled English or German STEP export copies may be published under `cad/step/` after filename, metadata, and integrity review. Preparing the publication copy must not rename, move, or rewrite the native CAD working files. Formatted workbooks that cannot be converted without risking formulas or layout also remain in local archival storage until a controlled conversion is available.

Run the repository language check before committing:

```bash
python scripts/check_repository_language.py
```

The check rejects Chinese characters in tracked paths and in supported text files. Binary English or German source documents are reviewed separately before they enter Git.
