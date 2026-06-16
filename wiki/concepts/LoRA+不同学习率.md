---
title: 配置不同的学习率，LoRA还能再涨一点？
definition: 介绍LoRA+论文结论：LoRA的B矩阵学习率应大于A矩阵学习率。从数值稳定和贡献相当两个假设出发，通过SignSGD简化分析推导出etaB
  >> etaA。
type: concept
source_url: https://spaces.ac.cn/archives/10001
date: '2024-02-27'
author: 苏剑林
tags:
- LoRA
- LoRA+
- 学习率
- 参数高效微调
- 初始化
status: draft
updated: '2026-06-12'
source_ids:
- '10001'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-02-27-配置不同的学习率-LoRA还能再涨一点.md
---

# 配置不同的学习率，LoRA还能再涨一点？

## 概述
介绍LoRA+论文结论：LoRA的B矩阵学习率应大于A矩阵学习率。从数值稳定和贡献相当两个假设出发，通过SignSGD简化分析推导出eta_B >> eta_A。

## 核心思想
1. 数值稳定：中间变量XA应为O(1)，导致A以方差1/n初始化，B以方差1/r初始化(n>>r)，A的分量绝对值小于B。
2. 贡献相当：每步更新中A、B对损失下降的贡献应一致。
3. SignSGD简化：beta1=beta2=0时Adam退化为SignSGD，可推导出eta_B >> eta_A。

## 关键推导
梯度不对称：grad_A = X^T (dL/dY) B^T, grad_B = A^T X^T (dL/dY)
因A分量远小于B分量，grad_A的分量远小于grad_B的分量，需要eta_B >> eta_A来平衡贡献。