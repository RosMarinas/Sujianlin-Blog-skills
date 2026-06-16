---
type: proposition
title: Muon是谱范数下的最速下降
statement: 在约束参数变化量谱范数（最大奇异值）小于等于学习率的优化问题中，损失函数在局部下降最快的参数变化矩阵即为 Muon 优化器的 Matrix Sign Function (msign) 的相反数。
assumptions:
  - 更新约束定义为权重变化矩阵的谱范数（最大奇异值）
  - 一阶梯度近似足够精确（一阶泰勒展开）
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
source_ids:
  - 10739
proof_route: 优化问题为 min_{Delta W} Tr(G^T Delta W) s.t. ||Delta W||_2 <= eta。利用矩阵的对偶范数性质，谱范数的对偶范数为核范数（Shatten-1 范数）。由 Holder 不等式可得，当权重改动 Delta W 取为极值 -eta * msign(G) 时，目标函数取得下界 -eta * ||G||_*。此时 W 的变化方向正对最大可能奇异值投影方向，即为谱范数下的最速下降方向。
evidence_spans:
  - ev::10739::优化原理
status: draft
updated: 2026-06-11
---

该命题指明了 Muon 并不是一个经验打补丁式的优化器，而是谱范数约束下精确的变分最速下降解。