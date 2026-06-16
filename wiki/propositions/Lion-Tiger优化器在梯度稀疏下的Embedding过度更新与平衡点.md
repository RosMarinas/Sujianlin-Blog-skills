---
type: proposition
title: Lion-Tiger优化器在梯度稀疏下的Embedding过度更新与平衡点
statement: 在梯度极端稀疏的参数层（如Embedding），使用符号优化器（Lion/Tiger）会导致未激活参数在没有样本梯度输入时发生方向锁定的过度更新，并渐近收敛于平衡点 \boldsymbol{\theta}^* = -\frac{\text{sign}(\boldsymbol{m})}{\lambda}。
assumptions:
  - 当前被优化的 Token $T$ 长期不出现在输入批次中，即样本梯度 \boldsymbol{g}_t = \boldsymbol{0}。
  - 动量初始值不为零且由于浮点表示精度限制不会立刻变为真零。
  - 权重衰减系数 \lambda > 0 为常数。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
source_ids:
  - "9736"
proof_route: |
  1. 假设某 Token 的当前即时梯度恒为 0，则一阶动量状态演化为：
     \boldsymbol{m}_t = \beta \boldsymbol{m}_{t-1}
     这是一个以 \beta 级指数衰减的动力系统。
  2. 由于 $\text{sign}$ 的非线性阶跃特性，只要 \boldsymbol{m}_t 尚未因下溢变成 0（这在有限精度浮点表示下需要极多步数），它的符号矢量就恒定等于其初始方向：
     \text{sign}(\boldsymbol{m}_t) = \text{sign}(\boldsymbol{m}_0) = \boldsymbol{S} \quad (\boldsymbol{S} \in \{-1, 1\}^d)
  3. 将常数符号方向 \boldsymbol{S} 代入带有权重衰减的参数更新方程：
     \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t (\boldsymbol{S} + \lambda \boldsymbol{\theta}_{t-1})
     = (1 - \eta_t \lambda)\boldsymbol{\theta}_{t-1} - \eta_t \boldsymbol{S}
  4. 该一阶差分方程具有解析收敛极限。当 $t \to \infty$ 时，设定 $\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} = \boldsymbol{\theta}^*$。代入方程解得平衡状态为：
     \boldsymbol{\theta}^* = -\frac{\boldsymbol{S}}{\lambda} = -\frac{\text{sign}(\boldsymbol{m}_0)}{\lambda}
     若设定权重衰减率 \lambda = 0.01，则各分量自然收敛到 \pm 100 边界。
evidence_spans:
  - ev::9736::异常值平衡点
  - ev::9736::过度更新原理
status: draft
updated: 2026-06-12
---

# Lion-Tiger优化器在梯度稀疏下的Embedding过度更新与平衡点

## 命题陈述

当使用符号优化器优化具有稀疏梯度的模型权重时，未激活权重会由于动量符号锁定而被持续更新，直到被权重衰减项拉回并稳定于平衡态 $\boldsymbol{\theta}^* = -\frac{\text{sign}(\boldsymbol{m})}{\lambda}$。

## 物理意义

这一解析平衡点完美解释了在使用 Lion/Tiger 训练语言模型时，低频 Token 的 Embedding 分量全部整齐地收敛至边界值（如 $\pm 100$）的现象。这也揭示了符号函数优化器在面对稀疏特征激活时的固有机制缺陷，指明了对其使用 Lazy 惰性更新或 Embedding 共享的必要性。
