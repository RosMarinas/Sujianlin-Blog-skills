---
type: example
title: 测地线距离计算
article_id: 9368
article: 从局部到全局：语义相似度的测地线距离
section: 测地距离
claim: 基于句向量近距离矩阵构建 k-NN 邻近网络，并计算远距离测地线的最短路径步骤。
steps: 1. 读入全体样本表示，计算两两之间的初始欧式或余弦距离；\n2. 对每个特征节点，仅保留距离最近的 $k$ 个邻近边，剔除大距离连边，构成带权局部邻近图 $G_k$；\n3. 设定起点句子向量为 $t_i$，大语义主题节点为 $c$；\n4. 针对图 $G_k$ 使用 Dijkstra 算法，检索 $t_i$ 到 $c$ 的连通最短路径 $P = (e_1, e_2, \dots, e_p)$；\n5. 累加各路段的局部距离权重：$\text{dist}_{\text{geo}} = \sum_{m=1}^p \text{weight}(e_m)$；\n6. 取语义相似度为 $s(t_i, c) = 1/\text{dist}_{\text{geo}}$ 作为全局相对排序的基础值。
used_concepts: ["[[测地线距离]]"]
notation_mapping: {"G_k": "局部可信的 $k$ 邻近网络", "\\text{dist}_{\\text{geo}}": "流形上的最短路径测地线近似"}
source_span: ev::9368::测地线距离
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-12-07-从局部到全局-语义相似度的测地线距离.md"]
source_ids: ["9368"]
status: stable
updated: 2026-06-12
---

# 测地线距离计算

## 演示过程
本例展示如何通过将高维特征在弯曲流形上的全局相似性，用局部可信的 $k$ 近邻网图的最短路径（Dijkstra）进行近似。

设原始高维句向量空间为 $\mathcal{X}$。局部相对测度 $\text{dist}(\boldsymbol{u}, \boldsymbol{v})$ 仅在 $\text{dist} < \epsilon$ 时可信。
1. 构建邻接图 $G = (V, E)$，两点连边条件为：
$$
e_{ij} \in E \iff \boldsymbol{v}_j \in \text{k-NN}(\boldsymbol{v}_i) \text{ 或 } \boldsymbol{v}_i \in \text{k-NN}(\boldsymbol{v}_j)
$$
2. 边权赋值为局部欧式距离：
$$
w(e_{ij}) = \Vert \boldsymbol{v}_i - \boldsymbol{v}_j \Vert
$$
3. 给定远端节点对 $(s, d)$，测地线最短距离路径可描述为：
$$
\text{dist}_{\text{geo}}(s, d) = \min_{P} \sum_{e \in P} w(e)
$$
其中 $P$ 为连接 $s$ 和 $d$ 的所有可能图路径集合。此方式平滑地沿着表示的流形几何进行推演，改善了全局比较的效果。