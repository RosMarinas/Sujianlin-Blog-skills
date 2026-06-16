---
type: proposition
title: HiPPO从正交投影导出线性ODE
aliases:
  []
statement: 在在线函数逼近问题中，正交基投影系数随时间变化的动力学可推导出线性 ODE 系统。
assumptions:
  - 源文对应章节的建模假设成立。
requires:
  - [[线性状态空间ODE]]
  - [[HiPPO矩阵]]
proof_route: 从 L2 正交投影得到系数内积表达，再对 T 求导并分部积分，特定基和区间映射下得到 A,B。
methods:
  []
limits:
  - 不自动推广到未在源文推导的后续模型。
examples:
  []
evidence_spans:
  - ev::10114::一般框架::projection_coefficients
  - ev::10114::延伸思考::hippo_bottom_up
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
source_ids:
  - "10114"
status: stable
updated: 2026-06-09
---
## 命题

在在线函数逼近问题中，正交基投影系数随时间变化的动力学可推导出线性 ODE 系统。

## 证明路线

从 L2 正交投影得到系数内积表达，再对 T 求导并分部积分，特定基和区间映射下得到 A,B。

## 适用边界

不把背景提到的 Mamba/S5 结论并入本 stable 命题。
