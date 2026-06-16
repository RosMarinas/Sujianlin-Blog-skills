---
type: article_summary
title: "变分自编码器（二）：从贝叶斯观点出发"
article_id: "5343"
source_url: https://spaces.ac.cn/archives/5343
date: 2018-03-28
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-03-28-变分自编码器-二-从贝叶斯观点出发.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[变分自编码器]]"
  - "[[联合分布KL散度]]"
  - "[[后验分布假设]]"
  - "[[重参数化技巧 (VAE中的)]]"
methods:
  - "[[VAE联合分布最小化]]"
evidence_spans:
  - ev::5343::直面联合分布
  - ev::5343::不能搞分裂
  - ev::5343::后验分布近似
  - ev::5343::生成模型近似
  - ev::5343::采样计算技巧
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-03-28-变分自编码器-二-从贝叶斯观点出发.md
source_ids:
  - "5343"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从贝叶斯概率图模型视角严格推导VAE，将VAE的目标函数重新定义为联合分布 $p(x,z)$ 与 $q(x,z)$ 之间的KL散度最小化，并系统地回答了"如何选择重构损失函数"（MSE与交叉熵的适用场景）以及"两类loss为何不能独立优化"的问题。

## 核心问题

VAE在贝叶斯框架下的严格推导是什么？重构损失为何要么用MSE要么用交叉熵？KL loss和重构loss能否分别最小化？为什么VAE训练有一个统一的进度指标而GAN没有？

## 关键结论

- VAE可以被直接推导为 $KL(p(x,z) \| q(x,z))$ 的最小化——一个比标准ELBO推导更直接的方式。无需聚焦于后验分布 $p(z|x)$ 的难解性，直面联合分布即可得到VAE损失函数。
- 解码器 $q(x|z)$ 的分布假设决定了具体的损失函数：伯努利分布 $\to$ 交叉熵损失（二值数据），固定方差的正态分布 $\to$ MSE损失（连续数据）。这直接回答了实践中的损失函数选择问题。
- 重构loss和KL loss是相互拮抗的，不能分开独立优化：KL loss为零意味着 $z$ 无辨识度，重构必然差；重构好则KL loss不可能为零。两者需联合最小化。
- VAE的 $\mathcal{L}$ 本身可作为生成质量的统一训练指标（loss越低越好），而原始GAN没有这样的指标，直到WGAN才解决。
- 单样本蒙特卡洛从 $p(z|x)$ 中采样足以支撑训练，因为多epoch的随机采样覆盖了整个分布。

## 核心推导

**从联合分布KL散度推导VAE损失**：

1. 定义目标：最小化 $KL(p(x,z) \| q(x,z))$，其中 $p(x,z) = \tilde{p}(x)p(z|x)$（数据确定的联合分布），$q(x,z) = q(x|z)q(z)$（模型联合分布）。
2. 展开：$$KL(p(x,z)\|q(x,z)) = \mathbb{E}_{x\sim\tilde{p}(x)}\left[\int p(z|x)\ln\frac{\tilde{p}(x)p(z|x)}{q(x|z)q(z)}dz\right]$$
3. 分离常数项 $\mathbb{E}_{x\sim\tilde{p}(x)}[\ln\tilde{p}(x)]$（数据决定，与模型无关），得到损失 $\mathcal{L}$。
4. 分解：$\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[\mathbb{E}_{z\sim p(z|x)}[-\ln q(x|z)] + KL(p(z|x)\|q(z))]$，即标准VAE损失。

**解码器分布与损失函数的对应**：
- 伯努利解码器 $q(x|z)$：$-\ln q(x|z)$ 展开为交叉熵 $\sum[-x_{(k)}\ln\rho_{(k)}(z)-(1-x_{(k)})\ln(1-\rho_{(k)}(z))]$
- 正态解码器（固定方差）：$-\ln q(x|z) \sim \|x-\tilde{\mu}(z)\|^2/(2\tilde{\sigma}^2)$，即MSE

## 关键公式

- $(8)$: $KL(p(x,z)\|q(x,z)) = \iint p(x,z)\ln\frac{p(x,z)}{q(x,z)}dzdx$ —— 核心优化目标
- $(13)$: $\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[\mathbb{E}_{z\sim p(z|x)}[-\ln q(x|z)] + KL(p(z|x)\|q(z))]$ —— 标准VAE损失函数
- $(16)$: $KL(p(z|x)\|q(z)) = \frac{1}{2}\sum_{k=1}^d(\mu_{(k)}^2(x)+\sigma_{(k)}^2(x)-\ln\sigma_{(k)}^2(x)-1)$ —— KL项闭式
- $(19)$: $-\ln q(x|z) = \sum[-x_{(k)}\ln\rho_{(k)}(z)-(1-x_{(k)})\ln(1-\rho_{(k)}(z))]$ —— 交叉熵损失（伯努利解码器）
- $(22)$: $-\ln q(x|z) \sim \|x-\tilde{\mu}(z)\|^2/(2\tilde{\sigma}^2)$ —— MSE损失（固定方差正态解码器）

## 实验或案例

本文无实验。全篇为理论推导和框架构建。

## 系列定位

本文是系列的第二篇，在首篇直观理解的基础上提供严格的贝叶斯推导。核心贡献是：(1) 以联合分布KL散度最小化出发，给出比标准ELBO推导更直接的推导路径；(2) 系统地阐了解码器分布假设与损失函数之间的对应关系；(3) 明确指出两部分loss的拮抗关系，反对独立优化；(4) 将VAE嵌入到贝叶斯概率图模型与深度学习结合的框架中。为第三篇（解释VAE为何成功）提供理论基础。
