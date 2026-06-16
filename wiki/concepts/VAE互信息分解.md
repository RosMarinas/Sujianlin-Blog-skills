---
type: concept
title: VAE互信息分解
aliases:
- VAE Mutual Information Decomposition
- VAE loss as prior KL + mutual information
- 变分自编码器互信息视角
definition: VAE的损失函数 $KL(\tilde{p}(x)p(z|x) \| q(z)q(x|z))$ 可分解为先验KL散度项和互信息项两项，分别对应"将后验推向先验"和"最大化输入与隐变量的互信息"。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-10-10-变分自编码器-最小化先验分布-最大化互信息.md
- Data/Spaces_ac_cn/markdown/Big-Data/2020-05-06-变分自编码器-五-VAE-BN-更好的VAE.md
source_ids:
- '6088'
- '7381'
prerequisites:
- '[[变分自编码器]]'
- '[[KL散度]]'
equivalent_forms:
- '[[ELBO分解]]'
direct_consequences:
- '[[Deep INFOMAX损失来源]]'
related_formulas:
- '[[VAE联合分布KL公式]]'
related_methods: []
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::6088::过程
status: draft
updated: '2026-06-12'
---

## 定义

VAE互信息分解是指将VAE的联合分布KL散度损失函数拆解为两项具有清晰语义的独立项：

$$
\begin{aligned}
&KL(\tilde{p}(x)p(z|x) \| q(z)q(x|z)) \\
&= \underbrace{\iint \tilde{p}(x)p(z|x)\log\frac{p(z|x)}{q(z)} dzdx}_{\text{先验KL：将后验推向先验}} - \underbrace{\iint \tilde{p}(x)p(z|x)\log\frac{q(x|z)}{\tilde{p}(x)} dzdx}_{\text{互信息：最大化 }I(x;z)}
\end{aligned}
$$

## 关键性质

- 第一项 $\iint \tilde{p}(x)p(z|x)\log\frac{p(z|x)}{q(z)} dzdx$ 是编码器后验与先验的KL散度的期望，**最小化**此项使编码后的隐变量分布接近先验分布。
- 第二项中的 $\log\frac{q(x|z)}{\tilde{p}(x)}$ 在信息论中正是点互信息（Pointwise Mutual Information）。积分后得到负的互信息 $I(x;z)$，因此**最小化**此项等价于**最大化** $x$ 与 $z$ 之间的互信息。
- 当解码器 $q(x|z)$ 具有无限容量时，最优解满足 $\tilde{p}(x)p(z|x) = q(x|z)p(z)$（贝叶斯公式），第二项严格等于 $KL(\tilde{p}(x)p(z|x) \| \tilde{p}(x)p(z)) = I(x;z)$。

## 意义

该分解揭示了VAE损失的深层语义：VAE同时在做两件事——（1）正则化隐空间使其服从先验分布，（2）确保隐变量 $z$ 包含关于输入 $x$ 的足够信息。这种理解自然地架起了VAE与Deep INFOMAX（深度互信息最大化）之间的桥梁。