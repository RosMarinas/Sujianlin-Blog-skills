---
type: article_summary
title: 生成扩散模型漫谈（二十）：从ReFlow到WGAN-GP
article_id: "9668"
source_url: https://spaces.ac.cn/archives/9668
date: 2023-06-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-06-28-生成扩散模型漫谈-二十-从ReFlow到WGAN-GP.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[矫流]]"
  - "[[零中心梯度惩罚]]"
  - "[[扩散ODE与GAN等价]]"
methods:
  - "[[矫流构造法]]"
evidence_spans:
  - ev::9668::理论回顾
  - ev::9668::相对运动
  - ev::9668::WGAN-GP
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-06-28-生成扩散模型漫谈-二十-从ReFlow到WGAN-GP.md
source_ids:
  - "9668"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从Rectified Flow（矫流）这一极简的扩散ODE构造框架出发，通过"梯度场"假设和有限差分近似，直接推导出了WGAN-GP的损失函数，提供了一个比Wasserstein梯度流路径更简单直观的GAN-扩散模型统一框架。

## 核心问题

第19篇使用Wasserstein梯度流（一种相对复杂的最优传输理论工具）建立了GAN作为扩散ODE的视角，但该路径在技术上与扩散主线的其他内容存在"断层"。能否使用更简单、与扩散系列更一致的Rectified Flow框架来重新建立GAN与扩散模型的联系？

## 关键结论

1. **ReFlow蕴含WGAN-GP**：在速度场$\boldsymbol{v}_{\boldsymbol{\varphi}}$是标量势$D_{\boldsymbol{\varphi}}$的梯度这一假设下，ReFlow的学习目标直接退化为WGAN-GP的判别器损失。
2. **梯度惩罚的自然出现**：ReFlow的展开式$\frac{1}{2}\|\boldsymbol{v}\|^2 - \langle\boldsymbol{v}, \boldsymbol{x}_1-\boldsymbol{x}_0\rangle$在梯度场假设下变为$\frac{1}{2}\|\nabla D\|^2 - dD/dt$，其中$\frac{1}{2}\|\nabla D\|^2$正是梯度惩罚项。
3. **零中心梯度惩罚**：推导自然产生以零为中心的梯度惩罚$\|\nabla D\|^2$（而非原始WGAN-GP中以1为中心），已有文献表明零中心效果通常更好。
4. **插值轨迹相同**：WGAN-GP在真假样本间线性插值（用于梯度惩罚）与ReFlow的直线轨迹$\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1$完全一致。
5. **生成器损失的继承**：生成器更新$\mathbb{E}[-D(\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}))]$在第19篇中已证明，此处直接使用。

## 核心推导

从ReFlow到WGAN-GP的推导仅需三步：

**步骤1**：从ReFlow目标出发（省略与$\boldsymbol{\varphi}$无关的$\frac{1}{2}\|\boldsymbol{x}_1-\boldsymbol{x}_0\|^2$项）：
$$\mathbb{E}\left[\frac{1}{2}\|\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)\|^2 - \langle\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t), \boldsymbol{x}_1-\boldsymbol{x}_0\rangle\right]$$

**步骤2**：假设$\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t) = \nabla_{\boldsymbol{x}_t} D_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)$（梯度场），则$\langle\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t), \boldsymbol{x}_1-\boldsymbol{x}_0\rangle = \langle\nabla D, d\boldsymbol{x}_t/dt\rangle = dD/dt$：
$$\mathbb{E}\left[\frac{1}{2}\|\nabla D_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)\|^2 - \frac{d D_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)}{dt}\right]$$

**步骤3**：假设$D$变化平稳，用有限差分近似时间导数$dD/dt \approx D(\boldsymbol{x}_1) - D(\boldsymbol{x}_0)$：
$$\mathbb{E}\left[\frac{1}{2}\|\nabla D_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)\|^2 - D_{\boldsymbol{\varphi}}(\boldsymbol{x}_1) + D_{\boldsymbol{\varphi}}(\boldsymbol{x}_0)\right]$$

这正是WGAN-GP的判别器损失——最大化$\mathbb{E}[D(\text{real})] - \mathbb{E}[D(\text{fake})]$同时对插值点施加梯度惩罚$\|\nabla D\|^2$。

## 关键公式

**ReFlow直线插值**：
$$\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t \boldsymbol{x}_1$$

**ReFlow学习目标**：
$$\boldsymbol{\varphi}^* = \mathop{\text{argmin}}_{\boldsymbol{\varphi}} \mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_1}\left[\frac{1}{2}\Vert\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t, t) - (\boldsymbol{x}_1 - \boldsymbol{x}_0)\Vert^2\right]$$

**展开后忽略常数项**：
$$\frac{1}{2}\Vert\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)\Vert^2 - \langle\boldsymbol{v}_{\boldsymbol{\varphi}}(\boldsymbol{x}_t), \boldsymbol{x}_1 - \boldsymbol{x}_0\rangle$$

**梯度场假设下转换为WGAN-GP损失**：
$$\frac{1}{2}\Vert\nabla D_{\boldsymbol{\varphi}}(\boldsymbol{x}_t)\Vert^2 - D_{\boldsymbol{\varphi}}(\boldsymbol{x}_1) + D_{\boldsymbol{\varphi}}(\boldsymbol{x}_0)$$

## 实验或案例

本文为纯理论推导，没有实验验证。作者指出推导中自然产生的零中心梯度惩罚$\|\nabla D\|^2$在已有工作（WGAN-div等）中被证明通常优于原始WGAN-GP的以1为中心的梯度惩罚。

## 系列定位

本文是系列第16-20篇"统一GAN与扩散模型"子主题的收官之作。它采用Rectified Flow（第17篇）作为起点，提供了一个比第19篇的Wasserstein梯度流路径更简单、与扩散系列主线更一致的统一框架。至此，五篇文章构成了一个完整的理论闭环：从W距离与得分匹配的联系（16），到ODE构建（17），到训练目标澄清（18），再到两种路径的GAN-扩散统一（19、20）。
