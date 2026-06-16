---
type: method
title: "用三角不等式指导Margin设计"
aliases:
  - "Triangle Inequality Margin Design"
  - "AM-Softmax Margin"
operation_types:
  primary: "Generalize from special cases"
  secondary:
    - "Dual / constraint rewrite"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-09-01-从三角不等式到Margin-Softmax.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-31-再谈类别不平衡问题-调节权重与魔改Loss的对比联系.md
source_ids:
  - "8656"
  - "7708"
method_summary: "从距离的三角不等式出发推导分类与排序的不等价性，得到margin必要性——margin ≈ 类平均直径。在假定距离函数满足三角不等式的前提下，自然导出AM-Softmax。对类别不平衡场景，margin可设为与先验概率有关：m_y = -τlog p(y)。"
typical_structure: |
  1. 选择距离函数d（如余弦距离或欧氏距离）。
  2. 对每个样本z和类中心c，要求d(z,c_y) + m < d(z,c_i)对所有i≠y成立。
  3. 若d满足三角不等式，margin≈类平均直径。
  4. 构造AM-Softmax Loss: log(1+∑e^{s·[cos(z,c_i)+m-cos(z,c_y)]})。
  5. 对类别不平衡，令m_y = -τlog p(y)，得Logits Adjustment形式。
applicability: 适用于用分类任务做排序/检索的场景，如人脸识别、句子相似度计算、图像检索等。
tools:
  - "三角不等式"
  - "排序不等式"
examples:
  - "spaces-8656-从三角不等式到Margin-Softmax"
problem_patterns: []
related_methods:
  - "[[用数据混合实现线性正则化]]"
evidence_spans:
  - "ev::8656::三角不等式推导margin"
  - "ev::8656::AM-Softmax导出"
status: draft
updated: 2026-06-12
---

## 适用问题

用分类任务做排序/检索的场景，如人脸识别、句子相似度计算、图像检索等。需要确保类间距离大于类内距离的度量学习问题。

## 核心变换

**输入**：样本表示$z$和类中心$c_y$的距离度量$d(z, c_y)$
**输出**：带有margin$m$的分类损失

要求对任意$i \neq y$满足：
$$
d(z, c_y) + m < d(z, c_i)
$$

在AM-Softmax中（余弦距离）：
$$
\mathcal{L} = \log\left(1 + \sum_{i \neq y} e^{s \cdot [\cos(z, c_i) + m - \cos(z, c_y)]}\right)
$$

## 典型步骤

1. **选择距离函数$d$**：通常为余弦距离或欧氏距离
2. **确定margin**：若$d$满足三角不等式，$m \approx$类平均直径（理论指导值）
3. **构造AM-Softmax**：在余弦相似度上加margin $m$，缩放因子$s$控制"尖锐度"
4. **类别不平衡调整**：设$m_y = -\tau \log p(y)$，低频类获得更大margin
5. **训练**：标准梯度下降优化

## 直觉

三角不等式 $d(a,c) \leq d(a,b) + d(b,c)$ 提供了从分类到排序的理论桥梁。分类只要求将样本分到正确类别，排序要求同类样本间距离小于异类样本间距离。三角不等式告诉我们：如果分类正确（$z$与$c_y$最近），但同类样本$z'$可能在$c_y$的另一侧，导致$d(z,z')$很大，排序效果差。加入margin迫使$z$不仅靠近$c_y$，还要远离其他$c_i$，使同类样本收缩在类中心周围。

margin的合理取值 ≈ 类平均直径：使得同类任意两个样本的距离小于到异类中心的距离。

## 边界

- 三角不等式仅保证必要条件（$m$的下界），实际$m$需实验调参
- margin过大（$m >$ 类间距离）会导致loss过大、训练困难
- 缩放因子$s$与margin$m$相互影响，大$s$需配合小$m$
- 面向检索任务设计，对纯分类任务无收益

## 例子

- 人脸识别：AM-Softmax加margin后，类间区分度显著提升
- 句子相似度：使用余弦距离加margin，语义相近句子聚拢
- 类别不平衡：$m_y = -\tau \log p(y)$，低频类margin更大，与Logit Adjustment等价

## 证据

- ev::8656::三角不等式推导margin：从三角不等式$d(a,c) \leq d(a,b) + d(b,c)$推导margin ≈ 类平均直径
- ev::8656::AM-Softmax导出：$\log(1+\sum e^{s \cdot [\cos(z,c_i)+m-\cos(z,c_y)]})$的margin形式
- ev::7708::不平衡margin：$m_y = -\tau \log p(y)$，低频类更大margin
