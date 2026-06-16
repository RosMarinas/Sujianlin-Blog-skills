---
type: concept
title: Sparse Softmax
aliases:
- 稀疏Softmax
- Sparsemax
definition: 只保留top-k个logits进行softmax归一化，其余位置概率置零的近似技巧。
standard_notation: $p_i = \begin{cases} \frac{e^{s_i}}{\sum_{j\in\Omega_k} e^{s_j}}
  & i\in\Omega_k \\ 0 & i\notin\Omega_k \end{cases}$
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-01-01-SPACES-抽取-生成-式长文本摘要-法研杯总结.md
source_ids:
- '8046'
related_methods:
- - - method::Sparse Softmax
status: draft
updated: '2026-06-12'
---

# Sparse Softmax

Sparse Softmax（稀疏Softmax）是一种通过将Softmax稀疏化来避免模型过度学习、防止过拟合的近似技巧。它的核心思想是在计算概率和交叉熵时，只保留logits最大的前$k$个元素，后面的直接置零。

## 核心数学定义

设 $\Omega_k$ 是将输入 logits $s_1, s_2, \dots, s_n$ 从大到小排列后前 $k$ 个元素的下标集合。稀疏版Softmax概率计算公式为：

$$p_i=\left\{\begin{aligned}&\frac{e^{s_i}}{\sum\limits_{j\in\Omega_k} e^{s_j}},\,i\in\Omega_k\\ &\quad 0,\,i\not\in\Omega_k\end{aligned}\right.$$

相应的，计算目标类别 $t$ 的交叉熵时，将原来对全体类别的 $\text{logsumexp}$ 操作，改为只对最大的 $k$ 个类别进行：

$$\text{Loss} = \log\left(\sum\limits_{i\in\Omega_k} e^{s_i}\right) - s_t$$

## 理论基础与过度学习问题

常规的Softmax交叉熵容易造成过度学习。假设模型已经成功分类，目标类别的分数最大（$s_{\max}=s_t$），此时原始交叉熵满足以下不等式：

$$
\begin{aligned}
\log\left(\sum\limits_{i=1}^n e^{s_i}\right)-s_{\max} &= \log\left(1+\sum\limits_{i\neq t} e^{s_i-s_{\max}}\right)\\
&\geq \log\left(1+(n-1) e^{s_{\min}-s_{\max}}\right)
\end{aligned}
$$

假设当前交叉熵值为 $\varepsilon$，解得：

$$s_{\max} - s_{\min}\geq \log (n-1) - \log \left(e^{\varepsilon} - 1\right)$$

以 $\varepsilon=\ln 2 \approx 0.69$ 为例，此时 $\log \left(e^{\varepsilon} - 1\right)=0$，即 $s_{\max} - s_{\min}\geq \log (n-1)$。这意味着为了让loss降到0.69，最大的logit和最小的logit之差就必须大于 $\log (n-1)$。当类别数 $n$ 较大时，对于分类问题来说这是一个没有必要的过大的间隔，常规的交叉熵容易造成过度学习而导致过拟合。而截断之后就不会有这个问题。

## 关键属性与适用条件

*   **适用场景（预训练Finetune）**：Sparse Softmax 只适用于有预训练的场景，因为预训练模型已经训练得很充分了，因此finetune阶段要防止过拟合。
*   **反面边界情况（从零训练）**：如果你是从零训练一个模型，那么 Sparse Softmax 会造成性能下降，因为每次只有 $k$ 个类别被学习到，反而会存在学习不充分的情况（欠拟合）。
*   **超参数设置与效果实例**：$k$ 是人为选择的超参数。在法研杯比赛（SPACES模型）中选取了 $k=10$。在大多数 NLP 和 CV 任务中，该技巧能带来约 1%~2% 的性能提升。

## 与其他概念的关系

该思想源于《From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification》及《Sparse Sequence-to-Sequence Models》等文章中提出的将Softmax稀疏化来增强其解释性乃至提升效果的做法。当前的 Sparse Softmax 是剥离了复杂设计后的极简版本，既能实现稀疏化约束，又降低了计算与实现的复杂性。
