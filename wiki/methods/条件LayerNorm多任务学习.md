---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 条件LayerNorm多任务学习
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
source_ids:
  - 8337
method_summary: 将任务类型ID作为条件向量注入Transformer各层LayerNorm的 $\beta,\gamma$ 参数，单一模型处理多个不同标准的文本匹配子任务
typical_structure: |
  1. 对于多个不同的子任务，分别赋予独立的任务 ID。
  2. 通过一个 Embedding 层将任务 ID 转换为条件向量 $c$。
  3. 在共享基础大模型（如 Transformer）的每一层的 LayerNorm 中，将原有的可学习参数 $\gamma$ 和 $\beta$ 替换为由条件向量 $c$ 生成的线性映射函数（如全连接网络生成）。
  4. 在多任务混合训练时，每个批次样本除了输入原始数据，还必须附带其对应的任务 ID。
  5. 模型主体参数完全共享，仅通过各个任务专属的条件 LayerNorm 适配器来扭转和输出不同标准的预测结果。
applicability: 多个相似但标准不同的任务（例如多类文本匹配场景中某些要求字面完全匹配，某些要求语义匹配），希望尽可能参数共享以提升训练效率和效果的多任务场景。
tools: 
related_methods: 
examples:
  - [[article::8337]]
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::8337::利用条件LayerNorm在搜狐文本匹配挑战赛中将6个不同任务整合在单个模型中进行训练的实战方案。
---

## 适用问题

多个相似但标准不同的任务（例如多类文本匹配场景中某些要求字面完全匹配，某些要求语义匹配），希望尽可能参数共享以提升训练效率和效果的多任务场景。

## 核心变换

将任务标识 $c$ 转化为条件向量，并以此作为 LayerNorm 层的仿射变换参数（$\beta, \gamma$）的输入进行自适应缩放与平移：
$$\text{LayerNorm}(x|c) = \gamma(c) \cdot \frac{x - \mu}{\sigma} + \beta(c)$$

## 典型步骤

1. 对于多个不同的子任务，分别赋予独立的任务 ID。
2. 通过一个 Embedding 层将任务 ID 转换为条件向量 $c$。
3. 在共享基础大模型（如 Transformer）的每一层的 LayerNorm 中，将原有的可学习参数 $\gamma$ 和 $\beta$ 替换为由条件向量 $c$ 生成的线性映射函数（如全连接网络生成）。
4. 在多任务混合训练时，每个批次样本除了输入原始数据，还必须附带其对应的任务 ID。
5. 模型主体参数完全共享，仅通过各个任务专属的条件 LayerNorm 适配器来扭转和输出不同标准的预测结果。

## 直觉

想象有一个万能厨师（基础大模型），他掌握了所有做菜的基本功。不同顾客的要求（子任务）不同，有的要微辣有的要重辣。我们不需要为每种辣度雇一个新厨师，只需要在每道工序最后的“撒调料”环节（LayerNorm），根据点菜单上的标签（条件向量）自动调整盐和辣椒的比例（生成不同的 $\gamma, \beta$）。这样同一个厨师就能无缝处理各种不同口味的订单。

## 边界

只适用于各任务在基础特征提取层面上具有高度同质性的情况。如果多任务之间的领域差异极大（比如一个是图像生成一个是文本分类），仅靠 LayerNorm 的仿射变换无法弥合鸿沟，会导致严重的负迁移现象。

## 例子

在搜狐校园文本匹配大赛中，共有要求各异的“短短”、“短长”、“长长”匹配以及宽松与严格两套标准组成的 6 个子任务。如果不单独训练 6 个模型，而是通过在 RoFormer 中嵌入带任务 ID 标签的条件 LayerNorm，成功用单模型实现了 SOTA 性能，并且推理与部署极其精简。

## 证据

- ev::8337::利用条件LayerNorm在搜狐文本匹配挑战赛中将6个不同任务整合在单个模型中进行训练的实战方案。
