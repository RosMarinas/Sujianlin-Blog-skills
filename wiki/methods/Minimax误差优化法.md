---
type: method
title: Minimax误差优化法
aliases:
  - Minimax error optimization
  - Chebyshev approximation
operation_types:
  primary: Estimate / sample instead of compute
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
source_ids:
  - "7309"
  - "8833"
method_summary: 通过数值优化求解参数以最小化目标函数与近似函数在整个定义域上的最大绝对误差。
typical_structure: |
  1. 选定参数化近似函数 $g(x,\theta)$ 的形式。
  2. 定义优化目标 $\min_\theta \max_x |f(x) - g(x,\theta)|$。
  3. 在定义域上密集采样，以离散近似替代连续 $\max$。
  4. 使用无梯度优化方法（如Powell）求解。
  5. 验证最优参数下的最大误差是否可接受。
applicability: 适用于需要保证整个定义域上最坏情况误差最小化的函数逼近问题。避免了对权重函数的主观选择，结果对异常值鲁棒。
tools:
  - scipy.optimize.minimize（Powell方法）
  - 密集网格采样
  - 误差函数的数值计算
examples:
  - "example::GELU双曲正切近似系数推导"
  - "example::SquarePlus最佳参数逼近SoftPlus"
problem_patterns:
  - "problem_pattern::用简单运算替代复杂计算"
evidence_spans: []
status: draft
updated: 2026-06-12
---

## 适用问题

需要在整个定义域上保证最坏情况误差最小化的函数逼近问题。特别适用于激活函数近似（如GELU的初等函数近似、SoftPlus的简单运算近似），以及用简单运算替代复杂计算的场景。

## 核心变换

**输入**：目标函数$f(x)$ + 参数化近似函数$g(x,\theta)$
**输出**：最优参数$\theta^*$使最大绝对误差最小化

$$
\theta^* = \arg\min_\theta \max_{x \in \mathcal{D}} |f(x) - g(x,\theta)|
$$

与常用L2损失不同，Minimax不涉及权重函数，把定义域上的最坏情况误差作为优化目标。

## 典型步骤

1. **选定参数化近似函数形式**：确定$g(x,\theta)$的结构（如GELU的双曲正切近似$0.5x(1+\tanh(\sqrt{2/\pi}(x+0.044715x^3)))$）
2. **定义Minimax目标**：$\min_\theta \max_x |f(x) - g(x,\theta)|$
3. **离散化定义域**：在函数定义域上密集采样，用离散最大值$\max_i |f(x_i) - g(x_i,\theta)|$替代连续$\max$
4. **数值优化**：使用Powell等无梯度优化方法求解（`scipy.optimize.minimize`，method='Powell'）
5. **验证**：在独立测试点上检验最优参数下的最大误差是否可接受

## 直觉

Minimax优化保证的是"最坏情况下的质量"，而非"平均质量"。在函数逼近中，L2损失可能让误差在某些区域很大但在其他区域很小，Minimax则强制所有点的误差都在同一水平。这特别适合激活函数等需要整个定义域上精度一致的场景。

一个关键洞察是：Minimax优化的结果通常不依赖于损失权重函数的选择，因为最佳逼近条件由误差函数$e(x) = f(x) - g(x,\theta)$在极值点处满足$e(x)$以交替正负号达到最大绝对值的等波纹条件决定（Chebyshev逼近定理）。

## 边界

- 需要对定义域密集采样来近似连续$\max$，采样密度影响精度
- 参数空间较小时效果最好；高维参数空间数值优化可能困难
- 无梯度方法（Powell）相比梯度方法收敛较慢，适合参数不多的场景
- 不能直接给出梯度信息，难以嵌入端到端训练
- 结果是最坏情况最优，但平均误差可能不如L2损失

## 例子

- GELU双曲正切近似系数确定：通过Minimax优化得到$\tanh$展开中的系数0.044715
- SquarePlus($\frac{x+\sqrt{x^2+4}}{2}$)的最佳参数逼近SoftPlus：找到使最大误差最小的参数
- 与Erf逼近的误差比较：Minimax优化的近似在整个定义域上最大误差小于L2优化的结果

## 证据

- ev::7309::GELU双曲正切近似的Minimax优化：确定系数0.044715使最大逼近误差最小
- ev::8833::SquarePlus参数Minimax优化：通过数值方法找到逼近SoftPlus的最优参数
- scipy.optimize.minimize（Powell方法）可用于求解Minimax优化问题的离散近似
