---
type: article_summary
title: "生成扩散模型漫谈（三）：DDPM = 贝叶斯 + 去噪"
article_id: "9164"
source_url: https://spaces.ac.cn/archives/9164
date: 2022-07-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-07-19-生成扩散模型漫谈-三-DDPM-贝叶斯-去噪.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[DDPM]]"
  - "[[前向扩散过程]]"
  - "[[反向去噪过程]]"
  - "[[累积信号率]]"
  - "[[噪声预测网络]]"
  - "[[预测器-校正器]]"
evidence_spans:
  - ev::9164::请贝叶斯
  - ev::9164::去噪过程
  - ev::9164::预估修正
  - ev::9164::遗留问题
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-07-19-生成扩散模型漫谈-三-DDPM-贝叶斯-去噪.md
source_ids:
  - "9164"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文利用贝叶斯定理给出了DDPM最直接优雅的推导——通过计算条件分布 $p(x_{t-1}|x_t, x_0)$ 并训练去噪网络来估计 $x_0$，从而一步到位地得到反向采样过程，比前两篇的推导更简洁且更具启发性。

## 核心问题

能否找到DDPM的最简推导路径——无需变分推断、无需噪声变量积分消去，直接用贝叶斯定理从已知分布推导出反向过程？如何理解DDPM中迭代去噪的本质机制？

## 关键结论

- 贝叶斯推导是最直接的方法：通过 $p(x_{t-1}|x_t, x_0) = \frac{p(x_t|x_{t-1})p(x_{t-1}|x_0)}{p(x_t|x_0)}$ 可获得解析形式，再用去噪模型 $\bar{\mu}(x_t)$ 替换 $x_0$ 即得反向过程。
- DDPM本质上是一个"预估-修正"（Predictor-Corrector）过程：去噪模型提供一个对 $x_0$ 的粗略预估，贝叶斯公式用此预估完成一步精细修正，类似于数值ODE求解器和Hinton的Lookahead Optimizer。
- 采样方差 $\sigma_t$ 的两个候选值可通过分析极端数据分布得到：单样本情形 $\sigma_t = \frac{\bar{\beta}_{t-1}\beta_t}{\bar{\beta}_t}$，标准正态数据情形 $\sigma_t = \beta_t$。两者在实践中效果相似。

## 核心推导

从贝叶斯定理出发，在给定 $x_0$ 的条件下计算 $p(x_{t-1}|x_t, x_0)$。代入三个已知正态分布 $p(x_t|x_{t-1})$、$p(x_{t-1}|x_0)$、$p(x_t|x_0)$ 的表达式，将指数部分展开为关于 $x_{t-1}$ 的二次型。通过提取 $\|x_{t-1}\|^2$ 系数得到方差 $\frac{\bar{\beta}_{t-1}^2 \beta_t^2}{\bar{\beta}_t^2} I$，提取一次项系数得到均值 $\frac{\alpha_t \bar{\beta}_{t-1}^2}{\bar{\beta}_t^2} x_t + \frac{\bar{\alpha}_{t-1} \beta_t^2}{\bar{\beta}_t^2} x_0$。引入去噪模型 $\bar{\mu}(x_t) = \frac{1}{\bar{\alpha}_t}(x_t - \bar{\beta}_t \epsilon_\theta(x_t, t))$ 替换 $x_0$，化简均值系数后得到最终采样分布。损失函数来自最小化 $\|x_0 - \bar{\mu}(x_t)\|^2$，直接得到与DDPM原论文一致的噪声预测损失。

## 关键公式

**条件贝叶斯公式：**
$$p(x_{t-1}|x_t, x_0) = \frac{p(x_t|x_{t-1}) p(x_{t-1}|x_0)}{p(x_t|x_0)}$$

**解析形式的 $p(x_{t-1}|x_t, x_0)$（式3）：**
$$p(x_{t-1}|x_t, x_0) = \mathcal{N}\left(x_{t-1}; \frac{\alpha_t \bar{\beta}_{t-1}^2}{\bar{\beta}_t^2} x_t + \frac{\bar{\alpha}_{t-1} \beta_t^2}{\bar{\beta}_t^2} x_0, \frac{\bar{\beta}_{t-1}^2 \beta_t^2}{\bar{\beta}_t^2} I\right)$$

**去噪模型参数化（式7）：**
$$\bar{\mu}(x_t) = \frac{1}{\bar{\alpha}_t}(x_t - \bar{\beta}_t \epsilon_\theta(x_t, t))$$

**最终反向采样分布（式10）：**
$$p(x_{t-1}|x_t) \approx \mathcal{N}\left(x_{t-1}; \frac{1}{\alpha_t}\left(x_t - \frac{\beta_t^2}{\bar{\beta}_t} \epsilon_\theta(x_t, t)\right), \frac{\bar{\beta}_{t-1}^2 \beta_t^2}{\bar{\beta}_t^2} I\right)$$

## 实验或案例

本文为纯理论推导，未提供新实验。但引用第二篇的实验结论——两个 $\sigma_t$ 选择在实践中表现相似，并通过理论分析为此提供了数学依据。

## 系列定位

本文是系列的第三篇，提供了DDPM的第三种推导路径——可以视为最优雅的推导。与前两篇相比：(1) 比第一篇的直观类比更严格；(2) 比第二篇的VAE推导更直接，无需积分消去噪声变量。其独特贡献是建立了"预估-修正"的直觉框架，并直接为第四篇（DDIM）铺平了道路——DDIM所使用的 $p(x_{t-1}|x_t, x_0)$ 正是本文的核心结果。
