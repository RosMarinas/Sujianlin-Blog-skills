---
title: 从梯度最大化看Attention的Scale操作
definition: 定义Softmax梯度的L1范数为优化目标，从最大化梯度角度探讨Attention Scale因子的最优选择，揭示标准1/sqrt(d)并非最优。
type: concept
source_url: https://spaces.ac.cn/archives/9812
date: '2023-10-22'
author: 苏剑林
tags:
- Attention
- Scale
- Softmax
- 梯度
- 温度参数
status: draft
updated: '2026-06-12'
source_ids:
- '9812'
sources:
- （待从源文章提取）
---

# 从梯度最大化看Attention的Scale操作

## 概述
定义Softmax梯度的L1范数为优化目标，从最大化梯度角度探讨Attention Scale因子的最优选择，揭示标准1/sqrt(d)并非最优。

## 核心思想
1. Softmax雅可比矩阵的L1范数: 0.5*||dp/ds||_1 = alpha*(1 - sum_i p_i^2)
2. 以梯度最大化为目标，求解最优alpha。
3. 正态分布下最优alpha ~ 2.5，建议scale取2.5/sqrt(d)。
4. 余弦分布下最优alpha ~ 25~35，解释cos相似度需乘30左右的温度。

## 与熵不变性的联系
优化目标中出现Reniy熵，最大化使熵关于n变化缓慢，约等于熵不变性。