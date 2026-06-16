---
title: Wasserstein距离
definition: '基于最优传输成本: W[p,q] = inf{γ∈Π[p,q]} ∬ γ(x,y) c(x,y) dx dy'
type: concept
status: draft
updated: '2026-06-12'
source_ids:
- '7388'
- '8512'
- '9797'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
- Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
- Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
---


# Wasserstein距离

## Definition
基于最优传输成本: W[p,q] = inf_{γ∈Π[p,q]} ∬ γ(x,y) c(x,y) dx dy

## Properties
- 对任意两个分布（哪怕没有交集）都有良好定义
- 对偶形式: W₁[p,q] = max_{f, ||f||_L≤1} E_p[f(x)] - E_q[f(x)]
- Lipschitz约束: ||f||_L ≤ 1

## Role in GAN
WGAN使用Wasserstein距离替代f散度，理论上解决梯度消失问题。

## Related Methods
- [[methods/WGAN]]
- [[sources/spaces-6280-Wasserstein-WGAN]]