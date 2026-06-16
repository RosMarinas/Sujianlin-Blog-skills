---
type: concept
title: Embedding过度更新
aliases:
  - Embedding过度更新问题
  - 符号优化器稀疏过度更新
  - Embedding over-update
definition: 符号型优化器在大模型稀疏参数层（如Embedding层）训练中，因为符号操作阻断了动量的指数衰减性质，导致即便当前样本不包含该Token，对应的Embedding依然被恒定方向持续累积更新，最终收敛至数值崩溃边缘的病态现象。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
source_ids:
  - "9736"
related_formulas:
  - "[[Lion优化器更新公式]]"
  - "[[Tiger优化器更新公式]]"
related_methods: []
evidence_spans:
  - ev::9736::过度更新原理
  - ev::9736::异常值平衡点
status: draft
updated: 2026-06-12
---

# Embedding过度更新

## 问题根源

在深度学习模型训练中，[Lion优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) 和 [Tiger优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Tiger优化器.md) 等依赖 `sign` 符号函数的优化器在大规模稀疏参数层（如 Embedding 层）往往会暴露其特有的**过度更新**缺陷：

1. **梯度稀疏性**：在语言模型中，每个样本批次只激活很少量的 Token。对于绝大部分未激活的 Token，其当前样本梯度 $\boldsymbol{g}_t$ 为零。
2. **动量符号锁定**：如果一个低频 Token 曾经出现过，其动量 $\boldsymbol{m}_t$ 会被更新为非零。在之后的数万步内，即使该 Token 长期不出现（梯度为零），其动量虽会以指数级衰减（乘以 $\beta$），但只要其动量尚未因为浮点误差归为纯零，其符号函数 $\text{sign}(\boldsymbol{m}_t)$ 就会保持恒定的 $\pm 1$。
3. **恒定幅值更新**：在 AdamW 中，因为更新量正比于动量本身，低频 Token 的更新量会随动量指数级消退至零；而在符号优化器中，由于 `sign` 的阶跃特性，低频 Token 却在每一步都被强迫以满负荷的全局步长更新，并在其梯度重新激活时加剧同一更新方向的锁定。

## 平衡点解析

当低频 Token 在极长步数中没有出现时，更新公式由于 $\text{sign}(\boldsymbol{m}_t)$ 保持恒定值而化为简单的常数项迭代。此时，符号方向累积步长与权重衰减（Weight Decay）项 $\lambda \boldsymbol{\theta}$ 在迭代中会达到一个动态极限平衡点：
$$
\boldsymbol{\theta}^* = -\frac{\text{sign}(\boldsymbol{m}_t)}{\lambda}
$$
若优化器设置的权重衰减率 $\lambda = 0.01$，则未激活 Token 的 Embedding 分量会被无阻碍地推向整齐的极限边界 $\pm 100$。这种数值异常会极大破坏低频 Token 的表征质量，并在跨语种迁移、下游微调等场景下由于低频 Token 被强行唤醒而引发数值不稳定和模型崩溃。

## 解决对策

1. **惰性更新（Lazy Update）**：修改优化器逻辑，判断当且仅当当前批次中包含该 Token 标识时，才允许对该 Token 的 Embedding 子向量进行动量和权重的更新。
2. **嵌入共享（Tied Embeddings）**：将输入与输出投影层参数共享。由于输出层在每步计算全局 Logits 时都重用了整个词表矩阵，导致整个 Embedding 矩阵梯度不再稀疏，天然消除了恒定符号锁定的产生。
3. **混合层间优化**：对 Embedding 矩阵单独指派 AdamW 优化器，而在模型其他层使用 Lion/Tiger。
