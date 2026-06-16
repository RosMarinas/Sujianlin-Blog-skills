---

type: formula
title: MuP稳定性三条件公式
aliases: []
latex: \max_x \Vert f(x;\omega)\Vert_{RMS}=\Theta(1),\quad \max_{x,\Delta x}\frac{\Vert
  f(x+\Delta x;\omega)-f(x;\omega)\Vert_{RMS}}{\Vert\Delta x\Vert_{RMS}}=\Theta(1),\quad
  \max_x\Vert f(x;\omega+\Delta\omega)-f(x;\omega)\Vert_{RMS}=\Theta(1)
symbol_meanings:
  RMS: 均方根尺度
  f: 模型或层
  omega: 参数
standard_notation:
  f: 模型或层
  omega: 参数
  RMS: 均方根尺度
conditions:
- 用 max/sup 消去输入，目标只保留模型、参数或增量尺度。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-21-MuP之上-1-好模型的三个特征.md
- Data/Spaces_ac_cn/markdown/Big-Data/2026-04-24-MuP之上-4-坚守参数的稳定性.md
source_ids:
- '11340'
- '11729'
derived_from: []
implies: []
appears_in:
- '11340'
- '11729'
evidence_spans:
- ev::11340::三个条件
- ev::11729::问题背景
status: draft
updated: "2026-06-14"
---

# MuP稳定性三条件公式


## 概述

（待补充）

## 公式

```tex
\max_x \Vert f(x;\omega)\Vert_{RMS}=\Theta(1),\quad \max_{x,\Delta x}\frac{\Vert f(x+\Delta x;\omega)-f(x;\omega)\Vert_{RMS}}{\Vert\Delta x\Vert_{RMS}}=\Theta(1),\quad \max_x\Vert f(x;\omega+\Delta\omega)-f(x;\omega)\Vert_{RMS}=\Theta(1)
```

## 条件

- 用 max/sup 消去输入，目标只保留模型、参数或增量尺度。

## 证据

- `ev::11340::三个条件`
- `ev::11729::问题背景`