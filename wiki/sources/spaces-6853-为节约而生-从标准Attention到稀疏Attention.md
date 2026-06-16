---
type: article_summary
title: 为节约而生：从标准Attention到稀疏Attention
article_id: "6853"
source_url: https://spaces.ac.cn/archives/6853
date: 2019-07-27
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
concepts:
  - "[[稀疏Attention结构]]"
  - "[[Attention Sparsity]]"
methods:
  - "[[用结构约束线性化Attention计算]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::6853::稀疏原理
  - ev::6853::局部空洞结构
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
source_ids:
  - "6853"
status: draft
updated: 2026-06-11
---

# 为节约而生：从标准Attention到稀疏Attention

## 文章核心问题

把全量自注意力改成局部、空洞和稀疏模式，用先验结构减少注意力矩阵的有效连接。

## 主要结论

- 稀疏Attention通过限制可见邻域来降低关联计算，而不是改变注意力的基本加权平均语义。
- Local与Atrous结构可组合成局部紧密、远程稀疏的长程建模模式。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用结构约束线性化Attention计算]]

## 原文证据锚点

- `ev::6853::稀疏原理`
- `ev::6853::局部空洞结构`
