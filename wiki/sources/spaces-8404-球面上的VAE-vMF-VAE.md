---
type: article_summary
title: "变分自编码器（七）：球面上的VAE（vMF-VAE）"
article_id: "8404"
source_url: https://spaces.ac.cn/archives/8404
date: 2021-05-17
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-05-17-变分自编码器-七-球面上的VAE-vMF-VAE.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[KL散度消失]]"
  - "[[von Mises-Fisher分布]]"
  - "[[球面VAE]]"
  - "[[变分自编码器]]"
methods:
  - "[[球面VAE构造法]]"
evidence_spans:
  - ev::8404::KL散度消失
  - ev::8404::vMF分布
  - ev::8404::从vMF采样
  - ev::8404::vMF-VAE
  - ev::8404::参考实现
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-17-变分自编码器-七-球面上的VAE-vMF-VAE.md
source_ids:
  - "8404"
status: draft
updated: 2026-06-09
---

## 一句话总结

用定义在超球面 $S^{d-1}$ 上的 von Mises-Fisher（vMF）分布替换标准VAE中的高斯先验/后验分布，使KL散度项成为仅依赖于维度 $d$ 和浓度 $\kappa$ 的常数，从而从根本上消除KL散度消失问题；vMF的采样通过数值逆CDF方法分解为 $w$（角度）采样和 $\nu$（正交方向）采样的组合。

## 核心问题

除了第5篇中用BN强制KL保底的方法外，能否从分布选择的角度出发，设计一种KL散度项天生就是常数的VAE架构，从根源上杜绝KL消失？

## 关键结论

1. vMF分布定义在超球面 $S^{d-1}$ 上，以余弦相似度 $\langle\mu, x\rangle$ 为度量，概率密度 $p(x) = C_{d,\kappa} e^{\kappa\langle\mu,x\rangle}$，其中 $\kappa$ 是浓度参数（$\kappa=0$ 为球面均匀分布）。
2. vMF-VAE配置：先验为球面均匀分布（$\kappa=0$），后验为 $p(z|x) = C_{d,\kappa} e^{\kappa\langle\mu(x),z\rangle}$。KL散度项 $KL(p(z|x) \| q(z))$ 的计算结果仅依赖于 $d$ 和 $\kappa$，不依赖于 $\mu(x)$，因此是一个常数。
3. vMF采样分解为两个独立子问题：（a）采样 $w \sim e^{\kappa w}(1-w^2)^{(d-3)/2}$（角度分量），（b）采样 $\nu$ 为与 $\mu$ 正交的超球面均匀方向。
4. 对于一维分布 $p(w)$，数值逆CDF方法（离散化 $\rightarrow$ cumsum $\rightarrow$ normalize $\rightarrow$ interpolate）比传统的beta分布拒绝采样更简单高效。
5. $\kappa$ 作为超参数（不通过梯度更新），因为保留 $\kappa$ 在 $w$ 采样过程中的梯度很困难。

## 核心推导

1. 球坐标分解将vMF采样问题分离为角度和方位两个独立部分：$e^{\kappa x_1}dS^{d-1} = (e^{\kappa\cos\varphi_1}\sin^{d-2}\varphi_1 d\varphi_1) dS^{d-2}$。
2. 令 $w = \cos\varphi_1$，$w$ 的PDF正比于 $e^{\kappa w}(1-w^2)^{(d-3)/2}$。
3. KL计算：代入vMF密度，利用一阶矩方向与 $\mu$ 一致且模长仅依赖 $d,\kappa$，得KL为常数。
4. 一般情形采样：$z = w\mu + \sqrt{1-w^2}\nu$，其中 $\nu$ 通过Gram-Schmidt从正态采样获得。

## 关键公式

$$\begin{aligned}
\mathcal{L} &= \|x - g(z)\|^2 \\
z &= w\mu(x) + \sqrt{1-w^2}\nu \\
w &\sim e^{\kappa w}(1-w^2)^{(d-3)/2} \\
\nu &= \frac{\varepsilon - \langle\varepsilon,\mu\rangle\mu}{\|\varepsilon - \langle\varepsilon,\mu\rangle\mu\|},\quad \varepsilon\sim\mathcal{N}(0,1_d)
\end{aligned}$$

## 实验或案例

提供了完整的MNIST Keras实现（github.com/bojone/vae/blob/master/vae_vmf_keras.py），并给出预计算 $10^6$ 个 $w$ 值缓存后随机索引的高效采样方案。

## 系列定位

本文是系列第7篇，与第5篇（BN方案）构成对KL散度消失问题的"双解法"。BN方案是修补式（不改分布，加BN保底），vMF方案是重构式（替换分布，彻底消除KL）。vMF-VAE使KL项变为常数后，训练退化为"AE + 重参数化"，极大简化了架构，但代价是 $\kappa$ 作为超参数需要人工调整。本文为第8篇（密度估计视角）提供了另一种理解VAE的切入角度。
