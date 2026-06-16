---
type: concept
title: ELBO
aliases:
- Evidence Lower Bound
- 证据下界
- 变分下界
definition: 变分推断中用于近似难解后验分布的核心不等式：$\ln p(x) \ge \mathbb{E}_{z\sim q(z|x)}[\ln p(x|z)]
  - KL(q(z|x)\|p(z))$，其中 $q(z|x)$ 是近似后验。最大化下界等价于最小化近似后验与真实后验的KL散度。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-03-28-变分自编码器-二-从贝叶斯观点出发.md
- Data/Spaces_ac_cn/markdown/Big-Data/2018-03-18-变分自编码器-一-原来是这么一回事.md
source_ids:
- '5343'
- '5253'
prerequisites:
- '[[后验分布假设]]'
equivalent_forms: []
direct_consequences:
- VAE的标准损失函数可直接从ELBO推导得出
related_formulas: []
related_methods:
- '[[VAE联合分布最小化]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::5343::直面联合分布
- ev::5253::分布标准化
status: draft
updated: '2026-06-12'
---

# ELBO (Evidence Lower Bound)

## 定义

ELBO是变分推断的核心工具。对于生成模型，直接最大化对数边际似然 $\ln p(x)=\ln\int p(x|z)p(z)dz$ 通常因积分难解而不可行。ELBO提供了一种可优化的替代目标：

$$\ln p(x) \ge \mathbb{E}_{z\sim q(z|x)}[\ln p(x|z)] - KL(q(z|x)\|p(z))$$

其中 $q(z|x)$ 是近似后验分布。

## 在VAE中的应用

VAE中，ELBO与联合分布KL散度最小化等价的。苏剑林在其VAE系列第二篇中论证了从 $KL(p(x,z)\|q(x,z))$ 出发的推导方式比ELBO更加直接，但最终得到的损失函数形式一致：

$$\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[\mathbb{E}_{z\sim p(z|x)}[-\ln q(x|z)] + KL(p(z|x)\|q(z))]$$

## 与联合分布KL的关系

- ELBO视角：最大化 $\ln p(x)$ 的下界
- 联合分布KL视角：最小化 $p(x,z)$ 与 $q(x,z)$ 的距离
- 两者在数学上等价，仅是推导路径不同