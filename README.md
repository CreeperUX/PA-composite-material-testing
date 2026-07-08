# PA Composite Material Testing

Lightweight project assets for PA composite material testing.

The currently tracked scope focuses on flexural testing. The repository stores analysis reports, method notes, processed result tables, exported PDFs, CSV summaries, and the local browser-based HTML analysis tool.

## Contents

- Flexural test analysis reports and method notes.
- Processed CSV and spreadsheet result summaries.
- Exported PDF test outputs.
- A single-file HTML analysis tool for local data exploration and figure export.

## Analysis Tool

The HTML analysis tool runs locally in a browser and does not require a backend service. Its default interface language is English. Chinese remains available through the language selector or the `?lang=zh` URL parameter.

## Versioning

The repository uses `VERSION` for the current repository version and `CHANGELOG.md` for release notes. Update both files whenever the analysis tool, data workflow, reports, or repository documentation change in a way that should be traceable.

Current repository version: `0.1.1`.

Version numbers follow Semantic Versioning where practical:

- MAJOR version changes for incompatible workflow or data-format changes.
- MINOR version changes for new analysis features or substantial reporting improvements.
- PATCH version changes for fixes, wording updates, and documentation-only updates.

## Data Storage Policy

Large raw datasets from the wider local project are intentionally not committed:

- Camera RAW files and photo exports (`*.ARW`, `*.JPG`, `*.JPEG`).
- CT reconstruction files (`*.rek`).
- CT image slices (`*.tif`, `*.tiff`).
- RAW photo sidecars (`*.xmp`).
- Local logs and Autodesk backup folders.

The full local project folder was about 17.4 GB when this repository was created, with several files larger than GitHub's normal file limit. Keep large raw files in the original local or OneDrive storage, or move them to a dedicated large-data solution such as Git LFS, Zenodo, OSF, or institutional storage if remote archival is required.
