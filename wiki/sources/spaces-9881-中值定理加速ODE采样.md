---
type: article_summary
title: 生成扩散模型漫谈（二十一）：中值定理加速ODE采样
article_id: "9881"
source_url: https://spaces.ac.cn/archives/9881
date: 2023-12-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-12-07-生成扩散模型漫谈-二十一-中值定理加速ODE采样.md
series: [生成扩散模型漫谈]
concepts: [中值定理加速, 概率流ODE]
methods: [AMED-Solver]
evidence_spans:
  - 9881-欧拉方法
  - 9881-高阶方法
  - 9881-中值定理
  - 9881-实验结果
  - 9881-假设分析
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-12-07-生成扩散模型漫谈-二十一-中值定理加速ODE采样.md
source_ids:
  - "9881"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文提出AMED（Approximate MEan-Direction Solver），通过类比积分中值定理为扩散ODE采样定制一种新型求解器，以极低的蒸馏成本（CIFAR10上单张A100仅需不到20分钟）在极低NFE（<=5）条件下取得SOTA加速采样效果。

## 核心问题

扩散模型的ODE采样过程可以形式化为求解 $d\boldsymbol{x}_t/dt = \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)$。传统的ODE求解器（Euler、Heun、DPM-Solver-2等）都是针对一般ODE的"通法"，没有针对扩散模型的特点进行定制，因此难以将采样步数降到极致（个位数）。如何在极低NFE条件下实现高质量的扩散模型采样？

## 关键结论

1. 扩散ODE的采样轨迹经PCA分析几乎落在二维子空间中，甚至接近一条直线，使得向量函数的积分中值定理近似成立。
2. 在NFE <= 5时，二阶通法（DPM-Solver、Heun）效果反而不如一阶DDIM，因为大步长下高阶方法误差反而更大。
3. 通过小网络预测最优采样点并结合蒸馏训练，AMED在低NFE下全面超越已有方法。
4. 蒸馏成本极低（CIFAR10单张A100 < 20分钟），远低于传统蒸馏方法（数天至数十天）。

## 核心推导

AMED的核心推导从积分形式的ODE出发：

$$\boldsymbol{x}_{t_{n+1}} - \boldsymbol{x}_{t_n} = \int_{t_n}^{t_{n+1}}\boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)dt$$

对标量函数，积分中值定理保证存在 $s_n \in (t_n, t_{n+1})$ 使得积分等于 $\boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_{s_n}, s_n)(t_{n+1} - t_n)$。对于向量函数这仅是近似，但扩散ODE轨迹的低维性使该近似成立。AMED使用小网络 $s_n = g_{\boldsymbol{\phi}}(\boldsymbol{h}_{t_{n+1}}, t_{n+1})$ 预测最优采样点，其中 $\boldsymbol{h}_{t_{n+1}}$ 是U-Net的中间特征；$\boldsymbol{x}_{s_n}$ 则用欧拉方法预估。

## 关键公式

扩散ODE定义：
$$\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t), \quad t \in [0, T]$$

AMED迭代格式：
$$\boldsymbol{x}_{t_n} \approx \boldsymbol{x}_{t_{n+1}} - \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_{s_n}, s_n)(t_{n+1} - t_n)$$

其中 $s_n = g_{\boldsymbol{\phi}}(\boldsymbol{h}_{t_{n+1}}, t_{n+1})$ 由小网络预测。

EDM时间离散化：
$$t_n = \left(t_1^{1/\rho} + \frac{n-1}{N-1}\left(t_N^{1/\rho} - t_1^{1/\rho}\right)\right)^\rho, \quad \rho > 0$$

AFS（Analytical First Step）技巧：利用 $\boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_{t_N}, t_N) \approx \boldsymbol{x}_{t_N}$ 省去第一步的NFE。

## 实验或案例

- 在CIFAR10、ImageNet等数据集上，AMED-Solver和AMED-Plugin在NFE <= 5时取得全面SOTA。
- PCA分析显示扩散ODE轨迹的top1主成分保留大部分精度，top2主成分几乎可以忽略误差。
- 蒸馏成本：CIFAR10单张A100 < 20分钟；256x256图像4张A100数小时。
- 表格中奇数的NFE来自AFS技巧，它减少了1个NFE。

## 系列定位

作为"生成扩散模型漫谈"系列的第21篇，本文聚焦于ODE采样的加速技术，在前序文章（第6、12、14、15、17篇）建立的扩散ODE框架基础上，提出了一种"定制化"而非"通用"的求解器思路，代表了采样加速从"通法改进"到"定制蒸馏"的方向转变。
