---
type: proposition
title: 随机Softmax梯度近似性
aliases: []
statement: 随机 Softmax 损失的梯度是由正确标签的梯度与采样子集中各个标签的梯度以子集内部 Softmax 概率为权重的加权和构成的，这在数学期望上是全局 Softmax 交叉熵梯度的无偏或强近似估计。
assumptions: ["随机采样负样本子集", "在子集上使用标准的交叉熵损失函数进行更新"]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md
source_ids:
  - '4402'
proof_route: |
  1. 计算 Random Softmax Loss 关于预测 logit $z_i$ 的梯度：$\nabla L = -\nabla z_t + \sum_{i \in \mathcal{S}} P_{\mathcal{S}}(i) \nabla z_i$，其中 $P_{\mathcal{S}}(i)$ 是在采样子集 $\mathcal{S}$ 内算出的 Softmax 概率。
  2. 全局 Softmax 交叉熵的真实梯度为 $\nabla L_{true} = -\nabla z_t + \sum_{j=1}^n P_{global}(j) \nabla z_j = -\nabla z_t + \mathbb{E}[\nabla z_j]$。
  3. 采样子集中的权重 $P_{\mathcal{S}}(i)$ 通过将求和范围限定在随机采样的负样本子集，自然实现了对真实期望项 $\mathbb{E}[\nabla z_j]$ 的蒙特卡洛均值估计，避免了计算全部 $n$ 个类别的配分函数 $Z$。
evidence_spans: ["ev::4402::随机损失"]
status: draft
updated: 2026-06-11
---

# 随机Softmax梯度近似性

该命题证明了 Random Softmax Loss 在理论上的自洽性，使其成为一种高效的多分类优化算法。
