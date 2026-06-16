---
type: article_summary
title: 生成扩散模型漫谈（二十二）：信噪比与大图生成（上）
article_id: "10047"
source_url: https://spaces.ac.cn/archives/10047
date: 2024-04-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-04-08-生成扩散模型漫谈-二十二-信噪比与大图生成-上.md
series: [生成扩散模型漫谈]
concepts: [信噪比感知噪声调度, 多尺度损失]
methods: [信噪比对齐调度迁移]
evidence_spans:
  - 10047-SNR分析
  - 10047-向低看齐
  - 10047-架构拓展
  - 10047-多尺度Loss
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-04-08-生成扩散模型漫谈-二十二-信噪比与大图生成-上.md
source_ids:
  - "10047"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文通过信噪比（SNR）视角分析高分辨率图像在像素空间直接训练的困难，提出SNR对齐的噪声调度迁移、高效架构扩展和多尺度损失三项技术，使像素空间扩散模型成功训练到1024x1024分辨率。

## 核心问题

LDM（Latent Diffusion Model）通过将图像编码到隐空间来实现高分辨率生成，但编码过程是有损的。能否直接在像素空间训练高分辨率扩散模型？直接套用低分辨率配置会遇到什么问题？

## 关键结论

1. LDM的成功归因于"降维+正则"降低隐空间信息量，以及Perceptual Loss保证FID几乎无损；但隐空间有损编码会丢失局部细节。
2. 高分辨率图像在相同噪声方差下信噪比比低分辨率图像高 $s^2$ 倍（因平均Pooling降低噪声方差），这使得去噪任务看似更简单——但实际生成任务更难，导致学习效率低下。
3. 通过SNR对齐，可以将低分辨率调好的噪声调度迁移到高分辨率：$\frac{(\bar{\alpha}_t^{w \times h})^2}{(\bar{\beta}_t^{w \times h})^2} \times s^2 = \frac{(\bar{\alpha}_t^{w/s \times h/s})^2}{(\bar{\beta}_t^{w/s \times h/s})^2}$。
4. 架构扩展应将参数集中于最低分辨率（16x16）处，而非平均分配给所有分辨率block。

## 核心推导

信噪比定义为 $SNR(t) = \bar{\alpha}_t^2 / \bar{\beta}_t^2$。对 $w \times h$ 图像进行 $s \times s$ 平均Pooling下采样到 $w/s \times h/s$ 时，噪声项方差从 $\bar{\beta}_t^2$ 降为 $\bar{\beta}_t^2 / s^2$（因独立正态分布可加性），信号均值不变，因此SNR增加 $s^2$ 倍。

SNR对齐条件：要求高分辨率调度降采样后的SNR等于低分辨率调度同时间点的SNR，结合约束 $\bar{\alpha}_t^2 + \bar{\beta}_t^2 = 1$ 可唯一确定高分辨率调度。

## 关键公式

正向扩散过程：
$$\boldsymbol{x}_t = \bar{\alpha}_t \boldsymbol{x}_0 + \bar{\beta}_t \boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{I})$$

SNR对齐条件：
$$\frac{(\bar{\alpha}_t^{w \times h})^2}{(\bar{\beta}_t^{w \times h})^2} \times s^2 = \frac{(\bar{\alpha}_t^{w/s \times h/s})^2}{(\bar{\beta}_t^{w/s \times h/s})^2}$$

多尺度损失：
$$\mathcal{L}_{s \times s} = \frac{1}{(w/s)(h/s)}\|\mathcal{D}_{w/s \times h/s}[\boldsymbol{\varepsilon}] - \mathcal{D}_{w/s \times h/s}[\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\bar{\alpha}_t \boldsymbol{x}_0 + \bar{\beta}_t \boldsymbol{\varepsilon}, t)]\|^2$$

## 实验或案例

- Simple Diffusion成功在像素空间训练分辨率高达1024x1024的图像扩散模型。
- 消融实验表明SNR对齐调度、架构扩展和多尺度损失均有提升。
- 最终效果与LDM在FID指标上具有竞争力。

## 系列定位

作为系列第22篇，本文从第21篇的采样加速转向高分辨率图像生成问题，引入SNR作为核心分析工具。它与第23篇（下篇）共同构成"信噪比与大图生成"主题，为后续的Upsample Guidance（无需训练的高分辨率生成）奠定SNR分析基础。
