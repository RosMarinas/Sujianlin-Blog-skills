---
type: article_summary
title: Cool Papers + 站内搜索的一些新尝试
article_id: "10311"
source_url: https://spaces.ac.cn/archives/10311
date: 2024-08-12
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-08-12-Cool-Papers-站内搜索-的一些新尝试.md
source_html: null
series: []
topics:
  - "[[Cool Papers工具生态]]"
  - "[[全文检索]]"
concepts:
  - "[[TF-IDF]]"
  - "[[BM25]]"
  - "[[词云]]"
  - "[[用户偏好排序]]"
methods:
  - "[[用TF-IDF关键词检索相关论文]]"
problem_patterns: []
evidence_spans:
  - ev::10311::相关论文
  - ev::10311::词云统计
  - ev::10311::偏好排序
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-08-12-Cool-Papers-站内搜索-的一些新尝试.md
source_ids:
  - "10311"
status: draft
updated: 2026-06-10
---

## 文章核心问题

在已有站内搜索基础上，如何通过算法进一步提升Cool Papers的论文筛选和检索效率。

## 主要结论

1. 基于TF-IDF提取每篇论文的10个关键词，作为论文压缩表征，用于"REL"相关论文搜索。
2. 用户点击过的论文关键词聚合成词云，反映阅读偏好并用于后续推荐。
3. 用户可设置偏好关键词，网站基于站内搜索算法对论文按个人偏好排序（"❤"按钮），替代全局"星标"排序。
4. 用户偏好数据存储在浏览器本地，Cool Papers不收集。

## 推导结构

相关论文（TF-IDF关键词+REL按钮）→ 历史词云（关键词聚合显示用户偏好）→ 偏好排序（关键词作为Query的搜索排序）。

## 关键公式

- TF-IDF：$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$

## 体现的方法

- **用TF-IDF关键词检索相关论文**：利用TF-IDF从论文标题和摘要提取关键词作为压缩表征，以此为基础搜索相关论文和构建用户偏好词云。

## 所属系列位置

Cool Papers搜索功能系列的增强篇。前置文章为[[spaces-10088-站内检索系统]]。

## 与其他文章的关系

- 前置文章：[[spaces-10088-站内检索系统]]（基础搜索功能）。
- 后文可能包括进一步的推荐系统优化。

## 原文证据锚点

- `ev::10311::相关论文`：TF-IDF提取关键词、"REL"按钮和相关论文搜索原理。
- `ev::10311::词云统计`：阅读词云的生成逻辑——聚合用户点击论文的关键词。
- `ev::10311::偏好排序`：偏好关键词设置和"★"/"❤"两种排序方式的原理。
