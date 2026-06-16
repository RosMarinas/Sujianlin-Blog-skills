---
type: article_summary
title: Cool Papers更新：简单适配Zotero Connector
article_id: "11250"
source_url: https://spaces.ac.cn/archives/11250
date: 2025-08-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-08-25-Cool-Papers更新-简单适配Zotero-Connector.md
source_html: null
series: []
topics:
  - "[[Cool Papers工具生态]]"
  - "[[论文管理工具]]"
concepts:
  - "[[Zotero Connector]]"
  - "[[Metadata嵌入]]"
  - "[[Translator]]"
methods:
  - "[[用Metadata嵌入和Translator适配Zotero]]"
problem_patterns: []
evidence_spans:
  - ev::11250::单篇导入
  - ev::11250::批量导入
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-08-25-Cool-Papers更新-简单适配Zotero-Connector.md
source_ids:
  - "11250"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何让Cool Papers支持用户将论文导入Zotero文献管理工具。

## 主要结论

1. 单篇导入：通过在网页头部嵌入Zotero可识别的Metadata，用户安装Zotero Connector后点击图标即可导入单篇论文，包括PDF。
2. 批量导入：需要编写Translator（JS代码），放入Zotero的translators目录。批量导入的论文范围为当前页面下用户曾点击过[PDF]或[Kimi]的论文。
3. Translator已开源在GitHub上。

## 推导结构

单篇导入（Metadata嵌入方案）→ 批量导入（Translator编写方案）。

## 关键公式

无定量公式。

## 体现的方法

- **用Metadata嵌入和Translator适配Zotero**：通过嵌入标准网页Metadata支持单篇自动导入，通过编写Zotero Translator JS代码支持批量导入，实现Cool Papers与Zotero文献管理工具的互通。

## 所属系列位置

Cool Papers工具生态系列的扩展篇。

## 与其他文章的关系

- 属于Cool Papers系列的功能扩展，与其论文管理流程相关。
- 前置文章：[[spaces-10088-站内检索系统]]和[[spaces-10311-站内搜索新尝试]]（搜索和筛选论文是管理流程的一部分）。
- 被引用：在Cool Papers整体论文工作流中作为"收藏/导出"环节。

## 原文证据锚点

- `ev::11250::单篇导入`：通过网页头部嵌入Metadata实现单篇论文一键导入Zotero。
- `ev::11250::批量导入`：通过编写Translator JS代码实现列表页批量导入，导入范围为点击过[PDF]/[Kimi]的论文。
