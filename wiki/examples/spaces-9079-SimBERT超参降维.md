---
type: example
title: SimBERT超参降维
article_id: 9079
article: 当BERT-whitening引入超参数：总有一款适合你
section: 思路分析
claim: 设定超参数 beta=gamma=0 以保持余弦相似度几何不失真，仅用正交基 U 对 SimBERT 特征进行无损 PCA 降维的步骤。
steps: 1. 读入已被有监督微调的 SimBERT 句向量 $\{x_i\}$；\n2. 计算特征协方差并做 SVD，提取正交基矩阵 $\boldsymbol{U}$；\n3. 设定超参数值 $\beta=\gamma=0$；\n4. 应用公式：$\tilde{\boldsymbol{x}}_i = \boldsymbol{x}_i \boldsymbol{U}$。此时由于基正交且无中心化，余弦度量完全等价；\n5. 为减小检索维度，截取前 $k=256$ 维表示 $\tilde{\boldsymbol{x}}_i[:,:256]$；\n6. 在 STS-B 与 ATEC 测试集上检验检索效果，证明降维几乎无损于原特征。
used_concepts: ["[[BERT-whitening]]", "[[SimBERT]]"]
notation_mapping: {"\\beta": "中心偏置超参数", "\\gamma": "对角特征拉伸平权度"}
source_span: ev::9079::超参数
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md"]
source_ids: ["9079"]
status: stable
updated: 2026-06-12
---

# SimBERT超参降维

## 演示过程
本例展示如何通过将白化变换超参数设定为 $\beta=\gamma=0$，从而在不改变相似度拓扑的同时完成 PCA 降维。

变换公式定义为：
$$
\tilde{\boldsymbol{x}}_i = (\boldsymbol{x}_i - \beta\boldsymbol{\mu})\boldsymbol{U}\boldsymbol{\Lambda}^{-\gamma/2}
$$
当超参数选取为 $\beta=\gamma=0$ 时：
$$
\tilde{\boldsymbol{x}}_i = \boldsymbol{x}_i \boldsymbol{U}
$$
计算内积：
$$
\langle \tilde{\boldsymbol{x}}_i, \tilde{\boldsymbol{x}}_j \rangle = \boldsymbol{x}_i \boldsymbol{U} (\boldsymbol{x}_j \boldsymbol{U})^{\top} = \boldsymbol{x}_i \boldsymbol{U}\boldsymbol{U}^{\top} \boldsymbol{x}_j^{\top}
$$
由于 SVD 得到的 $\boldsymbol{U}$ 是标准正交矩阵，满足 $\boldsymbol{U}\boldsymbol{U}^{\top} = \boldsymbol{I}$，因此有：
$$
\langle \tilde{\boldsymbol{x}}_i, \tilde{\boldsymbol{x}}_j \rangle = \langle \boldsymbol{x}_i, \boldsymbol{x}_j \rangle
$$
这也保证了余弦夹角大小的不变性。
由于对角矩阵 $\boldsymbol{\Lambda}$ 对特征值自大至小排好了序，正交投影基 $\boldsymbol{U}$ 的每列主成分也是依次递减的，保留前 $k$ 维即能无损压缩表示维度。