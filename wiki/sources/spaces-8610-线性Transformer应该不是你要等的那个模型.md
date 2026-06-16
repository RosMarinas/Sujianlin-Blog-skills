---
type: article_summary
title: 线性Transformer应该不是你要等的那个模型
article_id: "8610"
source_url: https://spaces.ac.cn/archives/8610
date: 2021-08-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-08-09-线性Transformer应该不是你要等的那个模型.md
series: [Transformer架构与归一化]
topics: [Attention优化]
concepts: [线性注意力, Attention Low Rank Bottleneck]
methods: [线性注意力复杂度与低秩瓶颈分析]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-09-线性Transformer应该不是你要等的那个模型.md
source_ids:
  - "8610"
status: draft
updated: 2026-06-12
---

# 线性Transformer应该不是你要等的那个模型

## 文章核心问题
为什么很多读者在使用线性注意力（Linear Attention）替代标准注意力后，在计算速度上几乎感觉不到提升？Transformer 层中自注意力（SA）与前馈网络（FFN）的真实计算量对比关系如何？在什么样的序列长度下，注意力层才会成为模型计算量的真正瓶颈？

## 主要结论
- 在序列长度 $n$ 较短（如 base 模型下 $n < 1536$）时，自注意力的计算复杂度并非模型的主导瓶颈。线性时间复杂度的 FFN（FeedForward Network）占据了大部分计算资源。
- 当序列长度 $n$ 接近 5000 时，二次方复杂度的自注意力层（SA）才会真正超越 FFN 并主导模型的总计算量。
- 线性注意力由于其严重的“低秩瓶颈”，若想达到与标准注意力相似的表现，通常必须将特征映射维度（head_size）扩大约 4 倍。在此种情况下，线性注意力比标准注意力更省计算量的实际阈值序列长度将从 $n > 64$ 暴增到 $n > 1024$。
- 因此，除非处理的序列长度达到成千上万级别，否则不推荐盲目替换为线性注意力。BERT 等模型训练慢的原因在于其整体深度与隐层参数规模大，而非 Attention 的平方复杂度。

## 推导结构
1. **SA 矩阵乘法计算量估算**：
   - 投影变换 ($Q, K, V$)：$3n(hd)^2$
   - 注意力得分矩阵 $QK^{\top}$ 乘法与汇聚：$2hn^2 d = 2n^2 hd$ (其中隐层维度为 $hd$)
   - 输出投影：$n(hd)^2$
   - SA 总乘法数：$4nh^2 d^2 + 2n^2 hd$
2. **FFN 计算量估算**：
   - 第一层全连接：$n \times hd \times 4hd$
   - 第二层全连接：$n \times 4hd \times hd$
   - FFN 总乘法数：$8nh^2 d^2$
3. **计算量对比分析**：
   - SA > FFN $\Leftrightarrow 4nh^2 d^2 + 2n^2 hd > 8nh^2 d^2 \Leftrightarrow n > 2hd$。对 base 模型 ($hd=768$)，此界限为 $n > 1536$。
   - 二次项占总计算量 $12nh^2 d^2 + 2n^2 hd$ 主导的条件：$2n^2 hd > 12nh^2 d^2 \Leftrightarrow n > 6hd$。对 base 模型，此界限为 $n > 4608$。
4. **线性注意力复杂度分析**：
   - 线性 Attention 复杂度为 $2nd^2$。若考虑 4 倍 head_size 扩展以弥补低秩缺陷，计算量变为 $2n(4d)^2 = 32nd^2$。
   - 此时相较于标准 Attention 头 $2n^2 d$ 更快的阈值为：$32nd^2 < 2n^2 d \Leftrightarrow n > 16d$。对 base 模型 ($d=64$)，对应 $n > 1024$。

## 关键公式
- SA 总计算量: $4nh^2 d^2 + 2n^2 hd$
- FFN 总计算量: $8nh^2 d^2$
- 线性注意力单头计算量: $2nd^2$
- 线性注意力在防低秩扩展后的单头计算量: $32nd^2$

## 体现的方法
- 线性注意力复杂度与低秩瓶颈分析

## 所属系列位置
Transformer架构与归一化系列第5篇，着重从计算量量化评估（FLOPs）角度指导模型的效率选择。

## 与其他文章的关系
本篇指出的线性注意力在 Causal 场景下损失并行性以及特征维度膨胀的痛点，直接促成了第6篇中 FLASH 提出的“分块混合注意力”（MCA）的诞生。MCA 在块内使用二次局部注意力，在块间使用低秩线性注意力，既避免了维度暴涨，又大幅削减了空间复杂度。

## 原文证据锚点
- SA 与 FFN 计算量推导：自“评估计算量”一节的公式推导。
SA > FFN 阈值: $n > 1536$；二次项主导阈值: $n > 4608$。
- 线性注意力 head_size 扩展：指出需要扩展为原来的 4 倍以克服低秩瓶颈，对应阈值 $n > 1024$。
- 各大高效自注意力工作对比图：包括 Reformer、Longformer、Performer、Luna 等工作均在数千长度起步展示性能优势。
