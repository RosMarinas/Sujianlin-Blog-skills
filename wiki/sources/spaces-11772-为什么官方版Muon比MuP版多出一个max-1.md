---
type: article_summary
title: 为什么官方版Muon比MuP版多出一个max(1, ⋅)？
article_id: "11772"
source_url: https://spaces.ac.cn/archives/11772
date: 2026-06-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-06-03-为什么官方版Muon比MuP版多出一个max-1.md
source_html: Data/Spaces_ac_cn/raw/articles/11772/page.html
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[矩阵符号函数]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::11772::几个版本
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-06-03-为什么官方版Muon比MuP版多出一个max-1.md
source_ids:
  - "11772"
status: draft
updated: 2026-06-09
---

# 为什么官方版Muon比MuP版多出一个max(1, ⋅)？

## 文章核心问题

本文解释 KellerJordan 版 Muon 相比 MuP 版多出的 `max(1, ·)` 缩放截断来自哪里。

## 主要结论

- 不同 Muon 版本的关键差异在学习率矩阵形状相关缩放因子。
- 官方版的 `max(1, ·)` 可以从特征增量均匀性的角度理解。
- 该文把 MuP 缩放、Muon 规则和矩阵形状联系起来。

## 推导结构

1. 列出 Muon 几个版本的缩放因子。
2. 分析特征增量。
3. 区分各向同性与各向异性情形。
4. 总结 `max(1, ·)` 的来源。

## 关键公式

- [[Muon更新公式]]：作为不同版本缩放因子的共同背景。

## 体现的方法

- [[用稳定性指标约束优化器缩放]]：通过增量均匀性解释缩放规则。

## 所属系列位置

这是 MVP 中连接 MuP 缩放和 Muon 实现差异的桥接文章。

## 与其他文章的关系

- belongs_to: `topic::矩阵优化`
- uses: `method::用稳定性指标约束优化器缩放`

## 原文证据锚点

- `ev::11772::几个版本`：列出不同版本的缩放因子。
- `ev::11772::文章小结`：总结 `max(1, ·)` 的解释角度。
