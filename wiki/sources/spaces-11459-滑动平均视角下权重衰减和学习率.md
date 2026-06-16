---
type: article_summary
title: 滑动平均视角下的权重衰减和学习率
article_id: 11459
source_url: https://spaces.ac.cn/archives/11459
date: 2025-12-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-12-05-滑动平均视角下的权重衰减和学习率.md
concepts:
  - [[平均场近似]]
  - [[优化器记忆周期]]
propositions:
  - [[常数权重衰减下最优学习率解]]
  - [[比例权重衰减下最优学习率与权重衰减解]]
methods:
  - [[平均场优化器动力学分析法]]
  - [[最优学习率与权重衰减调度法]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-12-05-滑动平均视角下的权重衰减和学习率.md
source_ids:
  - 11459
status: draft
updated: 2026-06-11
---

# 滑动平均视角下的权重衰减和学习率

本文采用指数滑动平均（EMA）视角，推导并分析了预训练优化中权重衰减（Weight Decay）与学习率（Learning Rate）调度的联合动态关系。

## 核心内容
- **滑动平均视角**：将权重更新写为 $\boldsymbol{\theta}_t = (1 - \lambda_t \eta_t)\boldsymbol{\theta}_{t-1} - \eta_t \boldsymbol{u}_t$。这意味着当前权重实际上是初始权重与历史数据的指数滑动平均。
- **记忆周期限制**：在常数设置下，模型能够保留的有效梯度步数受限于 $\mathcal{O}(1 / \lambda \eta)$，这也是模型的记忆周期。为了防止模型遗忘早期训练数据，记忆周期应与总步数正比。
- **最优调度推导**：基于所有训练 Batch 数据应具有同等重要性（梯度权重恒定）的假设，在 $\beta_1,\beta_2 \to 0$ 极限下，反解微分方程，推导出：
  1. 常数 Weight Decay 下，最优学习率服从 $\eta_s \approx \frac{\eta_{\max}}{\lambda\eta_{\max} s + 1}$；
  2. 在比例更新约束下（$\lambda_s = \alpha \eta_s$），最优学习率和权重衰减需共同按 $1 / \sqrt{s}$ 的速度进行衰减。