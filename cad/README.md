# CAD publication policy

Native CAD working files remain local and are excluded from Git. This includes Autodesk Inventor parts, assemblies, drawings, project files, working backups, DWG files, and derived PDFs.

The repository publishes only curated, neutral-format STEP copies under [`step/`](step/README.md). The publication set is grouped by fixture or specimen and includes a SHA-256 manifest. Every published STEP file is a byte-for-byte copy of its local export source; the working export is not moved or rewritten.

Published CAD content must use English or German names and documentation. Native Inventor files must never be added to Git without separate, explicit authorization.
