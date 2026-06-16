---

type: formula
title: PMI内积词向量公式
aliases: []
latex: \langle v_i,v_j\rangle=\log\frac{P(w_i,w_j)}{P(w_i)P(w_j)}
symbol_meanings:
  PMI: 点互信息
  P_ij: 共现概率
  v_i: 词向量
standard_notation:
  v_i: 词向量
  P_ij: 共现概率
  PMI: 点互信息
conditions:
- 用词对共现统计估计概率；内积模型拟合点互信息。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-二-对语言进行建模.md
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md
source_ids:
- '4669'
- '4671'
derived_from: []
implies: []
appears_in:
- '4669'
- '4671'
evidence_spans:
- ev::4669::从条件概率到互信息
- ev::4671::模型形式
status: draft
updated: "2026-06-14"
---

# PMI内积词向量公式


## 概述

（待补充）

## 公式

```tex
\langle v_i,v_j\rangle=\log\frac{P(w_i,w_j)}{P(w_i)P(w_j)}
```

## 符号

$w_i,w_j$ 是两个词，$P(w_i,w_j)$ 是它们在语料窗口中的共现概率，$P(w_i),P(w_j)$ 是各自边缘概率，$v_i,v_j$ 是对应词向量。右端是点互信息 PMI，衡量真实共现相对于随机相遇的对数偏离；左端用同一向量空间中的内积来拟合这个统计量。

## 条件

- 用词对共现统计估计概率；内积模型拟合点互信息。

## 用途

源文先将相关度矩阵视为需要压缩和平滑的大矩阵，再假设词对相关度是词向量内积的某个函数。为了让词向量的加减类比对应上下文组合关系，源文推导出指数相关度模型，等价地得到 PMI 等于内积。后续求解时，用经验概率 $\tilde{P}$ 直接构造平方损失来拟合该式，比带两套向量和偏置项的 GloVe 形式更简洁。

## 证据

- `ev::4669::从条件概率到互信息`
- `ev::4671::模型形式`
