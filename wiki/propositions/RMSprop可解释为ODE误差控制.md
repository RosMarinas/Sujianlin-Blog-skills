---
type: proposition
title: RMSprop可解释为ODE误差控制
aliases: []
statement: RMSprop 的自适应学习率可以从 ODE 数值求解误差控制角度解释。
assumptions:
  - 把极小值求解转为 ODE 求解
  - 按坐标调节步长
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-12-20-从动力学角度看优化算法-二-自适应学习率算法.md
source_ids:
  - "6234"
requires:
  - [[梯度流ODE公式]]
proof_route: 由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。
methods:
  - [[把优化算法解释为动力系统离散化]]
limits:
  - 当前只在本批次源文范围内稳定，跨系列推广需另行验证。
examples: []
evidence_spans:
  - ev::6234::变学习率思想
status: stable
updated: 2026-06-10
---

# RMSprop可解释为ODE误差控制

## 命题

RMSprop 的自适应学习率可以从 ODE 数值求解误差控制角度解释。

## 证明路线

由对应 evidence span 中的源文推导抽取；本页保留结论层节点，公式细节见 requires。

## 证据

- `ev::6234::变学习率思想`
