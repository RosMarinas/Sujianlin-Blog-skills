---
type: article_summary
title: 从重参数的角度看离散概率分布的构建
article_id: "9085"
source_url: https://spaces.ac.cn/archives/9085
date: 2022-05-25
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-05-25-从重参数的角度看离散概率分布的构建.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[重参数]]
  - [[Gumbel分布]]
  - [[Softmax]]
methods:
  - [[重参数技巧]]
  - [[Gumbel Softmax离散重参数]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-05-25-从重参数的角度看离散概率分布的构建.md
source_ids:
  - "9085"
status: draft
updated: 2026-06-11
---

## 文章核心问题

除了Softmax，还有什么操作能生成一个概率分布？从重参数的逆过程构造概率归一化方法。

## 主要结论

通过噪声扰动+argmax的重参数逆过程，可以构造出一类概率归一化方法。Gumbel噪声对应Softmax，正态分布噪声对应另一种光滑概率归一化。

## 推导结构

1. 定义概率分布变换的4个条件
2. 噪声扰动构造：$p_i = P[\text{argmax}(\mu+\varepsilon)=i]$
3. 代入Gumbel分布推导出Softmax
4. 数值计算方法（正态分布情形）

## 关键公式

$p_i = \int_{-\infty}^{\infty} p(\varepsilon_i)\left[\prod_{j\neq i} \Phi(\mu_i - \mu_j + \varepsilon_i)\right]d\varepsilon_i$

## 体现的方法

重参数技巧、Gumbel Softmax离散重参数

## 所属系列位置

属于重参数相关主题系列的一部分，与6705（漫谈重参数）紧密关联。

## 与其他文章的关系

6705（漫谈重参数）的逆向视角。正过程：重参数采样；逆过程：从重参数构造分布。

## 原文证据锚点

- 问题定义：4个基本条件
- 噪声扰动构造推导
- Gumbel分布代入得Softmax
- 数值计算方法
