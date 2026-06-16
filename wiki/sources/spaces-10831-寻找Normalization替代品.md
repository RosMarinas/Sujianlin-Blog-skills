---
type: article_summary
title: 通过梯度近似寻找Normalization的替代品
article_id: 10831
source_url: https://spaces.ac.cn/archives/10831
date: 2025-04-02
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
concepts:
  - [[Dynamic Tanh]]
  - [[Dynamic ISRU]]
methods:
  - [[对角雅可比梯度近似法]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
source_ids:
  - 10831
status: draft
updated: 2026-06-11
---

# 通过梯度近似寻找Normalization的替代品

本文通过对 RMSNorm 梯度的对角化近似，推导了无 Normalization 模型中使用的 DyT (Dynamic Tanh) 和 DyISRU (Dynamic ISRU) 激活函数的数学机理。

## 核心内容
- **RMSNorm 的梯度**：求得其 Jacobian 矩阵 $\nabla_{\boldsymbol{x}} \boldsymbol{y} = \frac{1}{\|\boldsymbol{x}\|_{RMS}} (I - \frac{\boldsymbol{y}\boldsymbol{y}^\top}{d})$。
- **雅可比矩阵对角近似**：因为逐元素（Element-wise）运算的雅可比矩阵必为对角矩阵，通过保留 RMSNorm 的对角部分 $\frac{dy_i}{dx_i} = \frac{1}{\|\boldsymbol{x}\|_{RMS}} (1 - \frac{y_i^2}{d})$，并在假设 RMS 模长为常数的条件下求解该微分方程，便导出了 DyT 的双曲正切结构。
- **DyISRU 的推导**：如果不作 RMS 模长为常数的假设，而是代入恒等式 $\|\boldsymbol{x}\|_{RMS} = x_i / y_i$，可以解得更精确的逐元素近似 DyISRU，形式为 $y_i = \frac{\sqrt{d} x_i}{\sqrt{x_i^2 + C}}$。
- **实践局限**：这类 Softcap 式的逐元素光滑裁剪在实践中依然无法完全抑制 Attention Logits 的底层增长，这也是为何 Gemma3 等工作最终放弃 Softcap 回归 QK-Norm 的本质原因。