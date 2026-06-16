---
type: article_summary
title: Google新作试图“复活”RNN：RNN能否再次辉煌？
article_id: 9554
source_url: https://spaces.ac.cn/archives/9554
date: 2023-03-28
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
status: draft
updated: 2026-06-12
---

# Google新作试图“复活”RNN：RNN能否再次辉煌？

本文介绍了Google提出的线性循环单元（Linear Recurrent Unit, LRU）模型，探讨了RNN在处理超长序列场景下的优势与改进空间。
作者指出，通过去掉RNN循环体中的非线性激活函数，可以得到极简的线性RNN。
线性RNN可以在复数域中进行对角化，使得所有的状态转移计算变为element-wise的标量运算。
为了防止梯度消失和爆炸，需要对特征值模长 $r$ 进行精细的参数化（$r = e^{-e^{
u^{\log}}}$）与初始化（圆环采样 $r \in [0.9, 0.999]$）。
同时，引入缩放因子 $\gamma = \sqrt{1 - r^2}$ 来稳定输出的模长。
线性RNN具有可以利用Prefix Sum并行前缀和算法实现 $O(\log L)$ 并行训练的特性，大大提升了训练速度。
作者提供了其Keras版本的代码实现，并分析了SLRU和RWKV模型。
在1亿参数量级的语言模型任务上，控制变量的对照实验表明，LRU优于实数域的SLRU，而RWKV是目前表现最好的RNN变体，但相较于注意力模型（GAU、SA）在语言模型效果上仍有一定差距，RNN系列可能需要更大的hidden_size或特殊技巧才能完全追平。