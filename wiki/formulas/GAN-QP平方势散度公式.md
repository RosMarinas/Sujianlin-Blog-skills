---
type: formula
title: GAN-QP平方势散度公式
aliases:
- QP-div formula
source_ids:
- '6163'
- '6214'
evidence_spans:
- ev::6163::平方势散度
- ev::6163::GAN-QP目标
standard_notation:
  p: real/data distribution
  q: generated distribution
  T: critic or discriminator potential
  Delta_T: antisymmetric critic difference
  d: sample-space distance
  lambda: quadratic potential scale
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
- Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
latex: \mathcal{L}[p,q]=\max_T\mathbb{E}_{x_r\sim p,x_f\sim q}\left[\Delta T-\frac{(\Delta
  T)^2}{2\lambda d(x_r,x_f)}\right],\quad \Delta T=T(x_r,x_f)-T(x_f,x_r).
symbol_meanings:
  \mathcal{L}[p,q]: QP 散度（Quadratic Potential Divergence）损失
  T: 判别器势函数（critic potential）
  \Delta T: 判别器反对称差值（$T(x_r,x_f)-T(x_f,x_r)$）
  \mathbb{E}: 期望算子
  x_r: 真实样本
  x_f: 生成（虚假）样本
  p: 真实数据分布
  q: 生成数据分布
  \lambda: 二次势缩放因子
  d(x_r,x_f): 样本空间距离度量
conditions: （待从源文章提取）
appears_in:
- '6163'
- '6214'
---

# GAN-QP平方势散度公式

## 概述

GAN-QP平方势散度公式 $$\mathcal{L}[p,q]=\max_T\mathbb{E}_{x_r\sim p,x_f\sim q}\left[\Delta T-\frac{(\Delta T)^2}{2\lambda d(x_r,x_f)}\right]$$ 是一种直接在对偶空间定义的新概率散度（QP-div，Quadratic Potential Divergence），其中 $\Delta T=T(x_r,x_f)-T(x_f,x_r)$ 是判别器产生的差值信号，$\lambda$ 是缩放因子，$d$ 为样本空间的某种距离。这一框架（GAN-QP）成功地同时解决了 SGAN 存在的梯度消失风险和 WGAN 需要严格 Lipschitz 约束的难题。通过变分法求解极值得出判别器最优解后，可以证明此公式实际上是一种“自适应的 L 约束”，其最优解不仅天然满足 Lipschitz 连续性，而且当分布极端不重叠时，它的惩罚项也能保证拉近分布距离，维持有效的梯度传递。在实际使用中，通常可将其简化为一元函数差值 $T(x_r)-T(x_f)$ 进行计算，不仅理论完备，计算效率也极高。
