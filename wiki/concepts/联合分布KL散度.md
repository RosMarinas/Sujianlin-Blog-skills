---
type: concept
title: 联合分布KL散度
aliases:
- Joint Distribution KL Minimization
- 联合分布近似
definition: VAE训练的核心优化目标——直接最小化数据确定的联合分布 $p(x,z)=\tilde{p}(x)p(z|x)$ 与模型联合分布 $q(x,z)=q(x|z)q(z)$
  之间的KL散度 $KL(p(x,z)\|q(x,z))$，这比传统ELBO推导更为直接。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-03-28-变分自编码器-二-从贝叶斯观点出发.md
- Data/Spaces_ac_cn/markdown/Big-Data/2018-09-17-变分自编码器-四-一步到位的聚类方案.md
source_ids:
- '5343'
- '5887'
prerequisites:
- '[[后验分布假设]]'
equivalent_forms:
- VAE标准损失函数 $\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[\mathbb{E}_{z\sim p(z|x)}[-\ln
  q(x|z)] + KL(p(z|x)\|q(z))]$
direct_consequences: []
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

# 联合分布KL散度 (Joint Distribution KL Minimization)

## 核心思想

传统的VAE推导从最大化下界（ELBO）出发，聚焦于后验分布 $p(z|x)$ 的近似。苏剑林在其VAE系列中提出了一种更直接的推导方式：直接定义两个联合分布，让它们相互接近。

$$p(x,z) = \tilde{p}(x)p(z|x) \quad \text{(由数据和编码器决定的真实联合分布)}$$
$$q(x,z) = q(x|z)q(z) \quad \text{(由解码器和先验决定的模型联合分布)}$$

通过最小化 $KL(p(x,z)\|q(x,z))$，两个分布相互靠近。

## 优势

1. **推导更直接**：无需经过ELBO的变分变换，直接展开KL散度即可得到标准VAE损失
2. **符合直觉**：既然目标是让模型分布 $q(x,z)$ 逼近数据分布 $p(x,z)$，直接度量其差异是最自然的
3. **可扩展性强**：这一框架可以轻松扩展到更复杂的隐变量结构（如聚类VAE中引入离散变量 $y$）

## 数学展开

$KL(p(x,z)\|q(x,z)) = \mathbb{E}_{x\sim\tilde{p}(x)}[\int p(z|x)\ln\frac{\tilde{p}(x)p(z|x)}{q(x|z)q(z)}dz]$

分离常数项后得到：
$\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[\mathbb{E}_{z\sim p(z|x)}[-\ln q(x|z)] + KL(p(z|x)\|q(z))]$

## 与传统ELBO的关系

二者的最终损失函数形式一致。区别在于推导路径：联合分布KL从"让两个联合分布接近"出发，ELBO从"最大化边际似然的变分下界"出发。联合分布KL推导得到的 $\mathcal{L}$ 有下界 $-\mathbb{E}_{x\sim\tilde{p}(x)}[\ln\tilde{p}(x)]$，且 $\mathcal{L}$ 与该下界的接近程度可衡量生成器的相对质量。