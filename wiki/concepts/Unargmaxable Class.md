---
type: concept
title: Unargmaxable Class
aliases:
- 无法预测的类别
- 无法预测的词
definition: 分类模型中永远不可能成为概率最大者的类别，当类别数远大于向量维度时理论上存在。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
source_ids:
- '9046'
prerequisites:
- - - concept::Softmax分类器
- - - concept::语言模型
status: draft
updated: '2026-06-12'
---

# Unargmaxable Class

## 定义与数学表述

Unargmaxable Class（无法预测的类别）指的是在训练好的分类模型（如语言模型）中，存在某些类别，不管输入是什么，都不可能预测出该类别，即该类别永远不可能成为概率最大的那个。特别地，在语言模型中，这指的是在 Greedy Search 解码下无法被选中的词。

假设各个类别向量分为 $\boldsymbol{w}_1,\boldsymbol{w}_2,\cdots,\boldsymbol{w}_n\in\mathbb{R}^d$，偏置项为 $b_1,b_2,\cdots,b_n$。
如果类别 $k$ 是**可预测的**，那么就存在 $\boldsymbol{z}\in\mathbb{R}^d$，同时满足：
$$
\langle\boldsymbol{w}_k,\boldsymbol{z}\rangle + b_k > \langle\boldsymbol{w}_i,\boldsymbol{z}\rangle + b_i\quad (\forall i \neq k)
$$
反过来说，如果类别 $k$ 是**不可预测的**（Unargmaxable），那么对于任意的输入表示 $\boldsymbol{z}\in\mathbb{R}^d$，必然存在某个 $i\neq k$，使得：
$$
\langle\boldsymbol{w}_k,\boldsymbol{z}\rangle + b_k \leq \langle\boldsymbol{w}_i,\boldsymbol{z}\rangle + b_i
$$

## 出现条件与特性

1. **类别数与维度的关系**：这种情况一般只出现在类别数远远超过编码向量维度的场景（即 Low-Rank 场景）。但在实际由于“维度灾难”，即便是几万的词表和几百维的向量空间，也算不上“远远大于”，因此在真实语言模型中实际出现的概率很小。
2. **向量模长差异**：如果所有的 $\boldsymbol{w}_i$ 互不相同但是模长都相等，那么是绝对不会出现“无法预测的词”，因此这种不可预测的情况只出现在 $\boldsymbol{w}_i$ 模长差异较大的情况。
3. **Normalization 的影响**：在当前主流的深度模型中，由于各种 Normalization 技术的应用，$\boldsymbol{w}_i$ 模长差异较大的情况很少出现了，这进一步降低了“无法预测的词”的出现概率。
4. **解码方式的局限**：本文的“无法预测的词”指的是最大化预测，也就是 Greedy Search，如果用 Beam Search 或者随机采样，那么即便存在“无法预测的词”，也依然是可能生成出来的。

## 判别方法

要判断一个给定的分类模型中某个类别 $n$ 是否可预测，可以将其转化为求解一个不等式优化问题。记 $\Delta\boldsymbol{w}_i = \boldsymbol{w}_n - \boldsymbol{w}_i, \Delta b_i = b_n - b_i$，为了避免发散，引入有界约束 $\|\boldsymbol{z}\|\leq r$：
$$
\max_{\|\boldsymbol{z}\|\leq r} \min_i \langle\Delta\boldsymbol{w}_i,\boldsymbol{z}\rangle + \Delta b_i
$$
引入单纯形 $\mathbb{P}^{n-1}$，根据冯·诺依曼的 Minimax 定理，可以交换 $\max$ 和 $\min$ 的顺序，当 $r$ 足够大时，等价于没有偏置项的情形：
$$
\min_{\alpha\in\mathbb{P}^{n-1}} \left\|\sum_i \alpha_i \Delta\boldsymbol{w}_i\right\|
$$
只要最大化的最终结果是正的，那么类别 $n$ 就是可预测的，否则就是不可预测的。最后的 $\min$ 的求解过程跟多任务学习中寻找“帕累托最优”的过程几乎一致，主要可以用到 Frank-Wolfe 算法。

## 示例

在无偏置项且 $k=n$ 的情况下，条件退化为 $\langle \boldsymbol{w}_i - \boldsymbol{w}_n, \boldsymbol{z}\rangle \geq 0$。当向量数大于空间维度且向量均匀分布在空间中时，这就有可能出现。例如在二维平面上构造 5 个向量的例子：
$$
\left\{\begin{aligned}
&\boldsymbol{w}_5 = (1, 1)\\
&\boldsymbol{w}_1 = (1, 1) + (0, 1) = (1, 2)\\
&\boldsymbol{w}_2 = (1, 1) + (1, 0) = (2, 1)\\
&\boldsymbol{w}_3 = (1, 1) + (0, -1) = (1, 0)\\
&\boldsymbol{w}_4 = (1, 1) + (-1, 0) = (0, 1)\\
\end{aligned}\right.
$$
在这个例子中，类别 5 无论代入怎样的 $\boldsymbol{z}$ 都无法成为概率最大的那个，因此类别 5 就是不可预测的。
