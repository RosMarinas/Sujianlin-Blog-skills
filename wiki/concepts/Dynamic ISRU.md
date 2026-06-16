---
type: concept
title: Dynamic ISRU
aliases:
- DyISRU
definition: 一种使用逐元素逆平方根单元光滑近似 Normalization 特征层梯度的动态激活函数。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
source_ids:
- 10831
status: draft
updated: '2026-06-12'
---

## 定义与推导

Dynamic ISRU (DyISRU) 是一种通过梯度近似寻找 Normalization 替代品的逐元素 (Element-wise) 运算。为了寻找 RMS Norm 的逐元素近似，使得每个分量独立运算（即其雅可比矩阵一定是对角阵），可以通过保留 RMS Norm 梯度的对角线部分得到以下方程：

$$
\frac{dy_i}{dx_i} = \frac{1}{\Vert\boldsymbol{x}\Vert_{RMS}}\left(1 - \frac{y_i^2}{d}\right)
$$

由于对于 RMS Norm 恒有 $y_i = x_i / \Vert\boldsymbol{x}\Vert_{RMS}$，因此可以将方程中的 $\Vert\boldsymbol{x}\Vert_{RMS}$ 替换为 $x_i/y_i$，从而得到一个免除 $\Vert\boldsymbol{x}\Vert_{RMS}$ 近似处理的微分方程：

$$
\frac{dy_i}{dx_i} = \frac{y_i}{x_i}\left(1 - \frac{y_i^2}{d}\right)
$$

求解该方程可得：

$$
y_i = \frac{\sqrt{d}x_i}{\sqrt{x_i^2 + C}}
$$

其中 $C$ 是任意常数。这种形式被称为 ISRU (Inverse Square Root Unit)。如果将 $C$ 视为可训练参数，那么就可以类比 DyT 称为 DyISRU (Dynamic ISRU)。

## 属性与特征

从形式上看，DyISRU 比 DyT 更直观。因为 $\Vert\boldsymbol{x}\Vert_{RMS}^2$ 即 $\mathbb{E}[x_i^2]$，既然要寻求 Element-wise 的运算，只好将 $\mathbb{E}[x_i^2]$ 换成 $x_i^2$ 了，最后加 $C$ 乘 $\sqrt{d}$ 算是平滑操作：

$$
\frac{x_i}{\sqrt{\frac{1}{d}\sum\limits_{i=1}^d x_i^2}}\quad\to\quad \frac{x_i}{\sqrt{x_i^2}}\quad\to\quad \frac{\sqrt{d} x_i}{\sqrt{x_i^2 + C}}
$$

DyISRU 是用 Element-wise 函数能做到的最好结果，因为除对角线假设外，它没有再加额外近似。

## 关联概念

*   **RMS Norm**: DyISRU 旨在作为无 Normalization 模型中 RMS Norm 的平替，通过解含自变量的对角雅可比微分方程推导得出，逼近 RMS Norm 的梯度行为，但免除了均值和方差的统计量计算。
*   **DyT (Dynamic Tanh)**: 另一种尝试替代 Normalization 的函数。DyT 在推导对角线微分方程时，假设了 $\rho = \Vert\boldsymbol{x}\Vert_{RMS}$ 为常数，从而得到了 $\tanh$ 的解形式；而 DyISRU 则通过代换消去了该项，避免了常数假设。
*   **ISRU (Inverse Square Root Unit) / SoftSign**: DyISRU 的基础函数形式，可视为符号函数的光滑近似。
