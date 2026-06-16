---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: Update RMS 对齐法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
source_ids:
  - 10739
method_summary: 将新设计出的优化器更新矩阵的 RMS 解析地映射或数值归一化到 Adam 优化器常用的 0.2 量级，实现 Adam 的超参数向新优化器的无缝迁移。
typical_structure: |
  1. 设定新优化器为求解到的更新方向矩阵 $\boldsymbol{\Phi}_t$。
  2. 计算该更新方向矩阵的 Root Mean Square (RMS)：$\text{RMS}(\boldsymbol{\Phi}_t) = \frac{\Vert \boldsymbol{\Phi}_t\Vert_F}{\sqrt{nm}}$。如果是数学结构固定的正交更新（如 Muon），解析地计算出其 RMS 的理论值。
  3. 将原始的更新步缩放对齐到 0.2 量级：采用 $0.2 \times \frac{\boldsymbol{\Phi}_t}{\text{RMS}(\boldsymbol{\Phi}_t)}$ 替代原来的 $\boldsymbol{\Phi}_t$。
  4. 结合权重衰减与学习率更新参数：$\boldsymbol{W}_t = \boldsymbol{W}_{t-1} - \eta_t (0.2\, \boldsymbol{\Phi}_t/\text{RMS}(\boldsymbol{\Phi}_t) + \lambda \boldsymbol{W}_{t-1})$，其中的学习率 $\eta_t$ 和衰减率 $\lambda$ 直接照搬 Adam 调好的参数。
applicability: 适用于需要在大模型上探索非 Adam 优化器（如 Muon 等正交优化），但缺乏大量算力资源进行网格搜索重新调参的阶段。
evidence_spans:
  - ev::10739::"我们观察到Adam更新量的RMS是比较稳定的，通常在0.2～0.4之间...基于此，我们建议通过RMS Norm将新优化器的Update RMS对齐到0.2...这样一来，我们就可以复用Adam的$\eta_t$和$\lambda$"
  - ev::10739::"特别地，Muon的$\text{RMS}(\boldsymbol{\Phi}_t)$还可以解析地算出来...$\text{RMS}(\boldsymbol{\Phi}_t) = \sqrt{1/\max(n,m)}$...最终没有用RMS Norm而是用等价的解析版本"
examples:
  - [[article::10739]]
status: stable
updated: 2026-06-13
---

# Update RMS 对齐法

## 适用问题

在深度学习模型（特别是大语言模型）的训练中，当尝试从久经考验的 Adam 优化器切换到新兴优化器（如 Muon 优化器）时，往往面临着超参数（学习率、权重衰减）极难调节的问题。通过网格搜索重新寻找最优超参数在大规模模型上成本极为高昂。需要一种机制来快速把 Adam 积攒的超参“白嫖”到新优化器上。

## 核心变换

将“盲目为新优化器寻找学习率”变换为“通过动力学规模的规范化对齐（RMS Alignment）强行复用现有超参”。由于不同优化器每步给出的更新矩阵 $\boldsymbol{\Phi}_t$ 在幅度上可能有天壤之别，但它们对参数空间的整体修剪力度是由该步的 RMS（Root Mean Square，即每个元素的平均幅度）决定的，通过强制把新优化器的 RMS 拉平到 Adam 常用的经验值（0.2），便实现了动力学规模的对齐。

## 典型步骤

1. **计算原始更新量**：在新优化器的每一步，计算出参数 $\boldsymbol{W}$ 的梯度或动量，并根据其自身算法求出初步的更新矩阵 $\boldsymbol{\Phi}_t$（例如在 Muon 中就是矩阵梯度的正交化）。
2. **计算 RMS 幅度**：计算 $\boldsymbol{\Phi}_t$ 的 RMS：$\text{RMS}(\boldsymbol{\Phi}_t) = \sqrt{\frac{1}{nm}\sum_{i=1}^n\sum_{j=1}^m \Phi_{i,j}^2}$。对于某些具有确定性范数约束的优化器，这一步可以直接解析求解（如 Muon 的更新量 RMS 解析值约为 $\sqrt{1/\max(n,m)}$）。
3. **恒定缩放对齐**：将更新方向做幅度缩放，统一归一化为 $\frac{0.2}{\text{RMS}(\boldsymbol{\Phi}_t)}\boldsymbol{\Phi}_t$。
4. **施加通用超参**：应用与 Adam 完全一致的学习率 $\eta_t$ 与权重衰减系数 $\lambda$ 进行参数更新：$\boldsymbol{W}_t = \boldsymbol{W}_{t-1} - \eta_t \left( \frac{0.2}{\text{RMS}(\boldsymbol{\Phi}_t)}\boldsymbol{\Phi}_t + \lambda \boldsymbol{W}_{t-1} \right)$。

## 直觉

为什么 Adam 的超参数不能直接给别的优化器用？因为两个优化器“迈步子的脾气”不一样。有的优化器算出的方向向量模长很大，套用 Adam 的学习率会直接跑飞；有的算出来很小，套上去根本不收敛。但如果我们统计一下 Adam 每次更新参数时，它加在参数上的那个矩阵（剔除学习率后的更新量）的平均元素大小（RMS），发现它竟然非常稳定，基本在 0.2 左右。所以，不管你提出多么花里胡哨的新优化器，只要你在应用学习率之前，先把你的更新矩阵强行按比例缩放，使得它的 RMS 也是 0.2，那在这个更新面上，你就“伪装”成了 Adam 的脾气，Adam 的学习率自然就能直接喂给你用了。

## 边界

- **非方阵的维度差异**：在模型包含大量非方阵参数（如 MoE 架构）时，不同矩阵的维度 $n, m$ 差异极大。如果简单用同一学习率而不进行各矩阵独立的解析缩放（即不同矩阵应用不同的 $\sqrt{\max(n,m)}$ 缩放），会导致不同矩阵更新不同步，拖累整体收敛效果。
- **次优解与局部最优**：Update RMS 缩放本质上只是实现了快速的“冷启动迁移”，并不能保证此时的超参数就是该新优化器的理论最优。为了挖掘新优化器的极致性能，仍需要以对齐后的超参为基准进行小范围微调。

## 例子

在引入 Muon 优化器对 16B 的 Moonlight MoE 模型进行预训练时。Muon 优化器给出的更新量 $\boldsymbol{\Phi}_t = \text{msign}(\boldsymbol{G})$ 本身是正交矩阵的一部分，具有很特殊的性质。研究发现它的 RMS 在理论上恒等于 $\sqrt{1/\max(n,m)}$。为了避免从头搜索它的学习率，我们直接修改它的更新公式，在更新量上乘上一个缩放因子 $0.2 \times \sqrt{\max(n,m)}$，从而强制让它每一步的平均变动幅度与 Adam 齐平。这样一来，直接套用原来的 Adam 学习率就可以稳定开始训练，且效果超越 Adam。

## 证据

- ev::10739::"我们观察到Adam更新量的RMS是比较稳定的，通常在0.2～0.4之间...基于此，我们建议通过RMS Norm将新优化器的Update RMS对齐到0.2...这样一来，我们就可以复用Adam的$\eta_t$和$\lambda$"
- ev::10739::"特别地，Muon的$\text{RMS}(\boldsymbol{\Phi}_t)$还可以解析地算出来...实践中一个矩阵严格低秩的概率比较小...从而有$\text{RMS}(\boldsymbol{\Phi}_t) = \sqrt{1/\max(n,m)}$...所以我们最终没有用RMS Norm而是用等价的解析版本"