---
type: concept
title: Newton-Schulz迭代
aliases:
- Newton-Schulz iteration
- NS迭代
- polar decomposition iteration
definition: 计算矩阵函数（特别是msign/极分解）的迭代算法，通过截断多项式展开以低计算成本近似msign。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-05-11-msign算子的Newton-Schulz迭代-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
source_ids:
- '10922'
- '10996'
prerequisites:
- '[[矩阵符号函数(msign)]]'
- '[[奇异值分解]]'
equivalent_forms: []
direct_consequences: []
related_formulas:
- '[[msign Newton-Schulz迭代公式]]'
related_methods:
- '[[用迭代逼近替代矩阵分解]]'
series: []
evidence_spans:
- ev::10922::NS迭代格式
- ev::10922::标量迭代分析
- ev::10996::贪心即最优
- ev::10996::等值振荡定理
status: stable
updated: '2026-06-12'
---

# Newton-Schulz迭代

## 基本格式

计算msign算子的Newton-Schulz迭代可写为（一般取3项截断）：

$$X_{t+1} = aX_t + bX_t(X_t^\top X_t) + cX_t(X_t^\top X_t)^2$$

其中 $X_0 = M / \|M\|_F$，$(a,b,c)$ 为优化系数。

## 标量简化

利用SVD可证明迭代等价于标量迭代：

$$x_{t+1} = a x_t + b x_t^3 + c x_t^5$$

这使得分析大大简化。目标是使任意 $x_0 \in (0,1]$ 经过 $T$ 步后尽可能接近1。

## 关键技巧

1. **不同步系数**：每步使用不同的 $(a_t, b_t, c_t)$，在不增加计算量前提下大幅提升收敛性。
2. **初值改良**：用 $\sqrt[4]{\|(M^\top M)^2\|_F}$ 替代 $\|M\|_F$ 做归一化，使小奇异值起点更高。
3. **区间预留+Recenter**：有限精度下，通过预留边界和重新居中消除累积误差。

## 理论最优解

基于等值振荡定理和"贪心即全局最优"性质，可求出理论最优系数。对于5阶迭代，$t \ge 7$ 时系数收敛到 $(1.875, -1.25, 0.375)$。

## 参考系数

| 来源 | (a,b,c) | 步数 |
|------|---------|------|
| KellerJordan | (3.4445, -4.7750, 2.0315) | 5 |
| 苏剑林(10922) | (3.3748, -4.6969, 2.1433) | 5 |
| 理论最优(t>=7) | (1.875, -1.25, 0.375) | 7+ |