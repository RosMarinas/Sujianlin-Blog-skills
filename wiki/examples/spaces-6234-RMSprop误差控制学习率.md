---
type: example
title: spaces-6234-RMSprop误差控制学习率
aliases: []
article_id: '6234'
article:
- - 从动力学角度看优化算法（二）：自适应学习率算法
section: 变学习率思想
claim: RMSprop 可被解释为根据数值误差控制调节各坐标学习率。
notation_mapping:
  theta: theta
  L: L
  gamma: source-local learning rate
steps:
- 把极小值点问题写成 ODE
- 从欧拉法误差角度考虑步长
- 按梯度尺度构造坐标学习率
- 通过滑动平均得到 RMSprop 形式
used_concepts:
- - - 梯度流
- - - 优化动力学视角
used_formulas:
- - - 梯度流ODE公式
used_methods:
- - - 把优化算法解释为动力系统离散化
problem_pattern:
- - 把优化器经验现象改写为动力系统问题
source_span: ev::6234::变学习率思想
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-12-20-从动力学角度看优化算法-二-自适应学习率算法.md
source_ids:
- '6234'
status: stable
updated: '2026-06-12'
---

# spaces-6234-RMSprop误差控制学习率

## 所在文章

[[从动力学角度看优化算法（二）：自适应学习率算法]]

## 原始问题

RMSprop 可被解释为根据数值误差控制调节各坐标学习率。

## 推导步骤

1. 把极小值点问题写成 ODE
2. 从欧拉法误差角度考虑步长
3. 按梯度尺度构造坐标学习率
4. 通过滑动平均得到 RMSprop 形式

## 证据锚点

- `ev::6234::变学习率思想`