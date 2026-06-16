---
type: concept
title: "Flooding"
aliases:
  - "洪泛训练"
definition: "损失降到阈值b后交替执行梯度下降和梯度上升的训练策略，等效于梯度惩罚正则化。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/...
source_ids:
  - "7643"
related_methods:
  - [[method::Flooding训练策略]]
status: draft
updated: 2026-06-13
---

Flooding是一种新颖的训练策略：当损失函数降到预设阈值b后，将损失改为|L(theta)-b|+b，从而交替执行梯度下降和梯度上升。通过泰勒展开分析，这种策略等效于以学习率epsilon^2/2最小化梯度范数||grad L(theta)||^2的梯度惩罚正则化。Flooding促使参数走向更平滑的区域，能有效提高模型的泛化性能和抗扰动能力。 实现简单只需在损失函数上加一行代码，实验显示在某些任务上能使验证集损失出现二次下降，有效提升泛化性能。
