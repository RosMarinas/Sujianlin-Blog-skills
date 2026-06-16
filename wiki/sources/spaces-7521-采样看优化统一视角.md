---
type: article_summary
title: 从采样看优化：可导优化与不可导优化的统一视角
article_id: "7521"
source_url: https://spaces.ac.cn/archives/7521
date: 2020-06-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-06-23-从采样看优化-可导优化与不可导优化的统一视角.md
series: []
topics:
  - 采样与估计
  - 优化理论
concepts:
  - importance sampling
  - policy gradient
  - REINFORCE
methods:
  - 采样-优化统一视角
  - 梯度下降法
  - 牛顿法
  - 基于重要性采样的不可导优化
  - 策略梯度
problem_patterns:
  - 损失函数与评测指标不一致
evidence_spans:
  - "7521::采样视角"
  - "7521::梯度下降"
  - "7521::牛顿法"
  - "7521::重要性采样"
  - "7521::借力可导"
  - "7521::策略梯度"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-06-23-从采样看优化-可导优化与不可导优化的统一视角.md
source_ids:
  - "7521"
status: draft
updated: 2026-06-10
---

## 文章核心问题

提出一个统一的可导/不可导优化的采样视角：将参数更新量 $\Delta\theta$ 视为随机变量，构建分布 $p(\Delta\theta|\theta) \propto e^{-[l(\theta+\Delta\theta)-l(\theta)]/\alpha}$，然后取期望作为更新方向。

## 主要结论

- 对可导目标，一阶展开$\to$梯度下降，二阶展开$\to$牛顿法
- 对不可导目标，用可导近似作为重要性采样建议分布来估计更新量
- 与策略梯度（REINFORCE）的区别：前者采样参数空间，后者采样输出空间

## 推导结构

1. 定义采样视角下的通用更新量公式
2. 可导情形：泰勒展开至一阶$\to$梯度下降，至二阶$\to$牛顿法
3. 不可导情形：用可导目标 $\tilde{l}(\theta)$ 构造正态建议分布 $q(\Delta\theta|\theta)=\mathcal{N}(-\nabla\tilde{l},\sigma^2)$，用重要性采样估计 $\Delta\theta_*$
4. 与策略梯度的对比分析

## 关键公式

$$p(\Delta\theta|\theta)=\frac{e^{-[l(\theta+\Delta\theta)-l(\theta)]/\alpha}}{Z(\theta)},\quad \Delta\theta_*=\mathbb{E}_{\Delta\theta\sim p}[\Delta\theta]$$

一阶展开 $\to$ 梯度下降：$\Delta\theta_* \propto -g$

二阶展开 $\to$ 牛顿法：$\Delta\theta_* = -\mathcal{H}^{-1}g$

重要性采样估计不可导目标：$\Delta\theta_* \approx \sum_i \frac{e^{-[l(\theta+\Delta\theta_i)-l(\theta)]/\alpha}/q(\Delta\theta_i)}{\sum_j e^{-[l(\theta+\Delta\theta_j)-l(\theta)]/\alpha}/q(\Delta\theta_j)} \Delta\theta_i$

## 体现的方法

- 采样-优化统一框架（核心方法）
- 重要性采样用于不可导优化（现有方法的重要性采样新应用）
- 策略梯度对比分析

## 所属系列位置

单篇，连接采样理论与优化理论。

## 与其他文章的关系

重要性采样部分与本批次中NCE文章共享"estimate/sample instead of compute"操作类型。

## 原文证据锚点

- 采样视角定义：采样视角节
- 梯度下降推导：可导目标-梯度下降节
- 牛顿法推导：可导目标-牛顿法节
- 不可导优化：不可导目标-借力可导节
- 策略梯度对比：不可导目标-策略梯度节
