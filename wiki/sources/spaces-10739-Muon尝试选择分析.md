---
type: article_summary
title: Muon续集：为什么我们选择尝试Muon？
article_id: 10739
source_url: https://spaces.ac.cn/archives/10739
date: 2025-02-27
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
concepts:
  - [[最小作用量原理优化]]
  - [[奇异值熵]]
propositions:
  - [[Muon是谱范数下的最速下降]]
methods:
  - [[Update RMS 对齐法]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
source_ids:
  - 10739
status: draft
updated: 2026-06-11
---

# Muon续集：为什么我们选择尝试Muon？

本文解读了 Moonlight (3B/16B MoE) 模型中使用 Muon 优化器实现 2 倍训练效率提升背后的数学机理及其实践经验。

## 核心内容
- **最小作用量原理**：理想的优化器在限制参数扰动（稳）的前提下，实现损失的最大下降（快）。将这一机制表述为约束优化问题。不同的优化器实质上是选择了不同的参数扰动范数。
- **谱范数约束**：若选择矩阵的谱范数 $\|\Delta \boldsymbol{W}\|_2 \leq \eta$ 作为稳的度量，可以得到最速下降更新量为 Matrix Sign Function，即 Muon 的核心运算。
- **Weight Decay**：在 Muon 中，必须配置适当的 Weight Decay 来保证参数的谱范数有界，这对于防止注意力爆炸等“内科”疾病至关重要。
- **Update RMS 对齐**：为了免除繁杂的 Muon 超参搜索，提出将 Muon 的更新量 RMS 解析地对齐到 Adam 习惯 of 0.2，从而直接复用 Adam 的学习率和 Weight Decay 超参。