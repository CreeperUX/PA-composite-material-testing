# PA Composite Material Testing

[English](#english) | [中文](#中文)

## English

This repository contains the lightweight, version-controlled assets for the PA composite-material testing project: material-property reports, flexural and impact-test records, processed data, analysis notes, browser-based analysis tools, and curated STEP exports.

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

Detailed indexes are available in [`cad/README.md`](cad/README.md), [`materials/README.md`](materials/README.md), and [`tests/README.md`](tests/README.md).

### Flexural analysis

Open [`tests/flexural/analysis/data-analysis-tool.html`](tests/flexural/analysis/data-analysis-tool.html) in a browser. The default [`data-analysis.csv`](tests/flexural/analysis/data-analysis.csv) is stored beside the tool. If a browser blocks local `fetch` requests, select the CSV manually or serve the directory through a local HTTP server.

### CAD usage

Native Autodesk Inventor files, working drawings, and other CAD working assets remain local and are intentionally ignored. A curated set of hash-verified STEP export copies is published under [`cad/step/`](cad/step/README.md). Preparing this publication set does not move or rewrite the working CAD files.

### Data-storage policy

Large or working datasets are intentionally excluded from Git:

- camera RAW files and photo exports (`*.ARW`, `*.JPG`, `*.JPEG`);
- CT reconstructions and image slices (`*.rek`, `*.tif`, `*.tiff`);
- native CAD working files and non-published CAD exports;
- RAW sidecars, local logs, temporary files, and Autodesk `OldVersions` folders;
- formatted workbooks that have not yet been safely converted to English or German.

Keep raw data in OneDrive or institutional storage. Use Git LFS, Zenodo, OSF, or an equivalent large-data archive only when remote versioned storage is required.

### Language and versioning

Repository-authored technical content uses English, while original German laboratory and supplier sources remain unchanged. Every README provides an English section first and a Chinese reading-support section second. See [`docs/language-policy.md`](docs/language-policy.md).

The current repository version is `0.2.0`. `VERSION` stores the version number and `CHANGELOG.md` records traceable changes. Semantic Versioning is followed where practical.

## 中文

本仓库保存 PA 复合材料测试项目中适合版本控制的轻量资料，包括材料性能报告、弯折与冲击试验记录、处理后数据、分析说明、浏览器端分析工具，以及经过整理的 STEP 导出文件。

### 仓库结构

```text
.
├── cad/
│   ├── README.md                 原生 CAD 与发布规则
│   └── step/                     整理后的中性格式 STEP 导出文件
├── materials/
│   └── fabric-reports/           供应商与织物分析报告
├── tests/
│   ├── flexural/                 分析、报告、表单与设备导出结果
│   └── impact/                   冲击试验计算工具
├── docs/
│   └── language-policy.md        仓库语言要求
├── CHANGELOG.md
└── VERSION
```

详细目录说明见 [`cad/README.md`](cad/README.md)、[`materials/README.md`](materials/README.md) 和 [`tests/README.md`](tests/README.md)。

### 弯折数据分析

使用浏览器打开 [`tests/flexural/analysis/data-analysis-tool.html`](tests/flexural/analysis/data-analysis-tool.html)。默认数据文件 [`data-analysis.csv`](tests/flexural/analysis/data-analysis.csv) 与工具位于同一目录。如果浏览器阻止本地 `fetch` 请求，可以手动选择 CSV 文件，或通过本地 HTTP 服务打开该目录。

### CAD 使用说明

Autodesk Inventor 原生文件、工作图纸和其他 CAD 工作资料仅保留在本地，并由 Git 忽略。经过整理和哈希验证的 STEP 发布副本位于 [`cad/step/`](cad/step/README.md)。创建发布副本时不会移动或改写工作用 CAD 文件。

### 数据存储规则

以下大型数据或工作文件不纳入 Git：

- 相机 RAW 文件及照片导出（`*.ARW`、`*.JPG`、`*.JPEG`）；
- CT 重建数据和图像切片（`*.rek`、`*.tif`、`*.tiff`）；
- 原生 CAD 工作文件及未发布的 CAD 导出文件；
- RAW 附属文件、本地日志、临时文件及 Autodesk `OldVersions` 目录；
- 尚未在不影响公式或格式的前提下转换为英语或德语的工作簿。

原始数据应保存在 OneDrive 或学校/机构存储中。只有在确实需要远程版本管理时，才使用 Git LFS、Zenodo、OSF 或同类大文件存储方案。

### 语言与版本管理

仓库自行编写的技术内容以英语为准，德语实验室报告和供应商原始资料保持不变。所有 README 均采用英语在前、中文阅读支持在后的结构。详细规则见 [`docs/language-policy.md`](docs/language-policy.md)。

当前仓库版本为 `0.2.0`。`VERSION` 保存版本号，`CHANGELOG.md` 记录可追踪的变更；在适用情况下遵循语义化版本规则。
