---
type: article_summary
title: 用变分推断统一理解生成模型（VAE、GAN、AAE、ALI）
article_id: "5716"
source_url: https://spaces.ac.cn/archives/5716
date: 2018-07-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-07-18-用变分推断统一理解生成模型-VAE-GAN-AAE-ALI.md
source_html: Data/Spaces_ac_cn/raw/articles/5716/page.html
series: []
topics:
  - "[[topic::生成模型]]"
concepts:
  - "[[concept::变分推断统一框架]]"
methods:
  - "[[method::用变分推断统一生成模型]]"
problem_patterns: []
evidence_spans:
  - ev::5716::变分推断新解
  - ev::5716::VAE
  - ev::5716::变分推断下的GAN
  - ev::5716::正则项
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-07-18-用变分推断统一理解生成模型-VAE-GAN-AAE-ALI.md
source_ids:
  - "5716"
status: draft
updated: 2026-06-11
---

## 文章核心问题

如何用变分推断的统一框架来理解VAE、GAN、AAE、ALI等看似不同的生成模型？

## 主要结论

1. 变分推断将边际KL散度转为联合KL散度KL(p(x,z)‖q(x,z))或KL(q(x,z)‖p(x,z))，VAE、GAN、AAE、ALI都可以作为变分推断的某个特例。
2. VAE是KL(p(x,z)‖q(x,z))的特例，GAN是KL(q(x,y)‖p(x,y))的特例，AAE是对偶版本的GAN，ALI是二者的融合。
3. 标准GAN的生成器loss缺少KL(q(x)‖q^o(x))正则项，导致训练不稳定，该正则项可用新旧生成样本的L2距离近似。
4. 缺少的正则项解释了为什么GAN训练需要梯度裁剪、Adam、BN等trick来稳定梯度。

## 推导结构

变分推断新解（将边际KL转为联合KL的通用框架）→ VAE和EM算法（作为框架的导出特例）→ 变分推断下的GAN（GAN作为框架特例，揭示缺失的正则项）→ GAN相关模型（AAE、ALI的框架统一）。

## 关键公式

- 变分推断核心：KL(p(x,z)‖q(x,z)) = KL(p̃(x)‖q(x)) + ∫p̃(x)KL(p(z|x)‖q(z|x))dx ≥ KL(p̃(x)‖q(x))
- VAE loss：E[-log q(x|z) + KL(p(z|x)‖q(z))]
- GAN生成器完整loss：E[-log D(G(z))] + KL(q(x)‖q^o(x)) ≈ E[-log D(G(z)) + λ‖G(z)-G^o(z)‖^2]
- GAN判别器最优：D(x) = p̃(x)/(p̃(x)+q^o(x))

## 体现的方法

- **用变分推断统一生成模型**：将变分推断的联合KL散度框架应用于VAE、GAN、AAE、ALI等生成模型，揭示各模型的内在联系和GAN缺失的正则项。

## 所属系列位置

独立文章，但于同一作者的"变分自编码器"系列（[[series::变分自编码器]]）和"能量视角下的GAN模型"系列（[[series::能量视角下的GAN模型]]）密切相关。

## 与其他文章的关系

- 与[[article::4293]]的损失函数改进思想类似（通过修改loss来改善训练）。
- 与[[article::7124]]的条件生成不直接相关，但生成模型是条件生成的基础。
- 与[[topic::LoRA微调]]的关联：LoRA的参数高效微调可视为一种"生成式知识迁移"的变分推断视角。
- 与[[method::用修正交叉熵聚焦难分样本]]都涉及到损失函数设计对模型训练稳定性的影响。

## 原文证据锚点

- `ev::5716::变分推断新解`：变分推断将边际KL转为联合KL的通用框架。
- `ev::5716::VAE`：VAE作为KL(p(x,z)‖q(x,z))特例的推导。
- `ev::5716::变分推断下的GAN`：GAN作为KL(q(x,y)‖p(x,y))特例的推导和缺失正则项。
- `ev::5716::正则项`：KL正则项的L2距离近似和实验验证。
