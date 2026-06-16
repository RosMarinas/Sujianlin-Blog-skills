---
type: formula
title: ThreTopK公式
latex: \mathcal{ST}_k(\boldsymbol{x}) = f(\boldsymbol{x} - \lambda(\boldsymbol{x}))
symbol_meanings:
  f: 任意[0, 1]的光滑单调增函数
  \lambda: 输入决定的待定阈值常数
standard_notation: f, \lambda
conditions: \sum_i f(x_i - \lambda) = k
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
- 10373
appears_in:
- - - spaces-10373-Softmax后传-寻找Top-K的光滑近似
status: draft
updated: '2026-06-14'
---

# ThreTopK公式


## 概述

（待补充）

## 公式

```tex
\mathcal{ST}_k(\boldsymbol{x}) = f(\boldsymbol{x} - \lambda(\boldsymbol{x})),
\qquad \sum_i f(x_i-\lambda(\boldsymbol{x}))=k
```

## 符号与条件

$\boldsymbol{x}\in\mathbb{R}^n$ 是待近似 Top-$k$ 的输入向量，$f:\mathbb{R}\to[0,1]$ 是光滑、单调递增并在两端趋近 0 与 1 的函数，$\lambda(\boldsymbol{x})$ 是由输入反解出的阈值常数。源文要求输出落在 $\Delta_k^{n-1}$ 中，即每个分量在 $[0,1]$ 内且总和为 $k$。

## 用途

ThreTopK 是硬 Top-$k$ 指派 $\mathcal{T}_k$ 的光滑近似。它通过阈值吸收平移常数，因此满足不变性；由 $f$ 的单调性继承输入排序；当温度趋于 0 时，最大的 $k$ 个分量趋向 1，其余趋向 0，从而逼近 Multi-Hot 的 Top-$k$ 结果。源文把它作为 Softmax 从 Top-1 推广到 Top-$k$ 的一种自下而上的构造。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md`
