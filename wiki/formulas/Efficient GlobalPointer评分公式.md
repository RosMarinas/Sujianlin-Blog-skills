---
type: formula
title: Efficient GlobalPointer评分公式
latex: s_{\alpha}(i,j) = \boldsymbol{q}_i^{\top}\boldsymbol{k}_j + \boldsymbol{w}_{\alpha}^{\top}[\boldsymbol{q}_i;\boldsymbol{k}_i;\boldsymbol{q}_j;\boldsymbol{k}_j]
symbol_meanings:
  s_{\alpha}(i, j): 输入连续跨度 [i, j] 作为实体类别 \alpha 的打分
  q_i: 序列位置 i 对应的通用查询向量 (Query)
  k_j: 序列位置 j 对应的通用键向量 (Key)
  w_{\alpha}: 针对特定实体类别 \alpha 的轻量级权重偏置向量
  ;: 向量拼接操作 (Concatenation)
standard_notation: s_{\alpha}(i,j) = \boldsymbol{q}_i^{\top}\boldsymbol{k}_j + \boldsymbol{w}_{\alpha}^{\top}[\boldsymbol{q}_i;\boldsymbol{k}_i;\boldsymbol{q}_j;\boldsymbol{k}_j]
conditions: 适用于Efficient GlobalPointer中对多类型实体跨度识别进行低参数量的统一打分
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
source_ids:
  - "8877"
appears_in:
  - [[spaces-8877-Efficient-GlobalPointer-少点参数-多点效果]]
  - [[spaces-8888-GPLinker-基于GlobalPointer的实体关系联合抽取]]
  - [[spaces-8926-GPLinker-基于GlobalPointer的事件联合抽取]]
status: stable
updated: 2026-06-12
---

# Efficient GlobalPointer评分公式

## 概述

该公式是Efficient GlobalPointer实现对多类别命名实体识别进行低显存、低参数量打分的核心表达式。

公式巧妙地将命名实体识别建模过程解耦为“跨度抽取”与“实体分类”两步。其中，前一项 $\boldsymbol{q}_i^{\top}\boldsymbol{k}_j$ 是一个类无关 of 通用Span抽取器（用以判定位置 $i$ 到 $j$ 是否为某个实体），其对应的查询向量 $\boldsymbol{q}_i$ 与键向量 $\boldsymbol{k}_j$ 投影矩阵权重由所有的实体类别共同共享，进行充分的共性学习。第二项则通过将起点与终点的投影表征拼接后与各个类别 $\alpha$ 专属的低维向量 $\boldsymbol{w}_{\alpha}$ 算内积，实现极轻量级的类别判定。这大幅降低了随着分类数膨胀导致的显存开销与过拟合风险。
