---

type: formula
title: SGD平均损失界
aliases: null
latex: \frac{1}{T}\sum_{t=1}^T L(x_t,\theta_t)-\frac{1}{T}\sum_{t=1}^T L(x_t,\theta^*)\le
  \frac{R^2}{2T\eta_T}+\frac{G^2}{2T}\sum_{t=1}^T\eta_t
symbol_meanings:
  G: 梯度范数上界或二阶矩平方根
  T: 总训练步数
  eta_t: 第 t 步学习率
  theta_star: 比较用最优参数
  theta_t: 第 t 步参数
standard_notation:
  theta_t: 第 t 步参数
  theta_star: 比较用最优参数
  eta_t: 第 t 步学习率
  G: 梯度范数上界或二阶矩平方根
  T: 总训练步数
conditions: 凸损失、有界凸域、梯度有界、学习率非增。
derived_from: null
implies: null
appears_in:
- '[[让炼丹更科学一些（一）：SGD的平均损失收敛]]'
evidence_spans:
- ev::9902::结论初探
- ev::9902::假设分析
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md
source_ids:
- '9902'
- '11469'
- '11480'
- '11494'
- '11530'
- '11540'
status: draft
updated: "2026-06-14"
---

# SGD平均损失界


## 概述

（待补充）

## 公式本体

```tex
\frac{1}{T}\sum_{t=1}^T L(x_t,\theta_t)-\frac{1}{T}\sum_{t=1}^T L(x_t,\theta^*)\le \frac{R^2}{2T\eta_T}+\frac{G^2}{2T}\sum_{t=1}^T\eta_t
```

## 成立条件

凸损失、有界凸域、梯度有界、学习率非增。

## 推导来源

- `ev::9902::结论初探`
- `ev::9902::假设分析`