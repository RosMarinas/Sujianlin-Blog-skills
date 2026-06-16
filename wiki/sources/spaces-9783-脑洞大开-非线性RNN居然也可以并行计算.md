---
type: article_summary
title: 脑洞大开：非线性RNN居然也可以并行计算？
article_id: 9783
source_url: https://spaces.ac.cn/archives/9783
date: 2023-09-26
category: Mathematics
source_markdown: |
  Data/Spaces_ac_cn/markdown/Mathematics/2023-09-26-脑洞大开-非线性RNN居然也可以并行计算.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-09-26-脑洞大开-非线性RNN居然也可以并行计算.md
source_ids:
  - 9783
status: draft
updated: 2026-06-12
---

# 脑洞大开：非线性RNN居然也可以并行计算？

本文探讨了非线性RNN的并行训练问题，提出了一种打破串行计算限制的迭代算法。
以 $x_t = \tanh(Ax_{t-1} + u_t)$ 为例，两边同时减去线性项 $Ax_{t-1}$，将其改写为 $x_t^{(n)} - Ax_{t-1}^{(n)} = \tanh(Ax_{t-1}^{(n-1)} + u_t) - Ax_{t-1}^{(n-1)}$。
在这个迭代格式中，由于右侧的 $x_{t-1}^{(n-1)}$ 是上一步迭代已知的常数，整个方程在当前步退化为一个可并行的对角化线性RNN。
基于“摄动法”思想，当输入和隐藏状态为小量时，该迭代序列只需极少步数即可快速逼近不动点解。
为了加快收敛，作者引入了基于一阶泰勒展开的牛顿迭代格式。
作者指出，在深度学习中，完全不需要纠结迭代是否严格收敛到原非线性模型，而是可以直接将该迭代格式作为基本的多层线性RNN模型。
最后，作者以GRU为例展示了这一迭代转换的适用性，并引导出“直接叠加多层线性RNN+MLP可能比纠结非线性并行化更具实用性”的观点。