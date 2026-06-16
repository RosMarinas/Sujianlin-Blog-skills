---
type: article_summary
title: Lion/Tiger优化器训练下的Embedding异常和对策
article_id: "9736"
source_url: https://spaces.ac.cn/archives/9736
date: 2023-08-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
series: []
topics:
  - "[[优化器稳定性与自适应机制]]"
concepts:
  - "[[Embedding过度更新]]"
  - "[[Lion优化器]]"
  - "[[Tiger优化器]]"
methods:
  - "[[用符号函数重写优化器更新方向]]"
problem_patterns: []
evidence_spans:
  - ev::9736::Embedding异常现象
  - ev::9736::过度更新原理
  - ev::9736::异常值平衡点
  - ev::9736::对策Lazy化
  - ev::9736::对策TiedEmbedding
  - ev::9736::对策混合优化器
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
source_ids:
  - "9736"
status: draft
updated: 2026-06-12
---

# Lion/Tiger优化器训练下的Embedding异常和对策

## 文章核心问题

为什么使用Lion/Tiger等符号（sign）优化器在大模型训练中会导致低频Token的Embedding分量整齐地膨胀到特定的常数值（例如 $\pm 100$），以及如何有效根治这一特有的数值病态问题。

## 主要结论

- **Embedding异常现象**：低频Token的Embedding矩阵元素会收敛到非常大的常数级（在其衰减率 $\lambda=0.01$ 时，表现为整齐的 $\pm 100$ 边界）。除Embedding矩阵外，其他权重一切正常，且通常不直接导致明显的Loss崩塌。
- **病态机制：过度更新**：只要某Token曾出现，其Embedding对应动量 $\boldsymbol{m}_t$ 被更新为非零值。之后即使该Token不再出现在输入样本中（其梯度 $\boldsymbol{g}_t=0$），其动量虽指数衰减，但在因精度限制化为绝对零之前，$\text{sign}(\boldsymbol{m}_t)$ 保持恒定为 $\pm 1$。这造成低频Token在样本不包含它的极长步数中被持续“过度更新”。
- **异常值数值解析**：由迭代公式 $\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t [\text{sign}(\boldsymbol{m}_t) + \lambda \boldsymbol{\theta}_{t-1}]$，在 $\text{sign}(\boldsymbol{m}_t)$ 长期不变的条件下，该迭代具有渐近稳定平衡点 $\boldsymbol{\theta}^* = -\frac{\text{sign}(\boldsymbol{m}_t)}{\lambda}$。若 $\lambda=0.01$，则平衡点自然落于 $\pm 100$。
- **解决方案**：
  1. **Lazy更新**：只有当当前样本实际包含该Token时才允许对其Embedding进行状态更新。
  2. **Tied Embeddings（共享嵌入）**：将输入与输出层Embedding共享。输出端的全局计算使得Embedding所有位置的梯度在每步都不为零，从而消除梯度稀疏导致的平衡点膨胀。
  3. **混合优化器（非优雅但有效）**：对Embedding层使用常规AdamW优化器，其余各参数层采用Lion/Tiger。

## 推导结构

1. **报告异常现象**：指出低频Token在Embedding矩阵的极大/极小值正好落在 $\pm 100$。
2. **分析机制机理**：比对AdamW与Tiger的动量指数级自然消散。AdamW的更新量正比于动量，低频时自动趋近零；而Tiger由于 $\text{sign}$ 非零的阻隔，只要动量不为零就一直以全幅更新。
3. **推导平衡解析解**：解出包含权重衰减的迭代平衡极限，完美吻合 $\pm 100$ 的实验现象。
4. **设计并实施方案**：提出Lazy优化策略、输出权重共享（Tied Embeddings）以及分层混合优化这三种应对措施，并展示了对齐通道共享Tied Embedding在实验中的良好表现。

## 关键公式

- **Embedding过度更新迭代平衡点**（由于 $\text{sign}(\boldsymbol{m}_t)$ 长期恒定）：
  $$
  \boldsymbol{\theta}^* = -\frac{\text{sign}(\boldsymbol{m}_t)}{\lambda}
  $$

## 体现的方法

- **梯度稀疏参数惰性更新**：通过显式控制在输入为零时截断更新项或动量项。
- **参数共享消除稀疏梯度**：重用权重矩阵以将局部零梯度的稀疏参数重映射为全局稠密梯度的常态参数。

## 所属系列位置

独立研究文章，属于深度学习优化器理论和自适应机制的探讨。

## 与其他文章的关系

- 前置的优化器机制来源于 [Lion优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) (9473) 和 [Tiger优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Tiger优化器.md) (9512)。
- 惰性优化思想来自于 LazyOptimizer (7094) 与 [Keras实现两个优化器：Lookahead和LazyOptimizer](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/sources/spaces-7094-6个派生优化器的简单介绍及其实现.md) (6869)。
- 嵌入共享对策关联到 [共享Embedding重新探索](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/sources/spaces-9736-Lion-Tiger优化器训练下的Embedding异常和对策.md) (9698)。

## 原文证据锚点

- **ev::9736::Embedding异常现象**: 第24-30行，罗列了低频Token的Embedding分量在整齐落于 $\pm 100$ 边界处的6点实验观察。
- **ev::9736::过度更新原理**: 第33-39行，分析了带动量优化器在稀疏样本梯度下低频Token的过度更新现象在 sign 和传统 Adam 下的不同结局。
- **ev::9736::异常值平衡点**: 第42-53行，通过简单的极限求导与稳定态代数求解，得出平衡点刚好为 $- \text{sign}(\boldsymbol{m}) / \lambda$ 的结论。
- **ev::9736::对策Lazy化**: 第56-57行，介绍了通过仅在 Token 出现时才更新 Embedding 的 Lazy 化修正对策。
- **ev::9736::对策TiedEmbedding**: 第58-59行，提出通过共享输入输出 Embedding 将稀疏梯度变为稠密梯度，进而抑制过度更新平衡点生成的原理。
- **ev::9736::对策混合优化器**: 第60-61行，介绍了来自 Lion 论文作者提供的 Embedding 使用 Adam 优化器、其余层使用 Lion 的混合调丹方案。
