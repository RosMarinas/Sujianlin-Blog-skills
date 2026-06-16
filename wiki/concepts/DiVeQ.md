---
type: concept
title: DiVeQ
definition: 一种可微向量量化方法，利用重参数化技巧在不牺牲前向离散性的前提下，在反向传播中引入差分向量模长的梯度以规避显式的辅助损失设计。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-08-DiVeQ-一种非常简洁的VQ训练方案.md
source_ids:
- 11328
status: draft
updated: '2026-06-12'
---

# DiVeQ

## 核心定义
DiVeQ (Differentiable Vector Quantization) 提出了一种新的 STE (Straight-Through Estimator) 技巧，最大亮点是不需要 Aux Loss（辅助损失）。在标准的 VQ-VAE 中，为了解决 $\mathop{\text{argmin}}$ 导致的梯度断裂问题，通常需要使用 STE 并且补上两项 Aux Loss。

为了在保持前向为量化向量 $q$ 的同时保留梯度的反向传播，最理想的 DiVeQ 方案（DiVeQ-detach）的形式如下：
$$
z_q = z + \Vert q - z\Vert \times \mathop{\text{sg}}\left[\frac{q - z}{\Vert q - z\Vert}\right]
$$
它在前向的时候严格有 $z_q = q$，但反向时保留了 $z$ 和 $\Vert q - z\Vert$ 的梯度。

在论文正文中，DiVeQ 提出了一种引入随机性的形式，可以看作是 DiVeQ-detach 和 NSVQ 的某种插值：
$$
z_q = z + \Vert q - z\Vert \times \mathop{\text{sg}}\left[\frac{q - z + \varepsilon}{\Vert q - z + \varepsilon\Vert}\right],\qquad \varepsilon\sim\mathcal{N}(0, \sigma^2 I)
$$
很明显，当 $\sigma=0$ 时，结果是“DiVeQ-detach”，当 $\sigma\to\infty$ 时，结果是“NSVQ”。实验表明，$\sigma^2 = 10^{-3}$ 是一个普遍较优的选择。

## 理论性质与条件
DiVeQ 能规避 Aux Loss 的核心在于引入了距离函数的梯度。将一般的距离函数记为 $r(q, z)$，如果使用 $z_q = z + r(q, z) \times \mathop{\text{sg}}\left[\frac{q - z}{r(q, z)}\right]$，其损失函数微分可表示为：
$$
d\mathcal{L} = \langle\nabla_{z_q} \mathcal{L},d z\rangle + \langle\nabla_{z_q} \mathcal{L}, q-z\rangle d(\ln r)
$$
除了原本 VQ 的梯度外，DiVeQ 多出了额外的 $\langle\nabla_{z_q} \mathcal{L}, q-z\rangle d(\ln r)$，相当于引入了隐式的 Aux Loss：$\mathop{\text{sg}}[\langle\nabla_{z_q} \mathcal{L}, q-z\rangle] \ln r$。如果 $r$ 代表 $q,z$ 的某种距离函数，那么它就是在拉近 $q,z$ 的距离。

该解释成立的必要条件是系数 $\langle\nabla_{z_q} \mathcal{L}, q-z\rangle > 0$。通过考虑损失函数 $\mathcal{L}(z)$ 在 $z_q$ 处的一阶近似可得：
$$
\langle\nabla_{z_q} \mathcal{L}, q-z\rangle\approx \mathcal{L}(z_q) - \mathcal{L}(z)
$$
由于 VQ 是一个损失信息的过程，用连续的 $z$ 重构目标任务通常比 $z_q$ 容易，因此 $\mathcal{L}(z_q) - \mathcal{L}(z) > 0$ 大概率成立。系数 $\mathcal{L}(z_q) - \mathcal{L}(z)$ 与主损失 $\mathcal{L}(z_q)$ 是齐次的，它能够较好地自适应主损失的 Scale，还能根据 VQ 前后的效果差距来调节 Aux Loss 权重。若取 $r(q,z)=\Vert q-z\Vert^{\alpha}$，个人实验发现 $\alpha=1$ 确实普遍表现较好。

## 与其他方法的联系
- **VQ-VAE / STE**：DiVeQ 替代了标准 VQ 方案中“STE + Aux Loss”的组合，避免了超参数调节并使网络更贴近端到端优化。
- **NSVQ**：NSVQ 将 $z_q$ 定义为 $z_q = z + \Vert q - z\Vert \times \frac{\varepsilon}{\Vert \varepsilon\Vert}$，它在以 $z$ 为中心、半径为 $\Vert q-z\Vert$ 的圆上均匀采样，但在前向传递时送入解码器的并非真实的 $q$，导致训练和推理不一致。DiVeQ 修复了这一前向不一致性。
- **FSQ**：FSQ 对低维向量做“四舍五入”来实现离散化且不需要 Aux Loss，但并不能在任意场景都取代 VQ。
- **编码表坍缩（Codebook Collapse）**：DiVeQ 只是提供了一种免 Aux Loss 的 VQ 训练方案，原则上不解决编码表利用率低或坍缩问题。它可以与 SFVQ（形成 SF-DiVeQ）或给编码表加线性变换等增强技巧组合使用，以进一步提升效果。
