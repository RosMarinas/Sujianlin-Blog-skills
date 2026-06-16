---

type: formula
title: HiPPO-LegS矩阵公式
aliases: '[]'
latex: x'(t)=\frac{A}{t}x(t)+\frac{B}{t}u(t),\quad A_{n,k}=-\begin{cases}\sqrt{(2n+1)(2k+1)},&k<n\\
  n+1,&k=n\\0,&k>n\end{cases}
symbol_meanings:
  A: 矩阵
  B: 矩阵
  k: 第 k 个分量 / Top-k 数量
  n: 序列长度 / 样本数量
  t: 时间步 / 自变量
  x: 输入变量 / 自变量
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions: LegS 使用整个区间映射；缩放版本在源文中另给出去根号形式。
derived_from: '[]'
implies: '[]'
appears_in:
- '[[重温SSM（一）：线性系统和HiPPO矩阵]]'
- '[[重温SSM（二）：HiPPO的一些遗留问题]]'
evidence_spans:
- ev::10114::整个区间::legs_matrix
- ev::10137::长尾衰减::polynomial
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
source_ids:
- '10114'
- '10137'
status: draft
updated: "2026-06-14"
---
## 概述

（待补充）



## 公式

```tex
x'(t)=\frac{A}{t}x(t)+\frac{B}{t}u(t),\quad A_{n,k}=-\begin{cases}\sqrt{(2n+1)(2k+1)},&k<n\\ n+1,&k=n\\0,&k>n\end{cases}
```

## 条件

LegS 使用整个区间映射；缩放版本在源文中另给出去根号形式。

## 证据

- `ev::10114::整个区间::legs_matrix`
- `ev::10137::长尾衰减::polynomial`