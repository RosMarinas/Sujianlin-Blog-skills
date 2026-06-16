---
type: concept
title: 条件LayerNorm
aliases:
- Conditional Layer Normalization
definition: 将条件向量注入LayerNorm的 $\beta$ 和 $\gamma$ 参数，控制模型输出行为的归一化方式。
standard_notation: $\text{LN}(x; c) = \gamma(c) \odot \frac{x - \mu}{\sigma} + \beta(c)$
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
source_ids:
- '8337'
related_methods:
- - - method::条件LayerNorm多任务学习
status: draft
updated: '2026-06-12'
---
# 条件LayerNorm

条件LayerNorm将条件信息通过可学习的 $\gamma(c)$ 和 $\beta(c)$ 注入LayerNorm层。在搜狐文本匹配任务中，将6个子任务的类型ID作为条件，单一模型通过条件LayerNorm生成针对不同标准的输出，实现参数完全共享的多任务学习。

顾名思义，比赛的任务是文本匹配，即判断两个文本是否相似，本来是比较常规的任务，但有意思的是它分了多个子任务。具体来说，它分A、B两大类，A类匹配标准宽松一些，B类匹配标准严格一些，然后每个大类下又分为“短短匹配”、“短长匹配”、“长长匹配”3个小类，因此，虽然任务类型相同，但严格来看它是六个不同的子任务。

```

{

title: 搜狐文本匹配：基于条件LayerNorm的多任务baseline

当然，如果看成是常规的多任务学习问题，那又太一般化了。针对这几个任务“形式一样、标准不一样”的特点，笔者构思了通过条件LayerNorm（Conditional Layer Normalization）来实现用一个模型做这6个子任务。

关于条件LayerNorm，我们之前在文章[《基于Conditional Layer Normalization的条件文本生成》](/archives/7124)也介绍过，虽然当时的例子是文本生成，但是它可用的场景并不局限于此。简单来说，条件LayerNorm就是一种往Transformer里边加入条件向量来控制输出结果的一种方案，它把条件加入到LayerNorm层的$\beta,\gamma$中。
