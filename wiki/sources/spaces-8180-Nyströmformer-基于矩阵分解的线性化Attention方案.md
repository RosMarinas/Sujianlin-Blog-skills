---
type: article_summary
title: Nyströmformer：基于矩阵分解的线性化Attention方案
article_id: "8180"
source_url: https://spaces.ac.cn/archives/8180
date: 2021-02-16
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
  - "[[低秩近似]]"
concepts:
  - "[[Nyströmformer]]"
  - "[[线性化Attention]]"
methods:
  - "[[用结构约束线性化Attention计算]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::8180::Nyström背景
  - ev::8180::三矩阵近似
  - ev::8180::伪逆近似
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
source_ids:
  - "8180"
status: draft
updated: 2026-06-11
---

# Nyströmformer：基于矩阵分解的线性化Attention方案

## 文章核心问题

用Nyström近似把完整Attention矩阵写成三个小矩阵乘积，再通过结合律实现线性化计算。

## 主要结论

- Nyströmformer把全量n×n注意力矩阵替换为n×m、m×m、m×n的结构化乘积。
- 中间逆矩阵可用伪逆和迭代求逆处理，体现低秩/骨架式结构分解思想。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用结构约束线性化Attention计算]]

## 原文证据锚点

- `ev::8180::Nyström背景`
- `ev::8180::三矩阵近似`
- `ev::8180::伪逆近似`
