---
type: article_summary
title: "闭门造车之多模态思路浅谈（一）：无损输入"
article_id: "9984"
source_url: https://spaces.ac.cn/archives/9984
date: 2024-02-21
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-02-21-闭门造车-之多模态思路浅谈-一-无损输入.md
series: [闭门造车之多模态思路浅谈]
topics: [多模态, 图像生成, 扩散模型, AR+Diffusion]
concepts: [连续型概率建模困难, 图像Tokenzier, 压缩损失, Patch输入, AR+Diffusion混合生成]
methods: [Patchify]
problem_patterns: [多模态生成架构设计, 连续型变量概率建模]
evidence_spans:
  - 9984-问题背景
  - 9984-离散之路
  - 9984-压缩损失
  - 9984-扩散模型
  - 9984-Patch输入
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-02-21-闭门造车-之多模态思路浅谈-一-无损输入.md
source_ids:
  - "9984"
status: draft
updated: 2026-06-10
---

## 文章核心问题

多模态LLM中，图像应该如何输入和生成？在保证无损输入的前提下，如何设计多模态生成架构？

## 主要结论

1. 图像生成的本质困难在于连续型变量的概率建模——神经网络是函数的万能拟合器，但不是概率密度的万能拟合器。
2. 离散化方案（VQ-VAE/VQ-GAN）存在严重信息损失，通过信息熵计算证明：对于256x256图像压缩到16x16 tokens，需要codebook大小达到2^144才可能无损，远非当前实际codebook规模可比。
3. 无条件压缩的前提下，唯一可行的生成方案是回归连续空间——Flow或扩散模型。
4. 提出AR+Diffusion混合生成方案：文本部分预测下一个token，图像部分用扩散模型去噪生成，两者在同一个Transformer中训练。
5. 直接以原始图像Patch作为输入的Transformer扩散模型可行（实验验证），但需要更多训练步数收敛。

## 推导结构

- 文本生成 vs 图像生成对比 → 连续型概率建模困难
- 离散化方案（VQ-VAE）→ 信息熵定量分析 → 证明信息损失不可避免
- AR+Diffusion混合方案 → 训练与推理流程设计
- Patch输入扩散模型实验验证 → DiT/U-ViT文献对比
