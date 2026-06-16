---
type: article_summary
title: 生成扩散模型漫谈（三十）：从瞬时速度到平均速度
article_id: "10958"
source_url: https://spaces.ac.cn/archives/10958
date: 2025-05-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-05-26-生成扩散模型漫谈-三十-从瞬时速度到平均速度.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[平均速度流]]"
  - "[[捷径模型]]"
  - "[[一致性模型]]"
  - "[[自一致性损失]]"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-05-26-生成扩散模型漫谈-三十-从瞬时速度到平均速度.md
source_ids:
  - "10958"
status: draft
updated: 2026-06-09
---

# 生成扩散模型漫谈（三十）：从瞬时速度到平均速度

## 一句话总结

本文介绍MeanFlow（Mean Flows for One-step Generative Modeling, arXiv:2505.13447），通过将建模目标从ODE的"瞬时速度"切换为"平均速度"，配合三个逐级优化的损失函数，实现理论上最严谨的单步扩散生成。

## 核心问题

ODE扩散模型本质上是$\Delta t \to 0$的框架，却要用于$\Delta t \to 1$的单步生成，这本身是"强模型所难"。能否换一个建模目标——直接学习有限时间区间上的"平均速度"——来实现原则上的单步生成？

## 关键结论

1. 定义平均速度$\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t) = \frac{1}{t-r}\int_r^t \boldsymbol{v}_\theta(\boldsymbol{x}_\tau, \tau)d\tau$，满足$\boldsymbol{x}_t - \boldsymbol{x}_r = (t-r)\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t)$，理论上可精准一步生成。
2. 通过恒等变换将平均速度与瞬时速度联系起来，代入ReFlow得到第一目标（理论上最优但需二阶梯度）。
3. 引入stop_gradient获得第二目标（节省计算，效果无损）和第三目标（最实用，但有标签泄漏）。
4. sCM是MeanFlow在$r=0$时的特例；MeanFlow的双时间参数$(r,t)$让ReFlow在$r=t$时"兜底"，提高了稳定性。

## 核心推导

### 恒等关系
从平均速度定义两边对$t$求导得到Identity 1：
$$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t) = \boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t) + (t-r)\left[\frac{d\boldsymbol{x}_t}{dt}\cdot\frac{\partial}{\partial\boldsymbol{x}_t}\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t) + \frac{\partial}{\partial t}\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t)\right]$$

Identity 2：$\lim_{r\to t}$平均速度=瞬时速度，即$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t) = \boldsymbol{u}_\theta(\boldsymbol{x}_t, t, t)$。

### 三个目标
- **第一目标**：Identity 2代入Identity 1再代入ReFlow——纯理论最优，需二阶梯度
- **第二目标**：第一目标+JVP部分加sg——节省计算，理论最优不变
- **第三目标**（MeanFlow最终方案）：将$d\boldsymbol{x}_t/dt$替换为$\boldsymbol{x}_1-\boldsymbol{x}_0$+sg——更高效但有标签泄漏

### 最优性证明
对第三目标求梯度为零，导出$\frac{d}{dt}[(t-r)\boldsymbol{u}_{\theta^*}(\boldsymbol{x}_t, r, t) - (\boldsymbol{x}_t - \boldsymbol{x}_r)] = 0$，在适当边界条件下得到期望结果。

## 关键公式

| 公式 | 含义 |
|------|------|
| $\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t) \triangleq \frac{1}{t-r}\int_r^t \boldsymbol{v}_\theta(\boldsymbol{x}_\tau, \tau)d\tau$ | 平均速度定义 |
| 第三目标公式(eq.6) | MeanFlow实用损失函数 |
| $\boldsymbol{u}_\theta(\boldsymbol{x}_t, r, t) = \frac{1}{2}[\boldsymbol{u}_\theta(\boldsymbol{x}_t, s, t) + \boldsymbol{u}_\theta(\boldsymbol{x}_s, r, s)], s = (r+t)/2$ | Shortcut自一致性在MeanFlow中的形式 |

## 实验或案例

本文为教学性文章。原始MeanFlow论文声称同时满足三个标准：清晰数学、单阶段训练、接近SOTA的单步生成（可多步改进）。

## 系列定位

本文是加速生成系列的集大成之作，对Shortcut（文章27）和CM/sCM（文章28）提供了统一视角。作者指出Shortcut缺乏严格理论支撑而MeanFlow补全了这一点，sCM是$r=0$的特殊情况。
