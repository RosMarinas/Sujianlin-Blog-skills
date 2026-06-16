---
type: example
title: spaces-6191-图书馆词向量类比
aliases:
- Library Word Vector Analogy
article_id: '6191'
article:
- - spaces-6191-最小熵原理-四-物以类聚-之从图书馆到词向量
section: 图书馆规划
claim: 图书馆排书的最佳方案等价于词向量训练：将共现频率高的书放得近、热门书放得靠门口，与Word2Vec将共现词在向量空间中靠近的几何一致。
notation_mapping:
  \boldsymbol{v}_i: 书i的坐标（词i的向量）
  p(i): 书i被借的概率（词i的频率）
  p(j|i): 借书i后再借j的概率（词j在词i上下文中出现的概率）
  \Vert\boldsymbol{v}_i\Vert: 书i到入口的距离（"热门度"对应的向量模长）
  \Vert\boldsymbol{v}_i-\boldsymbol{v}_j\Vert: 两本书之间的距离（两词向量的距离）
steps:
- 建立成本模型 $S = \sum_{i,j} p(i,j)[\|\boldsymbol{v}_i\| + \|\boldsymbol{v}_i - \boldsymbol{v}_j\|]$
- 加入最小间距约束避免所有书集中在入口（防止解坍缩）
- 去约束：用Softmax归一化将距离转化为概率
- 成本函数化为交叉熵 $S = -\sum p(i,j)\log q(j|i)$
- 最小化成本 = 最大似然 = 最小熵
- 选择内积度量 $e^{\langle\boldsymbol{v}_i,\boldsymbol{v}_j\rangle}/Z_i$ 得到Skip Gram
used_concepts:
- - - 互信息词向量
- - - 最小熵原理
used_methods:
- - - 用互信息内积构造词向量几何
problem_pattern:
- - 用熵最小化发现无监督结构
source_span: ev::6191::图书馆成本模型
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-12-02-最小熵原理-四-物以类聚-之从图书馆到词向量.md
source_ids:
- '6191'
status: draft
updated: '2026-06-12'
---

# 图书馆词向量类比

该类比是文章4的核心贡献：用图书馆排书这样直观的例子来解释Word2Vec，使得词向量的几何意义更加清晰。

在这个类比中，建立了一个简化的借书成本模型：假设读者先后去借两本书 $i$ 和 $j$，其概率联合分布为 $p(i,j) = p(i)p(j|i)$。如果在图书馆中建立三维坐标系，每本书的位置可以用一个向量 $\boldsymbol{v}_i$ 来表示。寻找第一本书的成本可看作其到图书馆入口（原点）的欧氏距离 $\Vert \boldsymbol{v}_i\Vert$，而在此基础上继续寻找第二本书的成本则对应于两本书之间的欧氏距离 $\Vert \boldsymbol{v}_i - \boldsymbol{v}_j\Vert$。

由此，可以得出对所有人的平均借书成本 $S$ 为：
$$
S = \sum_{i,j} p(i,j) \left[\Vert \boldsymbol{v}_i\Vert ＋ \Vert \boldsymbol{v}_i - \boldsymbol{v}_j\Vert\right]
$$

为了使平均找书的总力气 $S$ 最小化，排书方案必然倾向于满足以下两点：
1. **$\Vert \boldsymbol{v}_i\Vert$ 要尽量小**：这意味着被高频借阅的“热门书”应当放置在靠近图书馆出口（即坐标原点）的地方。
2. **$\Vert \boldsymbol{v}_i - \boldsymbol{v}_j\Vert$ 要尽量小**：这意味着在借书记录中经常被一起借阅（即共现概率 $p(i,j)$ 较高）的书籍应当被放在彼此相近的物理位置。

然而，如果没有其它约束直接优化这一成本目标，模型会导致所有的 $\boldsymbol{v}_i$ 坍缩为 0（即所有的书都挤在原点出口处），这就引出了书本之间必须存在一个最小间距 $d_{\min} > 0$ 的物理约束。因此，真实的图书馆排书实际上是一个带约束的优化规划问题。这种将经常共现的元素物理上靠近、高频元素靠近原点的“排书套路”，在数学上与以几何空间距离来构建自然语言内部规律的词向量（如 Word2Vec 模型）是高度一致的。
