---
type: article_summary
title: 为什么DeltaNet要加L2 Normalize？
article_id: 11486
source_url: https://spaces.ac.cn/archives/11486
date: 2025-12-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
concepts:
  - [[EFLA]]
propositions:
  - [[DeltaNet特征值界约束]]
methods:
  - [[连续动力学精确解递归法]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
source_ids:
  - 11486
status: draft
updated: 2026-06-11
---

# 为什么DeltaNet要加L2 Normalize？

本文分析了 DeltaNet 中对 Key 向量实施 L2 归一化的稳定性机理，并介绍了一种基于连续时间动力学精确解的参数化方案——EFLA (Error-Free Linear Attention)。

## 核心内容
- **稳定性分析**：DeltaNet 的状态转移矩阵为 $\boldsymbol{I} - \eta_t \boldsymbol{k}_t\boldsymbol{k}_t^\top$。为防止累乘下特征值发散，其特征值必须严格落在 $[-1, 1]$ 内，这推导出特征值约束。传统的实现选择将 $\boldsymbol{k}_t$ 进行 L2 归一化并给 $\eta_t$ 施加 Sigmoid 映射以实现这一约束。
- **连续时间视角（EFLA）**：将 Delta Rule 的离散递归视为一阶微分方程 $\frac{d}{dt}\boldsymbol{S}_t = -\boldsymbol{S}_t \boldsymbol{k}_t\boldsymbol{k}_t^\top + \boldsymbol{v}_t \boldsymbol{k}_t^\top$ 的离散化。
- **精确解递归**：解析地求解该线性常微分方程，得出精确转移格式为 $\boldsymbol{S}_t = \boldsymbol{S}_{t-1} (\boldsymbol{I} - \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{k}_t\boldsymbol{k}_t^\top) + \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{v}_t \boldsymbol{k}_t^\top$。分母自然出现的 $\|\boldsymbol{k}_t\|^2$ 在数学上完美地导出了 L2 归一化，为特征归一化提供了一个自然的理论通路。