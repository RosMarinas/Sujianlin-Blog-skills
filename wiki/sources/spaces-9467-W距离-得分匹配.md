---
type: article_summary
title: 生成扩散模型漫谈（十六）：W距离 ≤ 得分匹配
article_id: "9467"
source_url: https://spaces.ac.cn/archives/9467
date: 2023-02-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-02-14-生成扩散模型漫谈-十六-W距离-得分匹配.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[Wasserstein距离与得分匹配]]"
  - "[[得分匹配]]"
methods:
  - "[[Cauchy-Schwarz不等式放缩]]"
evidence_spans:
  - ev::9467::结论分析
  - ev::9467::牛刀小试
  - ev::9467::一鼓作气
  - ev::9467::艰难收尾
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-02-14-生成扩散模型漫谈-十六-W距离-得分匹配.md
source_ids:
  - "9467"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文证明了扩散模型的得分匹配损失是2-Wasserstein距离的上界，从而在理论上建立了扩散模型与WGAN之间的桥梁：最小化扩散模型的损失函数，实则与WGAN一样，都是在最小化两个分布之间的Wasserstein距离。

## 核心问题

扩散模型基于得分匹配进行训练，而WGAN基于Wasserstein距离进行优化，两者在形式上差异明显。核心问题在于：这两种生成模型之间是否存在理论上的深层联系？能否证明扩散模型的训练目标实际上也在优化Wasserstein距离？

## 关键结论

1. **核心不等式**：扩散模型的得分匹配损失构成了2-Wasserstein距离$\mathcal{W}_2[p_0,q_0]$的一个上界，其中$p_0$是真实数据分布，$q_0$是生成分布。
2. **条件得分匹配也是上界**：由于条件得分匹配（实际使用的训练目标）是得分匹配的上界，因此它也是Wasserstein距离的上界。
3. **系数舍去的解释**：扩散模型实践中舍去损失函数中的系数$1/\bar{\beta}_t^2$，可以理解为让训练目标更加接近Wasserstein距离。
4. **WGAN与扩散的统一**：本文揭示了扩散模型和WGAN在优化目标层面的统一性——两者都在隐秘地优化Wasserstein距离。
5. **ODE简化视角**：对于确定性ODE情形（而非完整SDE），可以给出更简洁清晰的证明。

## 核心推导

本文的证明采用"由简到繁"的策略，分为三个阶段：

**阶段1（简化ODE，相同初始分布）**：从同一个分布$q(\boldsymbol{z})$采样初始值，沿两个不同ODE$\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{f}_t(\boldsymbol{x}_t)$和$\frac{d\boldsymbol{y}_t}{dt} = \boldsymbol{g}_t(\boldsymbol{y}_t)$演化。通过"同一$\boldsymbol{z}$配对"构造传输方案，然后对$\tilde{\mathcal{W}}_2^2[p_t,q_t] = \mathbb{E}_{\boldsymbol{z}}[\|\boldsymbol{x}_t - \boldsymbol{y}_t\|^2]$求导，利用柯西不等式（向量版和期望版）和单侧Lipschitz约束进行放缩，最后用常数变易法求解微分不等式。

**阶段2（不同初始分布）**：将阶段1的同一$\boldsymbol{z}$配对替换为$p_T$和$q_T$之间的最优传输方案$\gamma^*(\boldsymbol{z}_1,\boldsymbol{z}_2)$，边界条件变为$C_T = \mathcal{W}_2[p_T,q_T]$，结果增加一项$I_T \mathcal{W}_2[p_T,q_T]$。

**阶段3（扩散模型）**：将具体的扩散模型反向SDE（用$\boldsymbol{s}_{\boldsymbol{\theta}}$近似得分）转化为ODE后代入阶段2的结果，得到最终的不等式$\mathcal{W}_2[p_0,q_0] \leq \int_0^T g_t^2 I_t (\mathbb{E}[\|\nabla\log p_t - \boldsymbol{s}_{\boldsymbol{\theta}}\|^2])^{1/2}dt + I_T\mathcal{W}_2[p_T,q_T]$。对于完整SDE情形，作者指出遇到了$\mathbb{E}[(\boldsymbol{x}_t - \boldsymbol{y}_t)\cdot(\nabla\log p_t - \nabla\log q_t)]\geq 0$无法在一般条件下证明的困难。

## 关键公式

**2-Wasserstein距离定义**：
$$\mathcal{W}_{\rho}[p,q]=\left(\inf_{\gamma\in \Pi[p,q]} \iint \gamma(\boldsymbol{x},\boldsymbol{y}) \Vert\boldsymbol{x} - \boldsymbol{y}\Vert^{\rho} d\boldsymbol{x}d\boldsymbol{y}\right)^{1/\rho}$$

**核心不等式**：
$$\mathcal{W}_2[p_0,q_0]\leq \int_0^T g_t^2 I_t \left(\mathbb{E}_{\boldsymbol{x}_t\sim p_t(\boldsymbol{x}_t)}\left[\left\Vert\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{x}_t) - \boldsymbol{s}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)\right\Vert^2\right]\right)^{1/2}dt + I_T \mathcal{W}_2[p_T,q_T]$$

**单侧Lipschitz约束**：
$$(\boldsymbol{g}_t(\boldsymbol{x}) - \boldsymbol{g}_t(\boldsymbol{y}))\cdot(\boldsymbol{x} - \boldsymbol{y}) \leq L_t \Vert \boldsymbol{x} - \boldsymbol{y}\Vert^2$$

**微分不等式推导**（简化ODE情形）：
$$-\frac{d\tilde{\mathcal{W}}_2[p_t,q_t]}{dt} \leq \left(\mathbb{E}\left[\Vert\boldsymbol{f}_t(\boldsymbol{x}_t) - \boldsymbol{g}_t(\boldsymbol{x}_t)\Vert^2\right]\right)^{1/2} + L_t\tilde{\mathcal{W}}_2[p_t,q_t]$$

## 实验或案例

本文为纯理论推导论文，没有设计实验或案例验证。其核心贡献在于提供一个比原论文更易于理解的证明思路（仅需W距离定义、微分方程和柯西不等式），降低了理论理解门槛。

## 系列定位

本文是"生成扩散模型漫谈"系列中承上启下的理论关键节点。它首次建立了扩散模型与WGAN之间的理论联系，为后续文章中进一步统一GAN和扩散模型（如第19篇"作为扩散ODE的GAN"）奠定了理论基础。同时，本文对"条件得分匹配是得分匹配上界"的阐述也直接引出了第18篇对两者等价性的更深入分析。
