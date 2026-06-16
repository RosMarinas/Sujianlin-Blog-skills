---
type: concept
title: EFLA
aliases:
- Error-Free Linear Attention
definition: 一种高稳定性线性注意力（线性 RNN）形式，通过在时间步区间内对连续状态微分方程求解精确解析解而非欧拉离散化近似得到。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
source_ids:
- 11486
status: draft
updated: '2026-06-12'
---

EFLA 公式为：$\boldsymbol{S}_t = \boldsymbol{S}_{t-1} (\boldsymbol{I} - \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{k}_t\boldsymbol{k}_t^\top) + \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{v}_t \boldsymbol{k}_t^\top$。该递归天然包含了对 Key 的 L2 Normalize，保障了数值稳定性。