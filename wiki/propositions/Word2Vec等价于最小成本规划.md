---
type: proposition
title: Word2Vec等价于最小成本规划
aliases:
  - Word2Vec as Minimum Cost Planning
statement: Word2Vec的Skip Gram模型可以等价地从图书馆排书的最小成本模型导出：将词语看作书，共现看作借书习惯，词向量训练等价于寻找使总访问成本最小的空间位置规划。
assumptions:
  - 词向量模型使用内积度量 $e^{\langle\boldsymbol{v}_i,\boldsymbol{v}_j\rangle}/Z_i$ 作为条件概率
  - 不需要区分中心词和上下文词向量（为理解本质可简化）
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-02-最小熵原理-四-物以类聚-之从图书馆到词向量.md
source_ids:
  - "6191"
requires:
  - [[最小熵原理]]
  - [[互信息词向量]]
proof_route: 图书馆成本模型 $S = \sum p(i,j)[\|\boldsymbol{v}_i\| + \|\boldsymbol{v}_i - \boldsymbol{v}_j\|]$，去约束后化为 $S = -\sum p(i,j)\log q(j|i)$。选择内积距离 $f(\boldsymbol{v}_i,\boldsymbol{v}_j) = -\log(e^{\langle\boldsymbol{v}_i,\boldsymbol{v}_j\rangle}/Z_i)$ 即得到Skip Gram优化目标。
methods:
  - [[用互信息内积构造词向量几何]]
  - [[用矩阵分解重写表示学习结构]]
examples:
  - [[spaces-6191-最小熵原理-四-物以类聚-之从图书馆到词向量]]
limits: 简化的类比忽略了Word2Vec中中心词/上下文词向量的区分和负采样等实现细节。
status: draft
updated: 2026-06-10
null_evidence_reason: "Key connection from article 4; evidence spans to be formalized."
---

# Word2Vec等价于最小成本规划

## 扩展：t-SNE

相同的数学框架可以导出t-SNE降维算法，只需将距离度量从高斯核换成t分布。这表明Word2Vec和t-SNE共享深层的数学结构。
