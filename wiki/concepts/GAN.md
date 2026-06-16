---
type: concept
title: GAN
definition: "生成对抗网络由生成器和判别器组成，两者在对抗博弈中进行联合优化，使生成器产生逼近真实分布的数据。"
sources:
  - wiki/sources/spaces-6016-f-GAN.md
  - wiki/sources/spaces-6549-GAN架构.md
source_ids:
  - "6016"
  - "6549"
status: draft
updated: 2026-06-12
---
# 生成对抗网络 (GAN)

## Definition
生成对抗网络（Generative Adversarial Network）由生成器（Generator）和判别器（Discriminator）组成，通过min-max对抗训练使生成器学习真实数据分布。

## Core Components
- **生成器 G**: 将随机噪声 z 映射到数据空间 x = G(z)
- **判别器 D**: 区分真实样本和生成样本

## Common Variants
- Vanilla GAN: 基于JS散度
- WGAN: 基于Wasserstein距离 + Lipschitz约束
- LSGAN: 最小二乘损失
- f-GAN: 基于f散度的统一框架

## Related Methods
- [[methods/f-GAN]]
- [[methods/WGAN]]
- [[methods/O-GAN]]

## Related Sources
- [[sources/spaces-6016-f-GAN]]
- [[sources/spaces-6280-Wasserstein-WGAN]]
- [[sources/spaces-7210-Designing-GANs]]
