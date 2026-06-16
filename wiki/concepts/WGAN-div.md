---
type: concept
definition: WGAN-div用带梯度范数惩罚项的W散度目标训练判别器，使WGAN式训练不再依赖外部施加的显式Lipschitz约束。
title: WGAN-div
aliases:
- Wasserstein Divergence GAN
source_ids:
- '6139'
evidence_spans:
- ev::6139::W散度目标
- ev::6139::WGAN-div训练
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
---

# WGAN-div

WGAN-div（Wasserstein Divergence for GANs）用带梯度范数惩罚项的W散度（Wasserstein Divergence）目标训练判别器，使WGAN式训练不再依赖外部施加的显式Lipschitz约束。

## 核心定义与数学表达

WGAN-div的训练模式基于W散度的一般化目标：
$$
W_{k,p}[\tilde{p}(x), q(x)] = \max_{T} \mathbb{E}_{x\sim \tilde{p}(x)}[T(x)] - \mathbb{E}_{x\sim q(x)}[T(x)] - k\mathbb{E}_{x\sim r(x)}[\Vert \nabla T\Vert^p]
$$
其中$k > 0, p > 1$。

基于此目标的WGAN-div生成模型训练可表示为：
$$
\begin{aligned}T =& \mathop{\text{argmax}}_{T} \mathbb{E}_{x\sim \tilde{p}(x)}[T(x)] - \mathbb{E}_{x\sim q(x)}[T(x)] - k\mathbb{E}_{x\sim r(x)}[\Vert \nabla T\Vert^p]\\
G =& \mathop{\text{argmin}}_{G} \mathbb{E}_{x\sim \tilde{p}(x)}[T(x)] - \mathbb{E}_{x\sim q(z)}[T(G(z))]\end{aligned}
$$
前者是为了通过W散度$W_{k,p}$找出W距离中最优的鉴别函数$T$，后者则是为了最小化W距离以训练生成器$G$。

## 核心性质

$W_{k,p}$ 具有非常好的理论性质：
1. **是一个对称的散度**：$\mathcal{D}[P,Q]\geq 0$且$\mathcal{D}[P,Q]=0\Leftrightarrow P=Q$。散度意味着当我们最小化它时，我们真正是在缩小两个分布的距离。
2. **最优解与W距离的联系**：当我们最大化$W_{k,p}$得到$T$之后，可以去掉梯度项，通过最小化 $\mathbb{E}_{x\sim \tilde{p}(x)}[T(x)] - \mathbb{E}_{x\sim q(z)}[T(G(z))]$ 来训练生成器。这也表明以$W_{k,p}$为目标，性质跟W距离类似，不会有梯度消失的问题。
3. **无严格的 $r(x)$ 限制**：W散度中对惩罚项采样分布 $r(x)$ 的要求非常宽松，基本只要求 $r(x)$ 是一个样本空间跟真实分布 $\tilde{p}(x)$ 和伪造分布 $q(x)$ 相同的分布，不需要像 WGAN-GP 必须在真假样本间随机插值。

## 与其他方法的联系与对比

WGAN-div被提出以解决原始WGAN在Lipschitz约束（L约束）上的实现痛点（如权重裁剪导致的优化不稳定，谱归一化把判别器限制在了一小簇函数之间等）。

与 **WGAN-GP** 的对比：
- **目标函数的性质**：带常数偏置的惩罚项 $\max_{T} \mathbb{E}_{x\sim \tilde{p}(x)}[T(x)] - \mathbb{E}_{x\sim q(x)}[T(x)] - k\mathbb{E}_{x\sim r(x)}[(\Vert \nabla T\Vert - n)^p]$ 不总是一个散度。当$n=1,p=2$时这就是WGAN-GP的梯度惩罚，原论文作者证明它不是一个散度。这意味着WGAN-GP在训练判别器时，并非总是会在拉大两个分布的距离。
- **理论支撑**：WGAN-GP的梯度惩罚只能算是一种经验方案，而WGAN-div目标是有严格的偏微分方程与最优传输理论保证的。
- **对采样方式的鲁棒性**：实验表明，WGAN-div 在面对多种不同的 $r(x)$ 采样方式（真假样本随机插值、纯真样本、纯假样本等）时表现都差不多（FID稳定），而 WGAN-GP 对于不同的采样方式差异极大。

## 超参数与具体实践

作者通过搜索实验发现，对于 WGAN-div，当 $k=2, p=6$ 时效果最好，这进一步与WGAN-GP的做法有出入（范数的二次幂并非是最好的选择）。一般选择 $r(x)$ 为 $\tilde{p}(x)、q(x)$ 两者共同衍生出来的分布，相对来说收敛快一点。
