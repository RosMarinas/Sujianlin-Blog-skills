---
type: example
title: Taylor-SoftMax构造
article_id: "7919"
article: "article::exp(x)在x=0处的偶次泰勒展开式总是正的"
section: 应用场景
claim: 利用 $e^x$ 偶次泰勒展开正定性，构造多项式归一化函数作为Softmax的替代。
notation_mapping:
  - "$f_n(x) = \sum_{k=0}^n x^k/k!$": e^x的n阶泰勒多项式
  - "$\text{taylor-softmax}(\boldsymbol{x}, n)_i$": 基于泰勒多项式的归一化输出
steps:
  - "从 $e^x$ 的偶次泰勒展开恒正性质 $f_n(x) > 0$（$n$为偶数）出发"
  - "构造替代归一化函数 $\text{taylor-softmax}(\boldsymbol{x}, n)_i = f_n(x_i) / \sum_k f_n(x_k)$"
  - "多项式函数增长较缓，可缓解softmax置信度过高导致的过拟合"
  - "若需要单调性，对 $f_n$ 在极小值点左侧进行截断修正"
used_concepts:
  - "concept::正定泰勒多项式"
used_formulas:
  - "formula::Taylor-SoftMax公式"
used_methods: []
problem_pattern: "problem_pattern::非光滑函数可导化"
source_span: ev::7919::应用场景
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-24-exp-x-在x-0处的偶次泰勒展开式总是正的.md
source_ids:
  - "7919"
status: draft
updated: 2026-06-12
---

## 示例说明

本示例展示了如何利用数学恒正性质设计新的归一化函数。关键洞察在于用多项式替代指数，避免输出概率过度极化。具体构造基于 $e^x$ 的偶次泰勒展开 $f_n(x)=\sum_{k=0}^n x^k/k!$ 恒大于零的性质，定义 $\text{taylor-softmax}(\boldsymbol{x}, n)_i = f_n(x_i)/\sum_k f_n(x_k)$。由于多项式增长比指数慢，Taylor-Softmax 可以缓解标准 Softmax 常见的置信度过高（概率值塌陷为0或1）问题。必要时可在唯一极小值点处截断以恢复单调性。
