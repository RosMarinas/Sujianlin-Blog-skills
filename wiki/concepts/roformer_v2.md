---
type: concept
title: RoFormerV2
definition: RoFormerV2 是一种旨在探索相同参数算力预算下自然语言理解（NLU）性能极限的Transformer架构升级版。它在旋转位置编码（RoPE）的基础上，通过移除网络中所有的偏置（Bias）参数、使用无参数 RMS Norm 替代传统 Layer Norm，并融入有监督多任务预训练来压榨模型能效。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-21-RoFormerV2-自然语言理解的极限探索.md
source_ids:
  - "8998"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# RoFormerV2

## Definition
RoFormerV2 是一种旨在探索相同参数算力预算下自然语言理解（NLU）性能极限的Transformer架构升级版。它在旋转位置编码（RoPE）的基础上，通过移除网络中所有的偏置（Bias）参数、使用无参数 RMS Norm 替代传统 Layer Norm，并融入有监督多任务预训练来压榨模型能效。

## Explanation
RoFormerV2 对 Transformer 模型结构做出了极其简练的修改：
- **无 Bias 设计**：去除 Attention 和 FFN 的所有 Bias 偏置项。
- **极简 RMS Norm**：移除归一化中的可学习缩放参数，使用无 $\gamma$ 和 $\beta$ 的 RMS Norm。在实验中，这带来了高达 1.2x ~ 1.3x 的训练吞吐加速。
- **预训练技术组合**：通过使用“动态残差缩放”稳定了 Post-Norm 在大规模无监督语料上从零开始训练的难度。结合有监督多任务联合训练，RoFormerV2 在参数量和运行速度占绝对优势的前提下，微调效果反超了常规的 BERT/RoBERTa，逼近了相同规模下的 NLU 拟合极限。
