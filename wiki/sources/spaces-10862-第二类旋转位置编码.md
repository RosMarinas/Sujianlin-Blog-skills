---
type: article_summary
title: Transformer升级之路：19、第二类旋转位置编码
article_id: "10862"
source_url: https://spaces.ac.cn/archives/10862
date: 2025-04-18
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-04-18-Transformer升级之路-19-第二类旋转位置编码.md
series: [Transformer升级之路]
topics: [RoPE, Value编码, 相对位置, VO-RoPE]
concepts: [vo-rope, second-type-rope]
methods: []
problem_patterns: [RoPE在Value上的应用, 位置编码完备性]
evidence_spans:
  - 10862-基础回顾
  - 10862-新的用法
  - 10862-简单实验
  - 10862-一些思考
  - 10862-相关工作
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-18-Transformer升级之路-19-第二类旋转位置编码.md
source_ids:
  - "10862"
status: draft
updated: 2026-06-09
---

## 文章核心问题

RoPE能否加在Value（V）上？如果可以，效果如何？有什么理论意义？

## 主要结论

1. 将RoPE加在V上，再在Output上加逆向RoPE（即VO-RoPE），可实现另一种相对位置编码——第二类旋转位置编码。
2. 1B模型实验显示：QK-RoPE ≈ QKVO-RoPE > K-RoPE ≈ VO-RoPE > QKV-RoPE > NoPE > Q/V/O-RoPE。
3. VO-RoPE优于NoPE但不如QK-RoPE，且与QK-RoPE叠加无增益，目前看没有必须替代QK-RoPE的理由。
4. VO-RoPE提供了从Attention到复线性RNN（如LRU、RetNet）的中间形式——当a_{i,j}=γ^{i-j}时退化为复数Decay的线性RNN。
5. VO-RoPE的潜在应用：解决MLA中K、V共享与RoPE不兼容的问题。

## 推导结构

1. 回顾标准QK-RoPE的推导
2. 提出V加RoPE + O加逆向RoPE的方案
3. 实验对比多种排列组合
4. 讨论理论完备性和复线性RNN联系
5. 联系MLA的兼容性问题

## 关键公式

VO-RoPE: o_i = R_i^T Σ_j a_{i,j} R_j v_j = Σ_j a_{i,j} R_{j-i} v_j

与复线性RNN的联系: a_{i,j}=γ^{i-j} → o_i = Σ (γ e^{-Iθ})^{i-j} v_j

## 体现的方法

- VO-RoPE（Value-Output RoPE）

## 所属系列位置

第19篇，补全RoPE的理论拼图。

## 与其他文章的关系

- 前驱：第2篇（RoPE提出）、第4篇（RoPE-2D）、第6篇（RoPE完备性）
- 与MLA（第20、21篇讨论）的K、V共享问题直接相关
- 与LRU、RetNet等线性RNN相关

## 原文证据锚点

- 基础回顾: 原文"基础回顾"节，回顾标准QK-RoPE的旋转矩阵性质
- 新的用法: 原文"新的用法"节，提出VO-RoPE公式(eq:vo-rope)
- 简单实验: 原文"简单实验"节，1B模型实验数据：QK-RoPE Loss=2.712, VO-RoPE Loss=2.770
- 一些思考: 原文"一些思考"节，讨论与MLA中K、V共享问题的潜在联系
- 相关工作: 原文"相关工作"节，与复线性RNN（LRU、RetNet）的联系推导
