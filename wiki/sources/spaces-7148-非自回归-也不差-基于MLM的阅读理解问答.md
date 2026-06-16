---
type: article_summary
title: “非自回归”也不差：基于MLM的阅读理解问答
article_id: "7148"
source_url: https://spaces.ac.cn/archives/7148
date: 2019-12-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-12-26-非自回归-也不差-基于MLM的阅读理解问答.md
series:
  - [[基于深度学习的阅读理解问答]]
concepts:
  - [[非自回归生成]]
  - [[曝光偏差]]
methods:
  - [[基于MLM的非自回归阅读理解问答]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-12-26-非自回归-也不差-基于MLM的阅读理解问答.md
source_ids:
  - "7148"
status: draft
updated: 2026-06-11
---

# “非自回归”也不差：基于MLM的阅读理解问答

## 内容概要
文章探讨了通过 BERT 的掩码语言模型（MLM）以“非自回归”生成方式进行阅读理解式问答的模型设计。在维持与自回归 Seq2Seq 相同高精度的同时，该方法实现了约 6 倍的推理速度提升。同时，文章深入对比了自回归生成与非自回归生成的异同。

## 关键内容
1. **MLM 非自回归问答模型设计**：
   - 设定答案的最大可能长度 $l_{\max}$。
   - 输入序列拼接格式为：`[CLS] 问题 [SEP] 篇章 [SEP] [MASK] [MASK] ... [MASK] [SEP]`。
   - 利用 BERT 一次性并行预测所有 $l_{\max}$ 个 `[MASK]` 位置的 Token 概率分布。
2. **性能与速度对比**：
   - 在 SogouQA 验证集上取得了 0.774 的综合得分，与 Seq2Seq 方案持平。
   - 推理速度从 Seq2Seq 的 2 条/秒提升至 12 条/秒，实现了 6 倍提速。
3. **自回归与非自回归对比**：
   - **自回归 (AR)** 建模联合条件概率：$P(Y|X) = \prod_{t=1}^T P(y_t | y_{<t}, X)$。解码必须递归进行，无法并行，且存在训练（Teacher Forcing）与推理预测不一致导致的“曝光偏差”（误差累积）。
   - **非自回归 (NAR / MLM)** 简化假设各输出词条件独立：$P(Y|X) = \prod_{t=1}^T P(y_t | X)$。
4. **非自回归的适用场景**：
   - 适用于**短文本生成**（文本越短越符合独立假设）。
   - 适用于**正确答案在设定任务下是唯一的场景**（如抽取式阅读理解、分词等）。如果答案不唯一（如自由标题生成），非自回归容易由于条件独立假设导致生成的句子逻辑混乱。
   - 由于训练和推理在 MLM 模式下完全一致（输入均无真实历史标签依赖），彻底消除了曝光偏差。
