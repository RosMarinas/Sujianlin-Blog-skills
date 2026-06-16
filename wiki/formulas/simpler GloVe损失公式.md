---

type: formula
title: simpler GloVe损失公式
aliases: []
latex: \sum_{w_i,w_j}\left(\langle v_i,v_j\rangle-\log\frac{\tilde P(w_i,w_j)}{\tilde
  P(w_i)\tilde P(w_j)}\right)^2
symbol_meanings:
  P_hat: 频率估计
  loss: 平方损失
  v: 词向量
standard_notation:
  P_hat: 频率估计
  v: 词向量
  loss: 平方损失
conditions:
- 使用语料窗口共现估计词对概率。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
source_ids:
- '4675'
derived_from: []
implies: []
appears_in:
- '4675'
evidence_spans:
- ev::4675::损失函数
status: draft
updated: "2026-06-14"
---

# simpler GloVe损失公式


## 概述

（待补充）

## 公式

```tex
\sum_{w_i,w_j}\left(\langle v_i,v_j\rangle-\log\frac{\tilde P(w_i,w_j)}{\tilde P(w_i)\tilde P(w_j)}\right)^2
```

## 条件

- 使用语料窗口共现估计词对概率。

## 证据

- `ev::4675::损失函数`