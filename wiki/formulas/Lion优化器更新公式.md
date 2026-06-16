---
type: formula
title: Lion优化器更新公式
aliases:
  - Lion更新公式
  - EvoLved Sign Momentum formula
latex: |
  \begin{aligned}
  \boldsymbol{u}_t &= \text{sign}\big(\beta_1 \boldsymbol{m}_{t-1} + (1 - \beta_1) \boldsymbol{g}_t\big) \\
  \boldsymbol{\theta}_t &= \boldsymbol{\theta}_{t-1} - \eta_t (\boldsymbol{u}_t + \lambda_t \boldsymbol{\theta}_{t-1}) \\
  \boldsymbol{m}_t &= \beta_2 \boldsymbol{m}_{t-1} + (1 - \beta_2) \boldsymbol{g}_t
  \end{aligned}
symbol_meanings:
  \boldsymbol{\theta}_t: 第 t 步的模型参数权重向量
  \boldsymbol{g}_t: 第 t 步的损失函数关于参数的梯度向量，\boldsymbol{g}_t = \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_{t-1})
  \boldsymbol{m}_t: 第 t 步的一阶指数滑动平均动量缓存
  \boldsymbol{u}_t: 第 t 步的符号更新矢量
  \eta_t: 第 t 步的全局学习率步长
  \lambda_t: 第 t 步的权重衰减系数
  \beta_1: 状态更新时的梯度与动量加权滑动平均系数
  \beta_2: 动量本身更新的指数衰减系数
  \text{sign}: 逐分量提取正负符号的阶跃函数，正数返回 1，负数返回 -1
standard_notation:
  \boldsymbol{\theta}: 模型参数向量
  \boldsymbol{m}: 动量缓存向量
  \boldsymbol{g}: 梯度向量
  \text{sign}: 符号算子
conditions: 模型训练处于常规一阶梯度优化阶段，超参数通常推荐取 $\beta_1=0.9, \beta_2=0.99$（CV）或 $\beta_1=0.95, \beta_2=0.98$（NLP）。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-02-16-Google新搜出的优化器Lion-效率与效果兼得的-训练狮.md
source_ids:
  - "9473"
appears_in:
  - "[[spaces-9473-Google新搜出的优化器Lion-效率与效果兼得的-训练狮]]"
  - "[[spaces-9512-Tiger-一个-抠-到极致的优化器]]"
  - "[[spaces-9736-Lion-Tiger优化器训练下的Embedding异常和对策]]"
evidence_spans:
  - ev::9473::Lion更新公式
status: draft
updated: 2026-06-12
---

# Lion优化器更新公式


## 概述

（待补充）

## 物理意义与机制

本公式定义了 **Lion优化器** 在每一步的状态迭代规则。不同于传统动量梯度下降（SGDM）或 AdamW，Lion 在更新参数时执行了错位更新：

1. 首先利用 $\beta_1$ 将历史动量 $\boldsymbol{m}_{t-1}$ 与当前的即时梯度 $\boldsymbol{g}_t$ 做一次插值，并对该插值求 `sign` 符号，作为实际执行的更新方向 $\boldsymbol{u}_t$。
2. 随后利用所得符号方向对参数 $\boldsymbol{\theta}_{t-1}$ 进行更新，并在此时施加权重衰减 $\lambda_t$。
3. 最后，利用 $\beta_2$ 对下一阶段的一阶动量 $\boldsymbol{m}_t$ 进行平滑更新。这种在参数更新之后再进行动量滚动的错位机制是其符号搜索算法的关键发现，也是在保持较小内存占用的同时维持模型收敛性和泛化性的本质所在。
