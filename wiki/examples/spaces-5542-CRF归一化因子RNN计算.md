---
type: example
title: CRF归一化因子RNN计算
aliases: []
article_id: "5542"
article: "[[spaces-5542-jian-ming-tiao-jian-sui-ji-chang-crf-jie-shao-fu-dai-chun-keras-shi-xian]]"
section: 归一化因子
claim: 利用RNN封装递归计算CRF归一化因子，将指数级路径求和转为线性复杂度
notation_mapping: 标准符号: Z_t（归一化因子向量）, G（指数化转移矩阵）；源文符号一致
steps:
  - "1. 将Z_t分解为k个分量Z_t^(1)..Z_t^(k)"
  - "2. Z_{t+1}^{(j)} = (Σ_i Z_t^(i) G_{ij}) * H_{t+1}(j|x)"
  - "3. 写为矩阵形式 Z_{t+1} = Z_t G ⊗ H(y_{t+1}|x)"
  - "4. 封装为RNN cell实现递归"
used_concepts: ["[[条件随机场]]", "[[线性链CRF]]"]
used_formulas: ["[[CRF归一化因子递推]]"]
used_methods: ["[[线性链CRF构建]]"]
source_span: "ev::5542::归一化因子"
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "5542"
status: draft
updated: 2026-06-12
---
# CRF归一化因子RNN计算

**本文来源：** 文章 5542

**所属章节：** 归一化因子

**核心观点：** 利用RNN封装递归计算CRF归一化因子，将指数级路径求和转为线性复杂度

## 推导步骤
- 1. 将Z_t分解为k个分量Z_t^(1)..Z_t^(k)
- 2. Z_{t+1}^{(j)} = (Σ_i Z_t^(i) G_{ij}) * H_{t+1}(j|x)
- 3. 写为矩阵形式 Z_{t+1} = Z_t G ⊗ H(y_{t+1}|x)
- 4. 封装为RNN cell实现递归

## 符号映射
标准符号: Z_t（归一化因子向量）, G（指数化转移矩阵）；源文符号一致
