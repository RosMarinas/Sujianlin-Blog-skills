---
type: concept
title: WGAN
aliases:
- Wasserstein GAN
definition: 使用Wasserstein距离作为优化目标的GAN，要求判别器满足Lipschitz约束
standard_notation: W(P_r,P_g)=sup_{|f|_L=1} E_{x~P_r}[f(x)]-E_{x~P_g}[f(x)]
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
- Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
source_ids:
- '6051'
- '8757'
related_methods:
- - 谱归一化满足L约束
- - 梯度惩罚满足L约束
- - 梯度归一化满足L约束
evidence_spans: []
series: []
status: draft
updated: '2026-06-12'
---

# WGAN

## 定义

使用Wasserstein距离作为优化目标的GAN，要求判别器满足Lipschitz约束

## 激活场景

WGAN 用于把 GAN 的判别器目标改写为 Wasserstein 距离的对偶形式。源文强调，在普通监督模型中 Lipschitz 约束可能只是提升泛化的附加条件，但在 WGAN 判别器里是必不可少的关键步骤，因为优化目标本身是在满足 L 约束的函数集合中取上确界。

## 关键关系

源文给出的形式是
$$
W(P_r,P_g)=\sup_{|f|_L=1}\mathbb{E}_{x\sim P_r}[f(x)]-\mathbb{E}_{x\sim P_g}[f(x)].
$$
其中 $P_r$ 是真实分布，$P_g$ 是生成分布，$|f|_L=1$ 表示判别器函数满足 1-Lipschitz 条件。实现难点因此转化为如何让判别器满足 $\Vert D\Vert_L\le 1$：源文讨论了参数裁剪、梯度惩罚、谱归一化以及后续的梯度归一化方案。

## 标准符号

W(P_r,P_g)=sup_{|f|_L=1} E_{x~P_r}[f(x)]-E_{x~P_g}[f(x)]

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md`
