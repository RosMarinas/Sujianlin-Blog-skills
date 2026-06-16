---
type: article_summary
title: 能量视角下的GAN模型（三）：生成模型=能量模型
article_id: "6612"
source_url: https://spaces.ac.cn/archives/6612
date: 2019-05-10
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-05-10-能量视角下的GAN模型-三-生成模型-能量模型.md
series:
  - [[能量视角下的GAN模型]]
topics:
  - [[生成模型]]
concepts:
  - [[能量模型]]
methods:

evidence_spans:
  - ev::6612::Langevin采样
  - ev::6612::Buffer机制
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-05-10-能量视角下的GAN模型-三-生成模型-能量模型.md
source_ids:
  - "6612"
status: draft
updated: 2026-06-10
---
# 能量视角下的GAN模型（三）：生成模型＝能量模型

## 文章核心问题

能否不依赖生成器网络，直接用Langevin动力学从能量分布中采样并训练能量模型？

## 主要结论

能量分布是特定Langevin方程的静态分布。利用Langevin方程 x_{t+1} = x_t - (ε/2)∇U(x_t) + √εα 可直接从能量分布采样，从而完成能量模型的训练与生成。训练需使用谱归一化、L2能量正则和一个Buffer机制来维持多样性。

## 推导结构

1. 能量分布的Langevin采样理论
2. 训练细节：谱归一化、L2正则、Buffer
3. 训练完成后的生成过程

## 关键公式

x_{t+1} = x_t - (ε/2)∇U(x_t) + √εα — Langevin方程采样

## 所属系列位置

系列第三篇，探讨纯能量模型（不含显式生成器）的训练与生成。

## 与扩散模型的关系

Langevin采样方法在扩散模型中被广泛使用，两者共享随机微分方程的理论基础。

## 原文证据锚点

- ev::6612::Langevin采样 — 能量模型的Langevin采样
- ev::6612::Buffer机制 — 维持采样多样性的Buffer策略
