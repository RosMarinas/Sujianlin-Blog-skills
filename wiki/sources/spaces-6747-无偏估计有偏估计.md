---
type: article_summary
title: 简述无偏估计和有偏估计
article_id: "6747"
source_url: https://spaces.ac.cn/archives/6747
date: 2019-06-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-06-19-简述无偏估计和有偏估计.md
series: []
topics:
  - 采样与估计
concepts:
  - unbiased estimation
  - biased estimation
  - Bessel's correction
methods:
  - 方差无偏估计校正
problem_patterns: []
evidence_spans:
  - "6747::简述无偏估计和有偏估计"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-06-19-简述无偏估计和有偏估计.md
source_ids:
  - "6747"
status: draft
updated: 2026-06-10
---

## 文章核心问题

解释为什么样本方差 $\frac{1}{n}\sum (x_i-\hat{\mu})^2$ 是有偏估计，而 $\frac{1}{n-1}\sum (x_i-\hat{\mu})^2$ 是无偏估计（Bessel校正）。

## 主要结论

- 方差的有偏估计源于期望运算的非线性：$\mathbb{E}[x^2] - \mathbb{E}[x]^2$ 中第二项的非线性导致有限样本估计的系统性低估
- 偏差因子是 $(n-1)/n$，乘以 $n/(n-1)$ 即可校正
- 不是所有有偏估计都能简单校正

## 推导结构

用 $n=2$ 特例推导：计算 $\mathbb{E}[\hat{\sigma}^2_{\text{有偏}}] = \frac{1}{2}(\mathbb{E}[x^2]-\mu^2) = \frac{n-1}{n}\sigma^2$，从而证明有偏因子为 $(n-1)/n$。

## 关键公式

$$\hat{\sigma}^2_{\text{有偏}} = \frac{1}{n}\sum_{i=1}^n (x_i - \hat{\mu})^2,\quad \hat{\sigma}^2_{\text{无偏}} = \frac{1}{n-1}\sum_{i=1}^n (x_i - \hat{\mu})^2$$

$$\mathbb{E}[\hat{\sigma}^2_{\text{有偏}}] = \frac{n-1}{n}\sigma^2$$

## 体现的方法

- 有限样本偏差分析与校正

## 所属系列位置

单篇独立文章。

## 与其他文章的关系

为批次中其他估计相关文章（NCE、变分积分估计）提供偏差分析基础。

## 原文证据锚点

- 有偏估计定义：文章开头
- n=2推导：中间推导
- 非线性解释：结尾理论分析
