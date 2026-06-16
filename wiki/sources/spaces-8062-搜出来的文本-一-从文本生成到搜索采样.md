---
type: article_summary
title: "【搜出来的文本】⋅（一）从文本生成到搜索采样"
article_id: "8062"
source_url: https://spaces.ac.cn/archives/8062
date: 2021-01-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-01-07-搜出来的文本-一-从文本生成到搜索采样.md
series: [搜出来的文本]
topics: [文本生成, 受限文本生成, 采样算法]
concepts: [受限文本生成, 重要性采样, 拒绝采样]
methods: [重要性采样, 拒绝采样]
problem_patterns: [受限文本生成中的采样困难]
evidence_spans:
  - 8062-明确目标
  - 8062-困难分析
  - 8062-重要采样
  - 8062-拒绝采样
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-01-07-搜出来的文本-一-从文本生成到搜索采样.md
source_ids:
  - "8062"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何通过离散优化的思想（不依赖标签数据）完成受限文本生成？

## 主要结论

1. 受限文本生成的核心思路：将文本生成目标量化为未归一化分布ρ(x,c)，通过最大化或采样来生成目标文本，无需标签数据训练新模型。
2. 从高维分布直接采样是困难的（组合爆炸），需要特别的采样算法。
3. 重要性采样（Importance Sampling）：通过易于采样的分布q(x)加权估计期望，适用于只知道未归一化分布ρ(x)的场景。
4. 拒绝采样（Rejection Sampling）：从q(x)采样后随机筛选，使剩余样本服从目标分布p(x)，接受率与q(x)和p(x)的相似度相关。

## 推导结构

- 受限文本生成问题形式化 → ρ(x,c) = p(x)·sim(x,c)·χ(x,c)
- 采样困难分析（组合爆炸）
- 重要性采样推导
- 拒绝采样推导（接受率设计）
