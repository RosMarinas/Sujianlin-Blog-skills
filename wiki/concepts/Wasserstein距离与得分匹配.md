---

type: concept
title: Wasserstein距离与得分匹配
aliases:
- Wasserstein Distance and Score Matching
- W距离与得分匹配
definition: 扩散模型的得分匹配损失构成了2-Wasserstein距离的一个上界，因此最小化得分匹配损失间接最小化了数据分布与生成分布之间的Wasserstein距离。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2023-02-14-生成扩散模型漫谈-十六-W距离-得分匹配.md
source_ids:
- '9467'
prerequisites:
- '[[得分匹配]]'
- '[[Wasserstein距离]]'
equivalent_forms:
- 条件得分匹配也是W距离的上界
series:
- '[[生成扩散模型漫谈]]'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: '2026-06-12'
---
# 得分匹配

## 定义
得分匹配（Score Matching）是一种用于估计未归一化概率密度模型参数的方法。它通过直接匹配模型得分（即概率对数的梯度 $\nabla_x \log p_\theta(x)$）和数据分布得分，避免了计算配分函数的巨大开销。

## 数学原理
模型得分函数定义为 $\boldsymbol{s}_\theta(x) = \nabla_x \log p_\theta(x)$。得分匹配的目标是最小化：
$$\mathcal{J}(\theta) = \frac{1}{2} \mathbb{E}_{p_{\text{data}}(x)} \left[ \|\boldsymbol{s}_\theta(x) - \nabla_x \log p_{\text{data}}(x)\|^2 \right]$$
通过分部积分，该目标可以化为与真实数据得分无关的等价形式：
$$\mathcal{J}(\theta) = \mathbb{E}_{p_{\text{data}}(x)} \left[ \text{tr}\left( \nabla_x \boldsymbol{s}_\theta(x) \right) + \frac{1}{2} \|\boldsymbol{s}_\theta(x)\|^2 \right]$$
