---
type: example
title: 重复解码概率推导
aliases: []
article_id: "8128"
article: "[[spaces-8128-seq2seq-zhong-fu-jie-ma-xian-xiang-de-li-lun-fen-xi-chang-shi]]"
section: 二元解码
claim: 二元解码模型下的重复概率等于无穷级数Σ Tr(P⊗P)^k，下界与转移矩阵非零概率ζ和迹相关
notation_mapping: 标准符号: P（转移矩阵），P⊗P（逐元素乘积）；源文符号一致
steps:
  - "1. 假设2-gram马尔可夫模型：p(y_t)=P_{y_{t-1},y_t}"
  - "2. 三元重复[i,j,k,i,j,k,i]的概率：P_{i,j}P_{j,k}P_{k,i}P_{i,j}P_{j,k}P_{k,i}"
  - "3. 所有三元重复和：Σ_{i,j,k} P_{i,j}^2 P_{j,k}^2 P_{k,i}^2 = Tr(P⊗P)^3"
  - "4. 所有长度重复和：R = Σ_{k=1}∞ Tr(P⊗P)^k"
  - "5. 下界估计：R ≥ Σ (Tr P^k)^2 / (ζ^k n^k)"
used_concepts: ["[[重复解码]]", "[[自回归生成模型]]"]
used_formulas: ["[[重复概率公式]]"]
used_methods: ["[[词级Rebalanced Encoding]]"]
source_span: "ev::8128::二元解码"
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "8128"
status: draft
updated: 2026-06-12
---
# 重复解码概率推导

**本文来源：** 文章 8128

**所属章节：** 二元解码

**核心观点：** 二元解码模型下的重复概率等于无穷级数Σ Tr(P⊗P)^k，下界与转移矩阵非零概率ζ和迹相关

## 推导步骤
- 1. 假设2-gram马尔可夫模型：p(y_t)=P_{y_{t-1},y_t}
- 2. 三元重复[i,j,k,i,j,k,i]的概率：P_{i,j}P_{j,k}P_{k,i}P_{i,j}P_{j,k}P_{k,i}
- 3. 所有三元重复和：Σ_{i,j,k} P_{i,j}^2 P_{j,k}^2 P_{k,i}^2 = Tr(P⊗P)^3
- 4. 所有长度重复和：R = Σ_{k=1}∞ Tr(P⊗P)^k
- 5. 下界估计：R ≥ Σ (Tr P^k)^2 / (ζ^k n^k)

## 符号映射
标准符号: P（转移矩阵），P⊗P（逐元素乘积）；源文符号一致
