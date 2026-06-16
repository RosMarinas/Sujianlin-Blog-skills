---
type: example
title: BioWord聚类哈希
article_id: 8159
article: 一个二值化词向量模型，是怎么跟果蝇搭上关系的？
section: BioHash
claim: 基于 K-Means 质心投影矩阵与 WTA 生成自适应稀疏哈希的计算步骤。
steps: 1. 在词向量语料上聚类得到 K 个中心点质心 U；\n2. 计算待编码向量与质心 U 的相似度矩阵；\n3. 通过 WTA 置最大前 k 个响应通道为 1，其余为 0；\n4. 输出二值稀疏签名。
used_concepts: ["[[BioHash]]", "[[FlyHash]]"]
notation_mapping: {"U": "聚类代表质心矩阵"}
source_span: ev::8159::高维低激活
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
status: stable
updated: 2026-06-12
---

# BioWord聚类哈希

## 演示过程
本例演示 BioHash 算法结合无监督聚类质心投影和 WTA 获得自适应稀疏二进制串的过程。

1. 对语料库中所有词向量做 K-Means 聚类，提取 $K$ 个质心向量作为投影轴：
   $$
   \boldsymbol{U} = [\boldsymbol{u}_1, \dots, \boldsymbol{u}_K]
   $$
2. 计算查询词向量 $\boldsymbol{x}$ 与质心轴的夹角余弦相似度：
   $$
   \boldsymbol{y}_j = \cos(\boldsymbol{x}, \boldsymbol{u}_j)
   $$
3. 对 $\boldsymbol{y}$ 执行 Winner-Take-All：
   - 保留最大的前 $k$ 个相似质心，对应的二进制位设为 1，其余位置为 0。