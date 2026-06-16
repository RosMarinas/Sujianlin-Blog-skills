---
type: article_summary
title: QK-Clip：让Muon在Scaleup之路上更进一步
article_id: 11126
source_url: https://spaces.ac.cn/archives/11126
date: 2025-07-12
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
topics:
  - [[MaxLogit爆炸]]
methods:
  - [[QK-Clip权重裁剪法]]
  - [[MuonClip优化方法]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
source_ids:
  - 11126
status: draft
updated: 2026-06-11
---

# QK-Clip：让Muon在Scaleup之路上更进一步

本文针对万亿参数模型 Kimi K2 训练中遇到的 MaxLogit 爆炸问题，提出了一种兼容 MLA (Multi-head Latent Attention) 的“QK-Clip”权重剪裁技术。

## 核心内容
- **MaxLogit 爆炸与谱范数**：Attention Logit 的最大值 $S_{\max}$ 超线性增长会导致训练不稳定。其背后的物理原因是权重矩阵 $\boldsymbol{W}_q, \boldsymbol{W}_k$ 的谱范数（最大奇异值）失控。
- **QK-Norm 与 MLA 的冲突**：传统的 QK-Norm 需在前向中显式对 $Q, K$ 进行归一化，这在推理阶段与 MLA 无法物化（Materialize）部分分量的设计冲突，从而无法应用于 MLA。
- **QK-Clip 方案**：作为一种事后策略，若在训练步之后发现某 Head 的 $S_{\max}^{(l,h)} > \tau$，则直接将对应的 $\boldsymbol{W}_q, \boldsymbol{W}_k$ 乘以裁剪系数 $\sqrt{\tau / S_{\max}}$，直接从权重层面实施控制。对于 MLA 共享的 $K$ 分量，只剪裁 $Q$ 以避免过度剪裁。
- **Muon 为什么更容易爆炸**：Muon 输出更新量为满秩正交更新，相比 Adam 的低秩更新，与历史参数发生“奇异向量重叠”的碰撞概率更高，因而会加速最大奇异值的增长。