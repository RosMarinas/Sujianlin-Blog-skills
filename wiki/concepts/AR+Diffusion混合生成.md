---
type: concept
definition: 一种多模态生成架构设计，在同一个Transformer中同时处理文本的自回归生成和图像的扩散生成。
title: AR+Diffusion混合生成
aliases:
- Autoregressive Diffusion Hybrid
- 自回归扩散混合生成
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


# AR+Diffusion混合生成

## Definition

一种多模态生成架构设计，在同一个Transformer中同时处理文本的自回归生成和图像的扩散生成。

## Training Stage

- 输入文本和加噪的图像
- 文本部分的训练目标是预测下一个token（标准自回归）
- 图像部分的训练目标是预测原图（或噪声，即扩散去噪）
- 文本和图像共享同一个Transformer主干

## Inference Stage

- 文本部分token by token递归预测，直到预测出[IMG]标记
- 然后并行输入若干个噪声向量
- 按照扩散模型的采样方式一次性生成整张图像

## Advantages

- 图像生成部分并行，不需要人为指定排序
- 在扩散模型加速采样技术下（约10 steps），生成速度可接受
- 图像部分使用连续空间生成，理论上可保持无损

## Related Works

Meta的Transfusion（2024.08）和Show-o（2024.08）与上述方案基本一致。

## Related Pages
- [[Patch输入]]
- [[连续型概率建模困难]]
- [[分离扩散模型方法]]