---

type: formula
title: 线性状态空间ODE公式
aliases: []
latex: x'(t)=Ax(t)+Bu(t),\quad y(t)=Cx(t)+Du(t)
symbol_meanings:
  x(t): 潜在状态变量
  u(t): 输入信号
  y(t): 输出信号
  A: 状态转移矩阵
standard_notation:
  convention: Use the symbols exactly as defined in `latex`; meanings are listed in
    `symbol_meanings`.
conditions: A,B,C,D 维度按源文具体设置；S4 中常取标量输入输出并可吸收 D 项。
derived_from: []
implies: []
appears_in:
- '[[重温SSM（一）：线性系统和HiPPO矩阵]]'
- '[[重温SSM（三）：HiPPO的高效计算（S4）]]'
evidence_spans:
- ev::10114::基本形式::linear_ode
- ev::10162::基本框架::s4_legs
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
- '10114'
- '10162'
status: draft
updated: '2026-06-14'
---


# 线性状态空间ODE公式


## 概述

（待补充）

## 公式本体

```tex
x'(t)=Ax(t)+Bu(t),\quad y(t)=Cx(t)+Du(t)
```

## 成立条件

A,B,C,D 维度按源文具体设置；S4 中常取标量输入输出并可吸收 D 项。

## 推导来源

- `ev::10114::基本形式::linear_ode`
- `ev::10162::基本框架::s4_legs`

## 详细说明

线性状态空间 ODE 公式 $$x'(t)=Ax(t)+Bu(t),\quad y(t)=Cx(t)+Du(t)$$ 构成了深度学习状态空间模型（SSM，包含 S4、Mamba 及其衍生变体）序列建模能力的几何动力学基石。它通过连续时间的常微分方程描述一维信号 $u(t)$ 与高维潜在状态 $x(t)$ 之间的演变映射规律。该框架的设计灵感来源于对动态更新区间连续信号的实时在线多项式逼近（如利用勒让德多项式的 HiPPO 矩阵进行投影）。矩阵 $A$ 决定了系统是如何随时间平滑积累记忆并指数衰减过去状态的，而借助诸如前向欧拉或双线性映射的数学离散化技巧，这套连续微分系统可以转化为一种高精度的离散线性 RNN。这使得算法可以在前馈训练时借助并行卷积极速计算，并在自回归生成阶段保持常数级的高效推断。
