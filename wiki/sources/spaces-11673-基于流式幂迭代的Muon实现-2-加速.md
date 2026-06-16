---
type: article_summary
title: 基于流式幂迭代的Muon实现：2. 加速
article_id: "11673"
source_url: https://spaces.ac.cn/archives/11673
date: 2026-03-26
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-03-26-基于流式幂迭代的Muon实现-2-加速.md
source_html: Data/Spaces_ac_cn/raw/articles/11673/page.html
series:
  - "[[基于流式幂迭代的Muon实现]]"
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[流式幂迭代]]"
methods:
  - "[[将昂贵矩阵运算流式化]]"
problem_patterns: []
evidence_spans:
  - ev::11673::流式迭代
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-03-26-基于流式幂迭代的Muon实现-2-加速.md
source_ids:
  - "11673"
status: draft
updated: 2026-06-09
---

# 基于流式幂迭代的Muon实现：2. 加速

## 文章核心问题

第一篇已经证明流式幂迭代能跑通，本文聚焦计算瓶颈：QR 分解如何加速到接近可用水平。

## 主要结论

- 流式方案把主要成本从 Newton-Schulz 迭代转移到 QR 分解。
- 双正交化、平移不变和多步修正都围绕降低条件数展开。
- 效率仍慢于标准 `msign` 实现，但提供更丰富的 SVD 信息。

## 推导结构

1. 重述流式迭代公式。
2. 分析朴素 QR 和 Cholesky QR 的成本。
3. 引入双正交化和平移加速。
4. 汇总效果与代价。

## 关键公式

- [[Muon更新公式]]：作为比较标准实现与流式实现的基准。

## 体现的方法

- [[将昂贵矩阵运算流式化]]：在可接受成本下保留更完整的 SVD 信息。

## 所属系列位置

这是系列第二篇，负责从可行性进入效率优化。

## 与其他文章的关系

- follows: `article::11654`
- precedes: `article::11697`
- refines: `concept::流式幂迭代`

## 原文证据锚点

- `ev::11673::流式迭代`：解释缓存上一步结果并每步只迭代一次 QR 的含义。
- `ev::11673::方法汇总`：汇总加速技巧的效果与代价。
