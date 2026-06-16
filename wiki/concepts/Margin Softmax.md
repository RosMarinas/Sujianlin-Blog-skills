---
type: concept
title: "Margin Softmax"
aliases:
  - "Margin-based Softmax"
  - "边距Softmax"
definition: "在Softmax中引入margin m使分类边界扩大，保证类内距离+margin < 类间距离，从而分类模型的特征可用于排序检索。AM-Softmax是典型实现。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-09-01-从三角不等式到Margin-Softmax.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-31-再谈类别不平衡问题-调节权重与魔改Loss的对比联系.md
source_ids:
  - "8656"
  - "7708"
prerequisites:
  - "[[Softmax]]"
  - "[[交叉熵]]"
equivalent_forms: []
related_methods:
  - "[[用三角不等式指导Margin设计]]"
evidence_spans:
  - "ev::8656::三角不等式推导margin"
  - "ev::8656::AM-Softmax导出"
status: draft
updated: 2026-06-12
---

# Margin Softmax

## Definition

通过三角不等式 d(z₁,c₁) + d(z₃,c₁) + d(z₂,c₂) < d(z₁,c₂) 可导出margin的必要性：分类只要求d(z₁,c₁) < d(z₁,c₂)，但排序需要额外的margin ≈ 类平均直径。AM-Softmax Loss: log(1+∑e^{s·[cos(z₁,cᵢ)+m-cos(z₁,c₁)]})。在类别不平衡场景，margin可设为m_y = -τlog p(y)，使少样本类有更大margin。
