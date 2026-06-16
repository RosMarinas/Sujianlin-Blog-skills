---
type: article_summary
title: 生成扩散模型漫谈（二十三）：信噪比与大图生成（下）
article_id: "10055"
source_url: https://spaces.ac.cn/archives/10055
date: 2024-04-17
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-04-17-生成扩散模型漫谈-二十三-信噪比与大图生成-下.md
series: [生成扩散模型漫谈]
concepts: [上采样引导, 信噪比感知噪声调度]
methods: [信噪比对齐调度迁移]
evidence_spans:
  - 10055-思想探讨
  - 10055-数学描述
  - 10055-再请SNR
  - 10055-分解近似
  - 10055-LDM扩展
  - 10055-思考分析
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-04-17-生成扩散模型漫谈-二十三-信噪比与大图生成-下.md
source_ids:
  - "10055"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文提出Upsample Guidance（UG），通过将低分辨率预训练扩散模型的下采样去噪结果作为主项、直接应用作为细节项，结合SNR对齐的时间偏移和引导权重，实现无需额外训练即可从低分辨率模型生成高分辨率图像（分辨率提升至少1倍）。

## 核心问题

能否将训练好的低分辨率扩散模型直接用于高分辨率图像生成，不需要任何额外训练？直接应用存在什么困难，如何解决？

## 关键结论

1. 将低分辨率模型直接当作高分辨率模型使用，虽然不能生成有效语义（如人脸），但保留了大量可用的纹理细节。
2. 理想的高分辨率去噪模型可以分解为低分辨率主项（先下采样再用低分辨率模型去噪再上采样）和高分辨率细节项（直接应用低分辨率模型减去其下采样版本）。
3. 主项需要SNR对齐的时间偏移（找到 $\tau$ 使 $SNR(\tau) = s^2 \cdot SNR(t)$）和幅度归一化（除以 $\rho_t$）。
4. UG的有效性依赖于CNN的架构先验（DIP效应）；纯Transformer扩散模型无法复现UG效果。
5. 对于LDM，UG仅在扩散前期有效，后期应关闭（通过时间依赖的引导权重 $w_t$）。

## 核心推导

主项近似：对精确高分辨率去噪模型 $\boldsymbol{\epsilon}^{\text{high}}(\boldsymbol{x}_t, t)$ 进行恒等分解：
$$\boldsymbol{\epsilon}^{\text{high}} = \mathcal{U}[\mathcal{D}[\boldsymbol{\epsilon}^{\text{high}}]] + (\boldsymbol{\epsilon}^{\text{high}} - \mathcal{U}[\mathcal{D}[\boldsymbol{\epsilon}^{\text{high}}]])$$

对主项用下采样+低分辨率模型近似，对细节项用直接应用近似：
$$\boldsymbol{\epsilon}^{\text{high}}(\boldsymbol{x}_t, t) \approx \frac{1}{s}\mathcal{U}\left[\boldsymbol{\epsilon}_{\boldsymbol{\theta}}\left(\frac{\mathcal{D}[\boldsymbol{x}_t]}{\rho_t}, \tau\right)\right] + \left\{\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t) - \mathcal{U}\left[\mathcal{D}\left[\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)\right]\right]\right\}$$

引入CFG风格的引导权重 $w$：
$$\tilde{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t) = (1 + w)\boldsymbol{\epsilon}_{\boldsymbol{\theta}}^{\text{approx}}(\boldsymbol{x}_t, t) - w\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)$$

## 关键公式

时间偏移求解方程：
$$\frac{\bar{\alpha}_{\tau}^2}{\bar{\beta}_{\tau}^2} = \frac{s^2\bar{\alpha}_t^2}{\bar{\beta}_t^2}$$

LDM时间依赖引导权重：
$$w_t = \begin{cases} w, & t \geq (1-\eta)T \\ -1, & t < (1-\eta)T \end{cases}$$

## 实验或案例

- 128x128训练的CelebA-HQ模型直接用UG生成256x256和512x512图像，效果显著优于直接放大。
- 最优引导权重 $w \approx 0.2$。
- LDM场景下UG能纠正直接应用造成的"畸形"。
- 计算开销仅增加约 $1/s^2$。
- 作者的纯Transformer扩散模型实验无法复现UG效果，确认了CNN架构先验的必要性。

## 系列定位

作为系列第23篇，本文与第22篇（上篇）共同构成"信噪比与大图生成"主题。本文从SNR分析出发，提出了一种无需训练的零成本高分辨率生成方案，体现了扩散模型研究中"免费午餐"式的巧妙设计。同时本文与第22篇形成互补：上篇通过修改训练流程（重新调度、扩大架构、多尺度损失）实现高分辨率生成，本文则在推理阶段复用已有低分辨率模型。
