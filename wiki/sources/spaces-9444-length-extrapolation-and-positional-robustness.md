---
type: article_summary
title: "Transformer升级之路：8、长度外推性与位置鲁棒性"
article_id: "9444"
source_url: https://spaces.ac.cn/archives/9444
date: 2023-01-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-01-31-Transformer升级之路-8-长度外推性与位置鲁棒性.md
series: [Transformer升级之路]
topics: [长度外推, 位置鲁棒性]
concepts: [Positional Robustness, Randomized Positional Training, CHE Benchmark, Length Extrapolation]
methods: [Equal Mean Randomized Position Training]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-31-Transformer升级之路-8-长度外推性与位置鲁棒性.md
source_ids:
  - "9444"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：8、长度外推性与位置鲁棒性

## 文章核心问题
能否不通过"强制截断"（局部注意力）的方式实现长度外推？如何从位置编码本身入手解决外推问题？

## 主要结论
- 针对注意力熵不一致问题，提出**log n缩放注意力**: 使用 $\text{softmax}(\log_m n / \sqrt{d} \cdot QK^{\top})$（$m$为训练长度，$n$为预测长度），在不同序列长度下稳定注意力熵。
- 针对未训练位置编码不一致问题，提出**随机位置训练（Randomized Positional Training）**: 训练时从更大的范围 $[0, L)$ 中随机采样 $N$ 个位置ID（具体参数 $L=2048, N=40$），使用排序后的随机位置而非 $[0,1,\dots,N-1]$，确保测试时的位置编码已在训练中出现过。
- 引入**CHE基准**（Chomsky Hierarchy Evaluation Benchmark）更严格测试长度外推，包含Regular、DCF、CS三类任务。
- ALIBI在CHE上失败，验证了其在语言任务上的成功归因于语言本身的局部性。
- RoPE + 随机位置训练在CHE上取得成功，Bucket Sort首次达到100%准确率。
- 随机位置训练的根本洞见是**等价类**：由于训练位置ID随机采样，模型无法依赖精确位置索引，而是通过序列的"顺序"编码位置。
- 改进版Equal Mean Randomized Position Training: 从指数或Beta分布采样 $n$ 并均匀取 $N$ 个点，使训练和预测位置分布更一致。

## 推导结构
在第7篇两大不一致框架基础上，分别对两个问题提出解决方案。注意力熵问题用log n缩放解决。位置编码不一致问题用随机位置训练解决，其核心思想是让模型在训练时见过所有可能的位置编码。进一步用CHE基准对比验证各方法。最后提出改进版Equal Mean Randomized Position Training，通过从指数或Beta分布采样 $n$ 并均匀取 $N$ 个点，使训练和预测位置分布更一致。

## 关键公式
- Log n缩放注意力: $\text{softmax}\left(\frac{\log_m n}{\sqrt{d}} QK^{\top}\right)$
- 随机位置训练: 训练时位置ID从 $[0, L)$ 随机采样 $N$ 个并排序
- Equal Mean Randomized Position Training: $n \sim \text{Exp}(\lambda)$ 或 $n \sim \text{Beta}(\alpha,\beta)$，均匀采样 $N$ 个点取自 $[0, n]$

## 体现的方法
- Log n缩放注意力: 使用 $\text{softmax}(\log_m n / \sqrt{d} \cdot QK^{\top})$ 稳定注意力熵
- 随机位置训练: 训练时从更大范围随机采样位置ID，使测试位置在训练中已出现
- Equal Mean Randomized Position Training: 控制训练和预测位置分布更一致

## 所属系列位置
Transformer升级之路系列第8篇，从位置鲁棒性角度解决长度外推问题。

## 与其他文章的关系
本文在第7篇诊断的两大不一致基础上提出了针对性解决方案（与第7篇的"强制截断"思路相反），是第7篇的自然延伸。通过随机位置训练的思路回避了局部注意力的局限，为第9篇和第10篇提供了不同视角。CHE基准的引入为后续方法提供了更严格的评估标准。

## 原文证据锚点
- Log n缩放在不同序列长度下稳定注意力熵
- 随机位置训练确保测试位置在训练中已出现
- ALIBI在CHE上失败，验证语言任务局部性假设
- RoPE + 随机位置训练在CHE上成功，Bucket Sort首次100%
- 随机位置训练的等价类解释
