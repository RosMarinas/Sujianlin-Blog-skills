---
type: article_summary
title: "生成扩散模型漫谈（四）：DDIM = 高观点DDPM"
article_id: "9181"
source_url: https://spaces.ac.cn/archives/9181
date: 2022-07-27
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-07-27-生成扩散模型漫谈-四-DDIM-高观点DDPM.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[DDIM]]"
  - "[[待定系数法]]"
  - "[[前向扩散过程]]"
  - "[[反向去噪过程]]"
  - "[[累积信号率]]"
  - "[[噪声预测网络]]"
evidence_spans:
  - ev::9181::待定系数
  - ev::9181::加速生成
  - ev::9181::微分方程
  - ev::9181::实验结果
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-07-27-生成扩散模型漫谈-四-DDIM-高观点DDPM.md
source_ids:
  - "9181"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从"高观点"视角重新审视DDPM，去掉了推导中对 $p(x_t|x_{t-1})$ 的依赖，通过待定系数法得到一族由 $\sigma_t$ 参数化的反向过程（DDIM），其中 $\sigma_t=0$ 的确定性过程可实现加速采样和隐空间插值。

## 核心问题

DDPM的推导是否真的需要 $p(x_t|x_{t-1})$（单步前向转移）？如果去掉这一依赖，能否得到更一般的框架？如何在不重新训练模型的前提下加速采样？

## 关键结论

- DDPM的推导本质上只需要边际分布 $p(x_t|x_0)$，不需要 $p(x_t|x_{t-1})$。这一观察催生了DDIM。
- 通过待定系数法，仅从边际条件 $\int p(x_{t-1}|x_t, x_0) p(x_t|x_0) dx_t = p(x_{t-1}|x_0)$ 求解，得到一族由 $\sigma_t$ 参数化的反向过程，DDPM是其中一个特例（$\sigma_t = \bar{\beta}_{t-1}\beta_t/\bar{\beta}_t$）。
- DDPM训练结果隐含着对任意子序列的训练：T步训练的模型可用于任意子序列 $\tau = [\tau_1, \dots, \tau_{\dim(\tau)}]$ 的采样，从而实现加速生成。
- 当 $\sigma_t = 0$ 时，反向过程是确定性的，可从噪声到图像建立一一映射，支持球面插值。
- 确定性DDIM等价于求解常微分方程（ODE），可借助欧拉法、Heun法、R-K法等数值方法进一步加速。

## 核心推导

文章从第三篇的关键公式 $p(x_{t-1}|x_t, x_0)$ 出发，注意到损失函数只依赖于 $p(x_t|x_0)$、采样只依赖于 $p(x_{t-1}|x_t)$，整个链条中 $p(x_t|x_{t-1})$ 实际上可以去掉。设 $p(x_{t-1}|x_t, x_0) = \mathcal{N}(\kappa_t x_t + \lambda_t x_0, \sigma_t^2 I)$，代入边际条件 $\int p(x_{t-1}|x_t, x_0) p(x_t|x_0) dx_t = p(x_{t-1}|x_0)$，得到两个方程 $\bar{\alpha}_{t-1} = \kappa_t \bar{\alpha}_t + \lambda_t$ 和 $\bar{\beta}_{t-1} = \sqrt{\kappa_t^2 \bar{\beta}_t^2 + \sigma_t^2}$。三个未知数两个方程，解出 $\kappa_t, \lambda_t$ 关于 $\sigma_t$ 的表达式。代入去噪模型 $\bar{\mu}(x_t)$ 后得到通用采样公式。对于加速生成，注意到损失函数仅使用 $\bar{\alpha}_t$ 和 $\bar{\beta}_t$，因此T步训练隐含着对子序列 $\tau$ 的训练，将采样公式中的 $t$ 替换为 $\tau_i$、$t-1$ 替换为 $\tau_{i-1}$ 即得加速采样公式。将 $\sigma_t = 0$ 的确定性公式改写为差分形式 $\frac{x_t}{\bar{\alpha}_t} - \frac{x_{t-1}}{\bar{\alpha}_{t-1}} = (\frac{\bar{\beta}_t}{\bar{\alpha}_t} - \frac{\bar{\beta}_{t-1}}{\bar{\alpha}_{t-1}})\epsilon_\theta(x_t, t)$，取连续极限得到 ODE。

## 关键公式

**通用形式 $p(x_{t-1}|x_t, x_0)$：**
$$p(x_{t-1}|x_t, x_0) = \mathcal{N}(x_{t-1}; \kappa_t x_t + \lambda_t x_0, \sigma_t^2 I)$$

**从边际条件解出的参数（式5）：**
$$\kappa_t = \frac{\sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}}{\bar{\beta}_t}, \quad \lambda_t = \bar{\alpha}_{t-1} - \frac{\bar{\alpha}_t \sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}}{\bar{\beta}_t}$$

**最终采样分布（式7）：**
$$p(x_{t-1}|x_t) \approx \mathcal{N}\left(x_{t-1}; \frac{1}{\alpha_t}\left(x_t - \left(\bar{\beta}_t - \alpha_t\sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}\right) \epsilon_\theta(x_t, t)\right), \sigma_t^2 I\right)$$

**DDPM特例（$\sigma_t = \frac{\bar{\beta}_{t-1}\beta_t}{\bar{\beta}_t}$）：**
$$p(x_{t-1}|x_t) = \mathcal{N}\left(x_{t-1}; \frac{1}{\alpha_t}\left(x_t - \frac{\beta_t^2}{\bar{\beta}_t} \epsilon_\theta(x_t, t)\right), \frac{\bar{\beta}_{t-1}^2 \beta_t^2}{\bar{\beta}_t^2} I\right)$$

**DDIM确定性采样（$\sigma_t = 0$，式9）：**
$$x_{t-1} = \frac{1}{\alpha_t}\left(x_t - (\bar{\beta}_t - \alpha_t \bar{\beta}_{t-1}) \epsilon_\theta(x_t, t)\right)$$

**ODE形式（式12）：**
$$\frac{d}{ds}\left(\frac{x(s)}{\bar{\alpha}(s)}\right) = \epsilon_\theta(x(s), t(s)) \frac{d}{ds}\left(\frac{\bar{\beta}(s)}{\bar{\alpha}(s)}\right)$$

**球面插值：**
$$z = z_1 \cos\frac{\lambda\pi}{2} + z_2 \sin\frac{\lambda\pi}{2}, \quad \lambda \in [0, 1]$$

## 实验或案例

作者引用DDIM论文的实验结论：噪声越小加速生成效果越好。自身实验发现：(1) 反直觉地，$\sigma_t$ 越小生成图像的噪声和多样性反而越大；(2) 步数越少图像越平滑、多样性降低；(3) 步数减少时可适当降低 $\sigma_t$ 保持质量；(4) $\sigma_t$ 较小时固定Sinusoidal编码优于可学习Embedding；(5) 确定性生成总体上不如随机生成鲁棒，受架构影响更大。展示了 $\sigma_t=0$ 时噪声向量的球面插值结果，呈现平滑的语义过渡。

## 系列定位

本文是系列的第四篇，在第三篇贝叶斯推导的基础上实现了关键突破。独特贡献：(1) 首次指出 $p(x_t|x_{t-1})$ 在DDPM推导中是不必要的，提供了更高视角的理解；(2) 得到带自由参数 $\sigma_t$ 的通用框架，将DDPM作为特例包含在内；(3) 实现了无需重新训练模型的加速采样；(4) 通过ODE连接为第五篇（SDE一般框架）搭建了桥梁。
