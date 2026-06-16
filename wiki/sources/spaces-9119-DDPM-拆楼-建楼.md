---
type: article_summary
title: "生成扩散模型漫谈（一）：DDPM = 拆楼 + 建楼"
article_id: "9119"
source_url: https://spaces.ac.cn/archives/9119
date: 2022-06-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-06-13-生成扩散模型漫谈-一-DDPM-拆楼-建楼.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[DDPM]]"
  - "[[前向扩散过程]]"
  - "[[反向去噪过程]]"
  - "[[方差保持约束]]"
  - "[[累积信号率]]"
  - "[[噪声预测网络]]"
  - "[[重参数化技巧]]"
methods:
  - "[[方差消减技术]]"
evidence_spans:
  - ev::9119::新的起点
  - ev::9119::拆楼建楼
  - ev::9119::该如何拆
  - ev::9119::降低方差
  - ev::9119::超参设置
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-13-生成扩散模型漫谈-一-DDPM-拆楼-建楼.md
source_ids:
  - "9119"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文通过"拆楼-建楼"的通俗类比引入DDPM（去噪扩散概率模型），仅利用正态分布的叠加性等基本概率论知识推导了DDPM的训练和采样过程，无需变分推断、得分匹配或朗之万动力学等复杂数学工具。

## 核心问题

如何用直观的方式理解DDPM这一新兴生成模型，并仅用基础数学工具完成其理论推导？DDPM与传统基于能量模型和朗之万采样的扩散模型有何本质区别？

## 关键结论

- DDPM与传统扩散模型有根本性不同：传统模型使用能量模型、得分匹配和朗之万动力学，而DDPM采用逐步加噪/去噪的"渐变模型"框架，更准确的名称应是"渐变模型"而非"扩散模型"。
- DDPM可以用仅包含正态分布叠加性的基本概率论完成完整推导，不需要变分推断。
- 方差保持约束 $\alpha_t^2 + \beta_t^2 = 1$ 是关键设计，它确保了信号方差在整个前向过程中保持恒定，从而导出简洁的 $x_t = \bar{\alpha}_t x_0 + \bar{\beta}_t \bar{\varepsilon}_t$ 形式。
- 大T值（T=1000）的必要性源于欧氏距离损失函数：欧氏距离仅在输入输出足够接近时效果良好，大T保证了每一步的变化足够小。
- DDPM相比PixelRNN/PixelCNN减少了归纳偏置（Inductive Bias），对像素的处理是平权的。

## 核心推导

文章从"拆楼"（前向过程）的数学建模开始：$x_t = \alpha_t x_{t-1} + \beta_t \varepsilon_t$，其中 $\alpha_t^2 + \beta_t^2 = 1$。反复展开该递推式，利用正态分布叠加性，将多个独立噪声项合并为单个正态随机变量，得到关键的单步跳跃公式 $x_t = \bar{\alpha}_t x_0 + \bar{\beta}_t \bar{\varepsilon}_t$。在"建楼"（反向过程）中，将生成模型参数化为 $\mu(x_t) = \frac{1}{\alpha_t}(x_t - \beta_t \epsilon_\theta(x_t, t))$，代入欧氏距离损失后得到 $\|\varepsilon_t - \epsilon_\theta(x_t, t)\|^2$ 形式的初步损失函数。进一步将 $x_t$ 展开为含 $\bar{\varepsilon}_{t-1}$ 和 $\varepsilon_t$ 两个独立噪声的表达式，通过变量代换将两个噪声合并为 $\varepsilon$ 和 $\omega$，再对 $\omega$ 做解析积分消去，最终获得方差降低后的简洁损失 $\|\varepsilon - \frac{\bar{\beta}_t}{\beta_t} \epsilon_\theta(\bar{\alpha}_t x_0 + \bar{\beta}_t \varepsilon, t)\|^2$。

## 关键公式

**前向单步（式1）：**
$$x_t = \alpha_t x_{t-1} + \beta_t \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, I), \quad \alpha_t^2 + \beta_t^2 = 1$$

**单步跳跃公式（式4）：**
$$x_t = \bar{\alpha}_t x_0 + \bar{\beta}_t \bar{\varepsilon}_t, \quad \bar{\varepsilon}_t \sim \mathcal{N}(0, I)$$
其中 $\bar{\alpha}_t = \alpha_1 \cdots \alpha_t$，$\bar{\beta}_t = \sqrt{1 - \bar{\alpha}_t^2}$。

**反向模型参数化（式5）：**
$$\mu(x_t) = \frac{1}{\alpha_t}(x_t - \beta_t \epsilon_\theta(x_t, t))$$

**最终损失函数（式9）——方差消减后：**
$$\left\|\varepsilon - \frac{\bar{\beta}_t}{\beta_t} \epsilon_\theta(\bar{\alpha}_t x_0 + \bar{\beta}_t \varepsilon, t)\right\|^2$$

**随机采样（式11）：**
$$x_{t-1} = \frac{1}{\alpha_t}(x_t - \beta_t \epsilon_\theta(x_t, t)) + \sigma_t z, \quad z \sim \mathcal{N}(0, I)$$

**DDPM的 $\alpha_t$ 调度：**
$$\alpha_t = \sqrt{1 - \frac{0.02t}{T}}$$

## 实验或案例

本文为纯理论推导，未提供实验。文章引用DALL-E 2和Imagen作为扩散模型在文本到图像生成中的SOTA应用案例。

## 系列定位

本文是整个"生成扩散模型漫谈"系列的开篇之作，建立了基础直觉和数学框架。其独特贡献在于：用最少的数学工具（仅正态分布叠加性）完成了DDPM的核心推导，让读者无需变分推理或能量模型背景即可入门。后续文章在此基础上分别从VAE、贝叶斯、DDIM和SDE视角逐步深化。
