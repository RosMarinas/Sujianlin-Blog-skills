---

type: concept
title: DDIM (去噪扩散隐式模型)
aliases:
- Denoising Diffusion Implicit Models
definition: DDPM的一种推广，去除了前向过程中对 $p(x_t|x_{t-1})$ 的依赖，仅通过边际分布 $p(x_t|x_0)$ 和待定系数法得到一族由
  $\sigma_t$ 参数化的反向过程。其中 $\sigma_t=0$ 的确定性过程支持加速采样和隐空间插值。DDIM与DDPM共享训练过程，仅采样方式不同。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-07-27-生成扩散模型漫谈-四-DDIM-高观点DDPM.md
source_ids:
- '9181'
prerequisites:
- '[[DDPM]]'
- '[[反向去噪过程]]'
- '[[累积信号率]]'
equivalent_forms: []
direct_consequences:
- '[[扩散SDE框架]]'
related_formulas: []
related_methods: []
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9181::待定系数
status: draft
updated: '2026-06-12'
---
# DDIM (Denoising Diffusion Implicit Models)

## 定义
DDIM 是一种确定性采样方法，用于加速扩散生成模型的推断过程。它通过将反向过程建模为非马尔可夫链，使得采样过程成为确定性的常微分方程（ODE）轨迹。

## 核心原理
在相同的边际分布下，DDIM 改变了前向和反向的联合分布。其采样公式为：
$$x_{t-1} = \sqrt{ar{lpha}_{t-1}} \left( rac{x_t - \sqrt{1 - ar{lpha}_t} \epsilon_	heta(x_t)}{\sqrt{ar{lpha}_t}} ight) + \sqrt{1 - ar{lpha}_{t-1} - \sigma_t^2} \epsilon_	heta(x_t) + \sigma_t \epsilon$$
当设置 $\sigma_t = 0$ 时，采样过程完全确定，不需要引入新的随机噪声，从而可以用极少的步数（如 20-50 步）完成高质量的图像生成。
