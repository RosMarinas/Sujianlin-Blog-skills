---
type: article_summary
title: 生成扩散模型漫谈（二十七）：将步长作为条件输入
article_id: "10617"
source_url: https://spaces.ac.cn/archives/10617
date: 2024-12-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-12-15-生成扩散模型漫谈-二十七-将步长作为条件输入.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[捷径模型]]"
  - "[[步长条件输入]]"
  - "[[自一致性损失]]"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-12-15-生成扩散模型漫谈-二十七-将步长作为条件输入.md
source_ids:
  - "10617"
status: draft
updated: 2026-06-09
---

# 生成扩散模型漫谈（二十七）：将步长作为条件输入

## 一句话总结

本文介绍Shortcut Models（arXiv:2410.12557），其核心思想是将生成步长$\epsilon$也作为扩散模型的条件输入，配合一个自一致性正则项，实现单阶段训练即可单步生成，无需蒸馏或对抗训练。

## 核心问题

扩散模型采样加速的主流思路（高效求解器、事后蒸馏）都很难将NFE降低到1（单步生成）。SiD能做到单步生成但需要额外的蒸馏成本和类似GAN的交替训练。是否存在一种方法，从零训练就能得到单步生成的扩散模型？

## 关键结论

1. 将步长$\epsilon$作为条件输入到速度模型$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, \epsilon)$中，使模型自适应不同的离散化步长。
2. 自一致性条件：用步长$2\epsilon$走一步应等于用步长$\epsilon$走两步的结果，由此构造的正则项$\mathcal{L}_2$可稳定训练。
3. 该方法在ICLR 2025获得全8分review，是单阶段训练扩散模型中单步生成效果最好的。
4. 与AMED（中值定理加速）的核心思想相通：真正要变的不是求解器，而是模型本身。

## 核心推导

### ReFlow ODE框架
使用线性插值轨迹 $\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1$（$\boldsymbol{x}_0$为噪声，$\boldsymbol{x}_1$为数据），ODE速度为$\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{x}_1 - \boldsymbol{x}_0$，训练速度模型$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t)$逼近$\boldsymbol{x}_1 - \boldsymbol{x}_0$。

### Shortcut模型的核心创新
将步长$\epsilon$作为额外条件，定义$\boldsymbol{x}_{t+\epsilon} - \boldsymbol{x}_t = \boldsymbol{v}_\theta(\boldsymbol{x}_t, t, \epsilon)\epsilon$。

损失函数由两部分组成：
- $\mathcal{L}_1$：精确ODE条件（$\epsilon=0$），训练$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, 0)$逼近$\boldsymbol{x}_1 - \boldsymbol{x}_0$
- $\mathcal{L}_2$：自一致性正则，要求$\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, 2\epsilon) = [\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, \epsilon) + \boldsymbol{v}_\theta(\tilde{\boldsymbol{x}}_{t+\epsilon}, t+\epsilon, \epsilon)]/2$

### 训练细节
- $\epsilon$取9个离散值$\{0, 2^{-7}, 2^{-6}, ..., 2^{-1}, 1\}$，通过Embedding加入模型
- 混合batch训练：3/4样本训练$\mathcal{L}_1$，1/4训练$\mathcal{L}_2$
- 对$\mathcal{L}_2$的教师项使用stop_gradient以节省计算

## 关键公式

| 公式 | 含义 |
|------|------|
| $\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1$ | ReFlow线性插值轨迹 |
| $\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{x}_1 - \boldsymbol{x}_0$ | ODE速度 |
| $\boldsymbol{x}_{t+\epsilon} - \boldsymbol{x}_t = \boldsymbol{v}_\theta(\boldsymbol{x}_t, t, \epsilon)\epsilon$ | Shortcut模型的欧拉步进 |
| $\mathcal{L}_2 = \mathbb{E}[\|\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, 2\epsilon) - \text{sg}[\boldsymbol{v}_\theta(\boldsymbol{x}_t, t, \epsilon) + \boldsymbol{v}_\theta(\tilde{\boldsymbol{x}}_{t+\epsilon}, t+\epsilon, \epsilon)]/2\|^2]$ | 自一致性损失 |

## 实验或案例

- 在单步生成任务上，Shortcut Model达到同阶段训练方法中SOTA水平
- 单步生成样本仍有可见瑕疵，说明有改进空间
- 开源代码：https://github.com/kvfrans/shortcut-models
- ICLR 2025全8分接收

## 系列定位

本文是扩散模型加速生成系列的开篇，后续文章28（一致性模型）、30（平均速度MeanFlow）延续了这一主线。Shortcut的"双时间参数"思想和自一致性正则，分别在MeanFlow中获得更严格的数学基础。
