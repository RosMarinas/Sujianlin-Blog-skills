---
type: formula
title: QK-Clip更新公式
latex: \boldsymbol{W}_t \leftarrow \boldsymbol{W}_t \times \sqrt{\frac{\tau}{S_{\max}^{(l,h)}}}
  \quad \text{or} \quad \boldsymbol{W}_t \times \frac{\tau}{S_{\max}^{(l,h)}}
symbol_meanings:
  W_t: 在优化器步更新后的 Query 或 Key 参数权重矩阵
  S_max: 当前注意力多头层中对应 Head 实际算得的 Softmax 前 Logit 最大绝对值
  tau: 规定的最大 Logit 安全阈值
standard_notation:
  weight_matrix: W_t
  max_logit: S_{max}
  threshold: tau
conditions: S_max 超过阈值 tau 且实施按 Head 对齐更新
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
source_ids:
- 11126
appears_in:
- - - spaces-11126-QK-Clip与Muon扩展
status: draft
updated: '2026-06-14'
---

## 概述

该公式提出了一种直接且无损的策略，以解决超大规模模型（如千亿参数的 Kimi K2）在使用 Muon 优化器时出现的 MaxLogit 爆炸现象。在标准的注意力机制 $\boldsymbol{O} = \text{softmax}(\boldsymbol{Q}\boldsymbol{K}^{\top})\boldsymbol{V}$ 中，全体 Logit 的最大值定义为 $S_{\max} = \max_{i,j}\, \boldsymbol{q}_i\cdot \boldsymbol{k}_j$。

从数学本质分析，根据不等式 $|\boldsymbol{q}_i\cdot \boldsymbol{k}_j| \leq \Vert\boldsymbol{x}_i\Vert \Vert\boldsymbol{x}_j\Vert \Vert\boldsymbol{W}_q\Vert \Vert\boldsymbol{W}_k\Vert$，由于输入向量 $\boldsymbol{x}$ 通常由 RMSNorm 约束其范数，因此 MaxLogit 的线性或超线性增长，直接意味着查询（Query）和键（Key）的映射权重矩阵 $\boldsymbol{W}_q$ 与 $\boldsymbol{W}_k$ 的谱范数（Spectral Norm）正在向无穷大发散。这种不受控的异常值膨胀轻则导致特定的 Attention Head 失效，重则引发梯度尖峰（Grad Spike）并导致训练彻底崩溃。

相较于通过增大 Weight Decay（这会带来明显的模型效果损失）或使用 Gemma2 的 $\text{softcap}(x;\tau) = \tau\tanh(x/\tau)$（仅能控制 $\text{softcap}$ 作用后的界限，无法阻止投影前的 Logit 原值继续膨胀），QK-Clip 直接对源头权重进行截断约束。当实际算得的 $S_{\max}$ 超过规定的最大安全阈值 $\tau$ 时，该公式计算出 $\sqrt{\frac{\tau}{S_{\max}^{(l,h)}}}$ 或 $\frac{\tau}{S_{\max}^{(l,h)}}$ 的收缩比例因子，对当前注意力多头层中对应 Head 的权重矩阵 $\boldsymbol{W}_t$ 直接进行乘性幅值微调。这种按 Head 施加的缩放更新强行在优化器迭代中将映射权重的范数拽回安全阈值内，从而在无损模型表现的前提下，从根本上消除了 MaxLogit 爆炸的风险。
