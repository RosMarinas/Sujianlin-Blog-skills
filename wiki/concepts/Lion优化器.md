---
type: concept
title: Lion优化器
aliases:
  - Lion
  - EvoLved Sign Momentum
definition: 一种通过符号发现算法搜索得出的一阶自适应优化器，它通过取动量与梯度的线性组合的符号（sign）作为参数更新量，仅需缓存一组一阶动量参数。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-02-16-Google新搜出的优化器Lion-效率与效果兼得的-训练狮.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
source_ids:
  - "9473"
  - "9736"
related_formulas:
  - "[[Lion优化器更新公式]]"
related_methods:
  - "[[用符号函数重写优化器更新方向]]"
evidence_spans:
  - ev::9473::Lion更新公式
status: draft
updated: 2026-06-12
---

# Lion优化器

## 核心定义

**Lion优化器**（EvoLved Sign Momentum）是Google通过符号发现（Symbolic Discovery）算法，消耗数千TPU小时搜索并结合人工干预设计出的一阶梯度优化器。其核心设计在于将参数的更新幅度完全符号化，通过对一阶动量和当前梯度的线性加权和进行 `sign` 运算来确定更新方向，同时抛弃了传统 AdamW 中开销较大的二阶矩缓存和逐元素除法/开根号计算。

## 机制特征

1. **更小的显存消耗**：相比于 AdamW 需要缓存一阶动量 $\boldsymbol{m}$ 和二阶矩 $\boldsymbol{v}$（共计 2 组模型参数量大小的额外状态），Lion 仅仅需要维护一阶动量 $\boldsymbol{m}$。在超大规模模型训练中能够节省约 $1/3$ 的优化器显存占用。
2. **极快的单步更新**：省去了除法和开根号运算，纯粹以符号和加法执行状态更新，计算速度更快。
3. **特殊的超参关系**：
   - 滑动平均衰减率默认取 $\beta_1 = 0.9, \beta_2 = 0.99$（对于 CV 任务）或 $\beta_1 = 0.95, \beta_2 = 0.98$（对于 NLP 任务）。
   - 由于更新量模长被限制为 $1$，Lion 的学习率 $\eta$ 必须较 AdamW 缩小约 10 倍以上，而对应的权重衰减率 $\lambda$ 则要放大 10 倍以上以保持等效衰减。
4. **独特的泛化机制**：符号函数运算会丢弃精确的梯度幅度并带来高频的方向方向噪声。原论文指出这种额外的噪声对于大模型逃离局部尖锐极小值、进入损失函数更平坦的泛化极值区域有正面助益。
5. **限制**：当 Batch Size 小于 64 时性能由于噪声叠加而恶化；且在大规模梯度稀疏参数层（例如 Embedding 层）中，由于符号阻断，存在显著的过度更新缺陷。
