---
type: concept
title: UniLM
definition: 一种融自然语言理解和生成能力于一体的预训练语言模型，通过注意力掩码控制注意力矩阵的单双向结构。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"]
source_ids: ["7427"]
aliases: ["Unified Language Model", "统一预训练语言模型"]
status: stable
updated: 2026-06-12
---

# UniLM

## 定义
UniLM（Unified Language Model）是微软提出的将自然语言理解（NLU）与自然语言生成（NLG）任务融合在单一 Transformer 架构下的预训练语言模型。

## 机制
其核心是利用特殊的注意力掩码（Attention Mask）矩阵调节自注意力计算流：
1. **双向注意力**：输入段（Segment A）的 token 之间可以相互可见，作为 NLU 编码器；
2. **单向注意力**：输出段（Segment B）的 token 之间采用下三角掩码，只能关注先前的 token，实现 NLG 自回归生成；
3. **单双向桥接**：自回归段对编码输入段完全可见，反向则遮蔽，从而构成无污染的 Seq2Seq 生成通道。