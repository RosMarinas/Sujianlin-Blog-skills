---
type: article_summary
title: "模型优化漫谈：BERT的初始标准差为什么是0.02？"
article_id: "8747"
source_url: https://spaces.ac.cn/archives/8747
date: 2021-11-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-11-08-模型优化漫谈-BERT的初始标准差为什么是0-02.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[PostNorm梯度消失]]"
  - "[[PreNorm vs PostNorm]]"
  - "[[Warmup训练策略]]"
  - "[[BERT初始化标准差]]"
evidence_spans:
  - "ev::8747::PostNorm指数衰减"
  - "ev::8747::LN加剧梯度消失"
  - "ev::8747::PreNorm对比"
  - "ev::8747::Adam克服梯度消失"
  - "ev::8747::Warmup必要性"
  - "ev::8747::0.02标准差原因"
  - "ev::8747::MLM多加Dense原因"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-08-模型优化漫谈-BERT的初始标准差为什么是0-02.md
source_ids:
  - "8747"
status: draft
updated: 2026-06-12
---

# 模型优化漫谈：BERT的初始标准差为什么是0.02？

## Summary

本文系统分析了BERT/Transformer的梯度消失问题，指出Post Norm的LN会加剧梯度消失（残差被指数衰减），但通过小标准差初始化（0.02）、Warmup和Adam优化器可有效缓解，并解释了BERT中多个设计细节的优化动机。

## Key Claims

1. Post Norm的LN在初始化阶段相当于除以√2，递归后残差贡献被指数衰减（x_l ≈ x₀/2^{l/2}）。
2. LN不仅不能缓解梯度消失，反而是梯度消失的"元凶"之一。
3. Pre Norm（x+F(Norm(x)))让各残差分支平权，无指数衰减问题。
4. Post Norm在Finetune时反而是优势：梯度消失保护了底层预训练参数。
5. Adam的更新量≈O(η)，与梯度大小无关，因此能克服梯度消失。
6. Warmup防止后面层过快收敛到糟糕局部最优点后崩盘。
7. 0.02标准差（约为标准初始化的一半）使初始化时F(x)方差更小，从而Norm后直路权重更大（更接近恒等函数）。

## Key Formulas

- Post Norm初始化: x_{t+1} = (x_t + F_t(x_t))/√2
- Adam更新量近似: Δθ = -η·E[g_t]/√E[g_t²] (O(1)量级)

## Connections

本文的梯度消失分析与7888中RNN梯度消失的分析角度互补。Post Norm的LN指数衰减与7681中权重尺度偏移对模型行为的影响都是"初始化/归一化设计影响优化"的典型案例。
