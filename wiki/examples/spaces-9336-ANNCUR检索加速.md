---
type: example
title: ANNCUR检索加速
article_id: 9336
article: 利用CUR分解加速交互式相似度模型的检索
section: CUR分解
claim: 利用CUR矩阵骨架近似，对Cross-Encoder的检索关联矩阵进行低秩表示加速的步骤。
steps: 1. 确定库中文档总数 $N$ 以及少量代表集 $\mathcal{U} \subset \mathcal{K}$（大小为 $c$）与请求代表集 $\mathcal{V} \subset \mathcal{Q}$（大小为 $r$）；\n2. 利用精确的单塔模型 Cross-Encoder 计算出相交方阵 $\boldsymbol{M}_{\mathcal{V}, \mathcal{U}}$ ；\n3. 计算 Moore-Penrose 伪逆矩阵 $\boldsymbol{G} = \boldsymbol{M}_{\mathcal{V}, \mathcal{U}}^{\dagger}$；\n4. 离线算好全库 key 与请求代表的打分矩阵 $\boldsymbol{H} \in \mathbb{R}^{r \times N}$，并缓存密集积 $\boldsymbol{M} = \boldsymbol{G}\boldsymbol{H}$；\n5. 检索时，对查询 $q$ 计算其与 $\mathcal{U}$ 代表的 $c$ 维打分向量 $\boldsymbol{f}$；\n6. 通过矩阵积 $\boldsymbol{f} \boldsymbol{M}$ 得到对全库的近似相似度向量。
used_concepts: ["[[CUR分解]]"]
notation_mapping: {"\\boldsymbol{G}": "代表对齐 Moore-Penrose 伪逆中间核", "\\boldsymbol{f}": "查询向量在代表基下的非线性打分"}
source_span: ev::9336::ANNCUR原理
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-11-02-利用CUR分解加速交互式相似度模型的检索.md"]
source_ids: ["9336"]
status: stable
updated: 2026-06-12
---

# ANNCUR检索加速

## 演示过程
本例展示如何用 CUR 近似关系，将复杂的 Cross-Encoder 检索开销由 $\mathcal{O}(N)$ 转化为少量基底打分与内积投影。

打分矩阵为 $\boldsymbol{S}_{M \times N}$。
我们选择请求子集索引 $S_1$ (大小为 $r$)，键子集索引 $S_2$ (大小为 $c$)。
抽取矩阵：
- $\boldsymbol{F} = \boldsymbol{S}_{[:, S_2]}$ (大小为 $M \times c$)
- $\boldsymbol{H} = \boldsymbol{S}_{[S_1, :]}$ (大小为 $r \times N$)
- 相交核心矩阵 $\boldsymbol{C}_{\text{inter}} = \boldsymbol{S}_{[S_1, S_2]}$ (大小为 $r \times c$)
其伪逆表示为 $\boldsymbol{G} = \boldsymbol{C}_{\text{inter}}^{\dagger}$。
则大得分矩阵可近似为：
$$
\boldsymbol{S} \approx \boldsymbol{F} \boldsymbol{G} \boldsymbol{H}
$$
在检索任意 query 时，对应于在 $\boldsymbol{F}$ 中添加一行 $\boldsymbol{f}$，近似相似度矩阵计算公式为：
$$
\boldsymbol{s}_{\text{approx}} = \boldsymbol{f} (\boldsymbol{G} \boldsymbol{H})
$$
其中 $\boldsymbol{G}\boldsymbol{H}$ 在代表和全库 key 确定后可直接离线算好，完成了 Cross-Encoder 检索性能的重构。