---
type: proposition
title: Tiger优化器在滑动平均相同下的等价性
statement: Tiger优化器在数学上等价于Lion优化器令其动量指数滑动平均衰减率 beta1 = beta2 = beta 的特化情形。
assumptions:
  - 优化更新在多维浮点数参数向量空间中进行。
  - 参数状态更新均包含解耦的权重衰减项（Weight Decay）。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
source_ids:
  - "9512"
proof_route: |
  1. 写出Lion优化器在 \beta_1 = \beta_2 = \beta 条件下的状态转移方程。
  2. 此时，更新矢量 \boldsymbol{u}_t 满足：
     \boldsymbol{u}_t = \text{sign}\big(\beta \boldsymbol{m}_{t-1} + (1-\beta)\boldsymbol{g}_t\big)
  3. 注意到 Lion 关于动量的更新公式为：
     \boldsymbol{m}_t = \beta \boldsymbol{m}_{t-1} + (1-\beta)\boldsymbol{g}_t
  4. 观察可以发现，\boldsymbol{u}_t 的括号内部表达式正是 \boldsymbol{m}_t 本身。因此有：
     \boldsymbol{u}_t = \text{sign}(\boldsymbol{m}_t)
  5. 将此代入参数更新式，得到：
     \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t \big[\text{sign}(\boldsymbol{m}_t) + \lambda_t \boldsymbol{\theta}_{t-1}\big]
     这与 Tiger 优化器的状态转移定义式完全一致。
evidence_spans:
  - ev::9512::Tiger更新公式
status: draft
updated: 2026-06-12
---

# Tiger优化器在滑动平均相同下的等价性

## 命题陈述

Tiger优化器在数学上对应于 [Lion优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) 在参数设定满足一阶动量滑动与权重更新插值共用同一个衰减常数 $\beta$ 时的等价形式。

## 物理意义

当这一参数设定被统一后，计算更新矢量时不再需要交织混合当前的原始梯度，使得优化更新对梯度的使用变为了纯粹的动量转移。这种等价性的简化对消除梯度缓存、优化计算架构发挥了关键作用。
