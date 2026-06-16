---
type: concept
title: 全局归一化vs局部归一化
aliases:
- Global vs Local Normalization
- 全局归一化与局部归一化
definition: 序列模型中对概率分布进行归一化的两种方式：全局归一化（如CRF）对整个输出空间做一次softmax；局部归一化（如MEMM）对每步输出分别做softmax。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-02-24-CRF用过了-不妨再了解下更快的MEMM.md
source_ids:
- '7213'
prerequisites:
- '[[CRF]]'
- '[[MEMM]]'
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
- ev::7213::两者关系
- ev::7213::MEMM的优劣
- ev::7213::思考与拓展
status: draft
updated: '2026-06-12'
---
# 全局归一化vs局部归一化

## Definition

CRF的分母∑_{y} e^{f(y;x)}包含所有可能路径（全局归一化），MEMM每步分母∑_{y_k} e^{g(y_{k-1},y_k)+f(y_k;x)}只包含当前步标签（局部归一化）。全局归一化效果更好但计算复杂（递归），局部归一化可完全并行但存在label bias。

MEMM全称Maximum Entropy Markov Model，中文名可译为“最大熵马尔可夫模型”。不得不说，这个名字可能会吓退80%的初学者：最大熵还没搞懂，马尔可夫也不认识，这两个合起来怕不是天书？而事实上，不管是MEMM还是CRF，它们的模型都远比它们的名字来得简单，它们的概念和设计都非常朴素自然，并不难理解。

作为对比，我们还是来回顾一下CRF。说是“回顾”，是因为笔者之前已经撰文介绍过CRF了，如果对CRF还不是很了解的读者，可以先去阅读旧作[《简明条件随机场CRF介绍（附带纯Keras实现）》](/archives/5542)。简单起见，本文介绍的CRF和MEMM都是最简单的“线性链”版本。

本文都是以序列标注为例，即输入序列$\boldsymbol{x}=(x_1,x_2,\dots,x_n)$，希望输出同样长度的标签序列$\boldsymbol{y}=(y_1,y_2,\dots,y_n)$，那么建模的就是概率分布

对比式$\eqref{eq:memm-p}$和式$\eqref{eq:crf-p}$，我们可以发现，MEMM跟CRF的区别仅在于分母（也就是归一化因子）的计算方式不同，CRF的式$\eqref{eq:crf-p}$我们称之为是全局归一化的，而MEMM的式$\eqref{eq:memm-p}$我们称之为是局部归一化的。

根据上面的结论，在深度学习时代，MEMM的“没落”似乎就可以理解了——MEMM除了训练速度快点之外，相比CRF似乎也就没什么好处了，两者的预测速度是一样的，而很多时候我们主要关心预测速度和效果，训练速度稍微慢点也无妨。这两个模型的比较结果是有代表性的，可以说这正是所有全局归一化和局部归一化模型的差异：全局归一化模型效果通常好些，但实现通常相对困难一些；局部归一化模型效果通常不超过全局归一化模型，但胜在易于实现，并与易于...
