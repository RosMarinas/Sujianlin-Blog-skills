---

type: concept
title: 扩散SDE框架
aliases:
- Diffusion SDE Framework
- SDE统一框架
- Score-Based Generative Modeling through SDEs
definition: 由宋飏等人提出的统一连续时间框架，将扩散模型的前向过程建模为随机微分方程 $dx = f_t(x) dt + g_t dw$，反向过程为 $dx
  = [f_t(x) - g_t^2 \nabla_x \log p_t(x)] dt + g_t dw$。DDPM（VP-SDE的离散化）、DDIM（ODE视角）、得分匹配等方法均是该框架的特例。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-08-03-生成扩散模型漫谈-五-一般框架之SDE篇.md
source_ids:
- '9209'
prerequisites:
- '[[DDPM]]'
- '[[DDIM]]'
equivalent_forms: []
direct_consequences:
- '[[得分匹配]]'
related_formulas: []
related_methods: []
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9209::随机微分
- ev::9209::逆向方程
status: draft
updated: '2026-06-12'
---
# 扩散 SDE 框架

## 定义
扩散 SDE 框架由 Song et al. (2020) 提出，通过随机微分方程（SDE）将离散步数的扩散模型（如 DDPM）推广到连续时间的无限维极限框架中。

## 数学结构
前向扩散过程由以下 SDE 描述：
$$dx = \boldsymbol{f}(x, t) dt + g(t) dw$$
其中 $\boldsymbol{f}(x,t)$ 是漂移系数，$g(t)$ 是扩散系数，$w$ 是标准布朗运动。对应的反向去噪过程同样满足一个反向 SDE：
$$dx = \left[ \boldsymbol{f}(x, t) - g(t)^2 \nabla_x \log p_t(x) \right] dt + g(t) d\bar{w}$$
其中 $\nabla_x \log p_t(x)$ 是数据在 $t$ 时刻的得分函数。
