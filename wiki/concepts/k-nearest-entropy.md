---
title: k邻近熵估计
definition: '使用k邻近方法非参数估计微分熵: H(Z) ≈ d/n Σ log εk(i) + log Bd + ψ(n) - ψ(k)'
type: concept
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# k邻近熵估计

## Definition
使用k邻近方法非参数估计微分熵: H(Z) ≈ d/n Σ log ε_k(i) + log B_d + ψ(n) - ψ(k)

## Intuition
通过样本到其第k个最近邻的距离来估计局部密度，进而估计熵。

## Application
EAE模型中用于估计隐变量z的熵，避免需要知道p(z)解析形式。

## Related Sources
- [[sources/spaces-7343-EAE]]