---
type: example
title: pLSA的EM算法推导
aliases: []
article_id: "4277"
article: article::4277
section: EM算法
claim: "通过构造Q函数将log-sum项线性化，使得在概率约束下可解析求解pLSA模型"
notation_mapping:
  p(x|z): 主题z到词x的分布
  p(z|y): 文档y到主题z的分布
  C_{x,y,z,n}: E步计算的后验权重常数
steps:
  - "将交叉熵表示为包含隐变量z的log-sum形式"
  - "构造近似Q函数 S'_n = -sum tilde{p}(x,y) sum_z C_{x,y,z,n} log p(x|z)p(z|y)"
  - "E步利用当前参数计算后验权重 C_{x,y,z,n}"
  - "M步固定权重求Q函数最小值（解析解）"
used_concepts:
  - "[[EM算法]]"
  - "[[最大似然]]"
source_span:
  start: 108
  end: 153
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-03-23-梯度下降和EM算法-系出同源-一脉相承.md
source_ids:
  - "4277"
method: "[[近似曲线迭代法]]"
status: draft
updated: 2026-06-13
---

pLSA模型中，通过构造Q函数 $S'_n = -\sum_{x,y} \tilde{p}(x,y)\sum_z C_{x,y,z,n}\log p(x|z)p(z|y)$ 将log-sum项线性化，使得在概率约束下可解析求解。其中E步计算 $C_{x,y,z,n}=p_n(x|z)p_n(z|y)/\sum_z p_n(x|z)p_n(z|y)$ 作为常数权重。这个构造与梯度下降法抛物线近似遵循相同的"近似曲线迭代"思想。
