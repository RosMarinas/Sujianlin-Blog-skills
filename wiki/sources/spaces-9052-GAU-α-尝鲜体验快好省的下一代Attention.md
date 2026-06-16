---
type: article_summary
title: GAU-α：尝鲜体验快好省的下一代Attention
article_id: "9052"
source_url: https://spaces.ac.cn/archives/9052
date: 2022-04-22
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
concepts:
  - "[[GAU]]"
  - "[[熵不变性]]"
methods:
  - "[[Attention-E熵不变性缩放]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::9052::GAU替换
  - ev::9052::GAU归一化
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
source_ids:
  - "9052"
status: draft
updated: 2026-06-11
---

# GAU-α：尝鲜体验快好省的下一代Attention

## 文章核心问题

开源GAU-alpha并说明训练配置：用两层GAU替换Attention+FFN，同时采用熵不变性Softmax归一化。

## 主要结论

- GAU-alpha把结构简化和归一化选择结合起来，在长序列场景下更快且更省显存。
- 熵不变性Softmax是GAU-alpha保持长度外推能力的重要配置。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[Attention-E熵不变性缩放]]

## 原文证据锚点

- `ev::9052::GAU替换`
- `ev::9052::GAU归一化`
