---
type: article_summary
title: 两个多元正态分布的KL散度、巴氏距离和W距离
article_id: "8512"
source_url: https://spaces.ac.cn/archives/8512
date: 2021-07-08
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[KL散度]]
  - [[巴氏距离]]
  - [[W距离]]
  - [[正态分布]]
  - [[舒尔补]]
methods:
  - [[高斯积分法]]
  - [[拉格朗日乘子法]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
source_ids:
  - "8512"
status: draft
updated: 2026-06-11
---

## 文章核心问题

计算两个多元正态分布之间的KL散度、巴氏距离和Wasserstein距离，给出显式解析解。

## 主要结论

- KL散度：$\frac{1}{2}[(\mu_p-\mu_q)^\top\Sigma_q^{-1}(\mu_p-\mu_q) - \log\det(\Sigma_q^{-1}\Sigma_p) + \text{Tr}(\Sigma_q^{-1}\Sigma_p) - n]$
- 巴氏距离：$\frac{1}{2}\log\frac{\det(\Sigma)}{\sqrt{\det(\Sigma_p\Sigma_q)}} + \frac{1}{8}(\mu_p-\mu_q)^\top\Sigma^{-1}(\mu_p-\mu_q)$
- W距离（$\mathcal{W}_2$）：$\|\mu_p-\mu_q\|^2 + \text{Tr}(\Sigma_p) + \text{Tr}(\Sigma_q) - 2\text{Tr}((\Sigma_p^{1/2}\Sigma_q\Sigma_p^{1/2})^{1/2})$

## 推导结构

1. 正态分布基础 + 高斯积分
2. KL散度推导（用迹恒等式）
3. 巴氏距离推导（高斯积分配方）
4. W距离推导：去均值 → 纯代数 → 舒尔补 → 乘子法 → Weyl不等式

## 关键公式

$KL(p\|q) = \frac{1}{2}[(\mu_p-\mu_q)^\top\Sigma_q^{-1}(\mu_p-\mu_q) - \log\det(\Sigma_q^{-1}\Sigma_p) + \text{Tr}(\Sigma_q^{-1}\Sigma_p) - n]$

## 体现的方法

高斯积分法、拉格朗日乘子法、舒尔补、Weyl不等式

## 所属系列位置

独立单篇，属于概率分布度量主题。

## 与其他文章的关系

与WGAN（6051、8757）中W距离的应用相关。

## 原文证据锚点

- KL散度推导和使用迹恒等式
- 巴氏距离的积分配方
- W距离的两种版本及其等价性
- 舒尔补和拉格朗日乘子法求最大值
