---
type: concept
title: LSH
definition: 局部敏感哈希（Locality Sensitive Hashing），利用随机投影和符号函数保持高维夹角余弦的离散表示技术。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
aliases: ["Locality Sensitive Hashing", "局部敏感哈希", "符号哈希"]
status: stable
updated: 2026-06-12
---

# LSH

## 定义
LSH（Locality Sensitive Hashing）是一种用于高维表示空间的快速相似度近似检索哈希算法，它确保哈希后特征的汉明距离成比例近似保持原有的高维角度余弦。

## LSH 几何特征
LSH 通过高斯随机分布生成几乎正交的投影核矩阵 $\\boldsymbol{W}$，将输入向量做内积映射并取 $\\text{sgn}$ 符号截断为由 $\\pm 1$（或 $0/1$）构成的编码。这种转换对各维度采用均匀概率划分，激活比率通常在一半左右，用于构建倒排索引或作为桥接离散模式识别与连续空间提取的基础算法。