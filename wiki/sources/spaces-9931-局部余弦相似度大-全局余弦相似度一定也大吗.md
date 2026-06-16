---
type: article_summary
title: 局部余弦相似度大，全局余弦相似度一定也大吗？
article_id: "9931"
source_url: https://spaces.ac.cn/archives/9931
date: 2024-01-09
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-01-09-局部余弦相似度大-全局余弦相似度一定也大吗.md
series: []
topics:
  - "[[优化器稳定性与自适应机制]]"
concepts:
  - "[[辛普森悖论]]"
methods: []
problem_patterns: []
evidence_spans:
  - ev::9931::局部与全局余弦问题背景
  - ev::9931::局部相似大全局不一定大分析
  - ev::9931::余弦相似度上界证明
  - ev::9931::辛普森悖论与皮尔逊相关系数
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-01-09-局部余弦相似度大-全局余弦相似度一定也大吗.md
source_ids:
  - "9931"
status: draft
updated: 2026-06-12
---

# 局部余弦相似度大，全局余弦相似度一定也大吗？

## 文章核心问题

在高维向量（如大模型全网权重）被拆分为若干个局部子空间（如逐层、逐参数矩阵）的情况下，如果每个局部子向量的余弦相似度都大于某个阈值，那么合并后的全局余弦相似度是否也有下界保证；这一结论如何与“辛普森悖论”相联系。

## 主要结论

- **局部余弦大全局不一定大**：答案是否定的。即使所有局部子向量的余弦相似度都不小于某阈值 $\lambda > 0$，全局余弦相似度依然可以无限趋近于 0（无法通过局部余弦给出大于 0 的下界）。
- **全局余弦上界定理**：在局部余弦相似度为正的前提下，全局余弦相似度的上界不超过局部余弦相似度的最大值，即：
  $$
  \cos(\boldsymbol{x},\boldsymbol{y})\leq \max\big\{\cos(\boldsymbol{x}_1,\boldsymbol{y}_1),\cos(\boldsymbol{x}_2,\boldsymbol{y}_2)\big\}
  $$
- **辛普森悖论的代数本质**：皮尔逊相关系数（Pearson Correlation Coefficient）本质上就是去均值后的向量余弦相似度。这解释了为什么在多组独立样本中表现为强正相关的数据，在全局合并后可能变成线性无关甚至负相关。

## 推导结构

1. **问题引入**：从优化器更新步长 $\boldsymbol{u}_t$ 与梯度 $\boldsymbol{g}_t$ 在逐层（局部）和全模型（全局）下的方向一致性分析出发，指出了局部截断全局却变小的意外发现。
2. **给出反例**：在 2 维情形下，通过 $\boldsymbol{x}=(1,1)$ 与 $\boldsymbol{y}=(1,2)$ 的一维分量分解（局部余弦全为 1，全局小于 1）简单否定了局部等价性。
3. **极限量化分析**：在 $\boldsymbol{x}=[\boldsymbol{x}_1, \boldsymbol{x}_2], \boldsymbol{y}=[\boldsymbol{y}_1, \boldsymbol{y}_2]$ 拆分下，通过控制子向量的范数极限 $\Vert\boldsymbol{x}_1\Vert \to 0$ 和 $\Vert\boldsymbol{y}_2\Vert \to 0$，证明全局余弦相似度可以被任意压缩至接近 0。
4. **证明上界定理**：基于柯西不等式形式，证明全局余弦小于或等于局部最大值。
5. **联系辛普森悖论**：将皮尔逊相关系数公式映射为去均值向量的余弦，并给出斜率正负反转的几何物理图像。

## 关键公式

- **高维子向量余弦展开公式**：
  $$
  \cos(\boldsymbol{x},\boldsymbol{y}) = \frac{\cos(\boldsymbol{x}_1, \boldsymbol{y}_1) \Vert\boldsymbol{x}_1\Vert \Vert\boldsymbol{y}_1\Vert+ \cos(\boldsymbol{x}_2, \boldsymbol{y}_2)\Vert\boldsymbol{x}_2\Vert \Vert\boldsymbol{y}_2\Vert}{\sqrt{\Vert\boldsymbol{x}_1\Vert^2 + \Vert\boldsymbol{x}_2\Vert^2} \sqrt{\Vert\boldsymbol{y}_1\Vert^2 + \Vert\boldsymbol{y}_2\Vert^2}}
  $$
- **皮尔逊相关系数的余弦表示**：
  $$
  r = \cos(\boldsymbol{x}-\bar{x},\boldsymbol{y}-\bar{y})
  $$

## 体现的方法

- **多维向量的局部-全局尺度分析**：通过将高维向量在正交子空间上投影并分析各分量模长对整体余弦的权值分配，探讨整体物理指标与分块指标的不一致性。

## 所属系列位置

独立研究文章，属于高维概率空间与优化分析中的数学基础探讨。

## 与其他文章的关系

- 从优化器一致性（更新向量与梯度的夹角）出发，背景关联到所有自适应优化器的更新规律（如 [Lion](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) 和 [Tiger](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Tiger优化器.md)）。

## 原文证据锚点

- **ev::9931::局部与全局余弦问题背景**: 第22-37行，说明了由于对优化器参数更新量与梯度夹角的局部和全局统计引起夹角不一致的数学背景。
- **ev::9931::局部相似大全局不一定大分析**: 第40-55行，通过一维反例和极限范数分析，计算并证明了全局下界为 0 的性质。
- **ev::9931::余弦相似度上界证明**: 第56-67行，推导并证明了全局相似度被局部最大相似度限制的定理。
- **ev::9931::辛普森悖论与皮尔逊相关系数**: 第70-87行，建立了皮尔逊相关系数作为去均值余弦的数学等价性，并结合几何图像分析了“辛普森悖论”中相关系数正负逆反的机制。
