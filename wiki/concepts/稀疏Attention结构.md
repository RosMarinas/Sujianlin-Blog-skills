---
type: concept
definition: 稀疏Attention结构用局部、空洞或组合稀疏模式限制token之间的可见关系，减少全量n×n注意力矩阵的计算。
title: 稀疏Attention结构
aliases:
- Sparse Attention Pattern
- Local/Atrous Attention
source_ids:
- '6853'
evidence_spans:
- ev::6853::稀疏原理
- ev::6853::局部空洞结构
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
---
# 稀疏Attention结构

稀疏Attention结构用局部、空洞或组合稀疏模式限制token之间的可见关系，减少全量n×n注意力矩阵的计算。

[《Attention is All You Need》](https://papers.cool/arxiv/1706.03762)一文讨论的我们称之为“乘性Attention”，目前用得比较广泛的也就是这种Attention：

$$

Attention(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = softmax\left(\frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d_k}}\right)\boldsymbol{V}

title: 为节约而生：从标准Attention到稀疏Attention

[![attention, please!](../../assets/6853/1271870192.jpg)](/usr/uploads/2019/07/1271870192.jpg)attention, please!

如今NLP领域，Attention大行其道，当然也不止NLP，在CV领域Attention也占有一席之地（Non Local、SAGAN等）。在18年初[《〈Attention is All You Need〉浅读（简介+代码）》](/archives/4765)一文中，我们就已经讨论过Attention机制，Attention的核心在于$\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}$三个向量序列的交互和融合，其中$\boldsymbol{Q},\boldsymbol{K}$的交互给出了两两向量之间的某种相关度（权重），而最后的输出序列则是把$\boldsymbol{V}$按照权重求和得到的。
