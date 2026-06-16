---
type: formula
title: GradTopK公式
latex: '[\mathcal{ST}_k(\boldsymbol{x})]_i = \frac{\sum_{i_2 < \cdots < i_k} e^{x_i+x_{i_2}
  + \cdots + x_{i_k}}}{\sum_{i_1 < \cdots < i_k} e^{x_{i_1} +x_{i_2}+ \cdots + x_{i_k}}}'
symbol_meanings:
  x_i: 输入分量
  k: 选择数
  \mathcal{ST}_k: Top-k光滑近似结果
standard_notation: x_i, k, \mathcal{ST}_k
conditions: 分量和为k，值在(0, 1)内
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
- 10373
appears_in:
- - - spaces-10373-Softmax后传-寻找Top-K的光滑近似
status: draft
updated: '2026-06-14'
---

# GradTopK公式


## 概述

（待补充）

## 公式

```tex
[\mathcal{ST}_k(\boldsymbol{x})]_i =
\frac{\sum_{i_2 < \cdots < i_k} e^{x_i+x_{i_2}+\cdots+x_{i_k}}}
{\sum_{i_1 < \cdots < i_k} e^{x_{i_1}+x_{i_2}+\cdots+x_{i_k}}}
```

## 符号与条件

$\boldsymbol{x}$ 是输入向量，$k$ 是要选择的元素个数，$\mathcal{ST}_k$ 是硬 Top-$k$ 算子 $\mathcal{T}_k$ 的光滑近似。分母遍历所有 $k$ 个分量组合的指数和，分子只遍历包含 $x_i$ 的组合。源文证明该定义满足 $0<[\mathcal{ST}_k(\boldsymbol{x})]_i<1$ 且 $\sum_i[\mathcal{ST}_k(\boldsymbol{x})]_i=k$。

## 用途

源文先观察到硬 Top-$k$ Multi-Hot 向量等于“最大 $k$ 个分量之和”的梯度，再用 logsumexp 光滑近似最大值。对该标量近似求梯度就得到 GradTopK。该公式理论性质好，满足单调性、不变性和趋近性，并在 $k=1$ 时退化为 Softmax；但直接计算有组合爆炸，源文还讨论了递归计算的数值稳定性问题。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md`
