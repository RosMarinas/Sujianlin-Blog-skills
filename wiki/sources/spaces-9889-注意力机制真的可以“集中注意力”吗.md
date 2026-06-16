---
type: article_summary
title: 注意力机制真的可以“集中注意力”吗？
article_id: 9889
source_url: https://spaces.ac.cn/archives/9889
date: 2023-12-12
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9889
status: draft
updated: 2026-06-12
---

# 注意力机制真的可以“集中注意力”吗？

本文使用基于 $l_1/l_2$ 范数的稀疏性指标 $S(x)$，定量考察了不同Attention机制“集中注意力”的能力及其极限。
在高维高斯分布的假设下，作者推导了不同注意力权重函数的稀疏度指标。
计算表明，使用指数函数（$\exp$）的标准Attention在参数模长或方差趋于无穷大时，稀疏度 $S(x) 	o 0$，即具备实现无限稀疏、完全集中注意力的能力。
相反，不加激活函数的极简线性Attention的稀疏度存在一个较高的非零下限，这意味着它无法任意稀疏，在面对长序列时难以精确定位到关键token，这从稀疏度视角解释了线性Attention的性能缺陷。
对于一般非负型线性Attention，要达到高稀疏度必须降低特征序列的信噪比，而这会降低其表达相对位置信息的能力（即退化为低秩瓶颈）。
相比之下，带有相对位置衰减（Decay）的线性RNN模型虽然稀疏度不受限，但其衰减形式是静态且固定的，无法自适应地关注长程Context。