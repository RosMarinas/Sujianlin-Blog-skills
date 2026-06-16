---
type: concept
title: "Focal Loss"
aliases:
  - "焦点损失"
definition: "通过$(1-\hat{y})^\gamma$调节因子降低易分类样本的权重，使模型聚焦于难分类样本。"
standard_notation: "$L_{fl}=-(1-\hat{y})^\gamma\log\hat{y}$"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "4733"
related_methods:
  - [[method::Focal Loss损失函数]]
status: draft
updated: 2026-06-13
---

Focal Loss是Kaiming团队为解决目标检测中类别不平衡问题提出的损失函数。通过引入调制因子(1-y_hat)^gamma，降低易分类样本的loss贡献，使模型聚焦于难分类样本。当gamma=0时退化为标准交叉熵。本文从硬截断loss的缺点出发，通过sigmoid平滑化得到类似loss，并指出gamma和K（平滑参数）作用等价。 gamma=2、alpha=0.25是Kaiming在目标检测任务上的推荐配置。在NLP领域，该损失同样可以应用于序列标注等类别严重不平衡的任务。
