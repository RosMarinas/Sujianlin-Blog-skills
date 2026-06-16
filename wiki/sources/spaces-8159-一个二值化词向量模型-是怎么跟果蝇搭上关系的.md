---
type: article_summary
title: 一个二值化词向量模型，是怎么跟果蝇搭上关系的？
article_id: 8159
source_url: https://spaces.ac.cn/archives/8159
date: 2021-02-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
status: draft
updated: 2026-06-12
---

# 一个二值化词向量模型，是怎么跟果蝇搭上关系的？

## 文章核心问题
探究二值化词向量模型（BioWord）是如何从仿生学（果蝇嗅觉回路）以及数学表示（Locality Sensitive Hashing, LSH）中演化出来的。

## 主要结论
BioWord 采用了 BioHash 进行向量二值化，而 BioHash 是从 FlyHash 演进而来。FlyHash 受到果蝇嗅觉回路的“高维 + 低激活”机制启发，通过随机稀疏矩阵投影并结合赢者通吃（WTA）保留最大前 $k$ 个激活值来完成二值化编码。BioHash 则将完全随机投影基底改为了基于特定数据集的 K-Means 聚类中心，使得在更低特征维度下有更精确的相似度保持能力。

## 推导结构
1. 介绍 BioWord 模型的词袋拼接表示以及 BioHash 的具体转换。
2. 剖析 BioHash 算法中基于内积距离的聚类和更新步骤。
3. 追溯 FlyHash 算法的起源，解析果蝇嗅觉系统的“高维 + 低激活”思想。
4. 补充 LSH 的高维空间正交高斯投影与符号函数截断二值化机制。

## 关键公式
- LSH 二值化：$\\text{sgn}(\\boldsymbol{x} \\boldsymbol{W})$，其中 $\\boldsymbol{W} \\in \\mathbb{R}^{D \\times K}$ 为高斯随机矩阵。

## 体现的方法
- [[LSH随机投影二值化]]：符号哈希逼近夹角余弦。
- [[FlyHash二值化]]：高维随机投影加 WTA 稀疏离散化。
- [[BioHash二值化]]：基于 K-Means 质心投影加 WTA 进行特征离散。

## 与其他文章的关系
- 使用随机投影加速自注意力的方法见 [[Nyströmformer：基于矩阵分解的线性化Attention方案]]。

## 原文证据锚点
- `ev::8159::高维低激活`：对应原文中介绍 FlyHash 算法通过随机投影和 Winner-Take-All 机制得到高维且仅保留 $k$ 个 1 的稀疏二值向量的过程。