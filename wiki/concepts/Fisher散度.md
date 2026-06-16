---
type: concept
title: Fisher散度
aliases:
- Fisher Divergence
- 费希尔散度
- 广义Fisher散度
definition: 一种衡量两个概率分布差异的散度，定义为 $p_{\boldsymbol{\theta}}$ 加噪分布与真实加噪分布之间的得分函数（Score
  Function）差值的加权L2范数，在SiD中用于解释蒸馏损失函数和 $\lambda$ 参数的选择。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-11-22-生成扩散模型漫谈-二十六-基于恒等式的蒸馏-下.md
source_ids:
- '10567'
prerequisites:
- 得分匹配
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods:
- 恒等式蒸馏法
series:
- 生成扩散模型漫谈
evidence_spans:
- 10567-广义散度
status: draft
updated: '2026-06-12'
---

## 定义

Fisher散度定义为分布 $p$ 和 $q$ 之间的得分函数差值的加权L2范数：
$$\mathcal{F}(p, q) = \int p(\boldsymbol{x}) \|\nabla\log p(\boldsymbol{x}) - \nabla\log q(\boldsymbol{x})\|^2 d\boldsymbol{x}$$

在SiD中，生成器损失 $\mathcal{L}_1$ 等价于最小化 $p_{\boldsymbol{\theta}}$（学生数据加噪分布）与 $p$（真实数据加噪分布）之间的Fisher散度。广义Fisher散度引入可任意选定的权重分布 $r(\boldsymbol{x})$：
$$\mathcal{F}(p, q|r) = \int r(\boldsymbol{x}) \|\nabla p(\boldsymbol{x}) - \nabla q(\boldsymbol{x})\|^2 d\boldsymbol{x}$$

当 $r(\boldsymbol{x}) > 0$ 处处成立时，$p=q$ 仍为最优解。

## 性质

- Fisher散度中的第一个分布（作为权重）若随参数优化，可能引致模式坍缩。固定第一个分布（施加stop-gradient）可缓解此问题。
- 在SiD上下文中，对第一个 $p_{\boldsymbol{\theta}}$ 施加stop-gradient后，对应的损失函数等价于 $\mathcal{L}_2 - \mathcal{L}_1$，解释了 $\lambda=1$ 的选择。
- 广义Fisher散度说明：权重分布 $r$ 只要处处非零，理论最优解不变；但优化行为的稳定性高度依赖于 $r$ 的选择。