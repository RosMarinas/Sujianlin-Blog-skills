---
type: article_summary
title: exp(x)在x=0处的偶次泰勒展开式总是正的
article_id: "7919"
source_url: https://spaces.ac.cn/archives/7919
date: 2020-11-24
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-11-24-exp-x-在x-0处的偶次泰勒展开式总是正的.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-24-exp-x-在x-0处的偶次泰勒展开式总是正的.md
source_ids:
  - "7919"
status: stable
updated: 2026-06-12
---

## 概述

本文探讨了一个有趣且强的数学结论：对于任意实数 $x$ 以及正偶数 $n$，$e^x$ 在 $x=0$ 处的 $n$ 阶泰勒展开式总是大于零。作者给出了一个极其简洁明了的微分极值证明，并分析了该多项式正定性在机器学习（特别是作为 Softmax 的替代品）中的实际应用：
1. **泰勒展开恒正性证明**：
   记多项式 $f_n(x) = \sum_{k=0}^n \frac{x^k}{k!}$。由于偶数阶 $n$ 使得两端极限为 $+\infty$，其最小值必在极值点取得。利用导数关系 $f_n'(x) = f_{n-1}(x)$，在任意极值点处有 $f_n(x) = f_{n-1}(x) + \frac{x^n}{n!} = \frac{x^n}{n!} \geq 0$。由于 $x=0$ 处不为 0 且不是极值点，容易得出对于任意实数 $x$ 恒有 $f_n(x) > 0$。
2. **Taylor-Softmax 激活函数**：
   由于 $f_n(x) > 0$ 且具有多项式性质，可以用它作为归一化因子设计 Taylor-Softmax。多项式相比于指数函数增长较缓，在分类输出中可以缓解置信度过高（即概率值塌陷为 0 或 1）引起的过拟合问题。
3. **单调性截断修改**：
   $f_n(x)$ 为 U 型非单调函数。为维持单调递增性，可定义截断函数 $\tilde{f}_n(x)$，在唯一极小值点 $x_n^*$ 左侧进行截断，使其等于极小值 $f_n(x_n^*)$。

## 关键数学公式

- **泰勒展开多项式**： $f_n(x) = \sum_{k=0}^n \frac{x^k}{k!} > 0 \quad (\forall x \in \mathbb{R}, \, n \text{ 是偶数})$
- **Taylor-Softmax**： $\text{taylor-softmax}(\boldsymbol{x}, n)_i = \frac{f_n(x_i)}{\sum_{k=1}^m f_n(x_k)}$
- **单调截断版本**： $\tilde{f}_n(x) = \begin{cases} f_n(x), & x > x_n^* \\ f_n(x_n^*), & x \leq x_n^* \end{cases}$
