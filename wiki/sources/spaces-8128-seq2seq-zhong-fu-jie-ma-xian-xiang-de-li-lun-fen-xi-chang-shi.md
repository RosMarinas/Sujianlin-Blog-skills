---
type: article_summary
title: Seq2Seq重复解码现象的理论分析尝试
article_id: "8128"
source_url: https://spaces.ac.cn/archives/8128
date: 2021-01-26
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-01-26-Seq2Seq重复解码现象的理论分析尝试.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-01-26-Seq2Seq重复解码现象的理论分析尝试.md
source_ids:
  - "8128"
status: draft
updated: 2026-06-12
---

## 文章核心问题
从理论上分析Seq2Seq重复解码现象，推导二元解码模型下的重复概率公式，并据此提出改进思路。

## 主要结论
重复概率R = Σ Tr(P⊗P)^k；下界分析表明Greedy Search的重复风险最高（ζ最小）；降低转移矩阵每行方差（如合并高频搭配词）有助于降低重复率。

## 推导结构
1. 二元解码模型假设（2-gram马尔可夫）
2. 重复概率公式推导
3. 下界估计：R ≥ Σ (Tr P^k)^2 / (ζ^k n^k)
4. 上界估计：R ≈ n λ_1/(1-λ_1)
5. Frobenius介值定理：λ_1介于min Σ_j P^2_{ij}和max Σ_j P^2_{ij}
6. 结论：降低方差→合并高频词（Rebalanced Encoding）

## 关键公式
- R = Σ_{k=1}∞ Tr(P⊗P)^k
- 均值不等式下界
- λ_1(P⊗P) ∈ [min_i Σ_j P^2_ij, max_i Σ_j P^2_ij]
- Σ_j P^2_ij ≥ 1/n

## 体现的方法
重复解码概率理论分析方法、转移矩阵方差降低方法（Rebalanced Encoding）、二元解码分析方法

## 所属系列位置
独立文章，属于Seq2Seq理论分析系列

## 与其他文章的关系
为[7500]的"根本停不下来"问题提供理论补充；与[7259]的Exposure Bias分析互补

## 原文证据锚点
重复概率公式推导、Frobenius介值定理应用、词合并建议