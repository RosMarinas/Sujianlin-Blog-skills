---
type: concept
title: Adam更新RMS
aliases:
- Update RMS
- 更新均方根
definition: 指在 Adam/AdamW 优化器参数更新过程中，更新步向量（除以学习率前的更新量）的二阶均方根值，体现了梯度的信噪比和尺度缩放特征。
standard_notation: \|\boldsymbol{u}_t\|_{RMS} = \sqrt{\text{mean}(\boldsymbol{u}_t^2)}
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
- '11267'
related_formulas:
- '[[Adam更新均方根公式]]'
related_methods:
- '[[MatchAdamUpdateRMS迁移法]]'
status: draft
null_evidence_reason: Initial compilation draft with updated schema
updated: '2026-06-12'
---

## 概述

Adam更新RMS是指更新向量 $\boldsymbol{u}_t = \hat{\boldsymbol{m}}_t / (\sqrt{\hat{\boldsymbol{v}}_t} + \epsilon)$ 的 Root Mean Square（均方根）。在实际的大规模语言模型（LLM）训练中，只要 warmup 结束进入稳态，该值会稳定在 0.2~0.3 之间（对于典型的超参数 $\beta_1=0.9, \beta_2=0.95$）。

## 稳态特征

1. **与二阶矩超参无关**：稳态下 Update RMS 几乎与 $\beta_2$ 无关，而主要取决于动量参数 $\beta_1$ 和梯度的信噪比（SNR）。
2. **与信噪比正相关**：随着梯度信噪比的提高，Update RMS 会逐渐增大；当信噪比极低（纯高斯噪声极限，SNR=0）时，其理论下界由 $\sqrt{\frac{1-\beta_1}{1+\beta_1}}$ 决定。
3. **迁移应用**：该特征为优化器迁移中的 Update RMS 对齐技术提供了理论支撑。