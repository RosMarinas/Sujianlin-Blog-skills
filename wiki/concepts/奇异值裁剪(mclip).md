---
type: concept
title: 奇异值裁剪(mclip)
aliases:
- mclip算子
- Singular Value Clipping
- spectral clipping
definition: 将矩阵的奇异值裁剪到指定区间内的运算。作为msign的推广，可视为更一般的奇异值操作。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-07-通过msign来计算奇异值裁剪mclip-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-通过msign来计算奇异值裁剪mclip-下.md
source_ids:
- '11006'
- '11059'
prerequisites:
- '[[奇异值分解]]'
- '[[矩阵符号函数(msign)]]'
equivalent_forms:
- $\text{mclip}_{[\alpha,\beta]}(M) = U \text{clip}_{[\alpha,\beta]}(\Sigma) V^\top$
direct_consequences: []
related_formulas:
- '[[mclip via msign公式]]'
related_methods:
- '[[用矩阵恒等式重写奇异值操作]]'
series: []
evidence_spans:
- ev::11006::mclip定义
- ev::11059::mclip通解
status: stable
updated: '2026-06-12'
---

# 奇异值裁剪(mclip)

## 定义

对标量clip运算的矩阵推广。将矩阵 $M$ 的奇异值裁剪到 $[\alpha, \beta]$ 区间内：

$$\text{mclip}_{[\alpha,\beta]}(M) = U \cdot \text{clip}_{[\alpha,\beta]}(\Sigma) \cdot V^\top$$

其中 $\text{clip}_{[\alpha,\beta]}(x) = \max(\min(x, \beta), \alpha)$。默认区间为 $[-1,1]$。

## 与msign的关系

- msign是mclip在 $\alpha=\beta=1$ 时的极限情况：把所有非零奇异值映射到1。
- 可以用msign的代数组合来计算mclip，避免为mclip单独设计迭代算法。

## 计算方式

1. **精确计算**：通过SVD。
2. **通过msign间接计算**：见[[用矩阵恒等式重写奇异值操作]]。将mclip表示为2-3次msign调用的组合。
3. **直接Newton-Schulz迭代**：对称版本的NS迭代也可用于mclip。

## 数值注意事项

- 当矩阵有远大于1的奇异值且msign精度不足时，嵌套方案可能产生大误差。
- 奇函数版本($\alpha=-1$)可利用误差抵消获得更高精度。
- bfloat16精度下不同公式的误差差异可达数十倍。