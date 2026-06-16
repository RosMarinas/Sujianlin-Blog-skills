---
type: formula
title: FBDM概率密度函数
aliases:
  - FBDM PDF
  - Fourier basis density model PDF
latex: p_\theta(x) = \frac{1}{2c_0}\sum_{n=-N}^N c_n e^{i\pi n x}, \quad c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*
symbol_meanings:
  - "$a_k \in \mathbb{C}$": 自由参数，$k=0,1,\dots,N$
  - "$c_n$": 傅里叶系数，通过自相关形式保证Toeplitz矩阵正定
  - "$x$": 定义在 $[-1,1]$ 上的变量
standard_notation: "$p_\theta(x)$"
conditions: "$x \in [-1,1]$，$a_k$ 为复数自由参数"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
source_ids:
  - "10007"
derived_from: []
implies: []
appears_in:
  - "article::用傅里叶级数拟合一维概率密度函数"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

截断傅里叶级数形式：
$$
f_{\theta}(x) = \sum_{n=-N}^{N} c_n e^{i\pi n x}
$$

非负性通过自相关参数化保证：
$$
c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*
$$

归一化后的概率密度函数：
$$
p_{\theta}(x) = \frac{f_{\theta}(x)}{2c_0} = \text{Re}\left[\frac{1}{2} + \sum_{n=1}^N \frac{c_n}{c_0} e^{i\pi n x}\right]
$$

扩展到 $\mathbb{R}$（通过 $\tanh$ 变换）：
$$
q_{\theta}(y) = \frac{1}{\sigma}\text{sech}^2\left(\frac{y-\mu}{\sigma}\right) p_{\theta}\left(\tanh\left(\frac{y-\mu}{\sigma}\right)\right)
$$

正则项：
$$
\gamma\int_{-1}^1 |f_{\theta}'(x)|^2 dx = \gamma\sum_{n=-N}^N 2\pi^2 n^2 |c_n|^2
$$
