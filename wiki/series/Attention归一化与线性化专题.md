---
type: series
title: Attention归一化与线性化专题
aliases: []
article_ids:
  - "4765"
  - "6853"
  - "7546"
  - "8180"
  - "8823"
  - "9019"
  - "9052"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-01-06-Attention-is-All-You-Need-浅读-简介-代码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
source_ids:
  - "4765"
  - "6853"
  - "7546"
  - "8180"
  - "8823"
  - "9019"
  - "9052"
series_goal: 沿着标准 Attention、稀疏化、线性化、低秩近似、熵不变缩放和 GAU 归一化，解释注意力机制如何从“可表达”推进到“可高效计算且可校准”。
entry_roles:
  "4765": 从 Transformer 原文切入，建立标准 Attention 的 Query-Key-Value、缩放点积和多头结构基线。
  "6853": 把效率问题显式化，比较局部、分块、稀疏等结构约束如何减少标准 Attention 的二次复杂度。
  "7546": 讨论 Softmax 是否必要，并用结合律把 Attention 改写为线性可计算形式。
  "8180": 引入 Nyström 低秩近似视角，把 Attention 近似为三块矩阵乘法，连接矩阵分解与高效注意力。
  "8823": 从熵不变性重新解释 Attention scale，说明温度缩放不只是经验超参。
  "9019": 回到 Softmax 归一化本身，分析归一化、熵和注意力分布之间的关系。
  "9052": 用 GAU/归一化的高效结构收束，说明下一代 Attention 可以同时追求速度、参数量和效果。
key_concepts:
  - [[Attention]]
  - [[Sparse Attention]]
  - [[Linear Attention]]
  - [[Nyströmformer]]
  - [[Attention信息熵]]
  - [[Gated Attention Unit]]
key_methods:
  - [[用结构约束线性化Attention计算]]
  - [[Attention-E熵不变性缩放]]
reading_paths:
  - [[Attention归一化与线性化阅读路径]]
status: draft
updated: 2026-06-14
---

# Attention归一化与线性化专题

## 系列核心问题

本系列不是简单收集 Attention 文章，而是围绕一个递进问题组织：标准 Softmax Attention 为什么有效，二次复杂度从哪里来，结构稀疏、线性化和低秩近似分别牺牲了什么，又如何用熵不变性和归一化设计把尺度校准回来。

## 文章顺序

1. [[spaces-4765-Attention-is-All-You-Need-浅读-简介+代码]] — 《Attention is All You Need》浅读（简介+代码）：先建立标准 Attention 的计算对象和多头结构。
2. [[spaces-6853-为节约而生-从标准Attention到稀疏Attention]] — 为节约而生：从标准Attention到稀疏Attention：把效率瓶颈转化为稀疏连接和结构约束问题。
3. [[spaces-7546-线性Attention的探索-Attention必须有个Softmax吗]] — 线性Attention的探索：Attention必须有个Softmax吗？：用结合律说明去掉 Softmax 后 Attention 可线性化。
4. [[spaces-8180-Nyströmformer-基于矩阵分解的线性化Attention方案]] — Nyströmformer：基于矩阵分解的线性化Attention方案：把线性化推进到 Nyström 低秩矩阵近似。
5. [[spaces-8823-从熵不变性看Attention的Scale操作]] — 从熵不变性看Attention的Scale操作：从分布熵角度重新解释 scale/temperature。
6. [[spaces-9019-听说Attention与Softmax更配哦～]] — 听说Attention与Softmax更配哦～：回看 Softmax 归一化为何仍然重要。
7. [[spaces-9052-GAU-α-尝鲜体验快好省的下一代Attention]] — GAU-α：尝鲜体验快好省的下一代Attention：用 GAU 把门控、归一化与高效注意力结构合并起来。

## 认知网络位置

这条线是 [[Transformer架构与归一化]] 和 [[LLM架构与上下文扩展]] 的底层机制支线：前者关注 Transformer 结构设计，后者关注 LLM 上下文容量，而本系列解释 Attention 分布本身如何被稀疏化、近似和校准。

## 关键方法

- [[用结构约束线性化Attention计算]]：把 Softmax Attention 的二次项改写成可交换或低秩结构，适用于长序列效率问题。
- [[Attention-E熵不变性缩放]]：用熵不变性替代经验 scale 调参，适用于需要比较不同维度或不同温度 Attention 分布的场景。

## 搜索入口

- 想查“Attention 是否必须 Softmax”：从 7546 和 9019 进入。
- 想查“线性 Attention 与低秩近似”：从 7546 到 8180。
- 想查“scale/temperature 为什么这样设”：从 8823 进入。
- 想查“GAU 与高效 Attention”：从 9052 进入。

## Probe entry

- `probe::gan_attention::attention_efficiency_path`
