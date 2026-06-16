---
type: article_summary
title: 为什么我们偏爱各向同性？基于最速下降的理解
article_id: 11549
source_url: https://spaces.ac.cn/archives/11549
date: 2026-01-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-01-20-为什么我们偏爱各向同性-基于最速下降的理解.md
concepts:
  - [[各向同性特征]]
propositions:
  - [[各向同性对齐参数与特征最速下降]]
methods:
  - [[最速下降双层对齐法]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-01-20-为什么我们偏爱各向同性-基于最速下降的理解.md
source_ids:
  - 11549
status: draft
updated: 2026-06-11
---

# 为什么我们偏爱各向同性？基于最速下降的理解

本文从优化层面的“最速下降”方向对准出发，解释了为什么深度学习模型中间表征应当满足各向同性（Isotropy）。

## 核心内容
- **参数与特征最速下降的冲突**：对于线性层 $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{W}$，梯度下降更新使参数沿损失下降最快方向更新。但映射到特征空间时，特征的变化量为 $\Delta \boldsymbol{Y} = -\eta \boldsymbol{X}\boldsymbol{X}^\top \frac{\partial \mathcal{L}}{\partial \boldsymbol{Y}}$。由于 Gram 矩阵 $\boldsymbol{X}\boldsymbol{X}^\top$ 的存在，特征更新方向并非特征空间的最速下降方向。
- **各向同性的作用**：当输入特征满足各向同性条件 $\boldsymbol{X}\boldsymbol{X}^\top \approx c I$ 时，特征空间的变化量与特征梯度方向平行，使得参数上的最速下降与特征层面的最速下降完美合一，大幅提高模型学习效率。
- **Muon 优化器的独特性**：对于谱范数优化器 Muon，当特征各向同性时，同样有参数谱范数最速更新等价于特征层面的谱范数最速下降，这显示了满秩正交更新在各向同性特征下的数学优越性。