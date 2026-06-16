---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: WMD文本相似度计算
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
method_summary: 使用均匀权重和欧氏距离，通过Wasserstein距离比较两个变长词向量序列的相似度
typical_structure: |
  1. 将两个文本表示为词向量的序列
  2. 假定每个词的重要性权重相等（均匀分布 $p_i = 1/m, q_j = 1/n$），或由归一化的词频等决定
  3. 计算词向量两两之间的几何距离（通常为欧氏距离）作为推土成本矩阵 $d_{i,j}$
  4. 利用 Wasserstein 距离（最优传输）计算将一个句子的词汇“搬运”到另一个句子词汇的最低成本
  5. 可选：由于 WMD 计算为 $O(mnd)$，在检索任务中可使用 WCD（句向量中心距离）作为下界进行快速初筛
applicability: 需要直接计算两个变长文本序列之间细粒度相似度的场景，适用于短文本匹配与检索重排。
tools: 
related_methods: 
examples:
  - [[article::7388]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::7388::文章介绍了如何将计算文本向量序列相似度转化为最优传输（推土机）问题，通过线性规划求出 Word Mover's Distance，并给出了基于 scipy 的代码实现---





---
## 适用问题

在自然语言处理中，直接比较两个变长词向量序列的差异性（如精细的文本匹配和相似度计算），比将句子压缩成固定大小的单个向量能保留更多细粒度的词汇级对齐信息。WMD 致力于解决这种“序列到序列”的集合匹配问题。

## 核心变换

将文本序列相似度计算变换为一个最优传输（推土机）问题，通过 Wasserstein 距离来衡量：
$$
\min_{\gamma_{i,j} \geq 0} \sum_{i,j} \gamma_{i,j} d_{i,j} \quad \text{s.t.} \quad \sum_j \gamma_{i,j}=p_i, \quad \sum_i \gamma_{i,j}=q_j
$$
其中 $p_i$ 和 $q_j$ 是词的权重，$d_{i,j}$ 是词向量之间的几何距离（如欧氏距离），从而找到将一个句子的语义分布转换为另一个句子的最优对齐和搬运成本。

## 典型步骤

1. **向量化与定权**：将两个待比较的句子表示为词向量序列，并为每个词分配权重（如均匀权重 $1/N$ 或归一化词频）。
2. **计算距离矩阵**：计算两两词向量之间的欧氏距离，构建推土成本矩阵 $D$。
3. **求解线性规划**：在边缘分布满足词权重的约束下，利用线性规划求解器求解将一个序列的“质量”推到另一个序列的最低成本。
4. **计算下界（可选）**：如果用于大规模检索，先计算两句话词向量重心的欧氏距离（Word Centroid Distance, WCD），因为 WCD 总是小于等于 WMD，可利用该性质进行快速过滤。

## 直觉

WMD 借鉴了 Earth Mover's Distance（推土机距离）的直觉概念：如果我们把每个词看作空间中堆积的“一堆土”，句子的含义就是这些土堆的总和。那么比较两个句子，就是计算把一句话中各处的土，搬运并重塑成另一句话的土堆分布所需要的最少做功。距离越小，说明两个句子在词义空间上越重合。

## 边界

- **计算复杂度高**：WMD 需要解一个线性规划问题，最坏情况时间复杂度达到 $\mathcal{O}(V^3 \log V)$（其中 $V$ 是词数），即使实际稍快，仍远慢于简单的向量内积，无法直接用于大规模库的粗排。
- **权重假设简单**：默认情况下将各词一视同仁或仅依赖词频，无法区分核心词与停用词在语义中的真实地位差异。
- **欧氏距离局限**：在高维词向量空间中，欧氏距离往往不能最好地反映词义相似度，余弦相似度通常更符合直觉。

## 例子

- **检索过滤策略**：计算 WCD 的复杂度仅为 $\mathcal{O}(d)$，在检索系统中，如果 WCD 已经大于设定的阈值，则由于 $WCD \le WMD$，WMD 必然也大于阈值，因此可以直接舍弃该样本，仅对 WCD 较小的候选集计算精确的 WMD。

## 证据

- **ev::7388::建模与实现**：博客指出，计算文本序列差异可以直接用最优传输理论建模，并通过 `scipy.optimize.linprog` 给出了极简的代码验证，论证了 WMD 作为比定长向量更精细度量方式的优雅性。
