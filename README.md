# PA Composite Material Testing

This repository contains the lightweight, version-controlled assets for the PA composite-material testing project: material-property reports, flexural and impact-test records, processed data, analysis notes, and browser-based analysis tools.

### Repository map

```text
.
├── cad/
│   ├── README.md                 Native-CAD and publication policy
│   └── step/                     Curated neutral-format STEP exports
├── materials/
│   └── fabric-reports/           Supplier and fabric-analysis reports
├── tests/
│   ├── flexural/                 Analysis, reports, forms, and machine exports
│   └── impact/                   Impact-test calculation tools
├── docs/
│   └── language-policy.md        Repository language requirements
├── CHANGELOG.md
└── VERSION
```

The detailed indexes are in [`cad/README.md`](cad/README.md), [`materials/README.md`](materials/README.md), and [`tests/README.md`](tests/README.md).

### Flexural analysis

Open [`tests/flexural/analysis/data-analysis-tool.html`](tests/flexural/analysis/data-analysis-tool.html) in a browser. The default [`data-analysis.csv`](tests/flexural/analysis/data-analysis.csv) is kept beside the tool. If a browser blocks local `fetch` requests, select the CSV manually or serve the directory through a local HTTP server.

### CAD usage

Native Autodesk Inventor files, working drawings, and other CAD working assets remain local and are intentionally ignored. A curated set of hash-verified STEP export copies is published under [`cad/step/`](cad/step/README.md). Preparing this publication set does not move or rewrite the working CAD files.

### Data-storage policy

Large raw datasets are intentionally excluded from Git:

- camera RAW files and photo exports (`*.ARW`, `*.JPG`, `*.JPEG`);
- CT reconstructions and image slices (`*.rek`, `*.tif`, `*.tiff`);
- native CAD working files and non-published CAD exports under the local `cad/` workspace;
- RAW sidecars, local logs, temporary files, and Autodesk `OldVersions` folders;
- formatted workbooks that have not yet been safely converted to English or German.

The full local project is much larger than the GitHub repository and contains files beyond normal GitHub limits. Keep raw data in OneDrive or institutional storage; use Git LFS, Zenodo, OSF, or an equivalent large-data archive only when remote versioned storage is required.

### Versioning

The current repository version is `0.2.0`. `VERSION` stores the version number and `CHANGELOG.md` records traceable changes. Semantic Versioning is followed where practical.
