---
type: article_summary
title: 互怼的艺术：从零直达WGAN-GP
article_id: "4439"
source_url: https://spaces.ac.cn/archives/4439
date: 2017-06-08
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-06-08-互怼的艺术-从零直达WGAN-GP.md
series:
  - "[[GAN目标函数与约束专题]]"
topics:
  - "[[GAN训练目标与约束]]"
  - "[[Lipschitz约束与泛化]]"
concepts:
  - "[[WGAN]]"
  - "[[Lipschitz约束]]"
methods:
  - "[[梯度惩罚满足L约束]]"
problem_patterns:
  - "[[把生成模型训练改写为分布差异最小化问题]]"
evidence_spans:
  - ev::4439::WGAN-GP直观目标
  - ev::4439::梯度惩罚
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-06-08-互怼的艺术-从零直达WGAN-GP.md
source_ids:
  - "4439"
status: draft
updated: 2026-06-11
---

# 互怼的艺术：从零直达WGAN-GP

## 文章核心问题

从直观分布比较出发推导WGAN-GP，把判别器的Lipschitz要求写成梯度范数惩罚。

## 主要结论

- GAN训练应比较批量分布的统计特征，而不是单样本真假标签。
- WGAN-GP把L约束软化为插值点上的梯度惩罚，得到可实现的判别器约束。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[梯度惩罚满足L约束]]

## 原文证据锚点

- `ev::4439::WGAN-GP直观目标`
- `ev::4439::梯度惩罚`
