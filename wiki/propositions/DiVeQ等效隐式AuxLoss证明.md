---
type: proposition
title: DiVeQ等效隐式AuxLoss证明
statement: DiVeQ 重新参数化公式 z_q = z + ||q-z|| * sg[(q-z)/||q-z||] 在反向传播梯度流中，在条件 L(z_q) - L(z) > 0 下，等效于引入了一个拉近编码向量 q 与连续向量 z 之间距离的自适应辅助损失函数。
assumptions:
  - 目标损失函数 L(z_q) 可微
  - 一阶近似满足 L(z) approx L(z_q) + grad_z_q L . (z - q)
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-08-DiVeQ-一种非常简洁的VQ训练方案.md
source_ids:
  - 11328
proof_route: 对 L(z_q) 微分展开得 dL = grad_z_q L . dz_q。由于 z_q = z + r(q,z) * sg[(q-z)/r(q,z)]，其微分为 dz_q = dz + dr * (q-z)/r。代入展开可得，dL 包含两部分：一部分是传统 STE 的 grad_z_q L . dz；另一部分是额外项 [grad_z_q L . (q-z)] * d(ln r)。利用一阶泰勒展开，grad_z_q L . (q-z) approx L(z_q) - L(z)。当模型收敛时，无损连续表示 z 的损失显然比离散量化后的 z_q 更好，即 L(z_q) - L(z) > 0。因此，当 r 取距离特征 ||q-z|| 时，第二项系数为正，等效于隐式添加了自适应拉近编码距离的 Loss。
evidence_spans:
  - ev::11328::理论分析
status: draft
updated: 2026-06-11
---

该命题在数学上论证了为何 DiVeQ 即使不加入任何外部辅助损失（Aux Loss），也能够端到端地学出高质量编码表的深层原理。