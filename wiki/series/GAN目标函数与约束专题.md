---
type: series
title: GAN目标函数与约束专题
aliases: []
article_ids:
  - "6387"
  - "6240"
  - "6214"
  - "6163"
  - "6139"
  - "6110"
  - "4439"
  - "4540"
status: draft
updated: 2026-06-11
---

# GAN目标函数与约束专题

围绕GAN训练目标的构造、Lipschitz约束、对偶散度、相对判别和实现层梯度控制，补齐生成模型网络中GAN目标函数这一支。

## 文章顺序

1. [[spaces-6387-巧断梯度-单个loss实现GAN模型]] — 巧断梯度：单个loss实现GAN模型
2. [[spaces-6240-【学习清单】最近比较重要的GAN进展论文]] — 【学习清单】最近比较重要的GAN进展论文
3. [[spaces-6214-BiGAN-QP-简单清晰的编码&生成模型]] — BiGAN-QP：简单清晰的编码&生成模型
4. [[spaces-6163-不用L约束又不会梯度消失的GAN-了解一下]] — 不用L约束又不会梯度消失的GAN，了解一下？
5. [[spaces-6139-WGAN-div-一个默默无闻的WGAN填坑者]] — WGAN-div：一个默默无闻的WGAN填坑者
6. [[spaces-6110-RSGAN-对抗模型中的-图灵测试-思想]] — RSGAN：对抗模型中的“图灵测试”思想
7. [[spaces-4439-互怼的艺术-从零直达WGAN-GP]] — 互怼的艺术：从零直达WGAN-GP
8. [[spaces-4540-fashion-mnist的gan玩具]] — fashion-mnist的gan玩具

## 关键方法

- [[用对偶散度构造对抗生成目标]]
- [[梯度惩罚满足L约束]]
- [[用梯度截断合并对抗训练目标]]

## Probe entry

- `probe::gan_attention::gan_objective_path`
