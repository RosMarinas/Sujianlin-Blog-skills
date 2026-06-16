---
type: concept
title: "Saliency Map"
aliases:
  - "显著性图"
  - "输入重要性热力图"
definition: "通过分析模型输出对输入的敏感度来可视化哪些输入特征对决策最重要。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "4582"
related_methods:
  - [[method::RNN输入重要性评估]]
status: draft
updated: 2026-06-13
---

Saliency Map（显著性图）分析输入特征对模型输出的影响程度。本文提出了一种针对RNN的Saliency评估方法：计算各时间步隐藏状态到最终状态的距离差值，反映每个输入词对分类结果的贡献程度。正值表示促进分类，负值表示反作用。该方法简单直观，可用于文本分类中的关键词识别和模型可解释性分析。 这种方法简单直观，不需要额外训练，是理解RNN决策过程的有效工具，可用于模型调试和错误分析。 该方法可作为模型调试工具，帮助识别模型在做决策时实际关注的输入区域。
