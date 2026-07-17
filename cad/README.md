# CAD publication policy

[English](#english) | [中文](#中文)

## English

Native CAD working files remain local and are excluded from Git. This includes Autodesk Inventor parts, assemblies, drawings, project files, working backups, DWG files, and derived PDFs.

The repository publishes only curated, neutral-format STEP copies under [`step/`](step/README.md). The publication set is grouped by fixture or specimen and includes a SHA-256 manifest. Every published STEP file is a byte-for-byte copy of its local export source; the working export is not moved or rewritten.

Published CAD content must use English or German names and documentation. Native Inventor files must never be added to Git without separate, explicit authorization.

## 中文

原生 CAD 工作文件仅保留在本地，并由 Git 忽略。这包括 Autodesk Inventor 零件、装配、工程图、项目文件、工作备份、DWG 文件以及由 CAD 生成的 PDF。

仓库只发布 [`step/`](step/README.md) 下经过整理的中性格式 STEP 副本。发布文件按夹具或试样分组，并附有 SHA-256 校验清单。每个 STEP 发布文件都与本地导出源文件逐字节一致；工作目录中的导出文件不会被移动或改写。

发布的 CAD 内容必须使用英语或德语文件名和说明文档。未经单独、明确授权，不得将原生 Inventor 文件加入 Git。
