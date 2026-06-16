---
type: example
title: spaces-9529-全双向与正反向混合注意力实验
article_id: 9529
article: |
  [spaces-9529-为什么现在的LLM都是Decoder-only的架构](wiki/sources/spaces-9529-为什么现在的LLM都是Decoder-only的架构.md)
section: 低秩问题
claim: 在MLM任务中正反向混合的单向注意力相比全双向注意力能够取得更好的效果
notation_mapping:
  A_mask: Attention mask pattern
  Loss: MLM training loss
steps:
  - 构建一个 1 亿参数规模的基于 Transformer-base 架构的 MLM 预训练语言模型。
  - 全双向基线：所有的 Head 均使用标准的双向无遮掩注意力矩阵（类似 BERT）。
  - 正反向混合版本：在 Multi-Head Attention 中，将一半 Head 的 Attention 矩阵截断为下三角阵（正向），另一半 Head 截断为上三角阵（反向）（或者层间交替使用下三角和上三角）。
  - 在完全一致的数据集和超参数（控制变量）下进行从零预训练，记录其 MLM 任务的 Loss 变化曲线。
  - 结果表明，正反向混合单向注意力模型不仅保留了交互的双向性，还融入了单向满秩的高表达能力，其训练 Loss 下降曲线明显优于全双向基线。
used_concepts:
  - [Decoder-only架构](wiki/concepts/Decoder-only架构.md)
source_span: ev::9529::mlm_hybrid_experiment
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
source_ids:
  - 9529
status: draft
updated: 2026-06-12
---

# spaces-9529-全双向与正反向混合注意力实验

## Claim
在MLM任务中正反向混合的单向注意力相比全双向注意力能够取得更好的效果

## Section
低秩问题

## Notation Mapping
- $A\_mask$: Attention mask pattern
- $Loss$: MLM training loss

## Steps
1. 构建一个 1 亿参数规模的基于 Transformer-base 架构的 MLM 预训练语言模型。
2. 全双向基线：所有的 Head 均使用标准的双向无遮掩注意力矩阵（类似 BERT）。
3. 正反向混合版本：在 Multi-Head Attention 中，将一半 Head 的 Attention 矩阵截断为下三角阵（正向），另一半 Head 截断为上三角阵（反向）（或者层间交替使用下三角和上三角）。
4. 在完全一致的数据集和超参数（控制变量）下进行从零预训练，记录其 MLM 任务的 Loss 变化曲线。
5. 结果表明，正反向混合单向注意力模型不仅保留了交互的双向性，还融入了单向满秩的高表达能力，其训练 Loss 下降曲线明显优于全双向基线。