---
type: article_summary
title: GPLinker：基于GlobalPointer的事件联合抽取
article_id: "8926"
source_url: https://spaces.ac.cn/archives/8926
date: 2022-02-21
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-02-21-GPLinker-基于GlobalPointer的事件联合抽取.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[GlobalPointer]]
  - [[Efficient GlobalPointer]]
  - [[完全子图]]
methods:
  - [[GPLinker事件联合抽取]]
  - [[基于完全子图搜索的事件划分]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-21-GPLinker-基于GlobalPointer的事件联合抽取.md
source_ids:
  - "8926"
---

# GPLinker：基于GlobalPointer的事件联合抽取

本文提出了将基于GlobalPointer的联合抽取框架GPLinker扩展应用到事件联合抽取任务的方案。传统的事件抽取包含多个繁琐的子任务（如触发词检测和论元分类等），GPLinker方案通过将触发词统一视为一种特殊的事件论元角色，从而将事件抽取核心问题简化为两个部分：论元识别与事件划分。

在论元识别部分，模型将（事件类型, 论元角色）组合为大类，应用能识别嵌套实体的GlobalPointer进行实体抽取。在事件划分部分，同一个句子中可能存在同一事件类型的多个实例，模型借用TPLinker的思想，通过预测论元实体间的首-首与尾-尾关联边构建论元关系无向图，进而将事件划分问题转化为图上的“完全子图（团）”搜索。文章还设计了一种高效的递归子图搜索算法，在线上评测任务中表现出了可圈可点的提取性能。
