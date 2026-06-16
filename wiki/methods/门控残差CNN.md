---
type: method
title: "门控残差CNN"
aliases:
  - "Gated ResNet"
operation_types:
  primary: "Construct auxiliary sequence"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-01-14-基于CNN和序列标注的对联机器人.md
source_ids:
  - "6270"
method_summary: "结合门控线性单元和残差连接的卷积模块，用于序列标注。"
typical_structure: |
  1. Conv1D输出2x_dim
  2. 前x_dim经sigmoid作为门
  3. 后x_dim经反门
  4. 残差连接输入
applicability: "序列标注，文本生成"
tools:
  - 门控机制
  - 残差连接
related_methods: []
examples:
  - [[article::6270]]
status: draft
updated: 2026-06-13
---

## 适用问题

序列标注和文本生成任务，特别是需要并行计算加速的场景。门控残差CNN在训练速度上远优于RNN/LSTM，适合处理长序列。

## 核心变换

**输入**：序列特征 $X$
**输出**：门控+残差处理后的特征 $Y$

Conv1D输出$2d$维向量，拆分为门控信号和非线性变换两部分：
$$
Y = \text{sigmoid}(XW_1) \odot (XW_2) + X
$$
即前$d$维经sigmoid作为门控$G$，后$d$维作为激活$H$，$G \odot H$后与输入残差连接。

## 典型步骤

1. **Conv1D**：一维卷积输出$2 \times \text{dim}$维向量
2. **拆分**：前dim维经sigmoid作为门控信号，后dim维作为内容信号
3. **门控相乘**：门控信号与内容信号逐元素相乘 $\sigma(\cdot) \odot (\cdot)$
4. **残差连接**：输出加上原始输入，缓解梯度消失
5. **堆叠多层**：可堆叠6+层构建深层门控残差CNN

## 直觉

门控机制控制信息流动比例：sigmoid输出在0-1之间，决定"让多少信息通过"。残差连接允许梯度直接流向浅层，使堆叠深层CNN成为可能。

与LSTM的门控相比，CNN门控的优势在于计算的完全并行化（不依赖前一时间步的隐藏状态），训练速度大幅提升。

## 边界

- 参数量比普通Conv1D翻倍（输出2x_dim）
- 对对联生成等任务效果优于双向LSTM，但泛化到其他任务需验证
- 门控信号的sigmoid可能导致梯度饱和（当门控接近0或1时）
- 残差连接要求输入和输出维度一致

## 例子

- 对联生成：6层门控残差CNN，效果优于双向LSTM且速度更快
- 序列标注：门控CNN替代LSTM作为序列编码器

## 证据

- ev::6270::门控残差CNN结构：Conv1D输出2x_dim → sigmoid门控 + 反门控 → 逐元素乘 → 残差连接
