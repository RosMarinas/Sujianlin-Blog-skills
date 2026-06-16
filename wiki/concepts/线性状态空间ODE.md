---
type: concept
title: 线性状态空间ODE
aliases: []
definition: 用线性 ODE 描述状态 x(t) 在输入 u(t) 驱动下演化，并通过 C 或 C* 读出输出 y(t)。
prerequisites: []
equivalent_forms: []
direct_consequences:
- - - HiPPO矩阵
- - - S4卷积核生成函数
related_formulas: []
related_methods: []
series:
- - - 重温SSM
evidence_spans:
- ev::10114::基本形式::linear_ode
- ev::10162::基本框架::s4_legs
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
- '10114'
- '10162'
status: stable
updated: '2026-06-13'
---

# 线性状态空间ODE

## 定义

线性状态空间 ODE 用 `x'(t)=Ax(t)+Bu(t)` 描述隐藏状态随输入演化，并用 `y(t)=Cx(t)+Du(t)` 或 S4 中的 `y(t)=C^*x(t)+Du(t)` 读出输出。源文说明 `u(t)` 是输入，`x(t)` 是状态，`y(t)` 是输出，`A,B,C,D` 是相应维度的线性参数。

## 激活场景

它是 HiPPO、S4 与后续 SSM 模型的基础框架。HiPPO 从在线正交投影推导出这类线性系统，S4 则使用该系统进行序列建模，并在离散化后得到线性 RNN 和卷积核。

## 关键关系

线性状态空间 ODE 的重要性在于既简单又有足够表达力：源文用指数函数和三角函数组合说明线性系统也能拟合复杂函数。S4 进一步利用相似不变性，把 `A` 换到计算更方便的相似矩阵中而不改变输出；离散化后，卷积核 `K_k=C^*\bar{A}^k\bar{B}` 可通过生成函数高效计算。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md`
- `Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md`
- `ev::10114::基本形式::linear_ode`
- `ev::10162::基本框架::s4_legs`
