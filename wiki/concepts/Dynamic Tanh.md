---
type: concept
title: Dynamic Tanh
aliases:
- DyT
definition: 一种基于对角雅可比梯度近似推导出的、包含自适应缩放因子的逐元素双曲正切激活机制，用于替代 Normalization 层。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
source_ids:
- 10831
status: draft
updated: '2026-06-12'
---

## 核心定义与公式

Dynamic Tanh (DyT) 是一种试图在 Transformer 模型中替代 Normalization 层的 Element-wise（逐元素）运算机制。其核心运算定义如下：

$$
\mathop{\text{DyT}}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \tanh(\alpha \boldsymbol{x}) + \boldsymbol{\beta}
$$

其中 $\alpha,\boldsymbol{\beta},\boldsymbol{\gamma}$ 都是可学参数。在该形式中，$\boldsymbol{\beta},\boldsymbol{\gamma}$ 是 Normalization 层本来就有的平移和缩放参数，而核心改动在于用 $\tanh(\alpha \boldsymbol{x})$ 替代了原有的 Normalize 运算。由于 $\tanh$ 是逐元素的运算，这种机制彻底免除了均值、方差这两个全局统计量的计算。

## 数学推导与梯度近似

DyT 的本质可以通过对 RMS Norm 的梯度（雅可比矩阵）进行对角近似来严格推导。对于 RMS Norm，其雅可比矩阵为：

$$
\nabla_{\boldsymbol{x}} \boldsymbol{y} = \frac{1}{\Vert\boldsymbol{x}\Vert_{RMS}}\left(\boldsymbol{I} - \frac{\boldsymbol{y}\boldsymbol{y}^{\top}}{d}\right)
$$

如果我们要给 RMS Norm 寻找一个 Element-wise 近似，意味着每个分量是独立运算的：$f(\boldsymbol{x}) = [f(x_1),f(x_2),\cdots,f(x_d)]$。这种独立性意味着它的雅可比矩阵一定是对角阵。为了尽可能保留 RMS Norm 的梯度，考虑仅保留上述梯度的对角线部分：

$$
\frac{dy_i}{dx_i} = \frac{1}{\Vert\boldsymbol{x}\Vert_{RMS}}\left(1 - \frac{y_i^2}{d}\right)
$$

此时引入一个关键的边界条件假设：假设 $\rho = \Vert\boldsymbol{x}\Vert_{RMS}$ 是常数。在初值条件为 $y_i(0)=0$ 的前提下，直接求解上述微分方程即可得到：

$$
y_i = \sqrt{d}\tanh\left(\frac{x_i}{\rho\sqrt{d}}\right)
$$

在实际的 DyT 实现中，相当于将式中的 $\sqrt{d}$ 吸收到 $\boldsymbol{\gamma}$ 参数里，并将括号内的 $\frac{1}{\rho\sqrt{d}}$ 视为训练参数 $\alpha$，以此来缓解“$\rho = \Vert\boldsymbol{x}\Vert_{RMS}$是常数”这一假设所带来的限制。

## 核心性质与边界案例

DyT 及其使用的 $\tanh$ 函数可以视为一种引入了光滑的 $\mathop{\text{clip}}$ 操作的机制，即 $\mathop{\text{softcap}}$。其核心目的是通过对特征进行硬上限控制，防止网络前向传播发生爆炸：

$$
\mathop{\text{clip}}(x, -t, t) \approx t\tanh\left(\frac{x}{t}\right)\triangleq \mathop{\text{softcap}}(x, t)
$$

**缺陷与局限性（治标不治本）：**
虽然 DyT/$\mathop{\text{softcap}}$ 之后的数值不会爆炸，但由于它并未像 Normalization 那样在底层消除尺度的增长，导致 $\mathop{\text{softcap}}$ 之前的数值（如 Attention Logits）依然存在爆炸风险。Normalization 能够无脑地稳定模型的前向传播，从而留下更多自由度给模型的效果优化，简单的 DyT 很难实现比有 Normalization 更优秀的通用效果（No Free Lunch）。

## 与其他概念的关联

*   **与 RMS Norm 的关系**：DyT 是 RMS Norm 梯度雅可比矩阵在“对角阵化”和“常数范数（$\Vert\boldsymbol{x}\Vert_{RMS}$为常数）”双重假设下求解出的解析近似。
*   **与 DyISRU 的关系**：如果不引入“$\rho = \Vert\boldsymbol{x}\Vert_{RMS}$是常数”的妥协假设，由于恒有 $y_i = x_i / \Vert\boldsymbol{x}\Vert_{RMS}$，可以将原微分方程中的 $\Vert\boldsymbol{x}\Vert_{RMS}$ 换成 $x_i/y_i$，得到 $\frac{dy_i}{dx_i} = \frac{y_i}{x_i}\left(1 - \frac{y_i^2}{d}\right)$。求解该方程得到 $y_i = \frac{\sqrt{d}x_i}{\sqrt{x_i^2 + C}}$，这被称为 DyISRU (Dynamic ISRU)。从梯度近似的角度看，DyISRU 除对角线假设外没加额外近似，因而是使用 Element-wise 函数能做到的最好结果，在数学形式上也比 DyT 更直观。
*   **与 Gemma2 / Gemma3 的关系（具体反例）**：Google 在 Gemma2 中曾提出将 $\mathop{\text{softcap}}$ 加在 Softmax 前的 Attention Logits 矩阵上防止爆炸。然而在最新的 Gemma3 中，Google 选择去掉了 $\mathop{\text{softcap}}$ 而改用 QK-norm。这一工程实践的变化间接提供了反例，表明 DyT 等 $\mathop{\text{softcap}}$ 类操作在实践中极难完全取代传统的 Normalization 机制。
