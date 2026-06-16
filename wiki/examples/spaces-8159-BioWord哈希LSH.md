---
type: example
title: BioWord哈希LSH
article_id: 8159
article: 一个二值化词向量模型，是怎么跟果蝇搭上关系的？
section: LSH
claim: 使用高斯随机超平面映射做余弦二值化符号截断的计算步骤。
steps: 1. 初始化多元标准正交高斯矩阵 W；\n2. 读入高维句向量 x；\n3. 计算投影内积 y = x * W；\n4. 应用符号函数 sgn(y) 得到 +1/-1 的离散特征签名。
used_concepts: ["[[LSH]]"]
notation_mapping: {"W": "高斯随机划分超平面"}
source_span: ev::8159::高维低激活
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-02-09-一个二值化词向量模型-是怎么跟果蝇搭上关系的.md"]
source_ids: ["8159"]
status: stable
updated: 2026-06-12
---

# BioWord哈希LSH

## 演示过程
本例演示了如何利用高斯随机投影矩阵进行局部敏感哈希（LSH）的符号二值化。

设输入向量 $\boldsymbol{x} \in \mathbb{R}^{d}$。
1. 产生随机高斯投影阵 $\boldsymbol{W} \in \mathbb{R}^{d \times K}$，每一分量独立服从标准高斯分布：
   $$
   \boldsymbol{W}_{ij} \sim \mathcal{N}(0, 1)
   $$
2. 计算投影结果 $\boldsymbol{y} = \boldsymbol{x}\boldsymbol{W}$。
3. 执行二值化符号切割：
   $$
   \boldsymbol{h} = \text{sgn}(\boldsymbol{y})
   $$
4. 生成汉明签名用于超快速余弦排序检索。