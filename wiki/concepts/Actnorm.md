---
type: concept
title: Actnorm
definition: Glow模型中提出的一种均值方差缩放平移可逆层，类似于 Batch Normalization 的激活重归一化层，旨在稳定深层可逆网络的训练并支持极小 Batch 训练。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-08-26-细水长flow之RealNVP与Glow-流模型的传承与升华.md
source_ids:
  - "5807"
status: draft
updated: 2026-06-12
aliases:
  - Activation Normalization
---

# Actnorm

## 定义

Actnorm（激活归一化，Activation Normalization）是 OpenAI 在 Glow 模型中提出的一种简单平移缩放层，其前向变换公式为：
$$
\hat{z} = \frac{z - \mu}{\sigma}
$$
其中，$\mu$ 和 $\sigma$ 分别是通道维度上的可训练缩放平移向量。

## 机制特点

### 数据自适应初始化
Actnorm 的核心特点在于其参数的初始化方式：在模型训练开始时，传入第一个 Batch 的特征数据，计算该 Batch 在各通道上的均值 $\mu_{\text{init}}$ 和标准差 $\sigma_{\text{init}}$。使用这些统计量对 Actnorm 的 $\mu$ 和 $\sigma$ 进行初始化，从而确保第一个 Batch 输出特征的均值为 0，方差为 1。在此之后，$\mu$ 和 $\sigma$ 伴随整个网络通过反向传播（Backpropagation）共同迭代优化。

### 支持极小 Batch Size
Batch Normalization (BN) 在 Batch Size 非常小时（例如由于显存限制而使用 Batch Size = 1 或 2），计算的 Batch 统计量方差非常大，导致模型无法收敛。Actnorm 由于在初始化后就使用完全独立的参数代表均值和方差，不再依赖每个 Batch 的统计数据，从而可以在极小 Batch 下稳定地工作，这在训练参数量巨大的三维图像流模型时非常有用。
