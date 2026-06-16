---
type: example
title: spaces-11459-平均场近似求解最优调度
article_id: 11459
article:
- - spaces-11459-滑动平均视角下权重衰减和学习率
section: 最优调度
claim: 在齐次自适应优化器中，利用平均场展开和连续时间近似，可以通过求解微分方程推导得到满足梯度恒定记忆系数的最优学习率和权重衰减联合函数
notation_mapping:
  eta_s: eta_s (连续训练步下的时变学习率)
  lambda_s: lambda_s (连续训练步下的时变权重衰减率)
  kappa_s: kappa_s (更新累积折算指数，kappa_s = integral_0^s eta_t * lambda_t dt)
steps:
- 根据滑动平均，求得第 j 步梯度的加权系数公式： beta_tilde(j,t) = e^kappa_j * eta_j / z_t
- 令该系数对于任意的历史时间步 j 均恒等于常数（数据权重均等），从而求导可得导数关系： d/dj (e^kappa_j * eta_j) = 0
- 将 kappa_j 的微分形式代入，化为常微分方程： lambda_s * eta_s + dot_eta_s / eta_s = 0
- 针对常数 WD 情形（lambda_s = lambda），代入解得： eta_s = eta_max / (lambda * eta_max * s + 1)
- 针对正比例 WD 情形（lambda_s = alpha * eta_s），代入解得： eta_s = eta_max / sqrt(2 * alpha * eta_max^2
  * s + 1)
used_concepts:
- - - 平均场近似
- - - 优化器记忆周期
used_formulas:
- - - 最优优化器调度公式
used_methods:
- - - 平均场优化器动力学分析法
- - - 最优学习率与权重衰减调度法
source_span: ev::11459::最优调度
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-05-滑动平均视角下的权重衰减和学习率.md
source_ids:
- 11459
status: stable
updated: '2026-06-12'
---

## 问题

源文“最优调度”要从滑动平均视角反推 Weight Decay Schedule 和 Learning Rate Schedule，使每个 Batch 的梯度贡献系数尽量恒定，而不是随时间距离衰减。

## 推导

在 $\beta_1,\beta_2\to0$ 的简化下，源文把期望条件写成
$$
\frac{e^{\kappa_i}\eta_i}{z_t}=\frac{e^{\kappa_j}\eta_j}{z_t}.
$$
取相邻步 $i=j-1$，得到递推方程
$$
e^{\lambda_j\eta_j}\eta_j=\eta_{j-1}.
$$
若想得到解析形式，则对两端取对数，并把 $\lambda_j,\eta_j$ 视作连续函数，令差分近似为导数，得到
$$
\lambda_s\eta_s+\frac{\dot{\eta}_s}{\eta_s}\approx0.
$$
当 $\lambda_s=\lambda$ 为常数时，解为 $\eta_s\approx \eta_{\max}/(\lambda\eta_{\max}s+1)$；若取 $\lambda_s=\alpha\eta_s$，则同时得到随 $1/\sqrt{s}$ 衰减的 $\eta_s$ 与 $\lambda_s$，并使 $\bar{\beta}_1(j,t),\bar{\beta}_2(j,t)\approx1/t$。

## 方法与证据

该例体现“从平均场系数恒定条件反解调度函数”的方法。证据锚点为 `ev::11459::最优调度`，源文还说明该推导可推广到 Adam、RMSProp、SignSGDM、Muon 等齐次自适应优化器。
