---
type: article_summary
title: WGAN新方案：通过梯度归一化来实现L约束
article_id: "8757"
source_url: https://spaces.ac.cn/archives/8757
date: 2021-11-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
series: []
topics:
  - [[Lipschitz约束与泛化]]
concepts:
  - [[梯度归一化]]
  - [[Lipschitz约束]]
  - [[WGAN]]
methods:
  - [[梯度归一化满足L约束]]
  - [[谱归一化满足L约束]]
  - [[梯度惩罚满足L约束]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
source_ids:
  - "8757"
status: draft
updated: 2026-06-11
---

## 文章核心问题

在WGAN中，如何通过梯度归一化实现判别器的Lipschitz约束？

## 主要结论

梯度归一化：$\hat{D}(x) = D(x) / (\|\nabla_x D(x)\| + |D(x)|)$ 自动满足 $\|\nabla_x \hat{D}(x)\| \leq 1$。但存在连续性疑问：分段线性函数的梯度不连续导致归一化后函数不连续。

## 推导结构

1. WGAN L约束回顾
2. 参数裁剪/谱归一化 vs 梯度惩罚
3. 梯度归一化方案：除以梯度范数
4. 连续性疑问和实验对比

## 关键公式

$\hat{D}(x) = \frac{D(x)}{\|\nabla_x D(x)\| + |D(x)|}$

## 体现的方法

梯度归一化满足L约束

## 所属系列位置

独立单篇，WGAN主题的一部分。

## 与其他文章的关系

与6051（Lipschitz约束）互补，讨论另一种实现L约束的方案。

## 原文证据锚点

- 方案简介：梯度归一化
- 连续性疑问
- 实验对比
