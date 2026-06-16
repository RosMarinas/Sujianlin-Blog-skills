---
type: article_summary
title: 细水长flow之RealNVP与Glow：流模型的传承与升华
article_id: "5807"
source_url: https://spaces.ac.cn/archives/5807
date: 2018-08-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-08-26-细水长flow之RealNVP与Glow-流模型的传承与升华.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-08-26-细水长flow之RealNVP与Glow-流模型的传承与升华.md
source_ids:
  - "5807"
status: draft
updated: 2026-06-12
---

# 细水长flow之RealNVP与Glow：流模型的传承与升华

## 文章核心问题

如何在流模型（Flow-based Models）中引入强非线性的卷积神经网络以处理高维图像数据，同时降低模型的计算复杂度、解决可逆变换的维度浪费问题，并提供高效特征通道打乱的数学方法。

## 主要结论

1. **仿射耦合层**（Affine Coupling Layer）：RealNVP 将 NICE 的加性耦合层推广为仿射耦合层，结合了乘性和加性变换，其雅可比行列式非常数（非体积保持），增强了单层的表示能力。
2. **局部相关性与通道划分**：为了在可逆网络中使用卷积，RealNVP 规定特征的分割与随机打乱只对“通道轴”（Channel axis）进行，并通过 **Squeeze 算子** 将空间分辨率转化为通道维度，有效保留了局部空间相关性。
3. **多尺度结构**（Multi-scale Architecture）：通过在流模型的中间步骤不断将一部分隐变量直接作为先验输出，另一部分继续进行下一步流变换，成功降低了计算量，并利用组合条件概率分布起到了类似正则化的机制，一定程度抑制了维度浪费。
4. **可逆 1x1 卷积**（Invertible 1x1 Convolution）：Glow 提出用 1x1 可逆卷积代替 RealNVP 的通道随机打乱。该操作通过 LU 分解（LU Decomposition）将权重矩阵 $W = P L U$ 参数化，大幅降低了求雅可比行列式的运算量（仅为对角线元素绝对值的对数和）。
5. **Actnorm**（Activation Normalization）：用均值/方差平移缩放层替代 Batch Normalization，以解决小 Batch 训练的稳定性问题，其均值和方差在初次前向传播时使用 batch 统计量进行初始化。

## 推导结构

1. **仿射耦合雅可比计算**：对输入 $x$ 分割为 $x_1, x_2$：
   $$h_1 = x_1$$
   $$h_2 = s(x_1) \otimes x_2 + t(x_1)$$
   其雅可比矩阵为分块三角矩阵：
   $$\left[\frac{\partial h}{\partial x}\right] = \begin{pmatrix}\mathbb{I}_d & \mathbb{O} \\ \left[\frac{\partial s}{\partial x_1}\otimes x_2 + \frac{\partial t}{\partial x_1}\right] & \text{diag}(s)\end{pmatrix}$$
   对数行列式即为各元素的对数和：$\sum \log |s_i|$。
2. **多尺度概率条件化**：多尺度结构下的先验分布：
   $$p(z_1, z_3, z_5) = p(z_1 | z_2) p(z_3 | z_4) p(z_5)$$
   这等价于变量代换：$\hat{z}_1 = (z_1 - \mu(z_2)) / \sigma(z_2)$，且设定 $\hat{z}$ 服从标准正态分布。
3. **可逆 1x1 卷积与 LU 分解**：对于通道维度的线性映射 $h = x W$，其雅可比行列式为对数决定式：
   $$\log | \det W | = \sum \log | \text{diag}(U) |$$
   利用 $W = P L U$ 极大地简化了雅可比行列式的求取和求逆过程。

## 关键公式

- 仿射耦合前向与逆向：
  $$h_2 = s(x_1) \otimes x_2 + t(x_1) \Longleftrightarrow x_2 = (h_2 - t(h_1)) / s(h_1)$$
- 1x1 可逆卷积行列式计算：
  $$\log | \det W | = \sum_{i=1}^c \log | U_{ii} |$$
- 多尺度代换变换式：
  $$\hat{z}_1 = \frac{z_1 - \mu(z_2)}{\sigma(z_2)}$$

## 体现的方法

- **仿射耦合层变换**：结合乘性因子和偏置平移实现特征可逆变换。
- **Squeeze 与 UnSqueeze 重排**：实现空间与通道的高效转化。
- **可逆 1x1 卷积通道混合**：替代硬置换（Shuffle），引入可学习的通道混合权重。
- **多尺度特征提取与约束**：降低局部尺度分辨率以节省空间计算量，并限制信息冗余。

## 所属系列位置

本篇为“细水长flow”系列的第 2 篇，系统地把 NICE 的加性单层重写为仿射形式，完成了可逆网络由全连接至卷积的过度，并形成了 Glow 的主体 RevNet 基本结构。

## 与其他文章的关系

- **NICE**：NICE 确立了流模型与加性耦合的最简架构；RealNVP 和 Glow 对其进行了多尺度卷积的彻底升级。
- **f-VAEs**：f-VAEs 使用了 Glow 与 RealNVP 中的 RevNet 模型作为其变分后验推断中“条件流”的基本映射模块，并使用了其特例来推导 Glow 的加入均匀噪声训练性质。

## 原文证据锚点

- **体积非保持（Non-Volume Preserving）定义**：参见原文 `### 仿射耦合层` 中关于雅可比行列式非 1 代表行列式体积变化的解释。
- **Squeeze 操作图示与细节**：参见原文 `### 引入卷积层` 中的通道对半分 mask 与棋盘 mask，以及 squeeze 像素重排。
- **LU 分解在 1x1 卷积中的运用**：参见 `### 可逆1x1卷积` 部分中置换矩阵一般化和 LU 分解逆运用的全过程。
- **Glow 编码器结构**：参见 `### 源码分析` 的 encoder、revnet、split2d 拆解图示。
