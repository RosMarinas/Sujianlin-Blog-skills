---

type: concept
title: Toeplitz矩阵正定性
aliases: []
definition: Toeplitz矩阵 $T_{mn}=c_{m-n}$（每条对角线元素相同），其正定性保证对应的傅里叶级数表示的概率密度非负（Herglotz定理）。
standard_notation: false
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
source_ids:
- '10007'
prerequisites: []
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods: []
series: []
evidence_spans: []
status: draft
updated: '2026-06-12'
---
# Toeplitz 矩阵正定性

## 定义
Toeplitz 矩阵（对角线上元素相等的矩阵）在信号处理与时间序列分析中广泛存在。其正定性是保证系统稳定与可逆的关键性质。

## 判定方法
对于实对称 Toeplitz 矩阵，其正定性可以通过以下方式判定：
1. **赫尔维茨判据**：检查所有顺序主子式均大于零。
2. **Levinson-Durbin 递推**：在求解 Yule-Walker 方程时，如果所有的反射系数（偏自相关系数）的绝对值都严格小于 1，则该 Toeplitz 矩阵是正定的。
3. **频谱条件**：其生成的三角 Laurent 级数在单位圆上的傅里叶变换值恒大于零。
