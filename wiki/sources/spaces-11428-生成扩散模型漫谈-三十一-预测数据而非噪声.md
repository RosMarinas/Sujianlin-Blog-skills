---
type: article_summary
title: 生成扩散模型漫谈（三十一）：预测数据而非噪声
article_id: "11428"
source_url: https://spaces.ac.cn/archives/11428
date: 2025-11-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-11-24-生成扩散模型漫谈-三十一-预测数据而非噪声.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[预测数据范式]]"
  - "[[低维流形假设]]"
  - "[[离散扩散自编码器]]"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-11-24-生成扩散模型漫谈-三十一-预测数据而非噪声.md
source_ids:
  - "11428"
status: draft
updated: 2026-06-09
---

# 生成扩散模型漫谈（三十一）：预测数据而非噪声

## 一句话总结

本文介绍JiT（Just image Transformers / Back to Basics, arXiv:2511.13720），基于"数据处在低维流形上而噪声充满全空间"这一事实，提出扩散模型应预测数据$\boldsymbol{x}$而非噪声$\boldsymbol{\varepsilon}$或速度$\boldsymbol{v}$，从而简化像素空间扩散模型的架构。

## 核心问题

像素空间扩散模型从低分辨率迁移到高分辨率时，即使调整Noise Schedule对齐信噪比，仍需要更多计算才能达到相近FID。为什么？如何解决？

## 关键结论

1. 噪声向量支撑全空间$\mathbb{R}^d$，预测噪声需要模型无低秩瓶颈；数据处于低维子流形，预测数据对低秩瓶颈容忍度高。
2. ViT使用大Patch Size时产生低秩瓶颈（如$32\times32$ patch投影到768维不可逆），此时只有数据预测（$\boldsymbol{x}$-pred）能成功训练。
3. 主动引入适当的低秩瓶颈反而有利于数据预测模型的FID——反直觉但符合流形假设。
4. JiT不刷新SOTA但降低SOTA成本，使低分辨率SOTA架构可低成本迁移到高分辨率。
5. 数据预测参数化$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t) = (\text{NN}_\theta(\boldsymbol{x}_t, t) - \boldsymbol{x}_t)/(1-t)$有一条关键直通连接$-\boldsymbol{x}_t$，解释U-Net多条skip connection中最核心的一条。

## 核心推导

### 核心论证（信息论视角）
- 噪声$\boldsymbol{\varepsilon} \sim \mathcal{N}(0, \boldsymbol{I})$支撑全空间$\mathbb{R}^d$，预测噪声需全维度表达能力
- 数据$\boldsymbol{x}_0$处于有效维度$d_{\text{eff}} \ll d$的低维流形，预测数据只要$d_{\text{bottleneck}} \geq d_{\text{eff}}$
- 低秩瓶颈（$\boldsymbol{x}$-pred时可接受）在噪声预测时会导致不可逆信息丢失

### 9组合对比
3种预测目标（$\boldsymbol{x}, \boldsymbol{\varepsilon}, \boldsymbol{v}$）$\times$ 3种回归目标，系统ablation确认仅有低秩瓶颈时预测目标的选择起决定性作用。

## 关键公式

| 公式 | 含义 |
|------|------|
| $\boldsymbol{v}_\theta(\boldsymbol{x}_t, t) = (\text{NN}_\theta(\boldsymbol{x}_t, t) - \boldsymbol{x}_t)/(1-t)$ | 数据预测参数化（含关键skip connection） |
| $\mathbb{E}[\|\boldsymbol{v}_\theta(\boldsymbol{x}_t, t) - (\boldsymbol{x}_1 - \boldsymbol{x}_0)\|^2]$ | ReFlow速度预测损失（回归目标为速度） |

## 实验或案例

- 9组合ablation：无低秩瓶颈时9种组合差距不大；有瓶颈时仅$\boldsymbol{x}$-pred成功
- 主动增加低秩瓶颈改善了FID（反直觉但符合理论）
- 不同分辨率（128/256/512）在相近计算量下达到相近FID
- 作者在CelebA HQ上的对比：$\boldsymbol{x}$-pred vs $\boldsymbol{v}$-pred，前者明显更好

## 系列定位

本文跳出加速生成主线，从模型架构角度提出核心洞见。文章29（DDCM）中"噪声不可压缩"的实践经验被用作论据。本文与文章27-30形成互补：前者关注"如何加速"（改变模型的目标/结构），后者关注"预测什么"（数据而非噪声/速度）。
