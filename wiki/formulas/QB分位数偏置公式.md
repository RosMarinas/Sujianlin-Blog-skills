---

type: formula
title: QB分位数偏置公式
aliases:
- Quantile Balancing bias formula
latex: \beta_j^* = \operatorname{quantile}(s_{:,j}, 1-k/n)
symbol_meanings:
  beta_j: 第 j 个 Expert 的偏置或阈值
  k: 每个 Token 的目标激活 Expert 数
  n: Expert 总数
  s: Router score matrix
standard_notation:
  s: Router score matrix
  beta_j: 第 j 个 Expert 的偏置或阈值
  k: 每个 Token 的目标激活 Expert 数
  n: Expert 总数
conditions: 动态激活版可一步求得；Top-k 版需要结合 `alpha` 做交替分位数更新。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
source_ids:
- '11619'
- '11626'
derived_from:
- '[[Quantile Balancing]]'
implies:
- '[[QB把负载均衡转化为分位数偏置]]'
- '[[动态QB一步分位数实现平均预算均衡]]'
appears_in:
- '[[MoE环游记：6. 最优分配促均衡]]'
- '[[MoE环游记：7. 动态激活极简解]]'
evidence_spans:
- ev::11619::交替迭代
- ev::11626::一步求解
status: draft
updated: "2026-06-14"
---

# QB分位数偏置公式


## 概述

（待补充）

## 公式

```tex
\beta_j^* = \operatorname{quantile}(s_{:,j}, 1-k/n)
```

## 解释与数学推导

在传统的基于 Top-k 的 Quantile Balancing (QB) 中，为了同时满足“每个 Token 恰好激活 $k$ 个 Expert” ($\sum_j x_{i,j} = k$) 和“每个 Expert 被激活 $mk/n$ 次” ($\sum_i x_{i,j} = mk/n$) 的双重约束，拉格朗日对偶问题中会同时引入 $\alpha_i$（处理 Token 行约束）和 $\beta_j$（处理 Expert 列约束），因此必须采用交替迭代的方式进行求解。

然而，如果在**动态激活**场景下放弃严格的每 Token 激活数量限制，仅保留全局的 Expert 负载均衡约束 $\sum_i x_{i,j} = mk/n$（即平均每个 Token 激活 $k$ 个 Expert），该问题可以极大简化。其等价的松弛目标函数通过分离变量 $\beta_j$，可将每个 Expert $j$ 的优化解耦为完全独立的子问题：

$$
\min_{\beta_j} \sum_{i,j} \max(0, s_{i,j} - \beta_j) + \frac{mk}{n} \sum_j \beta_j
$$

对于给定的 Expert $j$，若将其所有 $m$ 个 Token 的打分 $s_{i,j}$ 从大到小排列，可以从数学上推导出上述目标的最小值点出现在第 $mk/n$ 大与第 $mk/n+1$ 大的元素之间。为了确保激活逻辑严格成立，通常选取打分矩阵中 $s_{:,j}$ 列从大到小排列后的第 $mk/n+1$ 个元素。这一取值在数学上严格等价于计算该列分数的 $1-k/n$ 分位数（Quantile）。

通过这种方法，动态激活版 MoE 不再需要任何交替迭代（无需引入 $\alpha_i$）。只需对每列打分独立执行一步 `quantile` 计算即可得到最优偏置阈值 $\beta_j^*$。此后，只要 $s_{i,j} - \beta_j^* > 0$，对应的 Expert 即可被激活。这使得模型在保障绝对负载均衡的前提下，实现了极其优雅与高效的路由分配。
