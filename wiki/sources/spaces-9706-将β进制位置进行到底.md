---
type: article_summary
title: Transformer升级之路：11、将β进制位置进行到底
article_id: "9706"
source_url: https://spaces.ac.cn/archives/9706
date: 2023-07-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
series: [Transformer升级之路]
topics: [位置编码, 长度外推, NTK-RoPE, 混合进制]
concepts: [base-beta-encoding, ntk-aware-scaled-rope]
methods: [ntk-aware-scaled-rope, positional-interpolation]
problem_patterns: [长度外推, 位置编码泛化]
evidence_spans:
  - 9706-进制类比
  - 9706-修正NTK
  - 9706-混合进制
  - 9706-分摊优化
  - 9706-实验结果
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
source_ids:
  - "9706"
status: draft
updated: 2026-06-09
---

## 文章核心问题

如何进一步推广NTK-aware Scaled RoPE，以寻找更优的不微调扩展LLM的Context长度的策略。

## 主要结论

1. 之前的NTK-RoPE-old（NTK-aware Scaled RoPE）存在修正余地——进制转换时不仅底数要变，模周期也应同步放大，由此提出NTK-RoPE-fixed。
2. 混合进制视角启发了更优的方案NTK-RoPE-mixed，将外推压力不均匀地分摊到各维度（低位分摊更多、高位分摊更少），获得了比等进制NTK-RoPE更好的外推效果。
3. log n缩放因子的后验版本max(1, log_maxlen n)对预训练未加入log n技巧的模型仍有提升效果。

## 推导结构

1. 回顾RoPE的β进制类比和NTK-aware Scaled RoPE
2. 指出原有NTK-RoPE-old的不足——仅改底数未改模周期
3. 推导修正版NTK-RoPE-fixed
4. 从混合进制（不同位使用不同基数）推广到位置编码
5. 提出λ₁λ₂...λₘ = exp(amᵇ)形式的分摊方案，b=0.625为实验最优
6. 实验对比验证

## 关键公式

NTK-RoPE-fixed: θ_m = n / [λ(βλ)^{m-1}], λ = k^{2/d}

NTK-RoPE-mixed: θ_m = n / [β^{m-1}(λ₁λ₂...λₘ)], 约束λ₁λ₂...λ_{d/2}=k, λ₁≥λ₂≥...≥λ_{d/2}≥1

后验log n缩放: max(1, log_maxlen n)

## 体现的方法

- NTK-RoPE-fixed：修正版的NTK-aware Scaled RoPE
- NTK-RoPE-mixed：混合进制版本的NTK-RoPE
- 后验log n缩放因子

## 所属系列位置

Transformer升级之路系列第11篇，紧接第10篇（RoPE的β进制编码），进一步深化β进制视角。

## 与其他文章的关系

- 前驱：[第10篇——RoPE是一种β进制编码](/archives/9675)
- 后续直接引出第12篇的ReRoPE（本文结论指出NTK系列已达上限，需要另辟蹊径）
- 实验基准沿用了系列一贯的GAU+Deep Norm+Tiger+语言模型设置

## 原文证据锚点

- 进制类比: 原文"进制类比"节，给出β进制与Sinusoidal位置编码的对比公式(eq:mod, eq:sinu)
- 修正NTK: 原文"修正NTK"节，指出NTK-RoPE-old不足，给出NTK-RoPE-fixed公式(eq:ntk-fixed)
- 混合进制: 原文"混合进制"节，引入混合进制概念及其数学形式(eq:mod2)
- 分摊优化: 原文"分摊优化"节，导出混合进制下θ_m表达及约束，b=0.625为最优
- 实验结果: 原文"实验结果"节，表格显示NTK-RoPE-mixed+log n在4096不重复测试中达45.41%，显著优于NTK-RoPE-old
