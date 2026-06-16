---
type: article_summary
title: "变分自编码器 = 最小化先验分布 + 最大化互信息"
article_id: "6088"
source_url: https://spaces.ac.cn/archives/6088
date: 2018-10-10
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-10-10-变分自编码器-最小化先验分布-最大化互信息.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[VAE互信息分解]]"
  - "[[变分自编码器]]"
methods:
  - "[[KL损失分解技巧]]"
evidence_spans:
  - ev::6088::过程
  - ev::6088::结语
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-10-变分自编码器-最小化先验分布-最大化互信息.md
source_ids:
  - "6088"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文证明VAE的损失函数可以自然分解为"最小化先验KL散度"和"最大化互信息"两项，从而为Deep INFOMAX模型的损失函数提供了理论依据。

## 核心问题

Deep INFOMAX模型的损失函数看起来像是先验KL项与互信息项的拼凑组合，是否可以从VAE的理论框架中自然地推导出来？

## 关键结论

1. VAE损失 $KL(\tilde{p}(x)p(z|x) \| q(z)q(x|z))$ 可分解为两项：第一项 $\iint \tilde{p}(x)p(z|x)\log\frac{p(z|x)}{q(z)} dzdx$ 是先验KL散度，第二项 $-\iint \tilde{p}(x)p(z|x)\log\frac{q(x|z)}{\tilde{p}(x)} dzdx$ 是负互信息。
2. 当 $q(x|z)$ 具有无限拟合能力时，第二项等价于 $KL(q(x|z)p(z) \| \tilde{p}(x)p(z))$，即 $x$ 和 $z$ 的互信息。
3. Deep INFOMAX的损失函数不是拼凑的启发式组合，而是VAE理论的直接推论。

## 核心推导

标准VAE损失是联合分布的KL散度。将log项中的分式在 $\frac{p(z|x)}{q(z)}$ 和 $\frac{\tilde{p}(x)}{q(x|z)}$ 之间拆分，第一项变为先验KL，第二项中的 $\log\frac{q(x|z)}{\tilde{p}(x)}$ 正是点互信息。在 $q(x|z)$ 无限容量假设下，最优解满足 $\tilde{p}(x)p(z|x) = q(x|z)p(z)$（贝叶斯公式），第二项归结为 $KL(\tilde{p}(x)p(z|x) \| \tilde{p}(x)p(z)) = I(x;z)$。

## 关键公式

$$KL(\tilde{p}(x)p(z|x) \| q(z)q(x|z)) = \iint \tilde{p}(x)p(z|x)\log\frac{p(z|x)}{q(z)} dzdx - \iint \tilde{p}(x)p(z|x)\log\frac{q(x|z)}{\tilde{p}(x)} dzdx$$

其中第一项为先验KL，第二项为负互信息。

## 实验或案例

无。本文为纯理论推导。

## 系列定位

本文是变分自编码器系列的一篇补充性短文，架起了VAE与Deep INFOMAX之间的桥梁。它不属于编号1-8的正文章节，但为理解VAE损失的语义提供了一种全新的视角——VAE不仅是在做变分推断，同时也在隐式地最大化输入与隐变量之间的互信息。
