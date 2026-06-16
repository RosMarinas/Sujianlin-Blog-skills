---
type: article_summary
title: "Adam的epsilon如何影响学习率的Scaling Law？"
article_id: "10563"
source_url: https://spaces.ac.cn/archives/10563
date: 2024-11-18
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-11-18-Adam的epsilon如何影响学习率的Scaling-Law.md
series:
  - "[[重新思考学习率与Batch Size]]"
topics:
  - "[[优化动力学]]"
concepts:
  - "[[Adam epsilon]]"
  - "[[SoftSignSGD]]"
  - "[[学习率-Batch Size尺度律]]"
  - "[[Surge现象]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
  - "[[用等效Batch Size解释动量降噪]]"
evidence_spans:
  - "ev::10563::SoftSign"
  - "ev::10563::S型近似"
  - "ev::10563::均值估计"
  - "ev::10563::方差估计"
  - "ev::10563::结果初探"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-11-18-Adam的epsilon如何影响学习率的Scaling-Law.md
source_ids:
  - "10563"
status: draft
updated: 2026-06-10
---

# Adam的epsilon如何影响学习率的Scaling Law？

## Summary

将Adam近似从SignSGD推广到SoftSignSGD，分析epsilon对学习率-Batch Size尺度律的影响，发现epsilon越大Adam越接近SGD，"Surge现象"概率越低。

## Key Claims

1. Adam的更新量分母epsilon在LLM训练中不可忽略（常见1e-5），影响了学习率的Scaling Law。
2. 使用SoftSignSGD (x/√(x²+ε²)) 替代SignSGD近似Adam，结果介于SGD与SignSGD之间。
3. epsilon越大，Adam越接近SGD；ε→∞时还原为SGD结果。
4. epsilon增大降低Surge现象出现的概率（必要条件为∑ν_iν_jH_{i,j} - ∑H_{i,i} > 0，ν_i随ε增大而减小）。
