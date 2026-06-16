---
type: concept
title: 学习率-Batch Size尺度律
aliases: null
definition: 学习率与 Batch Size 的尺度律描述最优学习率、单步损失下降和训练步数如何随批量大小变化。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md
source_ids:
- '11260'
- '11280'
- '11285'
- '11301'
related_formulas:
- '[[二阶近似最优学习率公式]]'
related_methods:
- '[[用平均场近似替代复杂期望计算]]'
series:
- '[[重新思考学习率与Batch Size]]'
evidence_spans:
- ev::11260::热身练习
- ev::11260::数据效率
status: draft
updated: '2026-06-12'
---
# 学习率-Batch Size尺度律

## 定义

学习率与 Batch Size 的尺度律描述最优学习率、单步损失下降和训练步数如何随批量大小变化。

## 在本系列中的作用

该概念用于把优化器更新规则、采样噪声和 Batch Size 关系连接起来，避免只停留在经验调参描述。

## 证据

- `ev::11260::热身练习`
- `ev::11260::数据效率`

首先回顾一下之前的分析方法。在[《当Batch Size增大时，学习率该如何随之变化？》](/archives/10542)中，我们介绍了多种分析学习率与Batch Size规律的思路，其中OpenAI在[《An Empirical Model of Large-Batch Training》](https://papers.cool/arxiv/1812.06162)提出的二阶近似分析占了主要篇幅，本文也是沿用同样的思路。

接着需要引入一些记号。设损失函数为$\mathcal{L}(\boldsymbol{w})$，$\boldsymbol{w}\in\mathbb{R}^N$是参数向量，$\boldsymbol{g}$是它的梯度。注意理想的损失函数是在全体训练样本上算的期望，但实际我们只能采样一个Batch来算，这导致梯度也带有随机性，我们将单个样本的梯度记为$\tilde{\boldsymbol{g}}$，它的均值就是$\boldsymbol{g}$，而协方差矩阵记为$\boldsymbol{\Sigma}$；当Batch Size为$B$时，梯度记为$\tilde{\boldsymbol{g}}_B$，它的均值还是$\boldsymbol{g}$，但协方差矩阵变为$\boldsymbol{\Sigma}/B$。

进一步地，设当前学习率为$\eta$，更新向量为$\tilde{\boldsymbol{\varphi}}_B$，那么更新后的损失函数将是

沿着上文的记号，对于SignSGD我们有$\tilde{\boldsymbol{\varphi}}_B=\mathop{\text{sign}}(\tilde{\boldsymbol{g}}_B)$，我们需要先计算$\mathbb{E}[\tilde{\boldsymbol{\varphi}}_B]$和$\mathbb{E}[\tilde{\boldsymbol{\varphi}}_B\tilde{\boldsymbol{\varphi}}_B^{\top}]$，继而可以算出

$$

\eta^* \approx \frac{\mathbb{E}[\tilde{\boldsymbol{\varphi}}_B]^{\top}\boldsymbol{g}}{\mathop{\text{tr}}(\mathbb{E}[\tilde{\boldsymbol{\varphi}}_B\tilde{\boldsymbol{\varphi}}_B^{\top}]\boldsymbol{H})}\label{eq:eta-opt}

众所周知，[Muon](/archives/10592)的主要特点就是非Element-wise的更新规则，所以之前在[《当Batch Size增大时，学习率该如何随之变化？》](/archives/10542)和[《Adam的epsilon如何影响学习率的Scaling Law？》](/archives/10563)的Element-wise的计算方法将完全不可用。但幸运的是，上篇文章介绍的平均场依然好使，只需要稍微调整一下细节。

我们先引入一些记号。设损失函数为$\mathcal{L}(\boldsymbol{W})$，$\boldsymbol{W}\in\mathbb{R}^{n\times m}$是矩阵向量（设$n\geq m$），$\boldsymbol{G}$是它的梯度，单个样本的梯度记为$\tilde{\boldsymbol{G}}$，它的均值就是$\boldsymbol{G}$，而方差为$\sigma^2$；当Batch Size为$B$时，梯度记为$\tilde{\boldsymbol{G}}_B$，它的均值还是$\boldsymbol{G}$，但方差变为$\sigma^2/B$。注意，这里的方差只是一个标量$\sigma^2$，并不像之前那样考虑了完整的协方差矩阵。

之所以这样简化，最核心的原因是这里的随机变量本身就已经是一个矩阵，那么它对应的协方差矩阵实际上已经是一个4阶张量，这讨论起来比较麻烦。那么简化为单个标量会严重损失准确性吗？其实不会，前两篇文章我们虽然考虑了完整的协方差矩阵$\boldsymbol{\Sigma}$，但仔细观察就会发现最后结果只依赖于$\mathop{\text{tr}}(\boldsymbol{\Sigma})$，这跟开始就将它简化为标量是等价的。

从Adam的视角看，SignSGD对应$\beta_1=\beta_2=0$这个特例，或者对应于Adam的第一步更新量（不管$\beta_1,\beta_2$如何）。因此，我们认为它跟Adam肯定有一些共性，能够捕捉到一些通用的规律。

但是，它们之间也有一些明显的差异。比较典型的就是Update RMS的差异，SignSGD总是1，但Adam往往明显小于1；还有，Adam看上去更贴近SGD，它更像是SignSGD和SGD的一个中间版本。一开始，笔者以为这是Adam分母中的$\epsilon$导致的差异，所以在[《Adam的epsilon如何影响学习率的Scaling Law？》](/archives/10563)还特意计算了带$\epsilon$的SoftSignSGD。

后来，我们在[《为什么Adam的Update RMS是0.2？》](/archives/11267)从模拟和理论两方面估计了Adam的Update RMS，其实平均场近似的估计结果为$\sqrt{\frac{1-\beta_1}{1+\beta_1}}$，并且验证了它跟模拟结果和实际实验都很吻合。这个结果显式地依赖于$\beta_1$，所以很明显，它将我们的思考方向引向动量。
