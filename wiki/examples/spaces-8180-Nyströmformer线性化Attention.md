---
type: example
title: spaces-8180 Nyströmformer线性化Attention
source_ids:
- '8180'
evidence_spans:
- ev::8180::三矩阵近似
- ev::8180::伪逆近似
notation_mapping:
  A: Attention matrix
  Q: boldsymbol Q
  K: boldsymbol K
  V: boldsymbol V
  tilde_Q: tilde boldsymbol Q
  tilde_K: tilde boldsymbol K
  dagger: dagger
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
article_id: '8180'
article: '[[spaces-8180-Nyströmformer-基于矩阵分解的线性化Attention方案]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# spaces-8180 Nyströmformer线性化Attention

源文中通过Q,K的聚类中心构造三个小矩阵乘积，并用伪逆校正中间矩阵，使标准Attention近似可按线性Attention的顺序计算。

标准的Scaled-Dot Attention写成矩阵形式为 $Attention(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = softmax\left(\boldsymbol{Q}\boldsymbol{K}^{\top}\right)\boldsymbol{V}$，其中 $\boldsymbol{Q}, \boldsymbol{K}, \boldsymbol{V}\in\mathbb{R}^{n\times d}$。在此计算中，由于必须先计算出 $\boldsymbol{Q}\boldsymbol{K}^{\top}$ 才能执行softmax操作（此处softmax是对矩阵的第二个维度做归一化），这导致 $n^2$ 个向量内积的计算无法利用矩阵乘法结合律，进而使得全局的时间和空间复杂度均达到 $\mathcal{O}(n^2)$。

为了打破这一瓶颈，常规的线性Attention比较朴素的做法是通过非负激活函数 $\phi, \varphi$ 将计算表示为两矩阵相乘 $\left(\phi(\boldsymbol{Q})\varphi(\boldsymbol{K})^{\top}\right)\boldsymbol{V}=\phi(\boldsymbol{Q})\left(\varphi(\boldsymbol{K})^{\top}\boldsymbol{V}\right)$，从而优先计算后面两个矩阵的乘法，将整体复杂度降至 $\mathcal{O}(n)$。

在此基础上，以往的方法如Google提出的Performer模型，试图通过随机投影来找到低维矩阵 $\tilde{\boldsymbol{Q}},\tilde{\boldsymbol{K}}\in\mathbb{R}^{n\times m}$ 使得 softmax 中的核心项 $e^{\boldsymbol{Q}\boldsymbol{K}^{\top}}\approx \tilde{\boldsymbol{Q}}\tilde{\boldsymbol{K}}^{\top}$，以此将标准Attention近似为线性Attention。这种做法在本质上借用了SVM与核函数的思想（即低维空间中两个向量的核函数可以映射为高维空间中两个向量的内积），并且可以与LSH（Locality Sensitive Hashing）相联系。

Nyströmformer则从另一个角度实现了标准Attention的线性化。它引入了基于矩阵分解的Nyström方法，创造性地将注意力矩阵表示为三个矩阵相乘的形式。具体而言，Nyströmformer以双重softmax结构（即 $\left(softmax(\boldsymbol{Q}) softmax\left(\boldsymbol{K}^{\top}\right)\right)\boldsymbol{V}$）作为初步探索的出发点，通过在低维空间构造特征表示，结合聚类中心并利用伪逆操作校正中间矩阵，最终在满足线性乘法结合律的前提下，实现了对原始完整 $\mathcal{O}(n^2)$ 标准Attention行为的高保真近似。
