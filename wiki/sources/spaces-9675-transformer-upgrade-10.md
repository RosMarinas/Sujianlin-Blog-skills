---
type: article_summary
title: "Transformer升级之路：10、RoPE是一种β进制编码"
article_id: "9675"
source_url: https://spaces.ac.cn/archives/9675
date: 2023-07-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-07-06-Transformer升级之路-10-RoPE是一种β进制编码.md
series: [Transformer升级之路]
topics: [RoPE, β进制编码, 长度外推]
concepts: [Base-Beta Encoding]
methods: [NTK-aware Scaled RoPE, Positional Interpolation]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-06-Transformer升级之路-10-RoPE是一种β进制编码.md
source_ids:
  - "9675"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：10、RoPE是一种β进制编码

## 文章核心问题
RoPE与β进制编码之间是否存在深层等价关系？NTK-aware Scaled RoPE和Positional Interpolation两种上下文扩展方法在β进制编码视角下如何理解？

## 主要结论
- RoPE的构造与β进制表示数字的方式镜像对应：$\cos(n/\beta^0), \sin(n/\beta^0), \cos(n/\beta^1), \sin(n/\beta^1), \dots$ 本质上是用 $\beta = 10000^{2/d}$ 为底对位置 $n$ 进行编码。
- β进制编码视角统一了三种扩展策略：
  - 直接外推：保持基数不变，增加维度对→需要模型处理训练中为零的维度，无微调则失败。
  - Positional Interpolation (PI)：缩放 $n \to n/k$，将位置压缩到训练范围内→需要微调，因为均匀改变所有频率尺度（使低位"拥挤"）。
  - **NTK-aware Scaled RoPE（进制转换）**：转换到更大的基数 $\beta \cdot \lambda$，其中 $\lambda = k^{2/(d-2)}$→保留数字级别的比较规则，实现零样本扩展。
- NTK-RoPE的本质是"高频外推+低频内插"原则。
- NTK-RoPE在GAU + Post-Norm上实现了非平凡的零样本外推（4096 repeat-context: 51.28%，加log n后达61.71%），是NBCE之后的第二个有效零样本方法。
- β进制编码框架统一了PI（缩放 $n$）和NTK-RoPE（改变基数）作为扩展可表示范围的两种基本策略。

## 推导结构
首先建立RoPE与β进制编码的深层等价关系，指出RoPE的 $\cos(n/\beta^i), \sin(n/\beta^i)$ 与β进制数字提取的对应。然后用此框架分析三种扩展策略并推导NTK-RoPE的参数 $\lambda$：从低频约束 $n/((\beta\lambda)^{d/2-1}) = (n/k)/\beta^{d/2-1}$ 解出 $\lambda = k^{2/(d-2)}$，解释由于 $d$ 较大时 $\lambda \approx 1$ 对于高频分量（高 $i$）意味着高频外推+低频内插。最后在GAU + Post-Norm上实验验证。

## 关键公式
- RoPE的β进制编码表示: $[\cos(n/\beta^0), \sin(n/\beta^0), \cos(n/\beta^1), \sin(n/\beta^1), \dots]$, $\beta = 10000^{2/d}$
- 数字提取（β进制）: $\lfloor n / \beta^{m-1} \rfloor \bmod \beta$
- NTK-RoPE参数: $\lambda = k^{2/(d-2)}$
- 低频约束: $n/((\beta\lambda)^{d/2-1}) = (n/k)/\beta^{d/2-1}$
- PI: $n \to n/k$ 压缩位置

## 体现的方法
- 直接外推: 保持基数不变，增加维度对
- Positional Interpolation (PI): 缩放 $n \to n/k$ 压缩位置到训练范围
- NTK-aware Scaled RoPE（进制转换）: 转换到更大基数 $\beta \cdot \lambda$，$\lambda = k^{2/(d-2)}$
- Log n缩放用于辅助注意力聚焦

## 所属系列位置
Transformer升级之路系列第10篇，从β进制编码视角统一理解RoPE和上下文扩展方法。

## 与其他文章的关系
本文是系列中RoPE主题的深化，建立在第2篇（RoPE提出）和第6篇（RoPE完备性分析）的基础上。β进制编码视角为理解第7篇讨论的Sinusoidal/RoPE外推问题提供了新框架。与第9篇的HWFA同为GAU + Post-Norm架构上有效的零样本方法，但两者机制不同（HWFA通过架构设计，NTK-RoPE通过位置编码变换）。

## 原文证据锚点
- RoPE与β进制编码的深层等价关系建立
- NTK-RoPE参数 $\lambda = k^{2/(d-2)}$ 的推导
- NTK-RoPE在GAU + Post-Norm上零样本外推达61.71%（+log n）
- "高频外推+低频内插"原则
- β进制编码框架统一PI和NTK-RoPE
