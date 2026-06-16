---

type: formula
title: 词向量模长ICF公式
aliases: []
latex: \Vert v_w\Vert^2\sim -\log P(w)
symbol_meanings:
  v_w: 词 w 的词向量
  P(w): 词 w 的出现概率
  \Vert v_w\Vert^2: 词向量模长平方
standard_notation:
  v_w: 词向量
  P_w: 词频概率
conditions:
- 粗略认为窗口中同词共现概率 P(w,w) 与 P(w) 同阶。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-五-有趣的结果.md
source_ids:
- '4677'
derived_from: []
implies: []
appears_in:
- '4677'
evidence_spans:
- ev::4677::模长的含义
status: draft
updated: '2026-06-14'
---


# 词向量模长ICF公式


## 概述

（待补充）

## 公式

```tex
\Vert v_w\Vert^2\sim -\log P(w)
```

## 条件

- 粗略认为窗口中同词共现概率 P(w,w) 与 P(w) 同阶。

## 符号与用途

$v_w$ 是词 $w$ 的向量表示，$P(w)$ 是词频概率。源文从互信息词向量模型出发，先假设同一窗口中中心词重复出现是随机事件，因此 $P(w,w)\sim P(w)$；再由模型关系
$$
e^{\langle\boldsymbol{v}_w,\boldsymbol{v}_w\rangle}
=\frac{P(w,w)}{P(w)P(w)}
\sim\frac{1}{P(w)}
$$
推出 $\Vert v_w\Vert^2\sim-\log P(w)$。由于 $-\log P(w)$ 类似 IDF，源文称其为 ICF，并据此解释模长可以在一定程度上代表词的重要性。

## 成立范围

该公式是近似关系，不是精确等式；它依赖互信息内积词向量模型和 $P(w,w)\sim P(w)$ 的粗略假设。源文还用停用词、虚词模长较小的排序结果作为经验验证，但指出截断权重会影响排序。

## 证据

- `ev::4677::模长的含义`
