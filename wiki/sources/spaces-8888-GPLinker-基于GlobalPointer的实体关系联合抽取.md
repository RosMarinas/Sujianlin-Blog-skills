---
type: article_summary
title: GPLinker：基于GlobalPointer的实体关系联合抽取
article_id: "8888"
source_url: https://spaces.ac.cn/archives/8888
date: 2022-01-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-01-30-GPLinker-基于GlobalPointer的实体关系联合抽取.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[GlobalPointer]]
  - [[Efficient GlobalPointer]]
methods:
  - [[GPLinker实体关系联合抽取]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-30-GPLinker-基于GlobalPointer的实体关系联合抽取.md
source_ids:
  - "8888"
---

# GPLinker：基于GlobalPointer的实体关系联合抽取

本文提出了基于GlobalPointer的关系联合抽取模型GPLinker。传统实体关系三元组抽取本质上是五元组 $(s_h, s_t, p, o_h, o_t)$ 识别（即主实体首尾、客实体首尾与关系类型），由于直接预测五元组会导致计算复杂度过高，GPLinker提出将其在概念上分解为四个更低维度的打分项之和。

具体而言，模型包括用于识别Subject和Object实体的首尾打分项 $S(s_h,s_t)$ 和 $S(o_h,o_t)$，以及用于匹配特定关系类型 $p$ 下实体首-首、尾-尾对齐的打分项 $S(s_h,o_h|p)$ 和 $S(s_t,o_t|p)$。每一项都利用GlobalPointer（或Efficient GlobalPointer）进行统一建模。此外，针对大模型训练中概率对齐矩阵计算容易遭遇计算量爆炸和OOM的困境，模型引入了“稀疏版”多标签交叉熵，仅传递正类标签下标即可算得等价损失，极大加快了模型的训练与解码速度。
