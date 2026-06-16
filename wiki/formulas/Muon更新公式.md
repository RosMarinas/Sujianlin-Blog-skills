---

type: formula
title: Muon更新公式
aliases:
- Muon update
latex: \boldsymbol{M}_t = \beta\boldsymbol{M}_{t-1} + \boldsymbol{G}_t;\quad \boldsymbol{W}_t
  = \boldsymbol{W}_{t-1} - \eta_t[\mathop{\text{msign}}(\boldsymbol{M}_t)+\lambda\boldsymbol{W}_{t-1}]
symbol_meanings:
  G: G
  M: 矩阵
  W: 权重矩阵
  \beta: 二阶矩衰减系数 / 动量系数
  \boldsymbol{G}: boldsymbol{G}
  \boldsymbol{M}: 矩阵变量
  \boldsymbol{W}: 权重矩阵
  \eta: 学习率
  \lambda: 权重衰减系数 / 正则化系数
  t: 时间步 / 自变量
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions:
- 用于 Muon 系列文章中的矩阵参数更新语境。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-03-12-基于流式幂迭代的Muon实现-1-初识.md
source_ids:
- '11654'
derived_from: []
implies: []
appears_in:
- '[[基于流式幂迭代的Muon实现：1. 初识]]'
- '[[基于流式幂迭代的Muon实现：2. 加速]]'
evidence_spans:
- ev::11654::内容回顾
status: draft
updated: "2026-06-14"
---

# Muon更新公式


## 概述

（待补充）

## 公式

```tex
\boldsymbol{M}_t = \beta\boldsymbol{M}_{t-1} + \boldsymbol{G}_t
```

```tex
\boldsymbol{W}_t = \boldsymbol{W}_{t-1} - \eta_t[\mathop{\text{msign}}(\boldsymbol{M}_t)+\lambda\boldsymbol{W}_{t-1}]
```

## 作用

该公式是 MVP 中理解 [[矩阵符号函数]]、[[流式幂迭代]] 和 Muon 版本缩放差异的共同入口。

## 证据

- `ev::11654::内容回顾`