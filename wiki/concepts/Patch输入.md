---
type: concept
definition: Patch输入是将原始图像的像素数组直接分割为固定大小的Patch块，然后展平投影到模型隐层维度作为输入。区别于使用预训练Encoder提取特征的方式。
title: Patch输入
aliases:
- Patch Input
- Patchify
- Image Patch Embedding
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-02-21-闭门造车-之多模态思路浅谈-一-无损输入.md
- Data/Spaces_ac_cn/markdown/Big-Data/2024-07-08-闭门造车-之多模态思路浅谈-二-自回归.md
source_ids:
- '9984'
- '10197'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred.
status: draft
updated: '2026-06-12'
---


# Patch输入

## Definition

Patch输入是将原始图像的像素数组直接分割为固定大小的Patch块，然后展平投影到模型隐层维度作为输入。区别于使用预训练Encoder提取特征的方式。

## Broad Definition

广义的Patchify可以泛指一切将图像从 $w\times h\times 3$ 的数组变成 $s\times t\times d$（其中 $s < w, t < h$）的方案，包括：
- 狭义的像素Patch变形和转置
- VAE/LDM的Encoder编码为Latent特征
- VQ-Tokenizer将图像变为离散ID

## Advantages

- **无损性**：直接输入原始像素，避免压缩损失
- **特征不孤立**：当需要同时输入两幅图像I1,I2时，直接在Patch层面输入可避免Encoder造成的特征孤立

## Challenges

- 缺乏CNN的归纳偏置，需要更多训练步数才能收敛
- 主流做法（DiT、Stable Diffusion）仍使用LDM编码器降维后的特征，直接Patch输入的做法尚未成为主流

## Related Pages
- [[连续型概率建模困难]]
- [[图像Tokenzier]]
- [[AR+Diffusion混合生成]]