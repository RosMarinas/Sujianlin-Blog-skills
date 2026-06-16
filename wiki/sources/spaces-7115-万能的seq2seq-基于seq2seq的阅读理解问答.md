---
type: article_summary
title: 万能的seq2seq：基于seq2seq的阅读理解问答
article_id: "7115"
source_url: https://spaces.ac.cn/archives/7115
date: 2019-12-05
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-12-05-万能的seq2seq-基于seq2seq的阅读理解问答.md
series:
  - [[基于深度学习的阅读理解问答]]
concepts:
  - [[非自回归生成]]
methods:
  - [[多篇章投票Beam Search解码算法]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-12-05-万能的seq2seq-基于seq2seq的阅读理解问答.md
source_ids:
  - "7115"
status: draft
updated: 2026-06-11
---

# 万能的seq2seq：基于seq2seq的阅读理解问答

## 内容概要
文章探讨了如何使用统一的 Seq2Seq 架构 —— 采用 UNILM (Unified Language Model) 掩码方案 —— 来做事实类阅读理解式问答，并在 bert4keras 中进行了代码复现。作者进一步提出了一种将多篇章投票逻辑契合到 Beam Search 解码过程中的策略。

## 关键内容
1. **UNILM 架构的应用**：
   - 将阅读理解简化为 Seq2Seq 生成任务。输入拼接格式为：`[CLS] 问题 [SEP] 篇章 [SEP] 答案 [SEP]`。
   - 使用不同的 Attention Mask 矩阵实现条件语言模型训练（问题和篇章相互可见，答案部分单向自回归可见）。
2. **多篇章投票的 Beam Search 算法**：
   在搜索问答中存在多篇材料对应同一问题，作者提出在解码每一个字时，将所有候选篇章预测的概率分布进行对齐和平均：
   - *无答案篇章筛除*：在预测第一个字符时，若某个篇章对应的首字预测为 `[SEP]`，代表该篇章无答案，将其剔除。
   - *概率平均与 Beam 更新*：保留未被筛除的篇章，将其在当前时间步预测的字符概率分布求均值，作为当前生成步骤的概率，并以此选取 Top-$K$ 候选。
   - *循环迭代*：下一时间步将 Top-$K$ 候选字分别与各篇章拼接，重新预测并按篇章平均概率，直至输出 `[SEP]`。
3. **抽取式与生成式兼容**：
   解码过程中同时支持限制答案必须为篇章片段（抽取式）以及自由解码（生成式）两种模式。
4. **性能与代价**：
   在 SogouQA 验证集上取得了 0.770 的综合得分，远超以往的单模型。然而，其预测速度受到自回归递归解码的限制，降至每秒仅能预测 2 条数据左右。
