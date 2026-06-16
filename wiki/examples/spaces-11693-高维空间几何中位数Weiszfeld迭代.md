---
type: example
title: 高维空间几何中位数Weiszfeld迭代
article_id: 11693
article: '[[spaces-11693-中位数-Median-简介]]'
section: 高维空间
claim: 计算高维向量集的几何中位数点，对距离之和求偏导并构建不动点更新
notation_mapping:
  standard_mu: \boldsymbol{\mu}
  source_mu: \boldsymbol{\mu}
steps:
- 1. 列出距离和损失函数 f(mu) = sum_i ||x_i - mu||_2
- 2. 求其关于mu的梯度 ∇f(mu) = sum_i (mu - x_i)/||x_i - mu||_2 = 0
- 3. 移项整理得到 mu = sum_i (x_i / ||x_i - mu||_2) / sum_i (1 / ||x_i - mu||_2)
- 4. 构造不动点迭代公式，每一步代入上一步的估计值进行重新加权更新
used_concepts:
- - - 几何中位数
used_formulas:
- - - 几何中位数定义
- - - Weiszfeld迭代公式
used_methods:
- - - Weiszfeld迭代法
source_span: ev::11693::高维空间
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-03-31-中位数-Median-简介.md
source_ids:
- 11693
status: draft
updated: '2026-06-12'
---

# 高维空间几何中位数Weiszfeld迭代

此实例给出了高维鲁棒几何中位数中心计算的不动点迭代细节。

在优化视角下，高维空间中一批向量 $\boldsymbol{x}_1, \boldsymbol{x}_2, \cdots, \boldsymbol{x}_n$ 的几何中位数（Geometric Median）定义为使得所有点到该中心的欧氏距离之和最小的向量 $\boldsymbol{\mu}$，即目标函数为：
$$
\mathop{\text{median}}(\boldsymbol{x}_1,\boldsymbol{x}_2,\cdots,\boldsymbol{x}_n) = \mathop{\text{argmin}}_{\boldsymbol{\mu}} \sum_{i=1}^n \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2
$$
当 $n=3$ 时，目标函数的最优解即为经典的费马点（Fermat point）。

由于该优化问题无法求得解析解，通常采用不动点迭代法（Weiszfeld迭代）进行数值计算。对于更一般形式的目标函数 $f(\boldsymbol{\mu}) = \sum_{i=1}^n \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2^{\alpha}$，令其关于 $\boldsymbol{\mu}$ 的梯度 $\nabla_{\boldsymbol{\mu}} f(\boldsymbol{\mu}) = \boldsymbol{0}$，经过移项整理可以得到 $\boldsymbol{\mu}$ 的隐式表达式。

代入 $\alpha=1$ 对应几何中位数的情形，需要求解的方程等价于：
$$
\boldsymbol{\mu} = \frac{\sum_{i=1}^n \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2^{- 1}\boldsymbol{x}_i}{\sum_{i=1}^n\Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2^{- 1}}
$$
由此构造出 Weiszfeld 迭代公式。在第 $t+1$ 步时，将上一步的中心估计值 $\boldsymbol{\mu}_t$ 代入等式右端以进行重新加权更新，具体计算公式为：
$$
\boldsymbol{\mu}_{t+1} = \frac{\sum_{i=1}^n \boldsymbol{x}_i / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2}{\sum_{i=1}^n 1 / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2}
$$
该迭代过程利用各数据点与当前中心估计值的距离倒数作为权重，不断更新中位向量估计值。相比于均值模型中距离平方放大的误差，由于几何中位数的目标函数采用 $L_2$ 范数本身，距离误差不会被指数级放大，从而使得最终收敛的中心点能够更强地抵御异常值的干扰。
