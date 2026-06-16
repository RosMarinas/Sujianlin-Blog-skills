---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: WRD文本相似度计算
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
  - Data/wiki/sources/spaces-8512-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-正态分布距离.md
source_ids:
  - 7388
  - 8512
  - 9797
method_summary: 使用向量模长作为权重、余弦距离作为传输成本，通过Wasserstein距离比较两个变长序列的差异
typical_structure: |
  1. 将两个文本表示为词向量的序列
  2. 提取每个词向量的模长，将模长除以序列模长总和，计算得到各词的权重 $p_i$ 和 $q_j$
  3. 计算词向量间的余弦距离（$1 - \cos(\theta)$）作为推土成本矩阵 $d_{i,j}$
  4. 利用 Wasserstein 距离（线性规划）计算最低对齐成本
  5. 可选：利用公式推导下界（归一化模长的句向量之差）进行快速过滤
applicability: 需要直观感知相似度阈值的文本比较场景，且词向量模长代表词重要性（如未进行LayerNorm的高维空间）的假设成立时效果更好。
tools: 
related_methods: 
examples:
  - [[article::7388]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::7388::文章指出了 WMD 使用欧氏距离和均匀分布的缺陷，并介绍了 Word Rotator's Distance (WRD) 的解决思路：将模长融入权重并使用余弦距离---





---
## 适用问题

在比较变长文本序列相似度时，传统的 WMD (Word Mover's Distance) 存在两个局限：第一，简单使用欧氏距离并不总是匹配高维词向量的语义（余弦距离通常更佳）；第二，默认词权重为均匀分布忽略了核心词与停用词的重要性差异。WRD (Word Rotator's Distance) 旨在通过修改距离度量和边缘权重来解决上述问题。

## 核心变换

将 WMD 中的均匀分布权重替换为与词向量模长成正比的权重：
$$
p_i = \frac{\Vert\boldsymbol{w}_i\Vert}{\sum_k \Vert\boldsymbol{w}_k\Vert}
$$
并将欧氏距离替换为余弦距离：
$$
d_{i,j}=1 - \frac{\boldsymbol{w}_i\cdot \boldsymbol{w}'_j}{\Vert\boldsymbol{w}_i\Vert\times \Vert\boldsymbol{w}'_j\Vert}
$$
这使得匹配过程更像是在超球面上将一个单位向量“旋转”（rotate）到另一个方向，而非平移（move）。

## 典型步骤

1. **提取词表示与模长**：将文本映射为词向量序列，并分别计算各词向量的 $\mathcal{L}_2$ 模长。
2. **计算概率分布**：将词的模长在句子内部归一化，形成最优传输约束中的边缘概率分布 $p$ 和 $q$。
3. **计算距离矩阵**：对所有词对计算余弦距离（$1 - \cos$），构成代价矩阵 $D$。
4. **线性规划求解**：利用 `scipy.optimize.linprog` 等工具，求出在 $p$ 和 $q$ 的质量守恒约束下的最小转移代价。
5. **计算下界（可选）**：通过詹森不等式，可求出其计算下界为加权平均句向量之间的欧氏距离，可用作快速过滤策略。

## 直觉

经验和研究（如 Simpler GloVe）表明，词向量的模长往往与该词的信息量或重要性正相关。如果在计算距离前强制归一化词向量以使用余弦相似度，就会丢失模长信息。WRD 巧妙地将模长转化为“搬运的质量（权重）”，同时利用归一化后的向量计算余弦距离，使得重要的词获得更大的质量，从而对整体相似度产生更大的影响。由于使用的是余弦距离，最终结果被严格限制在 $[0, 2]$ 区间内，更加方便在实际系统中设定绝对的相似度阈值。

## 边界

- **模长假设依赖**：WRD 的有效性极其依赖于“词向量的模长正相关于重要程度”这一假设。如果词向量本身经过了 Layer Normalization 或其他强制归一化处理，这个优势就会完全消失。
- **复杂度未减**：本质上仍然是解一个线性规划问题， $\mathcal{O}(V^3 \log V)$ 的时间复杂度瓶颈没有得到缓解。

## 例子

- **参考实现与下界推导**：利用 `scipy` 只需几行代码便可实现 WRD；同时可以通过不等式推导理论下界，在文本匹配中用来初步筛除极度不相似的文本对。

## 证据

- **ev::7388::模长与权重的对应**：引用了原论文《Word Rotator's Distance: Decomposing Vectors Gives Better Representations》的核心观点，证实了将模长作为 Wasserstein 距离中的边缘约束是一种改进方案。
