---
type: formula
title: RSGAN相对判别目标公式
aliases:
- RSGAN objective
source_ids:
- '6110'
evidence_spans:
- ev::6110::RSGAN目标
standard_notation:
  p: real/data distribution
  q: generated distribution
  x_r: real sample
  x_f: fake sample
  T: discriminator score
  h: convex generator for f-divergence
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
latex: \min_G \mathbb{E}_{x_r\sim p,x_f\sim q}\left[h\left(\log\frac{p(x_f)q(x_r)}{p(x_r)q(x_f)}\right)\right].
symbol_meanings:
  T: discriminator score
  h: convex generator for f-divergence
  p: real/data distribution
  q: generated distribution
  x_f: fake sample
  x_r: real sample
conditions: （待从源文章提取）
appears_in:
- '6110'
---

# RSGAN相对判别目标公式

## 概述

$$\min_G \mathbb{E}_{x_r\sim p,x_f\sim q}\left[h\left(\log\frac{p(x_f)q(x_r)}{p(x_r)q(x_f)}\right)\right].$$

RSGAN相对判别目标公式是生成对抗网络（GAN）的一个重要变体（相对GAN，简称RSGAN）中生成器的优化目标。与标准GAN仅仅依赖判别器的“记忆”来指导生成器不同，RSGAN基于图灵测试的思想，在判别真假样本时通过相对作差（$T(x_r)-T(x_f)$）直接比较真实样本和伪造样本。通过变分法求解判别器极值并代入生成器损失中可以揭示出，这个优化目标的本质是在最小化联合分布 $p(x_r)q(x_f)$ 与交换分布 $p(x_f)q(x_r)$ 之间的 $f$-散度（通过凸函数 $h$ 定义）。这意味着生成器在训练时需要同时参考真实的分布特征和自己生成的分布特征。这种将真实样本显式引入生成器优化的方式有效提升了模型的收敛速度和训练稳定性，减少了原始GAN中判别器易出现的偏置问题。
