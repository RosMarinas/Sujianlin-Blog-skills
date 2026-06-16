---
type: method
title: "Deep INFOMAX无监督学习"
aliases:
  - "Deep INFOMAX"
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-02-深度学习的互信息-无监督提取特征.md
source_ids:
  - "6024"
method_summary: "通过最大化输入和编码表示的互信息进行无监督特征提取，使用JS散度替代KL散度。"
typical_structure: |
  1. 编码器将x映射为z
  2. 最大化I(X;Z)使用JS散度
  3. 加入先验分布约束KL(p(z)||q(z))
applicability: "无监督特征学习，视觉表示学习"
tools:
  - JS散度
  - 互信息最大化
related_methods: []
examples:
  - [[article::6024]]
status: draft
updated: 2026-06-13
---

## 适用问题

无监督特征提取，即在没有标签数据的情况下学习输入$x$的有用编码表示$z$。适用于下游分类任务，因为该方法的编码旨在最大化样本区分能力而非重建能力。

## 核心变换

**输入**：原始数据$x \in X$（如图像、文本）
**输出**：编码向量$z \in Z$

最大化输入$X$与编码$Z$之间的互信息$I(X;Z)$，同时约束编码分布$p(z)$接近标准正态先验$q(z)$：
$$
\min_{p(z|x)} \left\{ -\beta \cdot I(X;Z) + \gamma \cdot \mathbb{E}_{x\sim\tilde{p}(x)}[KL(p(z|x) \| q(z))] \right\}
$$

互信息项使用JS散度替代KL散度作为有上界的度量：
$$
I(X;Z) \approx JS(p(z|x)\tilde{p}(x),\; p(z)\tilde{p}(x))
$$
通过判别器网络$T$近似计算：
$$
JS(P\|Q) = \max_{T} \left( \mathbb{E}_{x\sim p}[\log \sigma(T(x))] + \mathbb{E}_{x\sim q}[\log(1-\sigma(T(x)))] \right)
$$

## 典型步骤

1. **编码器**：将输入$x$映射为编码分布$p(z|x)$（通常假设为高斯分布，输出均值和方差）
2. **互信息估计**：构建判别器网络$T(x,z)$，区分联合分布$p(z|x)\tilde{p}(x)$与边缘乘积$p(z)\tilde{p}(x)$的样本
3. **先验约束**：计算$KL(p(z|x)\|q(z))$项（与VAE的KL项相同），约束编码空间规整
4. **联合优化**：同时优化编码器（最小化目标函数）和判别器（最大化JS散度估计）

## 直觉

好特征的核心标准不是能重建输入（如自编码器），而是能**区分不同样本**。互信息$I(X;Z)$衡量编码$z$包含了关于$x$的多少独特信息。最大化互信息使得编码器为每个样本$x$学习专属于它的$z$，使得$p(z|x)$远大于随机概率$p(z)$。

JS散度替代KL散度的原因：KL散度无上界，最大化它可能导致无穷大的结果；JS散度有上界$\frac{1}{2}\log 2$，更稳定。

先验约束$KL(p(z)\|q(z))$使编码空间规整，避免编码分布自由扩散，有利于后续的解耦特征学习和下游任务。

## 边界

- 互信息估计依赖判别器的质量，判别器训练不足时互信息项估计不准确
- JS散度是有上界的替代度量，最大化JS散度不完全等价于最大化互信息
- 先验约束使用端到端的KL散度（非Deep INFOMAX原文的对抗方式），更稳定但可能限制编码表达能力
- 与自编码器相比，该方法不需要精确重构，更适合分类任务但不适合需要生成的任务

## 例子

- 图像无监督特征提取：在多个图像数据集上，互信息最大化方法学到的特征在KNN分类中优于自编码器基线
- 随机采样KNN样本的可视化（原文Figure 1）：互信息最大化编码的KNN邻居在语义上更相似

## 证据

- ev::6024::互信息定义与变换：$I(X,Z) = \iint p(z|x)\tilde{p}(x)\log \frac{p(z|x)}{p(z)}dxdz$，揭示互信息本质是$p(z|x)\tilde{p}(x)$与$p(z)\tilde{p}(x)$的KL散度
- ev::6024::JS散度替代KL散度：JS散度有上界$\frac{1}{2}\log 2$，避免最大化无界量的风险
- ev::6024::判别器近似：JS散度的变分推断形式，通过判别器$T$最大化$\mathbb{E}[\log\sigma(T)] + \mathbb{E}[\log(1-\sigma(T))]$
- ev::6024::先验约束：端到端$KL(p(z)\|q(z))$项使编码空间规整
