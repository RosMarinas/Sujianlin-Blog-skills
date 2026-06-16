---
type: article_summary
title: "再谈类别不平衡问题：调节权重与魔改Loss的对比联系"
article_id: "7708"
source_url: https://spaces.ac.cn/archives/7708
date: 2020-08-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-08-31-再谈类别不平衡问题-调节权重与魔改Loss的对比联系.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[类别不平衡Loss设计]]"
  - "[[Logits Adjustment]]"
  - "[[F1光滑化]]"
evidence_spans:
  - "ev::7708::光滑准确率梯度"
  - "ev::7708::F1光滑化推导"
  - "ev::7708::Logits调整"
  - "ev::7708::margin几何理解"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-31-再谈类别不平衡问题-调节权重与魔改Loss的对比联系.md
source_ids:
  - "7708"
status: draft
updated: 2026-06-12
---

# 再谈类别不平衡问题：调节权重与魔改Loss的对比联系

## Summary

本文从梯度视角分析了类别不平衡问题的各种Loss设计思路，论证了Focal Loss、Dice Loss、Logits Adjustment等本质上都是通过调整样本权重或类权重来影响梯度，并用几何直观解释了margin的作用。

## Key Claims

1. 交叉熵优于光滑准确率的原因在于梯度中去掉了p(1-p)因子，使误差大时梯度也大。
2. 从光滑F1可导出加权交叉熵，权重由F1值动态决定。
3. Logits Adjustment可理解为给少样本类分配更大的margin，几何上等价于让少数类样本"更能打"。
4. 各种"魔改Loss"本质上都是在调节梯度，与直接调节样本权重没有本质区别。

## Key Formulas

- 光滑准确率梯度(对正样本): -p(1-p)∇z (在p→0时梯度→0，不好)
- 交叉熵梯度(对正样本): -(1-p)∇z (p→0时梯度→1，好)
- Logits Adjustment: -log(e^{⟨f,u_y⟩+τlog p(y)}/∑_i e^{⟨f,u_i⟩+τlog p(i)})

## Connections

本文讨论的Margin Softmax与8656从三角不等式推导的AM-Softmax直接相关。Logits Adjustment的几何理解与7234中对抗训练的"坑底"几何图像有类似的分析风格（通过几何直观指导损失函数设计）。
