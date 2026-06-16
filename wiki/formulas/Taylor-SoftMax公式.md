---
type: formula
title: Taylor-SoftMax公式
aliases:
  - Taylor-softmax
latex: \text{taylor-softmax}(\boldsymbol{x}, n)_i = \frac{f_n(x_i)}{\sum_{k=1}^m f_n(x_k)}
symbol_meanings:
  - "$f_n(x) = \sum_{k=0}^n x^k/k!$": e^x 在 x=0 处的 n 阶泰勒展开多项式（n 为偶数）
  - "$x_i$": 输入向量的第 i 个分量
  - "$m$": 类别数
standard_notation: "$\text{taylor-softmax}(\boldsymbol{x}, n)_i$"
conditions: "n 为正偶数，$f_n(x) > 0$ 保证归一化有效"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-24-exp-x-在x-0处的偶次泰勒展开式总是正的.md
source_ids:
  - "7919"
derived_from:
  - "proposition::偶次泰勒展开正定性"
implies: []
appears_in:
  - "article::exp(x)在x=0处的偶次泰勒展开式总是正的"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

$$
\text{taylor-softmax}(\boldsymbol{x}, n)_i = \frac{f_n(x_i)}{\sum_{k=1}^m f_n(x_k)}, \quad f_n(x) = \sum_{k=0}^n \frac{x^k}{k!}
$$

### 单调截断版本

$$
\tilde{f}_n(x) = \begin{cases} f_n(x), & x > x_n^* \\ f_n(x_n^*), & x \leq x_n^* \end{cases}
$$

其中 $x_n^*$ 是 $f_n(x)$ 的唯一极小值点。
