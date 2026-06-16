---
type: article_summary
title: 生成扩散模型漫谈（六）：一般框架之ODE篇
article_id: "9228"
source_url: https://spaces.ac.cn/archives/9228
date: 2022-08-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-08-08-生成扩散模型漫谈-六-一般框架之ODE篇.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[概率流ODE]]"
  - "[[Fokker-Planck方程]]"
  - "[[前向过程等价性]]"
methods:
  - "[[Fokker-Planck方程推导法]]"
evidence_spans:
  - ev::9228::再次反思
  - ev::9228::F-P方程
  - ev::9228::等价变换
  - ev::9228::神经ODE
  - ev::9228::回顾DDIM
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-08-生成扩散模型漫谈-六-一般框架之ODE篇.md
source_ids:
  - "9228"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文通过Fokker-Planck方程推导了前向SDE的等价变换，从而引入概率流ODE（Probability Flow ODE），并证明DDIM是其在线性漂移下的特例，完成了SDE框架到ODE框架的理论扩展。

## 核心问题

在SDE篇（第五篇）的基础上，如何将扩散模型从随机过程推广到确定性过程？不同的SDE是否可能产生相同的边际分布？DDIM在连续时间框架下的理论本质是什么？

## 关键结论

- 不同的前向SDE可以产生完全相同的边际分布$p_t(\boldsymbol{x})$，只要它们满足相同的Fokker-Planck方程，扩散系数$\sigma_t^2 \leq g_t^2$的约束成立。
- 当$\sigma_t = 0$时，SDE退化为概率流ODE，这是一个确定性方程，其解轨迹的边际分布与原SDE完全相同。
- 概率流ODE是DDIM的连续时间推广：当漂移函数$\boldsymbol{f}_t(\boldsymbol{x})$为线性函数$f_t \boldsymbol{x}$时，概率流ODE严格恢复DDIM ODE。
- 概率流ODE允许精确似然计算、隐变量表征，并可使用高阶ODE求解器加速生成。

## 核心推导

文章的核心推导围绕Fokker-Planck方程展开。首先，从离散时间前向SDE $\boldsymbol{x}_{t+\Delta t} = \boldsymbol{x}_t + \boldsymbol{f}_t(\boldsymbol{x}_t)\Delta t + g_t\sqrt{\Delta t}\boldsymbol{\varepsilon}$出发，利用Dirac delta函数将概率密度转换为期望形式，再通过泰勒展开至$\mathcal{O}(\Delta t)$阶并取期望，得到Fokker-Planck方程$\partial_t p_t = -\nabla\cdot[\boldsymbol{f}_t p_t] + \frac{1}{2}g_t^2\nabla^2 p_t$。关键技巧在于：将扩散项拆分为两部分，一部分吸收到漂移项中形成$\boldsymbol{f}_t - \frac{1}{2}(g_t^2 - \sigma_t^2)\nabla\log p_t$，另一部分保留为$\frac{1}{2}\sigma_t^2\nabla^2 p_t$。由于F-P方程形式相同，对应的SDE即为$d\boldsymbol{x} = (\boldsymbol{f}_t - \frac{1}{2}(g_t^2 - \sigma_t^2)\nabla\log p_t)dt + \sigma_t d\boldsymbol{w}$。令$\sigma_t=0$即得概率流ODE。最后，代入线性漂移参数化$f_t\boldsymbol{x}$并利用噪声预测网络$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}$与score $\boldsymbol{s}_{\boldsymbol{\theta}}$的关系，整理得到与DDIM ODE完全等价的表达式。

## 关键公式

**Fokker-Planck方程**：
$$\frac{\partial}{\partial t} p_t(\boldsymbol{x}) = -\nabla_{\boldsymbol{x}}\cdot[\boldsymbol{f}_t(\boldsymbol{x})p_t(\boldsymbol{x})] + \frac{1}{2}g_t^2\nabla_{\boldsymbol{x}}\cdot\nabla_{\boldsymbol{x}}p_t(\boldsymbol{x})$$

**等价前向SDE**（相同边际分布）：
$$d\boldsymbol{x} = \left(\boldsymbol{f}_t(\boldsymbol{x}) - \frac{1}{2}(g_t^2 - \sigma_t^2)\nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{x})\right) dt + \sigma_t d\boldsymbol{w}, \quad \sigma_t^2 \leq g_t^2$$

**概率流ODE**（$\sigma_t=0$）：
$$d\boldsymbol{x} = \left(\boldsymbol{f}_t(\boldsymbol{x}) - \frac{1}{2}g_t^2\nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{x})\right) dt$$

**DDIM ODE等价形式**（线性漂移特例）：
$$\frac{d}{dt}\left(\frac{\boldsymbol{x}}{\bar{\alpha}_t}\right) = \boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)\frac{d}{dt}\left(\frac{\bar{\beta}_t}{\bar{\alpha}_t}\right)$$

## 实验或案例

本文为纯理论推导，未提供实验。

## 系列定位

作为扩散模型系列的第六篇，本文填补了第五篇（SDE篇）留下的概率流ODE空白，将随机框架扩展到确定性框架，建立了SDE与ODE两个视角的统一。这一定性变换（$\sigma_t \to 0$）为后续加速采样（如高阶ODE求解器）、精确似然估计和隐空间编辑铺平了道路。文章同时深化了DDIM的理论基础，证明其本质上就是概率流ODE在线性漂移特殊情形下的表现。
