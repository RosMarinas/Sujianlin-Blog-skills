---
type: article_summary
title: "隐藏在动量中的梯度累积：少更新几步，效果反而更好？"
article_id: "8634"
source_url: https://spaces.ac.cn/archives/8634
date: 2021-08-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-08-24-隐藏在动量中的梯度累积-少更新几步-效果反而更好.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[梯度累积]]"
  - "[[动量梯度累积等价性]]"
evidence_spans:
  - "ev::8634::SGDM分拆"
  - "ev::8634::Adam近似累积"
  - "ev::8634::beta调换等价性"
  - "ev::8634::少更新有效"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-24-隐藏在动量中的梯度累积-少更新几步-效果反而更好.md
source_ids:
  - "8634"
status: draft
updated: 2026-06-12
---

# 隐藏在动量中的梯度累积：少更新几步，效果反而更好？

## Summary

本文发现梯度累积可内置于带动量的优化器（SGDM和Adam）中，无需新增参数缓存。将动量系数β调整为1-(1-β)/k即可近似k步梯度累积，且仅减少参数更新频率本身就有正面效果。

## Key Claims

1. SGDM的梯度累积可通过修改动量更新公式实现，无需额外参数缓存。
2. Adam的二阶矩v因平方操作无法精确分拆，但"平方的平均≈平均的平方"假设下可近似实现。
3. 调整β为1-(1-β)/k并每k步更新一次参数，等价于梯度累积。
4. 仅降低参数更新频率（不调整β）也能改善小batch_size训练效果。

## Key Formulas

- SGDM梯度累积分拆: m_t = [(β-1)χ_{(t-1)/k}+1]m_{t-1} + (1-β)/k·g_t
- 参数更新: θ_t = θ_{t-1} - χ_{t/k}·α_t·m_t
- β调换: β̃ = 1 - (1-β)/k, 则β̃^k ≈ β

## Connections

本文的梯度累积与7469的梯度裁剪分享相同动机：改进优化器以加速和稳定训练。Adam近似累积的不精确性与7681中AdamW（L2正则与权重衰减在Adam下不等价）都涉及Adam优化器中的近似问题。
