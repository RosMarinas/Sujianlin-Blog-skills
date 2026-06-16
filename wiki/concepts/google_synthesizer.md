---
type: concept
title: Google Synthesizer
definition: Google Synthesizer 是一种重新思考并简化Transformer自注意力计算机制的框架。它探究了去除传统的 Query-Key 动态两两内积（token-to-token attention）的可行性，转而使用静态学习矩阵、简单的 Dense 网络或者它们的低秩分解形式生成注意力概率分布。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
source_ids:
  - "7430"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Google Synthesizer

## Definition
Google Synthesizer 是一种重新思考并简化Transformer自注意力计算机制的框架。它探究了去除传统的 Query-Key 动态两两内积（token-to-token attention）的可行性，转而使用静态学习矩阵、简单的 Dense 网络或者它们的低秩分解形式生成注意力概率分布。

## Explanation
标准的自注意力依赖于输入序列中 Token 两两之间的动态内积。Google Synthesizer 提出了几种变体以简化计算：
- **Dense 模式**：通过单位置前馈网络预测该位置对所有其他位置的注意力，相当于将 Key 矩阵设为固定的常数参数。
- **Random 模式**：完全抛弃输入特征的相关性，在模型中保存一个训练期间固定或更新的常数注意力矩阵 $R$，等价于可分离卷积运算。
- **Factorized 模式**：对 Dense/Random 进行低秩对角化分解以降低参数量。
该模型在机器翻译和对话生成等单任务上取得了媲美标准自注意力的成绩，表明自注意力的动态“token对token”内积并不是拟合序列顺序关系的唯一方式。
