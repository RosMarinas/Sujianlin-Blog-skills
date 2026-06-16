---
type: concept
title: 概率流ODE
aliases:
- Probability Flow ODE
definition: 概率流ODE是一个确定性常微分方程，其解轨迹与原始随机微分方程（SDE）具有完全相同的边际概率分布$p_t(\boldsymbol{x})$，通过将扩散系数$\sigma_t$设为零从广义前向SDE导出。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-08-08-生成扩散模型漫谈-六-一般框架之ODE篇.md
source_ids:
- '9228'
prerequisites:
- '[[Fokker-Planck方程]]'
- '[[前向过程等价性]]'
equivalent_forms:
- DDIM ODE（线性漂移特例）
direct_consequences: []
related_formulas: []
related_methods:
- '[[Fokker-Planck方程推导法]]'
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9228::神经ODE
status: draft
updated: '2026-06-12'
---

概率流ODE是扩散模型SDE理论框架的关键扩展。在广义前向SDE $d\boldsymbol{x} = (\boldsymbol{f}_t(\boldsymbol{x}) - \frac{1}{2}(g_t^2 - \sigma_t^2)\nabla\log p_t(\boldsymbol{x}))dt + \sigma_t d\boldsymbol{w}$中，令$\sigma_t=0$即得概率流ODE：$d\boldsymbol{x} = (\boldsymbol{f}_t(\boldsymbol{x}) - \frac{1}{2}g_t^2\nabla\log p_t(\boldsymbol{x}))dt$。由于实践中$\nabla\log p_t(\boldsymbol{x})$由神经网络$\boldsymbol{s}_{\boldsymbol{\theta}}(\boldsymbol{x},t)$近似，该ODE本质是一个神经ODE。概率流ODE的优点包括：前向和反向过程为同一确定性方程，可精确计算似然，支持隐变量编辑，且可使用高阶ODE求解器加速采样。