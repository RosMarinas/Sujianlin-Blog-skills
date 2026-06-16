---
type: formula
title: SoftMax作为onehot_argmax的光滑近似
aliases:
  - Softmax as smoothed onehot(argmax)
latex: \text{softmax}(\boldsymbol{x})_i = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}}
symbol_meanings:
  - "$x_i$": 输入向量的第 i 个分量
  - "$n$": 向量维度
standard_notation: "$\text{softmax}(\boldsymbol{x})_i$"
conditions: "任意实数向量 $\boldsymbol{x}$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
  - "6620"
derived_from: []
implies: []
appears_in:
  - "article::函数光滑化杂谈：不可导函数的可导逼近"
evidence_spans: []
status: draft
updated: 2026-06-12
---
## 概述

（待补充）



## 公式

$$
\text{onehot}(\text{argmax}(\boldsymbol{x})) \approx \left(\frac{e^{x_1}}{\sum_{i=1}^n e^{x_i}}, \dots, \frac{e^{x_n}}{\sum_{i=1}^n e^{x_i}}\right) \triangleq \text{softmax}(\boldsymbol{x})
$$

### Argmax光滑近似

$$
\text{argmax}(\boldsymbol{x}) \approx \sum_{i=1}^n i \times \text{softmax}(\boldsymbol{x})_i
$$

### 正确率光滑近似

$$
\text{正确率}\approx \frac{1}{|\mathcal{B}|}\sum_{\boldsymbol{x}\in\mathcal{B}} \langle \boldsymbol{1}_i(\boldsymbol{x}), p(\boldsymbol{x})\rangle
$$

### F1光滑近似（二分类）

$$
\text{正类F1}\approx\frac{2 \sum_{\boldsymbol{x}\in\mathcal{B}} t(\boldsymbol{x}) p(\boldsymbol{x})}{\sum_{\boldsymbol{x}\in\mathcal{B}} [t(\boldsymbol{x}) + p(\boldsymbol{x})]}
$$
