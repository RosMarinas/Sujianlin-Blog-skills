---
type: article_summary
title: 巧断梯度：单个loss实现GAN模型
article_id: "6387"
source_url: https://spaces.ac.cn/archives/6387
date: 2019-02-22
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-02-22-巧断梯度-单个loss实现GAN模型.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
concepts:
  - "[[生成对抗网络 (GAN)]]"
  - "[[梯度截断]]"
methods:
  - "[[用梯度截断合并对抗训练目标]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::6387::梯度截断
  - ev::6387::单一loss
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-02-22-巧断梯度-单个loss实现GAN模型.md
source_ids:
  - "6387"
status: draft
updated: 2026-06-11
---

# 巧断梯度：单个loss实现GAN模型

## 文章核心问题

用stop_gradient控制梯度流，把GAN的判别器和生成器两个交替loss合并为一个同步训练loss。

## 主要结论

- GAN同步训练的关键不是改变算法目标，而是精确控制每个loss项能回传到哪些参数。
- 判别器和生成器项可以合并为单一loss，但用stop-gradient保留原有交替优化的梯度语义。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用梯度截断合并对抗训练目标]]

## 原文证据锚点

- `ev::6387::梯度截断`
- `ev::6387::单一loss`
