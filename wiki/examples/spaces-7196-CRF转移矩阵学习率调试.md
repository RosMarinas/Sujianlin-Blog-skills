---
type: example
title: CRF转移矩阵学习率调试
aliases: []
article_id: "7196"
article: "[[spaces-7196-ni-de-crf-ceng-de-xue-xi-lv-ke-neng-bu-gou-da]]"
section: 学习率的不对等
claim: BERT+CRF中CRF层学习率需要为主体100倍以上才能学到合理的转移矩阵
notation_mapping: 标准符号: S_{i→j}（转移分数）；源文符号一致
steps:
  - "1. 观察BERT+CRF训练出的转移矩阵S_{s→e}不合理地大于S_{s→b}"
  - "2. 归因：BERT学习率10^-5，CRF层同速率，逐标签分布迅速收敛使CRF梯度消失"
  - "3. 将CRF层学习率提高到10^-2（1000倍主学习率）"
  - "4. 转移矩阵变得合理：S_{s→s,b} > S_{s→m,e}"
  - "5. 用只取BERT前1层的实验证明拟合能力弱时CRF更有效"
used_concepts: ["[[条件随机场]]", "[[线性链CRF]]"]
used_formulas: ["[[CRF条件概率]]"]
used_methods: ["[[线性链CRF构建]]"]
source_span: "ev::7196::学习率的不对等"
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "7196"
status: draft
updated: 2026-06-12
---
# CRF转移矩阵学习率调试

**本文来源：** 文章 7196

**所属章节：** 学习率的不对等

**核心观点：** BERT+CRF中CRF层学习率需要为主体100倍以上才能学到合理的转移矩阵

## 推导步骤
- 1. 观察BERT+CRF训练出的转移矩阵S_{s→e}不合理地大于S_{s→b}
- 2. 归因：BERT学习率10^-5，CRF层同速率，逐标签分布迅速收敛使CRF梯度消失
- 3. 将CRF层学习率提高到10^-2（1000倍主学习率）
- 4. 转移矩阵变得合理：S_{s→s,b} > S_{s→m,e}
- 5. 用只取BERT前1层的实验证明拟合能力弱时CRF更有效

## 符号映射
标准符号: S_{i→j}（转移分数）；源文符号一致
