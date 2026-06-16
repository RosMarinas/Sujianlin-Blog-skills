---
type: article_summary
title: 漫谈重参数：从正态分布到Gumbel Softmax
article_id: "6705"
source_url: https://spaces.ac.cn/archives/6705
date: 2019-06-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-06-10-漫谈重参数-从正态分布到Gumbel-Softmax.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[重参数]]
  - [[Gumbel分布]]
  - [[Softmax]]
  - [[SF估计]]
methods:
  - [[重参数技巧]]
  - [[Gumbel Softmax离散重参数]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-06-10-漫谈重参数-从正态分布到Gumbel-Softmax.md
source_ids:
  - "6705"
status: draft
updated: 2026-06-11
---

## 文章核心问题

重参数技巧（Reparameterization）如何处理含概率分布的期望目标函数，使其可微分地采样？

## 主要结论

- 连续情形（如正态分布）：$z = \mu_\theta + \sigma_\theta \varepsilon$，$\varepsilon\sim\mathcal{N}(0,1)$
- 离散情形：Gumbel Max提供离散采样，Gumbel Softmax提供可微近似
- 重参数比SF估计（Score Function Estimator）方差小，梯度更稳定

## 推导结构

1. 连续情形重参数：正态分布例子
2. 离散情形重参数：Gumbel Max → Gumbel Softmax + 退火
3. 梯度估计对比：重参数 vs SF估计

## 关键公式

重参数：$L_\theta = \mathbb{E}_{\varepsilon\sim q(\varepsilon)}[f(g_\theta(\varepsilon))]$

Gumbel Softmax：$\text{softmax}\left((\log p_i - \log(-\log\varepsilon_i))/\tau\right)$

## 体现的方法

重参数技巧、Gumbel Softmax离散重参数

## 所属系列位置

独立单篇，与9085（从重参数看离散概率分布构建）互为镜像。

## 与其他文章的关系

9085是本文的逆过程。本文也是VAE、文本GAN等模型的理论基础。

## 原文证据锚点

- 重参数基本概念
- 正态分布重参数
- Gumbel Max证明
- SF估计与方差对比
