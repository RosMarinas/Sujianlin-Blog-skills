---
type: proposition
title: LegS具有尺度等变和多项式衰减
aliases:
  []
statement: HiPPO-LegS 的离散化步长无关，并且历史衰减是多项式型长尾。
assumptions:
  - 源文对应章节的建模假设成立。
requires:
  - [[HiPPO-LegS]]
proof_route: 由 t=alpha tau 的尺度变换保持 ODE 形式，以及 A 的特征值为 -1,...,-d 推出衰减项为 m^j/n^j 的组合。
methods:
  []
limits:
  - 不自动推广到未在源文推导的后续模型。
examples:
  []
evidence_spans:
  - ev::10137::尺度等变::legs
  - ev::10137::长尾衰减::polynomial
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
source_ids:
  - "10137"
status: stable
updated: 2026-06-09
---
## 命题

HiPPO-LegS 的离散化步长无关，并且历史衰减是多项式型长尾。

## 证明路线

由 t=alpha tau 的尺度变换保持 ODE 形式，以及 A 的特征值为 -1,...,-d 推出衰减项为 m^j/n^j 的组合。

## 适用边界

不把背景提到的 Mamba/S5 结论并入本 stable 命题。
