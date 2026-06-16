---
type: article_summary
title: "变分自编码器（六）：从几何视角来理解VAE的尝试"
article_id: "7725"
source_url: https://spaces.ac.cn/archives/7725
date: 2020-09-10
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-09-10-变分自编码器-六-从几何视角来理解VAE的尝试.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[VAE几何视角]]"
  - "[[变分自编码器]]"
  - "[[重参数化技巧]]"
evidence_spans:
  - ev::7725::自编码器
  - ev::7725::编码空间
  - ev::7725::从点到面
  - ev::7725::采样重构
  - ev::7725::空间正则
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-09-10-变分自编码器-六-从几何视角来理解VAE的尝试.md
source_ids:
  - "7725"
status: draft
updated: 2026-06-09
---

## 一句话总结

用几何类比的方式理解VAE：自编码器将每个样本编码为"点"，VAE将每个样本编码为"椭圆"（高斯分布），通过重参数化从单位圆采样再仿射变换到椭圆，并用KL散度将所有椭圆向单位圆（标准正态分布）拉近，从而获得规整紧凑的编码空间。

## 核心问题

对于不熟悉概率论但想使用VAE的读者，如何直观地理解VAE相比自编码器（AE）做了什么、为什么有用、在什么场景下需要使用？

## 关键结论

1. 自编码器的编码空间存在四个典型形态：散乱无规律、线形（维数冗余）、环形（中心空洞）、圆形（理想：规整、连续、无冗余）。圆形是最理想的编码空间形态。
2. VAE的核心改动：将每个样本的编码从"点"变为"椭圆"（即高斯后验分布 $p(z|x)$）。点难以覆盖面，但面可以覆盖面，这使得编码空间更容易被均匀覆盖。
3. 重参数化：从单位圆（标准正态分布）采样 $\varepsilon$，通过 $\mu(x) + \varepsilon \otimes \sigma(x)$ 变换为目标椭圆内的点。
4. KL散度项的作用：将所有椭圆向单位圆拉近，使编码空间整体呈标准正态分布形态。

## 核心推导

1. AE目标：$E,D = \text{argmin}_{E,D} \mathbb{E}_{x\sim\mathcal{D}}[\|x - D(E(x))\|^2]$。
2. VAE目标（几何形式）：$\mu,\sigma,D = \text{argmin} \mathbb{E}_{x\sim\mathcal{D}}[\|x - D(\mu(x) + \varepsilon \otimes \sigma(x))\|^2]$，$\varepsilon \sim \mathcal{N}(0,1)$。
3. 正则项：$\mathbb{E}_{x\sim\mathcal{D}}[\sum_i \frac12(\mu_i^2 + \sigma_i^2 - \log\sigma_i^2 - 1)]$，作用是将椭圆拉向单位圆。

## 关键公式

$$\Vert x - D(\mu(x) + \varepsilon\otimes \sigma(x))\Vert^2 + \sum_{i=1}^d \frac12\big(\mu_i^2(x) + \sigma_i^2(x) - \log\sigma_i^2(x) - 1\big), \quad \varepsilon\sim\mathcal{N}(0,1)$$

## 实验或案例

无量化实验。文中用模拟图展示了四种编码空间形态（散乱、线形、环形、圆形），帮助读者建立直觉。

## 系列定位

本文是系列第6篇，完全抛开概率推导，从几何类比出发直观介绍VAE。它为前5篇的正式数学推导提供了一个友好的直觉接口，降低了入门门槛。文章末尾指出VAE的两个效果（随机采样生成 + 编码空间紧凑解耦），为后续文章（vMF-VAE、密度估计）提供了动机。
