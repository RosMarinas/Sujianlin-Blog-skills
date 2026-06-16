---
type: concept
title: R-Drop
definition: "一种通过两次随机Dropout生成同一输入的两个不同预测，并使用双向KL散度来约束两者一致性以提高模型泛化性能的正则化技术。"
sources:
  - wiki/sources/spaces-8496-R-Drop.md
source_ids:
  - "8496"
aliases: [R-Drop, Regularized Dropout, 正则化Dropout]
tags: [regularization, dropout, supervised-learning, semi-supervised]
related_concepts: [Dropout, SimCSE, 虚拟对抗训练]
related_sources: [spaces-8496-R-Drop]
status: draft
updated: 2026-06-12
---
## Definition

R-Drop（Regularized Dropout，2021）将"Dropout两次"的思想推广到有监督任务。通过对同一输入做两次Dropout得到两个不同的模型输出，用KL散度约束两者一致性，作为正则化项。

## Mathematical Formulation

对于分类任务，训练数据 $\{x_i, y_i\}$，模型 $P_\theta(y|x)$，两次Dropout输出分别为 $P_\theta^{(1)}(y|x)$ 和 $P_\theta^{(2)}(y|x)$。

损失函数：
$$
\mathcal{L}_i = \underbrace{-\log P_\theta^{(1)}(y_i|x_i) - \log P_\theta^{(2)}(y_i|x_i)}_{\text{交叉熵项}} + \alpha \underbrace{\frac{1}{2}\big[\text{KL}(P_\theta^{(2)}\|P_\theta^{(1)}) + \text{KL}(P_\theta^{(1)}\|P_\theta^{(2)})\big]}_{\text{一致性正则项}}
$$

一般形式（非分类任务）：
$$
\mathcal{L}_i = \mathcal{D}(y_i, f_\theta^{(1)}(x_i)) + \mathcal{D}(y_i, f_\theta^{(2)}(x_i)) + \frac{\alpha}{2}\big[\mathcal{D}(f_\theta^{(2)}, f_\theta^{(1)}) + \mathcal{D}(f_\theta^{(1)}, f_\theta^{(2)})\big]
$$

## Theoretical Insights

### 1. Training-Prediction Consistency
Dropout的最优预测是模型平均 $\mathbb{E}_\varepsilon[f_\theta(x,\varepsilon)]$，实践中使用权重平均 $f_\theta(x)$（关闭Dropout）。R-Drop强化了不同Dropout下输出的一致性，使两者更接近。

### 2. Model Continuity
类似虚拟对抗训练（VAT），R-Drop增强模型对扰动的鲁棒性。区别在于：VAT将扰动加在输入层并通过对抗优化，R-Drop的扰动可施加到模型每一层且是随机的。

### 3. Non-target Class Regularization
交叉熵只关注目标类得分大于非目标类，不关心非目标类的分布。R-Drop的KL散度项迫使所有类别的得分在不同Dropout下一致，提供了额外的正则化。

## Experimental Results

- **GLUE基准**：各NLP任务均取得明显提升
- **机器翻译**："Transformer + R-Drop"超越更复杂的方法
- **中文分类**：IFLYTEK 62.69%，TNEWS 57.51%，媲美对抗训练
- **文本生成**：CSL标题生成，Rouge-L 65.51，BLEU 47.82
- **半监督学习**：效果不逊于VAT，且实现更简单、速度更快

## Hyperparameters

- $\alpha \in [1,5]$ (推荐 $\alpha=4$)
- Dropout概率：推荐 0.3

## References

- 苏剑林. "又是Dropout两次！这次它做到了有监督任务的SOTA". 科学空间, 2021. [spaces-8496]
- Liang et al., "R-Drop: Regularized Dropout for Neural Networks", NeurIPS 2021.
