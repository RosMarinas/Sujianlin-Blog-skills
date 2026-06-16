---

type: formula
title: msign Newton-Schulz迭代公式
aliases:
- NS iteration for msign
standard_notation:
  M: input matrix
  X_t: Newton-Schulz iterate at step t
  a: linear coefficient
  b: cubic coefficient
  c: quintic coefficient
  x_t: scalar surrogate iterate
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-05-11-msign算子的Newton-Schulz迭代-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
source_ids:
- '10922'
- '10996'
related_concepts:
- '[[矩阵符号函数(msign)]]'
- '[[Newton-Schulz迭代]]'
related_propositions:
- '[[msign NS迭代收敛条件]]'
evidence_spans:
- ev::10922::NS迭代格式
- ev::10922::标量迭代分析
status: draft
updated: "2026-06-14"
latex: X_{t+1} = a X_t + b X_t(X_t^\top X_t) + c X_t(X_t^\top X_t)^2
symbol_meanings:
  M: input matrix
  X_t: Newton-Schulz iterate at step t
  a: linear coefficient
  b: cubic coefficient
  c: quintic coefficient
  x_t: scalar surrogate iterate
conditions: （待从源文章提取）
appears_in:
- '10922'
- '10996'
---

# msign Newton-Schulz迭代公式


## 概述

（待补充）

## 矩阵迭代（3项截断）

$$X_{t+1} = a X_t + b X_t(X_t^\top X_t) + c X_t(X_t^\top X_t)^2$$

其中 $X_0 = M / \|M\|_F$。

## 标量等价形式

$$x_{t+1} = a x_t + b x_t^3 + c x_t^5$$

## 不同步系数版本

$$X_{t+1} = a_{t+1} X_t + b_{t+1} X_t(X_t^\top X_t) + c_{t+1} X_t(X_t^\top X_t)^2$$

## 初值改良

用 $\sqrt[4]{\|(M^\top M)^2\|_F}$ 替代 $\|M\|_F$ 做归一化，可结合NS第一步的计算免费获得。

## 安全因子

实际应用时对输入做 $x \to x/1.01$ 的缩放，防止bfloat16精度下奇异值溢出。