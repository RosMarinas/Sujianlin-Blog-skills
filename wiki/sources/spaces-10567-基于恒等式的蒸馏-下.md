---
type: article_summary
title: 生成扩散模型漫谈（二十六）：基于恒等式的蒸馏（下）
article_id: "10567"
source_url: https://spaces.ac.cn/archives/10567
date: 2024-11-22
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-11-22-生成扩散模型漫谈-二十六-基于恒等式的蒸馏-下.md
series: [生成扩散模型漫谈]
concepts: [基于恒等式的蒸馏, Fisher散度]
methods: [恒等式蒸馏法]
evidence_spans:
  - 10567-恒等变换
  - 10567-直面梯度
  - 10567-广义散度
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-11-22-生成扩散模型漫谈-二十六-基于恒等式的蒸馏-下.md
source_ids:
  - "10567"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从梯度视角和广义Fisher散度视角为SiD中的超参数 $\lambda$ 提供了理论解释：FGM（Flow Generator Matching）通过精确的梯度计算确认 $\lambda=0.5$ 的选择，作者通过广义Fisher散度分析进一步解释了 $\lambda=1$ 的合理性。

## 核心问题

SiD（第25篇）的最终损失 $\mathcal{L}_2 - \lambda\mathcal{L}_1$ 中，$\lambda$ 的理论最优值是什么？为什么 $\lambda > 1$（即反向优化 $\mathcal{L}_1$）仍然有效？SiD的恒等变换是否可以做得更彻底？

## 关键结论

1. 恒等式 $\mathbb{E}[\langle\boldsymbol{f}(\boldsymbol{x}_t, t), \boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}\rangle] = \mathbb{E}[\langle\boldsymbol{f}(\boldsymbol{x}_t, t), \boldsymbol{\varepsilon}\rangle]$ 的核心是 $\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}(\boldsymbol{x}_t, t) = \mathbb{E}_{\boldsymbol{\varepsilon}\sim p(\boldsymbol{\varepsilon}|\boldsymbol{x}_t)}[\boldsymbol{\varepsilon}]$，条件为 $\boldsymbol{f}$ 仅依赖于 $\boldsymbol{x}_t$ 和 $t$。
2. FGM构造了损失 $\mathcal{L}_4$，使得 $\nabla_{\boldsymbol{\theta}}\mathcal{L}_4^{(\text{sg})} = \nabla_{\boldsymbol{\theta}}\mathcal{L}_{1/2/3}$，实现了梯度无偏估计。该损失满足 $\mathcal{L}_4^{(\text{sg})} = 2\mathcal{L}_2^{(\text{sg})} - \mathcal{L}_1^{(\text{sg})} = 2(\mathcal{L}_2^{(\text{sg})} - 0.5 \times \mathcal{L}_1^{(\text{sg})})$，确认 $\lambda=0.5$。
3. 从Fisher散度视角看，$\mathcal{L}_1$ 等价于最小化 $p_{\boldsymbol{\theta}}$ 与 $p$ 之间的Fisher散度。散度中作为权重分布的第一个 $p_{\boldsymbol{\theta}}$ 可能导致模式坍缩，应施加stop-gradient。
4. 在第一个 $p_{\boldsymbol{\theta}}$ 施加stop-gradient后的损失等价于 $2(\mathcal{L}_2 - \mathcal{L}_1)$，解释了 $\lambda=1$。
5. $\lambda$ 在 $0.5$ 到 $1.5$ 之间都能工作，$\lambda=1.2$ 在某些任务上最优。$\lambda > 1$ 相当于增加 $-\mathcal{L}_1$ 惩罚项，进一步降低模式坍缩风险。

## 核心推导

FGM的核心推导：对 $\mathbb{E}[\|\boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}\|^2]$ 分别进行"先恒等变换后求梯度"和"先求梯度后恒等变换"，比较两种路径得到：

$$\nabla_{\boldsymbol{\theta}}\mathbb{E}[\langle\boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}, \boldsymbol{\varepsilon}\rangle] = \nabla_{\boldsymbol{\theta}}\mathbb{E}[2\langle\boldsymbol{\epsilon}_{\text{sg}[\boldsymbol{\psi}^*]}, \boldsymbol{\varepsilon}\rangle - \|\boldsymbol{\epsilon}_{\text{sg}[\boldsymbol{\psi}^*]}\|^2]$$

从而得到 $\mathcal{L}_4^{(\text{sg})} = 2\mathcal{L}_2^{(\text{sg})} - \mathcal{L}_1^{(\text{sg})}$。

广义Fisher散度分析：$p_{\boldsymbol{\theta}}(\boldsymbol{x})$ 在Fisher散度中出现两次，第一次作为权重分布。若只优化第一次而固定第二次，最优解为Dirac delta——即模式坍缩。因此应对第一个 $p_{\boldsymbol{\theta}}$ 施加stop-gradient。

## 关键公式

恒等式的直接证明：
$$\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}(\boldsymbol{x}_t, t) = \mathbb{E}_{\boldsymbol{\varepsilon}\sim p(\boldsymbol{\varepsilon}|\boldsymbol{x}_t)}[\boldsymbol{\varepsilon}]$$
$$\mathbb{E}[\langle\boldsymbol{f}(\boldsymbol{x}_t, t), \boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}\rangle] = \mathbb{E}[\langle\boldsymbol{f}(\boldsymbol{x}_t, t), \boldsymbol{\varepsilon}\rangle]$$

FGM的损失函数：
$$\mathcal{L}_4^{(\text{sg})} = \mathbb{E}[\|\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}\|^2 - 2\langle\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}, \boldsymbol{\varepsilon}\rangle + 2\langle\boldsymbol{\epsilon}_{\text{sg}[\boldsymbol{\psi}^*]}, \boldsymbol{\varepsilon}\rangle - \|\boldsymbol{\epsilon}_{\text{sg}[\boldsymbol{\psi}^*]}\|^2]$$

广义Fisher散度：
$$\mathcal{F}(p, q|r) = \int r(\boldsymbol{x}) \|\nabla_{\boldsymbol{x}} p(\boldsymbol{x}) - \nabla_{\boldsymbol{x}} q(\boldsymbol{x})\|^2 d\boldsymbol{x}$$

当 $r(\boldsymbol{x}) > 0$ 处处成立时，$p = q$ 仍为最优解。

## 实验或案例

- 本文未提出新实验，而是为SiD已有的实验现象提供理论解释。
- 解释了 $\lambda$ 在 $0.5$ 到 $1.5$ 之间均能工作的原因。
- 解释了 $\lambda > 1.5$ 导致训练崩溃的原因（$-\mathcal{L}_1$ 惩罚过强）。

## 系列定位

作为系列第26篇，本文是第25篇的直接续作，为SiD中 $\lambda$ 的选择提供了坚实的理论支撑。它与FGM的发现相互印证，并引入广义Fisher散度视角提供了一个更完整的理解。本文标志着"生成扩散模型漫谈"系列在蒸馏理论层面的深化，也为后续可能的第27篇及以后的工作留下了探索空间。
