---
type: article_summary
title: 文本情感分类（四）：更好的损失函数
article_id: "4293"
source_url: https://spaces.ac.cn/archives/4293
date: 2017-03-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-03-30-文本情感分类-四-更好的损失函数.md
source_html: Data/Spaces_ac_cn/raw/articles/4293/page.html
series: []
topics:
  - "[[topic::文本情感分类]]"
concepts:
  - "[[concept::修正交叉熵]]"
methods:
  - "[[method::用修正交叉熵聚焦难分样本]]"
problem_patterns: []
evidence_spans:
  - ev::4293::修正交叉熵
  - ev::4293::实验测试
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-03-30-文本情感分类-四-更好的损失函数.md
source_ids:
  - "4293"
status: draft
updated: 2026-06-11
---

## 文章核心问题

分类模型的优化目标（交叉熵）与考核指标（准确率/泛化能力）不一致，如何设计更好的损失函数来缓解这一矛盾？

## 主要结论

1. 交叉熵追求所有样本的平均损失最小，但考核指标是准确率，两者并不完全等价。
2. 借鉴hinge loss和triplet loss思想，设计修正交叉熵：当正样本输出>阈值m或负样本输出<1-m时停止对该样本的更新，聚焦于模棱两可的样本。
3. IMDB实验：LSTM上测试准确率82.26%（vs交叉熵81.02%），提升约0.5%-1%；CNN上训练更稳定、波动更小。

## 推导结构

要平均不一定要拔尖（动机分析）→ 更好的更新方案（聚焦难分样本的思想）→ 修正的交叉熵损失（数学定义和λ函数）→ 基于IMDB的实验测试（LSTM和CNN结果）。

## 关键公式

- 原始交叉熵：L_old = -Σ y_true log y_pred
- 修正交叉熵：L_new = -Σ λ(y_true,y_pred) y_true log y_pred
- λ(1,y_pred) = 1-θ(y_pred-m)，λ(0,y_pred)=1-θ(1-m-y_pred)
- θ是单位阶跃函数，m是阈值（如0.6）

## 体现的方法

- **用修正交叉熵聚焦难分样本**：通过带阈值的修正λ函数让模型专注于模棱两可的样本，提升分类准确率和泛化能力。

## 所属系列位置

独立文章，为"文本情感分类"系列第四篇（但本编译批次只包含此一篇）。

## 与其他文章的关系

- 与[[article::4374]]同属情感分析任务（本文章改进损失函数，对方改进训练策略）。
- 与[[method::用AM-Softmax做句子相似度]]都涉及margin思想（margin用于分类损失 vs margin用于度量学习）。

## 原文证据锚点

- `ev::4293::修正交叉熵`：修正交叉熵损失函数的数学定义和λ函数。
- `ev::4293::实验测试`：IMDB上LSTM和CNN的实验对比结果。
