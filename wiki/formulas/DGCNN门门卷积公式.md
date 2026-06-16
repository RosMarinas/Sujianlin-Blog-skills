---
type: formula
title: DGCNN门卷积公式
latex: \boldsymbol{Y}=\boldsymbol{X}\otimes \Big(1-\boldsymbol{\sigma}\Big) + \text{Conv1D}_1(\boldsymbol{X}) \otimes \boldsymbol{\sigma}
symbol_meanings:
  X: 输入向量序列
  Y: 输出编码特征序列
  \sigma: 门卷积产生的选择系数序列
  \otimes: 元素逐点相乘 (Element-wise multiplication)
  Conv1D_1, Conv1D_2: 一维卷积运算
standard_notation: \boldsymbol{Y}=\boldsymbol{X}\otimes \Big(1-\boldsymbol{\sigma}\Big) + \text{Conv1D}_1(\boldsymbol{X}) \otimes \boldsymbol{\sigma}
conditions: 用于门卷积神经网络或膨胀门卷积层中选择性特征多通道传输
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-03-基于DGCNN和概率图的轻量级信息抽取模型.md
source_ids:
  - "6671"
appears_in:
  - [[spaces-6671-基于DGCNN和概率图的轻量级信息抽取模型]]
  - [[spaces-6906-开源一版DGCNN阅读理解问答模型-Keras版]]
status: stable
updated: 2026-06-12
---

# DGCNN门卷积公式

## 概述

该公式定义了DGCNN（膨胀门卷积神经网络）中基于残差与门卷积（GLU，Gated Linear Units）结合的特征提取结构。

在网络中，门控选择机制 $\boldsymbol{\sigma} = \sigma\Big(\text{Conv1D}_2(\boldsymbol{X})\Big)$ 用于自动评估和筛选输入信息的重要性。公式中第一项 $\boldsymbol{X}\otimes \Big(1-\boldsymbol{\sigma}\Big)$ 代表被保留的原始特征部分，第二项 $\text{Conv1D}_1(\boldsymbol{X}) \otimes \boldsymbol{\sigma}$ 代表经过卷积变换后被选中的新增特征部分。该公式在数学上完全等价于带有选择性多通道传输能力的Highway结构，能有效缓解梯度消失，使得全卷积结构在序列标注中能够替代复杂的循环神经网络（RNN）。
