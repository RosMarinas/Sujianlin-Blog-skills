---
type: article_summary
title: 听说Attention与Softmax更配哦～
article_id: "9019"
source_url: https://spaces.ac.cn/archives/9019
date: 2022-04-07
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
concepts:
  - "[[Softmax]]"
  - "[[熵不变性]]"
  - "[[GAU]]"
methods:
  - "[[Attention-E熵不变性缩放]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::9019::Softmax归一化
  - ev::9019::Softmax熵版本
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
source_ids:
  - "9019"
status: draft
updated: 2026-06-11
---

# 听说Attention与Softmax更配哦～

## 文章核心问题

分析GAU长度迁移失效来源，指出relu^2/n归一化不如Softmax，并解释Softmax能做熵调控。

## 主要结论

- GAU的长度迁移问题主要来自归一化方式，而不是门控或单头结构本身。
- Softmax可以通过温度调节熵，幂函数归一化因正齐次性难以做到这一点。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[Attention-E熵不变性缩放]]

## 原文证据锚点

- `ev::9019::Softmax归一化`
- `ev::9019::Softmax熵版本`
