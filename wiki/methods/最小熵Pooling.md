---
type: method
title: 最小熵Pooling
aliases:
  - Minimum Entropy Pooling
operation_types:
  primary: Estimate / sample instead of compute
  secondary:
    - Rewrite / identity transform
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
source_ids:
  - 9617
  - 9632
method_summary: 在NBCE进行上下文概率聚合时，通过选择各个短上下文独立预测的条件概率分布中信息熵最小（即确定性最高）的那个分布作为最终的投票聚合分布，以确保大模型在随机采样生成时的逻辑可读性。
typical_structure: |
  1. 利用同一batch并行计算各上下文在当前生成步骤的条件概率分布 $p(T|S_i)$
  2. 对每个上下文的条件分布计算其信息熵：$H_i = -\sum_T p(T|S_i) \log p(T|S_i)$
  3. 找出对应最小信息熵的上下文索引 $k = \mathop{\text{argmin}} H_i$
  4. 直接使用 $\log p(T|S_k)$ 替换传统的平均 Pooling 作为 NBCE 的 $\log p(T|S_1, \dots, S_n)$ 聚合项
applicability: 在执行基于朴素贝叶斯的上下文扩展（NBCE）或需要对多个平权上下文的预测分布进行鲁棒且具备极佳采样可读性的选择性聚合时。
tools:
  - 信息熵
  - 选择性 Pooling
related_methods:
  - [[无交跳转加权]]
  - [[NBCE朴素贝叶斯上下文扩展]]
examples:
  - [[article::9617]]
  - [[article::9632]]
status: draft
updated: 2026-06-14
---

## 适用问题

NBCE 将长上下文切分为多个短段落，在解码时并行计算每个段落条件下的预测分布。朴素贝叶斯假设这些上下文相互独立，因此需要一种聚合策略将多个分布合并为最终预测。标准平均 Pooling 在上下文数量增多时会导致尾部噪声放大，生成结果逐渐变为乱码。最小熵 Pooling 通过选择确定性最高的分布来保证生成质量。

## 核心变换

**输入**：各上下文的条件概率分布 $\{p(T|S_1), \dots, p(T|S_n)\}$
**输出**：经选择性聚合的最终分布 $p(T|S_1, \dots, S_n)$

标准平均 Pooling（易受噪声干扰）：
$$
\log p(T|S_1, \dots, S_n) = \frac{1}{n}\sum_{i=1}^n \log p(T|S_i)
$$

最小熵 Pooling（选择最确定的分布）：
$$
H_i = -\sum_T p(T|S_i) \log p(T|S_i), \quad k = \mathop{\text{argmin}}_i H_i
$$
$$
\log p(T|S_1, \dots, S_n) \approx \log p(T|S_k)
$$

## 典型步骤

1. **并行计算**：将各上下文与当前生成 tokens 组合，在同一 batch 中并行计算条件概率分布
2. **计算信息熵**：对每个上下文的条件分布计算熵 $H_i$
3. **选择最小熵**：找出熵最小的上下文索引 $k$
4. **使用其分布**：直接以 $\log p(T|S_k)$ 作为最终聚合分布

## 直觉

核心思想：**当多个专家意见不一致时，相信最自信的那个**。

语言模型的训练目标是 one-hot 分布（交叉熵），因此模型对正确的下一个 token 通常给出很高的置信度。当上下文 $S_i$ 与当前生成内容相关时，$p(T|S_i)$ 在正确的 token 上集中了大部分概率质量，熵较低。反之，如果 $S_i$ 与当前内容无关，$p(T|S_i)$ 会较为分散，熵较高。

平均 Pooling 乍看合理，但问题在于语言模型分布的尾部（低概率词）是不可靠的——这些低概率 token 的 $\log p$ 值噪音大，在平均操作中会被放大，导致采样出乱码。选择最小熵分布相当于"跟随最懂当前上下文的专家"，实际上等价于一种隐式的每步检索：模型通过熵来判断哪个上下文与当前生成最相关。

## 边界

- 最小熵 Pooling 假设至少有一个上下文与当前生成内容强相关；若所有上下文都不相关，所有分布的熵都很高，选择任意一个都可能出错
- 在生成长文本时，不同步骤所选上下文可能频繁切换，导致语义跳转——配合[[无交跳转加权]]使用
- 建议在计算熵之前做 Top-P 或 Top-K 截断，去除不可靠的尾部概率
- $\log p(T) = -\infty$ 处的未定义运算需特殊处理（直接取 Pooling 分布）

## 例子

- NBCE 在 7B 模型上实现 12 段上下文、总长超 1 万字的长文本阅读理解，最小熵 Pooling 保证了生成的可读性
- 与平均 Pooling 对比：平均 Pooling 在上下文数增多时逐步退化到乱码，最小熵 Pooling 始终保持高质量

## 证据

- ev::9617::最小熵 Pooling 公式：$k = \mathop{\text{argmin}} H_i$，使用 $\log p(T|S_k)$ 作为聚合
- ev::9632::平均 Pooling 失效原因分析：尾部预测不可靠，$-\log p(T)$ 中的负项在平均后放大不可信尾部词
- ev::9632::Top-P/Top-K 截断配合：在计算熵之前截断尾部噪声
