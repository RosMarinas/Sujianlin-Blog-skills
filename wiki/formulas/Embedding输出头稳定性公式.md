---

type: formula
title: Embedding输出头稳定性公式
aliases: []
latex: \rho(\Delta\omega)=\max_x\Vert f(x;\omega+\Delta\omega)-f(x;\omega)\Vert_{RMS}
symbol_meanings:
  omega: 参数
  rho: 更新稳定性指标
  x: 输入
standard_notation:
  rho: 更新稳定性指标
  x: 输入
  omega: 参数
conditions:
- 输入域或损失位置特殊时，max 的取值范围必须按模块重算。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-03-02-MuP之上-3-特殊情况特殊处理.md
source_ids:
- '11647'
derived_from: []
implies: []
appears_in:
- '11647'
evidence_spans:
- ev::11647::嵌入之层
- ev::11647::输出之头
status: draft
updated: "2026-06-14"
---

# Embedding输出头稳定性公式


## 概述

（待补充）

## 公式

```tex
\rho(\Delta\omega)=\max_x\Vert f(x;\omega+\Delta\omega)-f(x;\omega)\Vert_{RMS}
```

## 条件

- 输入域或损失位置特殊时，max 的取值范围必须按模块重算。

## 证据

- `ev::11647::嵌入之层`
- `ev::11647::输出之头`