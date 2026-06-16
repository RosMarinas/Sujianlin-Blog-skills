---
type: concept
title: Pre-Norm vs Post-Norm
aliases:
  - Pre-LN vs Post-LN
definition: Pre-Norm 与 Post-Norm 指的是在残差网络（如 Transformer）中层归一化（Layer Normalization）与残差连接（Residual Connection）的相对位置排布方式。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
source_ids:
  - "9009"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Pre-Norm vs Post-Norm

## Definition
Pre-Norm 与 Post-Norm 指的是在残差网络（如 Transformer）中层归一化（Layer Normalization）与残差连接（Residual Connection）的相对位置排布方式。

## Explanation
两者的基本公式为：
- **Pre-Norm**: $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t + F_t(Norm(\boldsymbol{x}_t))$
- **Post-Norm**: $\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + F_t(\boldsymbol{x}_t))$
目前学界的共识是，Pre-Norm 更加稳定，极易训练且不需要复杂的 Warmup 学习率计划。但由于其恒等映射比重过高，在深度很大时，前后层表征高度相关，使多层网络近似退化为“扁而宽”的浅层模型（深度水分/深度退化），丧失了一定的深度拟合能力。
相反，Post-Norm 在每一层对特征进行了 Norm 缩放，有效削弱了恒等分支的模长权重，突出了残差计算，使得其层数的有效表征深度更为“足秤”，因此在下游精调和泛化性能上，Post-Norm 通常显著优于 Pre-Norm。
