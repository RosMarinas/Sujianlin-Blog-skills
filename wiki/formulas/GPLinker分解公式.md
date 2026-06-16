---
type: formula
title: GPLinker分解公式
latex: S(s_h,s_t,p,o_h,o_t) = S(s_h,s_t) + S(o_h,o_t) + S(s_h,o_h| p) + S(s_t, o_t| p)
symbol_meanings:
  S(s_h,s_t,p,o_h,o_t): 包含主实体首尾和客实体首尾在关系 p 下的整体五元组得分
  S(s_h,s_t): 主实体 (Subject) 首尾跨度得分
  S(o_h,o_t): 客实体 (Object) 首尾跨度得分
  S(s_h,o_h| p): 在给定关系 p 下主实体起点与客实体起点的对齐关联得分
  S(s_t,o_t| p): 在给定关系 p 下主实体终点与客实体终点的对齐关联得分
  p: 谓词关系类别 (Predicate)
standard_notation: S(s_h,s_t,p,o_h,o_t) = S(s_h,s_t) + S(o_h,o_t) + S(s_h,o_h| p) + S(s_t, o_t| p)
conditions: 用于GPLinker联合关系/事件抽取模型中，实现五元组概率匹配状态空间的降维与完全匹配
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-30-GPLinker-基于GlobalPointer的实体关系联合抽取.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-21-GPLinker-基于GlobalPointer的事件联合抽取.md
source_ids:
  - "8888"
  - "8926"
appears_in:
  - [[spaces-8888-GPLinker-基于GlobalPointer的实体关系联合抽取]]
  - [[spaces-8926-GPLinker-基于GlobalPointer of 事件联合抽取]]
status: stable
updated: 2026-06-12
---

# GPLinker分解公式

## 概述

该公式定义了GPLinker联合抽取模型中将高维实体-关系匹配空间做因式重构与降维的基本模型假设。

直接预测包含主客实体首尾跨度和谓词类型的五元组 $S(s_h, s_t, p, o_h, o_t)$，由于在长文本中其计算量呈长度的四次方级别（$O(l^4)$），在算力限制下属于不可解问题。公式将该高维打分项重构为四个相互独立的子项之和。其中 $S(s_h, s_t)$ 和 $S(o_h, o_t)$ 独立解决主实体与客实体的跨度识别。而后两项 $S(s_h, o_h | p)$ 与 $S(s_t, o_t | p)$ 则在关系类别 $p$ 的前提下对实体的起点对与终点对进行双向配对。训练时确保全部项皆大于零，预测时枚举并求交集，将复杂度限制在 $O(l^2)$，实现了又快又好的抽取。
