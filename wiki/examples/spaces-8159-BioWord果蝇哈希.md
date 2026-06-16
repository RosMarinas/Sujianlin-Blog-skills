---
type: example
title: BioWord果蝇哈希
article_id: 8159
article: 一个二值化词向量模型，是怎么跟果蝇搭上关系的？
section: FlyHash
claim: 基于高维稀疏矩阵与 WTA 机制生成稀疏二值编码的计算步骤。
steps: 1. 设定升维参数 K ；\n2. 生成随机稀疏二值投影阵 W；\n3. 计算升维映射 y = x * W；\n4. 使用 WTA 算子仅置前 k 个最大激活为 1，其余置 0。
used_concepts: ["[[FlyHash]]"]
notation_mapping: {"W": "稀疏随机映射算子"}
source_span: ev::8159::高维低激活
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
status: stable
updated: 2026-06-12
---

# BioWord果蝇哈希

## 演示过程
本例演示果蝇嗅觉哈希算法（FlyHash）通过升维与稀疏激活（WTA）编码高维特征的过程。

设输入向量 $\boldsymbol{x} \in \mathbb{R}^{d}$，升维目标为 $K$。
1. 构造一个随机的稀疏连接矩阵 $\boldsymbol{W} \in \mathbb{R}^{d \times K}$，每一列中仅有 $10\%$ 的元素为 1（代表嗅觉受体与投射神经元的稀疏连接），其余为 0。
2. 计算映射结果 $\boldsymbol{y} = \boldsymbol{x}\boldsymbol{W}$。
3. 使用 Winner-Take-All 机制：
   - 排序并找到 $\boldsymbol{y}$ 中最大的前 $k$ 个元素索引集 $\mathcal{I}$；
   - 设 $\boldsymbol{h}_j = 1$ 若 $j \in \mathcal{I}$，否则 $\boldsymbol{h}_j = 0$。