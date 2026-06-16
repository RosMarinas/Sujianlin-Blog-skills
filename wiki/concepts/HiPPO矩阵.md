---
type: concept
title: HiPPO矩阵
aliases: []
definition: 从正交多项式投影的在线系数动力学中解析推出的状态矩阵 A。
prerequisites: []
equivalent_forms: []
direct_consequences:
- - - HiPPO-LegS
- - - 对角加低秩分解
related_formulas: []
related_methods: []
series:
- - - 重温SSM
evidence_spans:
- ev::10114::延伸思考::hippo_bottom_up
- ev::10137::计算高效::od
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
source_ids:
- '10114'
- '10137'
status: stable
updated: '2026-06-13'
---

# HiPPO矩阵

## 定义

HiPPO矩阵是在线函数逼近中系数向量 `x(t)` 所满足线性 ODE 的状态矩阵 `A`。源文从用正交基压缩持续输入 `u(t)` 的目标出发，推导出 `x'(t)=Ax(t)+Bu(t)` 或 `x'(t)=A x(t)/t + B u(t)/t`，其中 `A` 就是 HiPPO 系列的核心矩阵。

## 激活场景

它用于把连续流式信号或离散序列历史压缩为有限维状态。HiPPO 告诉我们当用勒让德等正交多项式近似动态更新的函数时，系数更新自然落到线性系统，因此它是 SSM、S4 等序列模型的数学基础之一。

## 关键关系

HiPPO-LegT 近似邻近窗口，HiPPO-LegS 关注全局历史；后续 S4 选用 HiPPO-LegS 的 `A`，再在常系数线性 ODE 框架中分析其指数衰减记忆和高效离散化。源文还讨论 `A` 可对角化及“对角+低秩”计算路径，为 S4 卷积核生成函数服务。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md`
- `Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md`
- `ev::10114::延伸思考::hippo_bottom_up`
- `ev::10137::计算高效::od`
