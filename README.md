# PA Composite Material Testing

English | 中文

## English

Lightweight project assets for PA composite material testing.

The currently tracked scope focuses on flexural testing. The repository stores analysis reports, method notes, processed result tables, exported PDFs, CSV summaries, and the local browser-based HTML analysis tool.

### Contents

- Flexural test analysis reports and method notes.
- Processed CSV and spreadsheet result summaries.
- Exported PDF test outputs.
- A single-file HTML analysis tool for local data exploration and figure export.

### Analysis Tool

The HTML analysis tool runs locally in a browser and does not require a backend service. Its default interface language is English. Chinese remains available through the language selector or the `?lang=zh` URL parameter.

### Versioning

The repository uses `VERSION` for the current repository version and `CHANGELOG.md` for release notes. Update both files whenever the analysis tool, data workflow, reports, or repository documentation change in a way that should be traceable.

Current repository version: `0.1.2`.

Version numbers follow Semantic Versioning where practical:

- MAJOR version changes for incompatible workflow or data-format changes.
- MINOR version changes for new analysis features or substantial reporting improvements.
- PATCH version changes for fixes, wording updates, and documentation-only updates.

### Data Storage Policy

Large raw datasets from the wider local project are intentionally not committed:

- Camera RAW files and photo exports (`*.ARW`, `*.JPG`, `*.JPEG`).
- CT reconstruction files (`*.rek`).
- CT image slices (`*.tif`, `*.tiff`).
- RAW photo sidecars (`*.xmp`).
- Local logs and Autodesk backup folders.

The full local project folder was about 17.4 GB when this repository was created, with several files larger than GitHub's normal file limit. Keep large raw files in the original local or OneDrive storage, or move them to a dedicated large-data solution such as Git LFS, Zenodo, OSF, or institutional storage if remote archival is required.

## 中文

本仓库用于保存 PA 复合材料测试项目中的轻量级资料。

当前已纳入版本管理的范围以弯折测试为主，包括分析报告、方法说明、处理后的结果表格、导出的 PDF、CSV 汇总数据，以及可在本地浏览器运行的 HTML 数据分析工具。

### 仓库内容

- 弯折测试分析报告和方法说明。
- 处理后的 CSV 与电子表格结果汇总。
- 导出的 PDF 测试结果。
- 用于本地数据查看和图表导出的单文件 HTML 分析工具。

### 分析工具

HTML 分析工具可直接在浏览器中本地运行，不需要后端服务。默认界面语言为英语；如需中文，可通过界面语言选择器切换，或在 URL 后添加 `?lang=zh`。

### 版本管理

仓库使用 `VERSION` 记录当前版本，并使用 `CHANGELOG.md` 记录更新日志。当分析工具、数据流程、报告或仓库文档发生需要追踪的变化时，应同步更新这两个文件。

当前仓库版本：`0.1.2`。

版本号尽量遵循语义化版本规则：

- 主版本号用于不兼容的流程或数据格式变化。
- 次版本号用于新增分析功能或较大的报告改进。
- 修订版本号用于修复、文字调整和仅文档类更新。

### 数据存储策略

本地项目中的大型原始数据不会提交到该仓库：

- 相机 RAW 文件和照片导出文件（`*.ARW`、`*.JPG`、`*.JPEG`）。
- CT 重建文件（`*.rek`）。
- CT 图像切片（`*.tif`、`*.tiff`）。
- RAW 照片的附属文件（`*.xmp`）。
- 本地日志和 Autodesk 备份文件夹。

创建仓库时，完整本地项目文件夹约为 17.4 GB，其中包含多个超过 GitHub 普通文件限制的文件。大型原始文件应继续保存在本地或 OneDrive 中；如果需要远程归档，建议使用 Git LFS、Zenodo、OSF 或学校/机构提供的大文件存储方案。
