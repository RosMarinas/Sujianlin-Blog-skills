---
type: proposition
title: S4用对角加低秩分解高效计算HiPPO矩阵
aliases:
  []
statement: S4 的关键数学技巧是把 HiPPO-LegS 矩阵稳定地转为对角加低秩结构，从而高效计算离散状态矩阵与卷积核生成函数。
assumptions:
  - 源文对应章节的建模假设成立。
requires:
  - [[HiPPO-LegS]]
  - [[对角加低秩分解]]
  - [[S4卷积核生成函数]]
proof_route: 先指出直接对角化数值不稳定，再构造反对称矩阵获得酉对角化，最后在 A=Lambda-uv* 下用 Woodbury 计算。
methods:
  []
limits:
  - 不自动推广到未在源文推导的后续模型。
examples:
  []
evidence_spans:
  - ev::10162::特征向量::unstable_diagonalization
  - ev::10162::点睛之笔::dlr
  - ev::10162::最后冲刺::s4_kernel
  - ev::10162::文章小结::s4_summary
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
  - "10162"
status: stable
updated: 2026-06-09
---
## 命题

S4 的关键数学技巧是把 HiPPO-LegS 矩阵稳定地转为对角加低秩结构，从而高效计算离散状态矩阵与卷积核生成函数。

## 证明路线

先指出直接对角化数值不稳定，再构造反对称矩阵获得酉对角化，最后在 A=Lambda-uv* 下用 Woodbury 计算。

## 适用边界

不把背景提到的 Mamba/S5 结论并入本 stable 命题。
