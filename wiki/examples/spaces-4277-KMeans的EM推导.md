---
type: example
title: KMeans的EM推导
aliases: []
article_id: "4277"
article: article::4277
section: K-Means
claim: "通过光滑max函数近似min操作推导K-Means的EM迭代算法"
notation_mapping:
  c_j: 第j个聚类中心
  x_i: 第i个数据点
  Delta_{i,j}: 数据点i是否属于聚类j（0/1指示变量）
steps:
  - "将min操作替换为光滑近似：min ≈ -1/M ln sum exp(-M * distance)"
  - "对光滑近似求梯度，得到加权平均形式的更新公式"
  - "取M→∞极限，权重退化为0/1指示函数"
  - "最终迭代：新聚类中心 = 同类点的平均"
used_concepts:
  - "[[EM算法]]"
  - "[[梯度下降]]"
source_span:
  start: 157
  end: 224
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-03-23-梯度下降和EM算法-系出同源-一脉相承.md
source_ids:
  - "4277"
method: "[[近似曲线迭代法]]"
status: draft
updated: 2026-06-13
---

K-Means聚类通过光滑max函数近似min操作，推导出指数族加权平均的迭代公式。取极限后得到经典K-Means：$\boldsymbol{c}^{(n+1)}_j = \sum_{i=1}^N \Delta^{(n)}_{i,j}\boldsymbol{x}_i / \sum_{i=1}^N \Delta^{(n)}_{i,j}$，其中 $\Delta_{i,j}$ 指示最近的聚类中心。这展示了EM算法在非概率模型（聚类）中的同样适用性。
