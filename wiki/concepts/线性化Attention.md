---
type: concept
definition: 线性化Attention把标准Attention中的相似度矩阵改写为可分解、可结合的矩阵乘法或核函数形式，从而把复杂度从O(n^2)降到O(n)或近似线性。
title: 线性化Attention
aliases:
- Linearized Attention
- Linear Attention
source_ids:
- '7546'
- '8180'
evidence_spans:
- ev::7546::结合律线性化
- ev::8180::Nyström背景
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
---
# 线性化Attention

线性化Attention把标准Attention中的相似度矩阵改写为可分解、可结合的矩阵乘法或核函数形式，从而把复杂度从O(n^2)降到O(n)或近似线性。

当前最流行的Attention机制当属[Scaled-Dot Attention](https://papers.cool/arxiv/1706.03762)，形式为

$$

Attention(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = softmax\left(\boldsymbol{Q}\boldsymbol{K}^{\top}\right)\boldsymbol{V}\label{eq:std-att}

title: 线性Attention的探索：Attention必须有个Softmax吗？

url: https://spaces.ac.cn/archives/7546

众所周知，尽管基于Attention机制的Transformer类模型有着良好的并行性能，但它的空间和时间复杂度都是$\mathcal{O}(n^2)$级别的，$n$是序列长度，所以当$n$比较大时Transformer模型的计算量难以承受。近来，也有不少工作致力于降低Transformer模型的计算量，比如模型剪枝、量化、蒸馏等精简技术，又或者修改Attention结构，使得其复杂度能降低到$\mathcal{O}(n\log n)$甚至$\mathcal{O}(n)$。

如果读者对线性Attention还不是很了解，那么建议先通读一下[《线性Attention的探索：Attention必须有个Softmax吗？》](/archives/7546)和[《Performer：用随机投影将Attention的复杂度线性化》](/archives/7921)。总的来说，线性Attention是通过矩阵乘法的结合律来降低Attention的复杂度。

标准的Scaled-Dot Attention写成矩阵形式就是（有时候指数部分还会多个缩放因子，这里我们就不显式写出来了）：

$$

title: Nyströmformer：基于矩阵分解的线性化Attention方案

url: https://spaces.ac.cn/archives/8180

标准Attention的$\mathcal{O}(n^2)$复杂度可真是让研究人员头大。前段时间我们在博文[《Performer：用随机投影将Attention的复杂度线性化》](/archives/7921)中介绍了Google的Performer模型，它通过随机投影的方式将标准Attention转化为线性Attention。无独有偶，前些天Arxiv上放出了AAAI 2021的一篇论文[《Nyströmformer: A Nyström-Based Algorithm for Approximating Self-Attention》](https://papers.cool/arxiv/2102.03902)，里边又提出了一种从另一个角度把标准Attention线性化的方案。
