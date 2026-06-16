---
type: article_summary
title: "变分自编码器（三）：这样做为什么能成？"
article_id: "5383"
source_url: https://spaces.ac.cn/archives/5383
date: 2018-04-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-04-03-变分自编码器-三-这样做为什么能成.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[变分自编码器]]"
  - "[[资源争用]]"
  - "[[后验分布假设]]"
  - "[[重参数化技巧 (VAE中的)]]"
methods:
  - "[[VAE联合分布最小化]]"
evidence_spans:
  - ev::5383::采样之惑
  - ev::5383::一个点确实够了
  - ev::5383::耿直的IWAE
  - ev::5383::重参之神
  - ev::5383::后验的先验
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-04-03-变分自编码器-三-这样做为什么能成.md
source_ids:
  - "5383"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文回答了VAE实践中的核心疑问——为什么单样本后验采样可行而先验采样会失败，引入了"资源争用"($僧多粥少$)的直观解释，介绍了重要性加权自编码器（IWAE）作为VAE的自然推广，并高度评价重参数化技巧为整个框架的"点睛之笔"。

## 核心问题

为什么从后验分布 $p(z|x)$ 中采样一个 $z$ 就足以训练VAE，而从先验分布 $q(z)$ 中采样相同数量的样本却会导致训练失败？VAE的这个设计"凑巧"有效还是存在深层原因？

## 关键结论

- **从先验 $q(z)$ 采样失败的原因——"资源争用"**：先验 $q(z)$ 是标准正态分布（覆盖全空间），采样出的 $z$ 样本数量远少于batch中 $x$ 的数量，多个 $x$ 需要"争夺"有限的几个 $z$ 样本。每次迭代的随机性导致争抢结果不稳定，训练无法收敛。
- **从后验 $p(z|x)$ 采样成功的原因——"低方差收敛"**：训练收敛后，$p(z|x)$ 和 $q(x|z)$ 都变为方差极小的正态分布，$z$ 和 $x$ 之间接近一一对应（确定性函数关系），因此不同次采样结果几乎一致，单样本足以代表整个分布。
- **低方差性质是先验假设**：真实数据集（如MNIST）本身就是高维空间中的低维流形，因此编码和解码过程的方差很小是合理的先验认识，模型训练只是实现了这一预期。
- **IWAE是VAE的自然推广**：通过重要性采样技巧，从 $p(z|x)$ 采样 $k$ 个样本并加权，得到更紧的下界。$k=1$ 退化为标准VAE；$k$ 越大生成质量越好，但编码器质量下降。更大 $k$ 会削弱 $p(z|x)$ 的重要性。
- **重参数化技巧是关键使能技术**：若没有重参数化 $z = \mu(x) + \varepsilon \times \sigma(x)$，采样操作对 $\mu(x)$ 和 $\sigma(x)$ 的梯度为零，编码器将无法获得任何梯度反馈进行更新。

## 核心推导

**IWAE推导**：从边缘似然出发
$$\int q(x|z)q(z)dz = \int p(z|x)\frac{q(x|z)q(z)}{p(z|x)}dz = \mathbb{E}_{z\sim p(z|x)}\left[\frac{q(x|z)q(z)}{p(z|x)}\right]$$

引入 $k$ 个样本的蒙特卡洛估计：
$$\int q(x|z)q(z)dz \approx \frac{1}{k}\sum_{i=1}^k \frac{q(x|z_i)q(z_i)}{p(z_i|x)},\quad z_i\sim p(z|x)$$

代入最大似然框架得到IWAE目标函数 $(11)$：$\mathcal{L}_k = \mathbb{E}_{x\sim\tilde{p}(x)}[-\ln(\frac{1}{k}\sum_{i=1}^k \frac{q(x|z_i)q(z_i)}{p(z_i|x)})],\quad z_i\sim p(z|x)$

当 $k=1$ 时，IWAE退化为完全采样的VAE变体：$\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[-\ln q(x|z) + \ln p(z|x) - \ln q(z)],\quad z\sim p(z|x)$

## 关键公式

- $(5)$: $\mathcal{L} = \mathbb{E}_{x\sim\tilde{p}(x)}[-\ln q(x|z) + \ln p(z|x) - \ln q(z)],\quad z\sim p(z|x)$ —— 完全采样的VAE变体
- $(9)$: $\int q(x|z)q(z)dz = \int p(z|x)\frac{q(x|z)q(z)}{p(z|x)}dz$ —— IWAE重要性采样关键等式
- $(11)$: $\mathcal{L}_k = \mathbb{E}_{x\sim\tilde{p}(x)}[-\ln(\frac{1}{k}\sum_{i=1}^k \frac{q(x|z_i)q(z_i)}{p(z_i|x)})]$ —— IWAE目标函数
- $z = \mu(x) + \varepsilon \times \sigma(x),\quad \varepsilon\sim\mathcal{N}(0,I)$ —— 重参数化技巧

## 实验或案例

无定量实验。定性地讨论MNIST encoder输出方差极小的事实，支持"低方差后验"的论点。间接引用IWAE原始论文的实验结果。

## 系列定位

本文是系列的第三篇，重点解决"为什么这样做可行"的深层疑问。核心贡献是：(1) 提出了"资源争用"的直观概念来解释先验采样的失败；(2) 基于低维流形先验论证后验采样的成功；(3) 引入IWAE作为VAE的自然推广，揭示VAE的边界；(4) 高度提炼重参数化技巧的关键作用。为第四篇（VAE聚类应用）提供了理解基础。
