---
type: concept
definition: ReRoPE（Rectified RoPE）是对标准RoPE的一种后处理修改方案，通过截断相对位置矩阵来实现免微调的长度外推。它在窗口w内保持标准RoPE的相对位置步长1，在窗口外将所有相对位置截断为常数w，从而理论上支持任意长度的上下文处理。
title: ReRoPE (Rectified RoPE)
status: draft
created: '2026-06-09'
tags:
- RoPE
- 长度外推
- 位置编码
- 相对位置矩阵
related_articles:
- 9708
- 9728
- 9731
- 9948
related_concepts:
- leaky-rerope
- length-extrapolation
- rotary-position-embedding
evidence_spans:
- 9708-融合
- 9708-实验
- 9948-保近压远
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

ReRoPE（Rectified RoPE）是对标准RoPE的一种后处理修改方案，通过截断相对位置矩阵来实现免微调的长度外推。它在窗口w内保持标准RoPE的相对位置步长1，在窗口外将所有相对位置截断为常数w，从而理论上支持任意长度的上下文处理。

从数学形式上看，ReRoPE的相对位置矩阵是：

- 当 i - j < w 时，使用标准RoPE的相对位置 (i-j)
- 当 i - j ≥ w 时，使用常数 w

ReRoPE是Leaky ReRoPE在 k→∞ 时的极限情况。

## 关键性质

1. **无限外推潜力**：窗口外的相对位置被截断为常数w，因此无论输入多长，位置编码都不会超出训练范围。
2. **局部性保持**：窗口w内保持标准步长1，不改变邻近Token的相对距离，保持了语言的局部分辨率。
3. **"保近压远"原则**：窗口中保持局部不失真（保近），窗口外压缩远处不越界（压远）。
4. **训练效果保持**：窗口w内与标准RoPE完全一致，因此在训练长度内的效果不会下降（无"外推税"）。
5. **w的选择鲁棒**：最优w大致为训练长度的1/4到1/2。
6. **Longer Context, Lower Loss**：在LLAMA2-13b上验证，随着context增长，loss持续下降。

## 计算代价

ReRoPE需要计算两次Attention矩阵再进行拼接（因分段线性的相对位置无法通过单次绝对位置编码实现），导致：
- 推理第一步需算两次Attention
- 不兼容Flash Attention等加速技术
- 但结合分块计算时开销可忽略

## 出现位置

- [第12篇](/archives/9708) "融合"节首次提出
- [第12篇](/archives/9708) "实验"节验证效果
- [第16篇](/archives/9948) "保近压远"节作为核心方法讨论

## 原文证据

- 原文9708"融合"节给出了ReRoPE的矩阵定义（eq:rerope），明确"窗口内保持1间隔、窗口外截断为w"
- 原文9708"实验"节显示ReRoPE-w256+log n在4096不重复测试中达49.07%，在LLAMA2-13b上loss从1.4967(4096)降至1.4001(16384)
- 原文9948"保近压远"节将ReRoPE置于整体框架中讨论，指出其实现了"Train Short, Test Long"的理想特性

## 与其他概念的关系

- **前驱**：[RoPE](/archives/8265)提供了基础位置编码机制
- **扩展**：Leaky ReRoPE是ReRoPE的一般化（k取有限值）
- **互补**：HWFA2结合了HWFA和ReRoPE以降低推理成本
- **对比**：与NTK-aware Scaled RoPE不同，ReRoPE不存在外推上限