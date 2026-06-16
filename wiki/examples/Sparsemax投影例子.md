---
type: example
title: Sparsemax投影例子
aliases: '[]'
article_id: '10289'
article: '[[spaces-10289-通向最优分布之路]]'
section: 一个例子
claim: Sparsemax是欧氏空间到概率单纯形的投影操作
notation_mapping:
  x: 输入向量
  p: 输出概率分布
  lambda: 阈值
steps: '["1. 定义F(p)=||p-x||^2", "2. 梯度nabla F(p)=2(p-x)", "3. 极小值条件p·(p-x)=(p-x)_{min}",
  "4. 解出p_i=relu(x_i-lambda(x))", "5. lambda由sum p_i=1确定"]'
used_concepts: '[["概率空间"]]'
used_methods: '[["凸集搜索法"]]'
problem_pattern: '[[概率空间中的优化问题]]'
source_span: ev::10289::一个例子
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
source_ids:
- '['
- '"'
- '1'
- '0'
- '2'
- '8'
- '9'
- '"'
- ']'
evidence_spans: '[]'
status: draft
updated: '2026-06-12'
---

## 演示内容

以Sparsemax为例，它的原始定义为寻找一个概率分布$\boldsymbol{p}\in\Delta^{n-1}$，使得其与输入向量$\boldsymbol{x}\in\mathbb{R}^n$的欧氏距离最小：
$$
\text{Sparsemax}(\boldsymbol{x}) = \mathop{\text{argmin}}\limits_{\boldsymbol{p}\in\Delta^{n-1}}\Vert \boldsymbol{p} - \boldsymbol{x}\Vert^2
$$
从投影梯度下降的角度来看，Sparsemax正好是从欧氏空间$\mathbb{R}^n$到概率单纯形$\Delta^{n-1}$的“投影”操作。

## 步骤

1. **定义目标泛函**：我们记要极小化的目标函数为 $F(\boldsymbol{p})=\Vert \boldsymbol{p} - \boldsymbol{x}\Vert^2$。

2. **计算梯度**：函数 $F(\boldsymbol{p})$ 对 $\boldsymbol{p}$ 的梯度为 $\nabla_{\boldsymbol{p}} F(\boldsymbol{p}) = 2(\boldsymbol{p} - \boldsymbol{x})$。

3. **利用极小值条件**：根据概率空间中极小值点满足的方程 $\boldsymbol{p}\cdot\nabla_{\boldsymbol{p}} F(\boldsymbol{p}) = (\nabla_{\boldsymbol{p}} F(\boldsymbol{p}))_{\min}$，极小值点必须满足的条件为：
   $$
   \boldsymbol{p}\cdot(\boldsymbol{p}-\boldsymbol{x}) = (\boldsymbol{p}-\boldsymbol{x})_{\min}
   $$

4. **推导各分量的解**：约定 $x_i = x_j\Leftrightarrow p_i = p_j$。在该约定下，当且仅当 $p_i > 0$ 时，有 $p_i-x_i = (\boldsymbol{p}-\boldsymbol{x})_{\min}$。因为 $\boldsymbol{p}$ 可以由 $\boldsymbol{x}$ 确定，设 $(\boldsymbol{p}-\boldsymbol{x})_{\min} = -\lambda(\boldsymbol{x})$，则此时 $p_i = x_i - \lambda(\boldsymbol{x})$。而对于 $p_i=0$ 的情况，有 $p_i-x_i > (\boldsymbol{p}-\boldsymbol{x})_{\min}$，即 $x_i - \lambda(\boldsymbol{x}) < 0$。综合这两点，输出概率 $\boldsymbol{p}$ 的第 $i$ 个分量可以统一表示为：
   $$
   p_i = \text{relu}(x_i - \lambda(\boldsymbol{x}))
   $$

5. **确定阈值 $\lambda$**：$\lambda(\boldsymbol{x})$ 是一个关于 $\boldsymbol{x}$ 的函数，它由概率单纯形的约束条件（即 $\boldsymbol{p}$ 的各分量之和为 $1$，$\sum_i p_i = 1$）来唯一确定。
