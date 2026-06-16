---
type: formula
title: DiVeQ重参数更新公式
latex: z_q = z + \|q - z\| \times \text{sg}\left[\frac{q - z + \varepsilon}{\|q -
  z + \varepsilon\|}\right]
symbol_meanings:
  z: 连续输入特征
  q: 离散最近邻量化特征
  epsilon: 服从标准正态分布的平滑高斯噪声
  sg: stop_gradient 算子
standard_notation:
  continuous: z
  discrete: q
  noise: \varepsilon
conditions: 噪声平滑标准差 sigma^2 设为 10^-3 可在 DiVeQ-detach (sigma=0) 与正态随机采集中取得最佳均衡
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-08-DiVeQ-一种非常简洁的VQ训练方案.md
source_ids:
- 11328
appears_in:
- - - spaces-11328-DiVeQ训练方案
status: draft
updated: '2026-06-14'
---

## 概述

传统的 VQ-VAE 通常依赖标准的 STE（Straight-Through Estimator）技巧，其核心实现公式为 $z_q = z + \mathop{\text{sg}}[q - z]$。这种做法虽然保证了反向传播时 $\nabla z_q = \nabla z$ 从而让编码器（encoder）能够获得梯度，但由于 $q$ 被完全包含在 `stop_gradient` 算子中，导致编码表无法直接通过重构误差获得优化梯度。为此，传统的 VQ 方案不得不引入额外的辅助损失函数（Aux Loss），例如 $\beta\Vert q - \mathop{\text{sg}}[z]\Vert^2 + \gamma\Vert z - \mathop{\text{sg}}[q]\Vert^2$，或者依赖滑动平均策略来强制 $z$ 与 $q$ 相互靠近，这不仅破坏了端到端的简洁性，还引入了额外的超参数。

DiVeQ 通过引入重参数化技巧（Reparameterization Trick）优雅地解决了这一痛点。如公式所示，DiVeQ 将标量距离函数 $\|q - z\|$ 显式地提取到了 `stop_gradient` 算子 $\text{sg}[\cdot]$ 的外部，并结合服从标准正态分布的平滑噪声 $\varepsilon$ 来处理方向向量。这一设计使得公式在前向上依然严格输出量化特征 $z_q = q$（当随机扰动忽略不计时），但在反向传播中，重构损失能够直接通过 $\|q - z\|$ 产生连续的端到端梯度流，同时作用于连续输入特征 $z$ 和离散最近邻量化特征 $q$。这种机制使得量化向量能够自动获得来自距离函数的更新，彻底免去了传统 VQ-VAE 中繁杂的 Aux Loss，实现了一种极其简洁且漂亮的端到端 VQ 训练框架。
