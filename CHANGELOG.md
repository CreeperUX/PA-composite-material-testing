# Changelog

All notable changes to this repository will be documented in this file.

This project follows Semantic Versioning where practical:

- MAJOR version for incompatible workflow or data-format changes.
- MINOR version for new analysis features or substantial UI/reporting improvements.
- PATCH version for fixes, wording changes, and documentation-only updates.

## [0.2.0] - 2026-07-15

### Added

- Added material-property reports and English four-point flexural-test forms.
- Added section-level README indexes and Git attributes for engineering binary formats.
- Added a repository-language policy and an automated language check.
- Added 14 hash-verified STEP export copies, grouped by fixture or specimen, with an integrity manifest.
- Added an English-first Chinese reading-support section to every README.
- Restored Chinese flexural reports and method notes to version control.
- Added complete English translations for every Chinese flexural Markdown document.

### Changed

- Reorganized version-controlled files under `materials/` and `tests/`.
- Split flexural-test content into `analysis/`, `docs/`, `forms/`, and `test-results/` without separating the analysis tool from its default CSV.
- Renamed repository-authored paths, documentation, analysis fields, and user-interface text to English.
- Kept German third-party reports and original German machine exports unchanged.
- Kept native Inventor working files and non-English formatted workbooks outside Git.
- Restricted CAD publication to copied STEP exports so native working files remain unchanged.
- Updated the language check to validate bilingual README structure while keeping other authored content English or German.
- Organized separate English and Chinese flexural documents under matching `en/` and `zh/` directories.
- Aligned paired flexural documents section by section and extended the language check to require matching headings, tables, fenced blocks, displayed equations, lists, and navigation links.
- Expanded the repository overview and storage policy to match the revised project scope.

## [0.1.2] - 2026-07-09

### Changed

- Reworked the README into a bilingual English and Chinese project overview.
- Updated the documented repository version to `0.1.2`.

## [0.1.1] - 2026-07-08

### Changed

- Rewrote the repository README as a pure English project overview.
- Clarified the tracked scope, analysis-tool usage, versioning policy, and large-data storage policy.

## [0.1.0] - 2026-07-08

### Changed

- Set the flexural test HTML analysis tool to use English as the default interface language.
- Kept Chinese available through the language selector or the `?lang=zh` URL parameter.

### Added

- Added an explicit analysis-tool version marker in the HTML interface.
- Added repository-level version tracking through `VERSION`.
- Added this changelog for future release notes.
