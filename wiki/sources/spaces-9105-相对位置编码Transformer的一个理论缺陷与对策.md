---
type: article_summary
title: 相对位置编码Transformer的一个理论缺陷与对策
article_id: "9105"
source_url: https://spaces.ac.cn/archives/9105
date: 2022-06-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
series: [Transformer架构与归一化]
topics: [相对位置编码, Attention优化]
concepts: [相对位置编码, 探针实验, l2注意力归一化]
methods: [l2注意力归一化, 标记符边界解耦法]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "9105"
status: draft
updated: 2026-06-12
---

# 相对位置编码Transformer的一个理论缺陷与对策

## 文章核心问题
为什么在使用相对位置编码（如 RoPE, T5, Transformer-XL）且输入序列的所有 token 完全相同时，Transformer 模型的每一层输出自始至终在空间上都是完全相同的？为什么这种设计在理论上无法成为“万能拟合器”？有哪些方法可以打破这个理论限制？

## 主要结论
- 提出“全同输入排序”探针实验：对于具备位置识别能力的编码机制，在输入全 0 向量时，模型应能独立且准确地映射输出有序的位置标号 $[1, 2, \dots, n]$。
- 除了 Shaw 的经典设计外，大多数相对位置编码（包括 RoPE）都只修改了 Softmax 前的 Attention 得分矩阵。其行概率归一化（$\sum_j a_{i,j}=1$）导致在全同输入下，注意力机制的加权和 $\boldsymbol{o}_i = \sum_j a_{i,j}\boldsymbol{v}_j = \boldsymbol{v}$ 永远在各个位置上表现恒等。因此，模型在理论上无法区别位置（破坏了万能拟合性）。
- **破局方案 1**：在 Softmax 中引入 Toeplitz 乘性权重矩阵 $C$（如 $\boldsymbol{A} \odot \boldsymbol{C}$，其中 $c_{i,j}=g(i-j)$），打破行概率和为 1 的约束，但缺乏长度通用性。
- **破局方案 2**：去除 Softmax 分母（直接如 GAU 利用 $\text{relu}^2$ 后除以序列长度 $n$）。
- **破局方案 3**：用 $l_2$ 归一化（$a_{i,j} = \frac{e^{b_{i,j}}}{\sqrt{\sum_j e^{2b_{i,j}}}}$）代替 $l_1$ 归一化。这在 GAU 模型中实验证明可以加快收敛并轻微提升效果。
- **意外发现**：在输入首尾注入 `[CLS]` 和 `[SEP]` 等特定标记字符（边界 Token），可以有效打破全同输入的空间对称性，使其自发避开了这一理论缺陷。

## 推导结构
1. **构建探针任务**： 输入全 0 序列，要求输出有序位置。
2. **推导理论缺陷**：
   对于相同的输入，所有的 Value 向量 $\boldsymbol{v}_j = \boldsymbol{v}$。自注意力核心步为 $\boldsymbol{o}_i = \sum_j a_{i,j}\boldsymbol{v}_j$。
   若采用相对位置编码但保留 softmax 行归一化，则 $\sum_j a_{i,j}=1$。
   故而：$\boldsymbol{o}_i = \left(\sum_j a_{i,j}\right)\boldsymbol{v} = \boldsymbol{v}$。
   每一层的输出完全丧失空间差异性。
3. **推导 $l_2$ 归一化自注意力**：
   $a_{i,j} = e^{b_{i,j}} / \sqrt{\sum_k e^{2b_{i,k}}}$。计算 $\sum_j a_{i,j}$ 的行和并不为常数 1，而是随着 $b_{i,j}$ 强相关变化，顺利在全同输入下引入了位置偏差，通过了探针实验。

## 关键公式
- 概率和限制证明: $\boldsymbol{o}_i = \sum_j a_{i,j}\boldsymbol{v}_j = \left(\sum_j a_{i,j}\right)\boldsymbol{v} = \boldsymbol{v}$
- l2 归一化注意力: $a_{i,j} = \frac{e^{b_{i,j}}}{\sqrt{\sum_k e^{2b_{i,k}}}}$
- 乘性 Toeplitz 修正: $\boldsymbol{o}_i = \sum_j a_{i,j}c_{i,j}\boldsymbol{v}_j$

## 体现的方法
- $l_2$ 注意力归一化方法
- 标记符边界解耦位置法

## 所属系列位置
Transformer架构与归一化系列第10篇，是位置编码的理论收官之作，深入研究了概率行和约束对表示学习的潜在局限。

## 与其他文章的关系
本篇解释了第6篇中 GAU 采用 $\text{relu}^2/n$ 归一化能够成功通过探针实验的理论根源，并针对 GAU 的初始化特征对角线分布设计了 $l_2$ 归一化自注意力的改进方案。同时，本篇指出 `[CLS]` 标记符对位置泄露的作用，揭示了 BERT 结构中非词义符号隐藏的工程价值。

## 原文证据锚点
- 简单探针定义： 见“简单探针”小节。
- 恒同输出数学证明： 见“无法胜任”小节的数学推导公式。
- $l_2$ 归一化公式： 见“新归一化”小节。
- 特殊 Token 对抗对称性： 见“峰回路转”小节的 CNN padding 泄露类比分析。
