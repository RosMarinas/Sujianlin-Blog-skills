---
type: formula
title: WGAN-div目标公式
aliases:
- Wasserstein divergence objective
source_ids:
- '6139'
evidence_spans:
- ev::6139::W散度目标
- ev::6139::WGAN-div训练
standard_notation:
  p: real/data distribution
  q: generated distribution
  r: auxiliary sampling distribution
  T: critic function
  k: gradient penalty coefficient
  p_power: gradient norm power
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
latex: T=\arg\max_T\mathbb{E}_{x\sim p}[T(x)]-\mathbb{E}_{x\sim q}[T(x)]-k\mathbb{E}_{x\sim
  r}\|
  \nabla T(x)\|^p.
symbol_meanings:
  T: critic function
  k: gradient penalty coefficient
  p: real/data distribution
  p_power: gradient norm power
  q: generated distribution
  r: auxiliary sampling distribution
conditions: （待从源文章提取）
appears_in:
- '6139'
---

# WGAN-div目标公式

## 概述

$$T=\arg\max_T\mathbb{E}_{x\sim p}[T(x)]-\mathbb{E}_{x\sim q}[T(x)]-k\mathbb{E}_{x\sim r}\|
abla T(x)\|^p.$$

WGAN-div目标公式是在生成对抗网络中引入 Wasserstein Divergence（W散度）的核心判别器优化目标。它试图解决 WGAN 中对判别器施加 Lipschitz 约束（L约束）时引发的困难。与 WGAN-GP 采用固定梯度范数为 1 的经验性惩罚不同，WGAN-div 直接将判别器梯度的 $p$ 次幂作为正则项减去，无需严格限制梯度趋向某一个特定常数（即不需要强制 $\|
abla T\| \approx 1$）。理论证明这构成了一个严格的对称散度，从而保证了当判别器以此为目标最大化时，确实是在衡量真实数据分布 $p$ 和生成分布 $q$ 之间的差异。超参数 $k>0$ 控制正则化强度，$p>1$ 为范数幂次（实验表明 $k=2, p=6$ 时效果最佳）。同时，采样分布 $r$ 的选择极其宽松，即便直接混合真实与虚假样本而无需随机插值，也能取得稳定的训练效果。
