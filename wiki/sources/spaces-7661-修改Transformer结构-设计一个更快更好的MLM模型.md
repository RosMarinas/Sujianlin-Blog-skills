---
type: article_summary
title: 修改Transformer结构，设计一个更快更好的MLM模型
article_id: "7661"
source_url: https://spaces.ac.cn/archives/7661
date: 2020-08-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
series: [Transformer架构与归一化]
topics: [Attention优化]
concepts: [T-TA (Transformer-based Text Autoencoder)]
methods: [T-TA (Transformer-based Text Autoencoder)]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
source_ids:
  - "7661"
status: draft
updated: 2026-06-12
---

# 修改Transformer结构，设计一个更快更好的MLM模型

## 文章核心问题
传统的 MLM（Masked Language Model）预训练方法由于每次只能选择一小部分（如15%）的 token 替换为 `[MASK]`，导致模型对每个样本的参数更新极不充分（仅有 15% 的 token 获得预测损失反馈），训练效率十分低下。如何在保证双向上下文建模能力的同时，能在一遍前向计算中预测整句所有的 token 分布，并且避免 `[MASK]` 带来的预训练-微调不一致性？

## 主要结论
- 提出 T-TA（Transformer-based Text Autoencoder）结构。通过重构 Query、Key、Value 的依赖路径，实现在没有 `[MASK]` 标记的情况下对全句所有 token 的并行自监督预测。
- T-TA 能够在相同的模型规模下，训练速度和语义表征能力媲美甚至超越标准 MLM 预训练的模型。
- 证明了在低算力条件下（如仅使用 3 层小模型），通过合理重构注意力结构同样可以设计出高性能、高效率的语言模型结构并发表顶级会议。

## 推导结构
1. **泄漏瓶颈分析**：双向语言模型若要一次前向输出所有位置 $p(x_i | \boldsymbol{x} \backslash \{x_i\})$，则第 $i$ 个位置的特征聚合路径绝不能含有 $x_i$ 的信息。
2. **构建 T-TA 机制**：
   - **第一层 Query 去词义**：第一层的 Query 只使用位置向量 $Q_0 = P$，不带任何词向量信息，阻断最初的信息泄漏通道。
   - **对角线 Mask**：在第一层中，将对角线处的自注意力设为 0，防止当前的 Query（只有位置信息 $i$）在做注意力汇聚时，读取到 Key 和 Value 对应位置 $i$ 的词特征。
   - **恒定 K, V 共享**：如果第二层之后继续使用传统的 Transformer 迭代，注意力机制会将其他位置已经混入的当前词特征带回，导致防泄漏机制失效。因此，T-TA 规定所有 Attention 层的 $K, V$ 都是恒定不变的输入特征，即 $K = V = E + P$（Token embedding 加上 Position embedding）。
   - **计算层迭代**：$Q_{n} = Attention(Q_{n-1}, E+P, E+P)$。
3. **下游微调**：在微调下游任务时，去掉预训练时的对角线 Attention Mask，退化为全局注意力以获取最大表示能力。

## 关键公式
- 传统 BERT 自注意力迭代: $Q_n = Attention(Q_{n-1}, Q_{n-1}, Q_{n-1})$ (其中 $Q_0 = E + P$)
- T-TA 注意力迭代: $Q_n = Attention(Q_{n-1}, E + P, E + P)$ (其中 $Q_0 = P$)
- 预训练对角线约束: $sim(q_i, k_i) = 0$ (对角线 Mask)

## 体现的方法
- T-TA (Transformer-based Text Autoencoder) 架构重构

## 所属系列位置
Transformer架构与归一化系列第3篇，着重从预训练任务与自注意力计算机制的契合度进行硬件训练加速设计。

## 与其他文章的关系
T-TA 规定所有深层 Attention 中 $K, V$ 恒为常数（随输入确定的输入表示），证明了 Key-Value 静态对表示学习的有效性，这与第2篇中 Synthesizer 探究的静态自注意力矩阵理念相契合，同时也与第5篇中对线性注意力低秩和 head 复杂度限制的研究遥相呼应。

## 原文证据锚点
- T-TA 示意图与对角线掩码：文中 "T-TA的Attention Mask模式" 图示及说明。
- 迭代计算对比公式：BERT 与 T-TA 计算公式对比图。
- 实验结论：3 层 T-TA 媲美 Base 版本的标准 MLM 表现。
