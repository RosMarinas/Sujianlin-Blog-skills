---
type: concept
title: KL散度消失
aliases:
- KL Vanishing
- KL散度坍缩
- Posterior Collapse in VAE
definition: 在VAE训练中，强大的解码器（尤其是自回归语言模型）倾向于忽略隐变量 $z$，导致编码器后验分布 $p(z|x)$ 退化为与先验 $q(z)$
  完全相同的分布，KL散度项 $KL(p(z|x) \| q(z))$ 趋近于0，编码器输出常数向量的现象。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-05-06-变分自编码器-五-VAE-BN-更好的VAE.md
- Data/Spaces_ac_cn/markdown/Big-Data/2021-05-17-变分自编码器-七-球面上的VAE-vMF-VAE.md
source_ids:
- '7381'
- '8404'
prerequisites:
- '[[变分自编码器]]'
- '[[ELBO]]'
equivalent_forms: []
direct_consequences:
- '[[BN防止KL消失]]'
- '[[球面VAE构造法]]'
related_formulas:
- '[[VAE KL散度公式]]'
related_methods:
- '[[BN防止KL消失]]'
- '[[球面VAE构造法]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::7381::NLP中的VAE
- ev::8404::KL散度消失
status: draft
updated: '2026-06-12'
---

## 定义

KL散度消失（KL Vanishing / Posterior Collapse）是VAE在NLP任务中遇到的典型困难。VAE的训练目标包含重构项和KL散度项，两项之间存在对抗关系：KL散度项的存在使解码器更难利用 $z$ 中的信息（因为噪声 $\varepsilon$ 破坏了 $z$ 的信道）。当解码器是自回归语言模型（如LSTM、Transformer）时，它本身已经足够强大，即使没有 $z$ 的信息也能准确预测下一个token。解码器于是"选择"忽略 $z$，编码器输出变成常数（即 $p(z|x) \approx q(z)$），KL散度项归零。

## 数学特征

在Gaussian VAE中，KL散度项的计算式为：

$$
\mathbb{E}_{x\sim\tilde{p}(x)}[KL(p(z|x) \| q(z))] = \frac{1}{b}\sum_{i=1}^b\sum_{j=1}^d \frac12(\mu_{i,j}^2 + \sigma_{i,j}^2 - \log\sigma_{i,j}^2 - 1)
$$

当KL消失时，对所有 $i,j$ 有 $\mu_{i,j} \to 0$ 且 $\sigma_{i,j} \to 1$，该项趋近于0。

## 影响

KL散度消失意味着VAE退化为普通自编码器（编码器输出常数）加上一个无条件语言模型（解码器在无 $z$ 条件下生成），失去了VAE无监督学习编码向量的核心价值。

## 常见解决方案

1. **退火策略**：训练初期降低KL项权重，逐步增加。
2. **更换先验分布**：如vMF-VAE（第7篇），使KL天生为常数。
3. **结构调整**：如BN-VAE（第5篇），在编码器输出加BN强制KL有正下界。
4. **词丢弃（Word Dropout）**：训练时随机丢弃解码器部分输入词，迫使其依赖 $z$。