---
type: article_summary
title: 不用L约束又不会梯度消失的GAN，了解一下？
article_id: "6163"
source_url: https://spaces.ac.cn/archives/6163
date: 2018-11-20
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
  - "[[生成模型]]"
concepts:
  - "[[GAN-QP平方势散度]]"
  - "[[Wasserstein距离]]"
methods:
  - "[[用对偶散度构造对抗生成目标]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::6163::对偶散度定义
  - ev::6163::平方势散度
  - ev::6163::GAN-QP目标
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
source_ids:
  - "6163"
status: draft
updated: 2026-06-11
---

# 不用L约束又不会梯度消失的GAN，了解一下？

## 文章核心问题

从对偶空间直接定义散度，提出平方势散度和GAN-QP，使GAN无需显式L约束也能避免梯度消失。

## 主要结论

- GAN目标可以从对偶空间直接构造散度，然后通过min-max过程训练生成器。
- QP-div在WGAN差值项上加入二次势能项，使最优解自动满足类似L约束的性质。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用对偶散度构造对抗生成目标]]

## 原文证据锚点

- `ev::6163::对偶散度定义`
- `ev::6163::平方势散度`
- `ev::6163::GAN-QP目标`
