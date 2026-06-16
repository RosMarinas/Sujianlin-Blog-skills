---

type: concept
title: Xavier初始化
aliases: []
definition: 一种深度学习参数初始化方法，权重从 $\mathcal{N}(0,2/(fan_{in}+fan_{out}))$ 采样，保持前向/反向传播的信号方差稳定。
standard_notation: true
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2020-01-16-从几何视角来理解模型参数的初始化策略.md
source_ids:
- '7180'
prerequisites: []
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods: []
series: []
evidence_spans: []
status: draft
updated: '2026-06-12'
---
# Xavier 初始化

## 定义
Xavier 初始化（也称 Glorot 初始化）是一种用于深度神经网络的参数初始化方法，旨在保持各层激活值和梯度的方差在传播过程中基本不变。

## 数学原理
对于输入维度为 $n_{\text{in}}$、输出维度为 $n_{\text{out}}$ 的线性层，其权重 $W$ 服从均匀分布：
$$W \sim \mathcal{U}\left(-\frac{\sqrt{6}}{\sqrt{n_{\text{in}} + n_{\text{out}}}}, \frac{\sqrt{6}}{\sqrt{n_{\text{in}} + n_{\text{out}}}}\right)$$
或服从均值为 0 的正态分布，其方差为：
$$\text{Var}(W) = \frac{2}{n_{\text{in}} + n_{\text{out}}}$$
这在 Sigmoid 或 Tanh 激活函数的网络中效果极佳。
