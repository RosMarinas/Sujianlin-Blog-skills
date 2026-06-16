---
type: article_summary
title: SquarePlus：可能是运算最简单的ReLU光滑近似
article_id: "8833"
source_url: https://spaces.ac.cn/archives/8833
date: 2021-12-29
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
source_ids:
  - "8833"
status: stable
updated: 2026-06-12
---

## 概述

本文介绍了一种极其简单的ReLU光滑近似——SquarePlus，其形式为 $\text{SquarePlus}(x) = (x + \sqrt{x^2 + b}) / 2$。该函数源自 $\max(x,0) = (x + |x|)/2 = (x + \sqrt{x^2})/2$，通过在根号内引入正常数 $b > 0$ 消除原点不可导性。SquarePlus 仅涉及加、乘、除和开方运算，相比 SoftPlus（需指数和对数）、GeLU（需erf）等计算量更小。

文章分析了SquarePlus的数学性质：
1. **单调性**：一阶导数恒正，全局单调递增。
2. **凸性**：二阶导数恒正，为凸函数。
3. **逼近分析**：讨论了两个练习题——当 $b \geq 4\log^2 2$ 时 SquarePlus 恒大于 SoftPlus；通过数值minimax优化求得最佳参数 $b \approx 1.5238$，使得 SquarePlus 与 SoftPlus 的最大绝对误差约为 $0.0759$。

## 关键数学公式

- **SquarePlus定义**：$\text{SquarePlus}(x) = \dfrac{x + \sqrt{x^2 + b}}{2}, \quad b > 0$
- **导数**：$\frac{d}{dx}\text{SquarePlus}(x) = \frac{1}{2}\left(1 + \frac{x}{\sqrt{x^2+b}}\right) > 0$
- **二阶导数**：$\frac{d^2}{dx^2}\text{SquarePlus}(x) = \frac{b}{2(x^2+b)^{3/2}} > 0$
- **恒大于SoftPlus条件**：$b \geq 4\log^2 2$
- **最优逼近参数**：$b \approx 1.5238$（minimax准则）
