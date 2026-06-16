---
type: article_summary
title: "生成扩散模型漫谈（五）：一般框架之SDE篇"
article_id: "9209"
source_url: https://spaces.ac.cn/archives/9209
date: 2022-08-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-08-03-生成扩散模型漫谈-五-一般框架之SDE篇.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[扩散SDE框架]]"
  - "[[得分匹配]]"
  - "[[前向扩散过程]]"
  - "[[反向去噪过程]]"
  - "[[累积信号率]]"
  - "[[噪声预测网络]]"
  - "[[DDPM]]"
  - "[[DDIM]]"
evidence_spans:
  - ev::9209::随机微分
  - ev::9209::逆向方程
  - ev::9209::得分匹配
  - ev::9209::结果倒推
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-03-生成扩散模型漫谈-五-一般框架之SDE篇.md
source_ids:
  - "9209"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文介绍宋飏博士提出的基于随机微分方程（SDE）的扩散模型一般框架，将DDPM、DDIM、得分匹配和ODE方法统一在连续时间视角下，并提出了"结果倒推"的实用策略——先定义 $p(x_t|x_0)$ 再反推对应SDE。

## 核心问题

能否构建一个统一的连续时间理论框架，将DDPM、DDIM、得分匹配和ODE视角下的扩散模型联系起来？如何在不陷入严格随机微积分理论的前提下理解这一框架？

## 关键结论

- SDE框架提供了扩散模型的最一般化视角：前向过程 $dx = f_t(x) dt + g_t dw$，反向过程 $dx = [f_t(x) - g_t^2 \nabla_x \log p_t(x)] dt + g_t dw$，统一了DDPM、得分匹配和ODE方法。
- 不同T值对应同一SDE的不同离散化精度：SDE将理论分析和代码实现分离，实践中选择任意合适的离散化步长。
- 噪声项必须为 $\mathcal{O}(\sqrt{\Delta t})$ 而非 $\mathcal{O}(\Delta t)$：这是确保随机效应在长期过程中不相互抵消的关键，也是伊藤微积分的基本性质。
- 得分函数 $\nabla_x \log p_t(x)$ 可通过条件得分匹配学习，无需计算不可处理的归一化常数，且与DDPM的噪声预测网络等价：$s_\theta(x_t, t) = -\epsilon_\theta(x_t, t)/\bar{\beta}_t$。
- "结果倒推"策略更实用：先定义 $p(x_t|x_0)$ 的形式，再反推对应的SDE参数 $(f_t, g_t)$，避免了求解正向SDE解析解的困难。

## 核心推导

文章从SDE离散近似 $x_{t+\Delta t} - x_t = f_t(x_t) \Delta t + g_t \sqrt{\Delta t} \varepsilon$ 出发，其条件概率为 $p(x_{t+\Delta t}|x_t) = \mathcal{N}(x_{t+\Delta t}; x_t + f_t(x_t)\Delta t, g_t^2 \Delta t I)$。用贝叶斯定理求反向条件概率 $p(x_t|x_{t+\Delta t})$，对 $\log p(x_{t+\Delta t})$ 做泰勒展开（含空间梯度项和时间偏导项），代入后配方得反向SDE。对于得分匹配，从 $\nabla_{x_t} \log p(x_t) = \frac{\mathbb{E}_{x_0}[p(x_t|x_0) \nabla_{x_t} \log p(x_t|x_0)]}{\mathbb{E}_{x_0}[p(x_t|x_0)]}$ 出发，用最小二乘原理推导条件得分匹配损失 $\mathbb{E}[\|s_\theta(x_t, t) - \nabla_{x_t} \log p(x_t|x_0)\|^2]$。对于"结果倒推"，假定 $p(x_t|x_0) = \mathcal{N}(\bar{\alpha}_t x_0, \bar{\beta}_t^2 I)$ 和线性SDE $dx = f_t x dt + g_t dw$，匹配一阶矩和二阶矩得 $f_t = \frac{d}{dt}(\ln \bar{\alpha}_t)$ 和 $g_t^2 = \bar{\alpha}_t^2 \frac{d}{dt}(\frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2})$。特别地，$\bar{\alpha}_t^2 + \bar{\beta}_t^2 = 1$ 给出VP-SDE，$\bar{\alpha}_t \equiv 1$ 给出VE-SDE。

## 关键公式

**前向SDE（式1）：**
$$dx = f_t(x) dt + g_t dw$$

**离散近似：**
$$x_{t+\Delta t} - x_t = f_t(x_t) \Delta t + g_t \sqrt{\Delta t} \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, I)$$

**反向SDE（式5）：**
$$dx = [f_t(x) - g_t^2 \nabla_x \log p_t(x)] dt + g_t dw$$

**条件得分匹配损失（式8）：**
$$\mathbb{E}_{x_0, x_t \sim p(x_t|x_0)\tilde{p}(x_0)} \left[\|s_\theta(x_t, t) - \nabla_{x_t} \log p(x_t|x_0)\|^2\right]$$

**得分与噪声预测的关系：**
$$s_\theta(x_t, t) = -\frac{\epsilon_\theta(x_t, t)}{\bar{\beta}_t}$$

**反向工程SDE参数（从 $p(x_t|x_0)$ 到 SDE）：**
$$f_t = \frac{d}{dt}(\ln \bar{\alpha}_t), \quad g_t^2 = \bar{\alpha}_t^2 \frac{d}{dt}\left(\frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}\right)$$

**边界条件：**
$$\bar{\alpha}_0 = 1, \quad \bar{\alpha}_1 = 0, \quad \bar{\beta}_0 = 0, \quad \bar{\beta}_1 = 1$$

## 实验或案例

本文为理论综述文章，未提供新实验。引用Song Yang等人的SDE论文的实验结果作为框架有效性的支撑。

## 系列定位

本文是系列第五篇，也是第一阶段的集大成之作。独特贡献在于：(1) 将前四篇的离散视角提升到连续时间SDE的一般框架；(2) 揭示了DDPM（对应VP-SDE的离散化）与得分匹配的内在等价性；(3) 提出了"结果倒推"的方法论创新——从边际分布出发反向设计SDE，而非传统地从SDE求解边际分布；(4) 统一了前四篇中看似不同的推导路径（直观类比、VAE、贝叶斯、DDIM），展示了它们作为SDE框架不同离散化或特殊情况的统一图景。
