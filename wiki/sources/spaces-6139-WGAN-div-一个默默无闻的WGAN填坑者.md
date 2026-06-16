---
type: article_summary
title: WGAN-div：一个默默无闻的WGAN填坑者
article_id: "6139"
source_url: https://spaces.ac.cn/archives/6139
date: 2018-11-07
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
  - "[[Lipschitz约束与泛化]]"
concepts:
  - "[[WGAN]]"
  - "[[WGAN-div]]"
  - "[[Lipschitz约束]]"
methods:
  - "[[用对偶散度构造对抗生成目标]]"
  - "[[梯度惩罚满足L约束]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::6139::W散度目标
  - ev::6139::WGAN-div训练
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
source_ids:
  - "6139"
status: draft
updated: 2026-06-11
---

# WGAN-div：一个默默无闻的WGAN填坑者

## 文章核心问题

介绍WGAN-div：用带梯度范数惩罚的W散度目标替代经验式L约束，作为WGAN-GP的理论化改写。

## 主要结论

- WGAN-div把梯度惩罚内化为W散度的构造，而不只是给WGAN判别器加经验正则项。
- 判别器目标仍服务于寻找分布差异方向，生成器则最小化该判别器差值。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用对偶散度构造对抗生成目标]]
- [[梯度惩罚满足L约束]]

## 原文证据锚点

- `ev::6139::W散度目标`
- `ev::6139::WGAN-div训练`
