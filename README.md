# PA Composite Material Testing

PA composite material testing project files.

This repository currently focuses on the `弯折测试/` portion of the local project. It stores the flexural test analysis reports, test result spreadsheets, exported PDFs, CSV data, and the local HTML analysis helper.

## Versioning

The repository uses `VERSION` for the current tracked version and `CHANGELOG.md` for release notes. Update both files whenever the analysis tool, data workflow, or reports change in a way that should be traceable.

The current version is `0.1.0`.

Large raw datasets from the wider local project are intentionally not committed:

- Sony RAW/JPEG photo sets (`*.ARW`, `*.JPG`)
- CT reconstruction files (`*.rek`)
- CT image slices (`*.tif`)
- RAW photo sidecars (`*.xmp`)
- local logs and Autodesk `OldVersions` backup folders

The full local project folder was about 17.4 GB when this repository was created, with several files larger than GitHub's normal file limit. Keep those large raw files in the original local/OneDrive storage, or move them to a dedicated large-data solution such as Git LFS, Zenodo, OSF, or institutional storage if they need remote archival.
