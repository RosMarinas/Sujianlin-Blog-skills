---
title: Numpy Apriori算法
type: method
aliases: [Numpy Apriori, 关联规则挖掘]
tags: [data-mining, apriori, numpy, association-rules]
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: ["Estimate / sample instead of compute"]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-10-用Numpy实现高效的Apriori算法.md
source_ids: ["5525"]
status: draft
updated: 2026-06-13
method_summary: "使用纯Numpy实现的高效Apriori关联规则挖掘算法，通过0-1矩阵列连乘快速计算项集支持度。"
typical_structure: "构建物品0-1矩阵；字典序排序的频繁项组合；矩阵连乘计算支持度；遍历所有排列计算置信度。"
applicability: "中小规模数据的关联规则挖掘，购物篮分析等场景。"
examples: "购物篮数据（啤酒与尿布）关联规则挖掘"
belongs_to: [数据挖掘算法]
layering: [数据分析, 关联规则]
formula_standard_notation: false
related_concepts: [Apriori算法]
---

## 适用问题

中小规模数据的关联规则挖掘（购物篮分析），即从事务数据中发现物品之间的频繁共现模式（关联规则）。经典的"啤酒与尿布"场景。

## 核心变换

**输入**：事务数据（每行记录为逗号分隔的物品列表）
**输出**：满足最小支持度和置信度的关联规则（前件→后件）

使用物品-事务0-1矩阵$D \in \{0,1\}^{N \times M}$（$N$为事务数，$M$为物品种类数），通过矩阵列连乘快速计算项集支持度：
$$
\text{support}(I) = \frac{\sum_{i=1}^N \prod_{j \in I} D_{ij}}{N}
$$
其中$I$为物品集合，$D_{ij}=1$表示事务$i$包含物品$j$。

## 典型步骤

1. **扫描数据**：统计各物品出现频次，过滤支持度低于`min_support`的物品，构建物品到ID的映射
2. **构建0-1矩阵**：将事务数据转换为$N \times M$的布尔矩阵$D$
3. **生成频繁1项集**：支持度超过阈值的单个物品
4. **迭代生成$k+1$项集**：
   - 对$k$频繁项按字典序排序
   - 前$k-1$个相同的项进行两两组合生成候选$k+1$项集
   - 用矩阵列连乘`prod(D[:, item_ids], axis=1)`计算支持度
   - 保留超出阈值的项集
5. **生成关联规则**：遍历所有频繁项集的所有排列，计算置信度$\text{conf}(X\to Y) = \frac{\text{support}(X\cup Y)}{\text{support}(X)}$
6. **输出**：返回置信度超过阈值的规则

## 直觉

Apriori算法的核心是利用"频繁项集的所有非空子集也一定是频繁的"这一反单调性质来剪枝。Numpy实现的加速关键：用0-1矩阵的列连乘（`np.prod`）一次性计算所有候选$k+1$项集的支持度，替代逐项扫描的循环，充分利用了Numpy的向量化计算能力。

## 边界

- 适合中小规模数据（物品数数千以内），随物品数增加候选集呈指数增长
- 依赖支持度阈值过滤，阈值过低导致候选项集爆炸
- 目前实现不支持变长数据（所有事务需统一为物品ID数组）
- 关联规则挖掘的是相关性而非因果性，需谨慎解读发现的规则
- 稀疏矩阵场景下性能不如专门的频繁模式挖掘算法（如FP-Growth）

## 例子

- 购物篮数据："啤酒,尿布,牛奶"等事务，发现"啤酒→尿布"的关联规则
- 最小支持度0.1，最小置信度0.5的参数设置：`Apriori(0.1, 0.5)`
- 矩阵列连乘计算示例：对候选物品集{2,5,7}，`sum(np.prod(D[:, [2,5,7]], 1)) / N`即为支持度

## 证据

- ev::5525::0-1矩阵列连乘支持度计算：`sum(np.prod(self.D[:, _id], 1)) / self.total`
- ev::5525::字典序排序+两两组合生成候选$k+1$项集：频繁项集的Apriori生成策略
- ev::5525::支持度和置信度定义：频繁项集过滤和关联规则输出的完整流程
