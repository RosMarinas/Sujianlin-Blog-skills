---
type: topic
title: LLM架构与上下文扩展
scope: |
  涵盖大语言模型（LLM）的注意力机制优化、Decoder-only与双向架构满秩表达能力的理论对比、线性RNN（如LRU、RWKV）的参数化及对角化并行计算、基于朴素贝叶斯的推理期上下文窗口扩展（NBCE）、注意力机制的稀疏性数学量化，以及利用偏置项（Bias）增强RoPE长度外推性能的研究。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-20-为什么现在的LLM都是Decoder-only的架构-FAQ.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-06-08-Naive-Bayes-is-all-you-need.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-09-26-脑洞大开-非线性RNN居然也可以并行计算.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9529
  - 9547
  - 9554
  - 9577
  - 9593
  - 9617
  - 9632
  - 9648
  - 9783
  - 9889
series:
  - [LLM架构与上下文扩展](wiki/series/LLM架构与上下文扩展.md)
concepts:
  - [Decoder-only架构](wiki/concepts/Decoder-only架构.md)
  - [LRU](wiki/concepts/LRU.md)
  - [SLRU](wiki/concepts/SLRU.md)
  - [NBCE](wiki/concepts/NBCE.md)
  - [RoPE-Bias](wiki/concepts/RoPE-Bias.md)
  - [Attention信息熵](wiki/concepts/Attention信息熵.md)
  - [Attention Sparsity](wiki/concepts/attention_sparsity.md)
formulas:
  - [NBCE概率聚合公式](wiki/formulas/NBCE概率聚合公式.md)
  - [LRU循环方程](wiki/formulas/LRU循环方程.md)
  - [注意力稀疏度指标公式](wiki/formulas/注意力稀疏度指标公式.md)
propositions:
  - [Decoder-only满秩优势](wiki/propositions/Decoder-only满秩优势.md)
  - [Softmax注意力防噪](wiki/propositions/Softmax注意力防噪.md)
  - [注意力作为广义朴素贝叶斯](wiki/propositions/注意力作为广义朴素贝叶斯.md)
  - [线性Attention注意力集中局限性](wiki/propositions/线性Attention注意力集中局限性.md)
  - [RoPE-Bias外推性](wiki/propositions/RoPE-Bias外推性.md)
methods:
  - [LRU参数化与初始化](wiki/methods/LRU参数化与初始化.md)
  - [LRU并行化递归算法](wiki/methods/LRU并行化递归算法.md)
  - [最小熵Pooling](wiki/methods/最小熵Pooling.md)
  - [无交跳转加权](wiki/methods/无交跳转加权.md)
  - [非线性RNN摄动并行化](wiki/methods/非线性RNN摄动并行化.md)
open_questions:
  - 如何通过复数化改造RWKV以融合LRU的对角化特征表达优势？
  - 如何在NBCE中更好地处理强耦合或需要严格序列顺序的长上下文生成？
status: draft
updated: 2026-06-12
---

# LLM架构与上下文扩展

## Scope
涵盖大语言模型（LLM）的注意力机制优化、Decoder-only与双向架构满秩表达能力的理论对比、线性RNN（如LRU、RWKV）的参数化及对角化并行计算、基于朴素贝叶斯的推理期上下文窗口扩展（NBCE）、注意力机制的稀疏性数学量化，以及利用偏置项（Bias）增强RoPE长度外推性能的研究。

## Open Questions
- 如何通过复数化改造RWKV以融合LRU的对角化特征表达优势？
- 如何在NBCE中更好地处理强耦合或需要严格序列顺序的长上下文生成？