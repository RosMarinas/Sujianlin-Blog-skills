---
type: concept
title: Surge现象
aliases: null
definition: 某些优化器和 Hessian 结构下，Batch Size 增大后最优学习率先增后降的反常尺度行为。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md
source_ids:
- '11280'
- '11301'
related_formulas:
- '[[二阶近似最优学习率公式]]'
related_methods:
- '[[用平均场近似替代复杂期望计算]]'
series:
- '[[重新思考学习率与Batch Size]]'
evidence_spans:
- ev::11280::反常现象
- ev::11301::一般分析
status: draft
updated: '2026-06-12'
---

# Surge现象

## 定义

“Surge现象”指当Batch Size超过某个阈值后，最优学习率随着Batch Size的增大而减少的反常尺度行为。在SignSGD的平均场分析中，当 $\sum_{i\neq j} H_{i,j}\mathop{\text{sign}}(g_i g_j) > 0$ 时，根据基本不等式可以得出关于标准化的Batch Size $\beta$ 的分母存在一个最小值点：
$$
\beta^* = \sqrt{\frac{\sum_i H_{i,i}}{\sum_{i\neq j} H_{i,j}\mathop{\text{sign}}(g_i g_j)}}
$$
在附加条件 $\beta^*\in(0, 1)$ 成立时，最优学习率 $\eta^*$ 关于 $B$ 就不再是单调递增，而是先增后减。存在一个临界Batch Size，超过这个临界Batch Size后学习率反而应该降低。

## 产生原因与属性

- **优化器假设与真实Hessian的偏离**：为什么会出现Surge现象这种反常行为呢？事实上，这是优化器本身的假设与我们的分析方法不完全相容的体现。为了估计最优学习率，通常将Loss的增量展开到了二阶近似，并假设了Hessian矩阵的正定性。Surge现象实际体现了 $B\to\infty$ 时，SignSGD等优化器所假设的Hessian矩阵与实际Hessian矩阵的偏离程度在变大。
- **损失增量的单调性（反直觉现象）**：尽管学习率 $\eta^*$ 可能会出现Surge现象，但损失函数的平均增量 $\overline{\Delta\mathcal{L}}$ 并没有这个现象，它关于 $B$ 始终是单调递增的，并且还保持跟SGD相同的形式：$\overline{\Delta\mathcal{L}} \approx \frac{\Delta\mathcal{L}_{\max}}{1 + \mathcal{B}_{\text{noise}}/B}$。

## 与EMA、Adam和Muon的关系

动量（EMA机制）的引入会显著影响Surge现象的出现阈值：
- **加速Surge现象出现**：对于动量优化器，动量机制的引入约等于将 Batch Size 扩大到了 $\frac{1 + \beta_1}{1 - \beta_1} > 1$ 倍，这自然增加了超过阈值的可能性。因此，Adam的 $\beta_1$ 的增大，将会加速“Surge现象”的出现。
- **对角Hessian假设下的差异**：跟SignSGD不同的是，SignSGD如果假设Hessian矩阵是对角阵，那么就不会出现Surge现象。但 Adam 即便是在对角Hessian假设下依然出现Surge现象。
- **Adam的临界条件**：当 $\beta_1 > 1/3$ 且 $\beta > \beta^*$（即 $B > \frac{1-\beta_1}{3\beta_1-1}\mathcal{B}_{\text{simple}}$）时，学习率应该随着Batch Size的增加而减小。在常用设置（如 $\beta_1=0.9$）下，Adam 必然会出现Surge现象，意味着Batch Size超过一定值后学习效率下降。
- **与Muon对比**：Muon 的表现跟 SignSGDM 类似，在特定 Hessian 结构假设下它不会出现 Surge 现象，这意味着增大 Batch Size 总可以提高学习效率，这也是 Muon 能够支持更大 Batch Size 的原因。
