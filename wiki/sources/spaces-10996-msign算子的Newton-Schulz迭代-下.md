---
type: article_summary
title: msign算子的Newton-Schulz迭代（下）
article_id: "10996"
source_url: https://spaces.ac.cn/archives/10996
date: 2025-06-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[Newton-Schulz迭代]]"
  - "[[等值振荡定理]]"
  - "[[极分解]]"
  - "[[Remez算法]]"
methods:
  - "[[用迭代逼近替代矩阵分解]]"
  - "[[等值振荡最优多项式逼近]]"
problem_patterns: []
evidence_spans:
  - ev::10996::极分解关联
  - ev::10996::贪心即最优
  - ev::10996::等值振荡定理
  - ev::10996::解方程组
  - ev::10996::有限精度问题
  - ev::10996::贪心最优性证明
  - ev::10996::最优系数结果
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
source_ids:
  - "10996"
status: draft
updated: 2026-06-10
---

# msign算子的Newton-Schulz迭代（下）

## 文章核心问题

如何用严格的最优化理论（而非启发式优化）求解msign算子Newton-Schulz迭代理论最优系数。基于等值振荡定理和"贪心即全局最优"的结论，给出解析解和迭代算法。

## 主要结论

- 复合奇多项式逼近1的优化问题，其贪心解（逐步求解单步最优）就是全局最优解。
- 基于等值振荡定理，3阶奇多项式情况下可给出解析解，5阶可给出迭代求解算法（简化版Remez算法）。
- 有限精度（bfloat16）下需要考虑区间预留和Recenter技巧来消除累积误差。
- 给出了8步5阶NS迭代的理论最优系数，收敛值为 (1.875, -1.25, 0.375)。
- 论文《The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm》(2505.16932) 给出了更优雅的数学推导。

## 推导结构

1. 将问题形式化：在区间 $[l,u]$ 上求最佳奇多项式逼近常数1。
2. 引入等值振荡定理，给出最优逼近的充要条件。
3. 将T步复合函数优化转化为T个单步优化（贪心即全局最优）。
4. 通过等值振荡条件建立方程组求解单步最优多项式。
5. 用积分形式参数化规避求根问题，适用于更高阶。
6. 处理有限精度问题：区间预留 + Recenter技巧。
7. 给出完整Mathematica/Python求解代码和结果。
8. 证明贪心解即全局最优（数学归纳法）。

## 关键公式

- 优化目标: $\argmin_f \max_{x\in[l,u]} |f(x) - 1|$
- 等值振荡条件: $f^*(x_k) - 1 = (-1)^{k+\sigma} \mathcal{E}$
- 3阶奇多项式解析解: $x_1 = \sqrt{(l^2+lu+u^2)/3}, k = -6/(l^2u+lu^2+2x_1^3)$
- 5阶参数化: $f_t'(x) = k(x^2-x_1^2)(x^2-x_2^2)$
- 最终收敛系数(step>=7): $(a,b,c) = (1.875, -1.25, 0.375)$

## 体现的方法

- **等值振荡最优多项式逼近**：用等值振荡定理求解最佳奇多项式逼近常数函数，获得Newton-Schulz迭代的理论最优系数。
- **贪心递推优化**：将T步复合函数全局优化转化为T个单步优化，每步保持最优性。
- **参数化消元**：用极值点参数化多项式导数，避免求解驻点方程。
- **有限精度防护**：通过区间预留和Recenter技巧应对bfloat16精度限制。

## 所属系列位置

独立文章，msign算子Newton-Schulz迭代的下篇，与上篇(10922)构成完整讨论。

## 与其他文章的关系

- 上篇(10922) 提出启发式系数优化，本文给出理论最优解。
- 直接基于等值振荡定理(10972) 的数学结论。
- 参考论文《The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm》。
- msign计算的改进直接服务于Muon优化器及其变种。

## 原文证据锚点

- ev::10996::极分解关联: 第33-40行，msign与极分解(Polar Decomposition)的关系。
- ev::10996::贪心即最优: 第44-60行，贪心解即全局最优的结论。
- ev::10996::等值振荡定理: 第69-86行，等值振荡定理在奇多项式上的表述和应用。
- ev::10996::解方程组: 第90-113行，建立并求解等值振荡方程组。
- ev::10996::有限精度问题: 第117-135行，两种有限精度问题及对策。
- ev::10996::贪心最优性证明: 第231-259行，数学归纳法证明。
- ev::10996::最优系数结果: 第157-173行，8步5阶最优系数表。
