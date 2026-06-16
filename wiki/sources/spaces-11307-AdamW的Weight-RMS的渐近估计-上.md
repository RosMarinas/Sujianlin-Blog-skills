---
type: article_summary
title: AdamW的Weight RMS的渐近估计（上）
article_id: "11307"
source_url: https://spaces.ac.cn/archives/11307
date: 2025-10-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-10-01-AdamW的Weight-RMS的渐近估计-上.md
series: []
topics:
  - "[[优化器分析]]"
concepts:
  - "[[优化动力学视角]]"
  - "[[平均场近似]]"
  - "[[SGD-SDE近似]]"
  - "[[RMS尺度]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
  - "[[用变分法反推学习率]]"
  - "[[通过恒等式重写优化轨迹]]"
problem_patterns: []
evidence_spans:
  - ev::11307::EMA视角
  - ev::11307::快速估计
  - ev::11307::平均场推导
  - ev::11307::结果分析
  - ev::11307::符号版本
  - ev::11307::TUC概念
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-10-01-AdamW的Weight-RMS的渐近估计-上.md
source_ids:
  - "11307"
status: draft
updated: 2026-06-10
---

# AdamW的Weight RMS的渐近估计（上）

## 文章核心问题

AdamW训练出来的模型，其权重的RMS是否可以在训练前就估计出来？本文用平均场近似方法推导AdamW的Weight RMS渐近表达式。

## 主要结论

- AdamW的Weight RMS在常学习率和常Weight Decay下可渐近估计：$\|\theta_t\|_{RMS} \approx \sqrt{\eta / (2\lambda)}$。
- 更多一般情况（含动量项、非零均值梯度）下给出更完整的表达式。
- SignSGDMW的Weight RMS是AdamW的 $\sqrt{(1+\beta_1)/(1-\beta_1)}$ 倍。
- 从EMA视角重新理解Weight Decay：$\theta_t = \beta_3\theta_{t-1} + (1-\beta_3)(-u_t/\lambda)$。
- 与《Rotational Equilibrium》论文结论一致，但推导更通用。

## 推导结构

1. 回顾AdamW更新规则，引入EMA视角理解Weight Decay。
2. 初步快速估计：假设 $\theta_{t-1}$ 与 $u_t$ 正交，得到 $\|\theta\|_{RMS} \propto \sqrt{\eta/\lambda}$。
3. 平均场近似完整推导：将权重展开为加权和，分五步计算期望。
4. 分析 $\mu=0$ 特例和 $\lambda\to0$ 极限。
5. 推广到SignSGDMW（符号动量+Weight Decay）。
6. 讨论原论文的TUC概念，解释其隐含的平均场假设。

## 关键公式

- EMA视角: $\theta_t = \beta_3\theta_{t-1} + (1-\beta_3)(-u_t/\lambda)$, $\beta_3 = 1-\eta\lambda$
- 快速估计: $\|\theta_t\|_{RMS} \approx \sqrt{\frac{1-\beta_1}{1+\beta_1} \frac{\eta}{2\lambda}}$
- 平均场结果($\mu=0$): $\|\theta_t\|_{RMS}^2 \approx \beta_3^{2t}\|\theta_0\|_{RMS}^2 + (1-\beta_3^{2t}) \eta/2\lambda$
- 稳态: $\|\theta\|_{RMS} \approx \sqrt{\eta / (2\lambda)}$
- SignSGDMW稳态: $\|\theta\|_{RMS} \approx \sqrt{\frac{\eta}{2\lambda} \frac{1+\beta_1}{1-\beta_1}}$
- 无Weight Decay: $\|\theta_t\|_{RMS}^2 \approx \|\theta_0\|_{RMS}^2 + \eta^2 t$

## 体现的方法

- **用平均场近似替代复杂期望计算**：将复杂的随机更新期望用一阶矩和二阶矩近似，推导Weight RMS渐近结果。
- **EMA视角转化**：将Weight Decay项重新解释为EMA更新，获得更直观的理解。
- **正交假设简化**：假设高维权重向量与更新向量近似正交，简化模长分析。

## 所属系列位置

独立文章，与"重新思考学习率与Batch Size"系列方法相通。是两篇中的上篇。

## 与其他文章的关系

- 前提是文章 为什么Adam的Update RMS是0.2%(11267) 中关于Update RMS的计算。
- 下篇(11404) 推广到动态学习率和动态Weight Decay。
- 与论文《Rotational Equilibrium》(2305.17212) 结论一致。
- 与MuP之上的参数稳定性约束(11729) 互补——前者约束参数范数，本文预测自然范数。

## 原文证据锚点

- ev::11307::EMA视角: 第37-41行，Weight Decay的EMA视角转化。
- ev::11307::快速估计: 第59-73行，基于正交假设的快速推导。
- ev::11307::平均场推导: 第80-146行，完整五步平均场推导。
- ev::11307::结果分析: 第148-166行，特例分析和解释。
- ev::11307::符号版本: 第193-218行，SignSGDMW的推广。
- ev::11307::TUC概念: 第221-239行，Total Update Contribution概念及其平均场解释。
