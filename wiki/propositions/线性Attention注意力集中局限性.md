---
type: proposition
title: 线性Attention注意力集中局限性
aliases:
  - Sparsity Limitation of Linear Attention
statement: |
  不加激活函数的极简线性 Attention 的稀疏度指标 $S(\boldsymbol{a})$ 存在一个较高的非零下限，无法随着参数模长或输入方差的增大而趋于 0，表明其在长序列中无法“集中注意力”到关键位置。
assumptions:
  - 高维 Key 向量满足各向同性高斯分布
  - 注意力权重与 Key 的内积呈线性关系
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9889
proof_route:
  - 在高斯分布 Key 假设下，化简稀疏度指标 $S(\boldsymbol{a})$ 的多维积分为一维高斯积分形式。
  - 对于 $f=\text{identical}$ 的极简线性 Attention，硬积分算出：$S(\boldsymbol{a}) = \frac{\sqrt{2/\pi}\gamma e^{-\beta^2/(2\gamma^2)} + \beta \text{erf}(\beta/(\sqrt{2}\gamma))}{\sqrt{\beta^2+\gamma^2}}$，其中 $\beta = \boldsymbol{q}\cdot\boldsymbol{\mu}$ 且 $\gamma = \sigma\Vert\boldsymbol{q}\Vert$。
  - 分析该公式在自变量趋于无穷时的极限，或者绘制函数图，其最小值有显著的非零下限（约为 0.6 级量），无法平滑衰减至零点。
  - 这证明了线性 Attention 从根本上无法产生类似于 Softmax 指数放大带来的 one-hot 极端稀疏分布，限制了其处理长文本关联的上限。
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# 线性Attention注意力集中局限性

## Statement
不加激活函数的极简线性 Attention 的稀疏度指标 $S(\boldsymbol{a})$ 存在一个较高的非零下限，无法随着参数模长或输入方差的增大而趋于 0，表明其在长序列中无法“集中注意力”到关键位置。

## Assumptions
- 高维 Key 向量满足各向同性高斯分布
- 注意力权重与 Key 的内积呈线性关系

## Proof Route
1. 在高斯分布 Key 假设下，化简稀疏度指标 $S(\boldsymbol{a})$ 的多维积分为一维高斯积分形式。
2. 对于 $f=\text{identical}$ 的极简线性 Attention，硬积分算出：$S(\boldsymbol{a}) = \frac{\sqrt{2/\pi}\gamma e^{-\beta^2/(2\gamma^2)} + \beta \text{erf}(\beta/(\sqrt{2}\gamma))}{\sqrt{\beta^2+\gamma^2}}$，其中 $\beta = \boldsymbol{q}\cdot\boldsymbol{\mu}$ 且 $\gamma = \sigma\Vert\boldsymbol{q}\Vert$。
3. 分析该公式在自变量趋于无穷时的极限，或者绘制函数图，其最小值有显著的非零下限（约为 0.6 级量），无法平滑衰减至零点。
4. 这证明了线性 Attention 从根本上无法产生类似于 Softmax 指数放大带来的 one-hot 极端稀疏分布，限制了其处理长文本关联的上限。