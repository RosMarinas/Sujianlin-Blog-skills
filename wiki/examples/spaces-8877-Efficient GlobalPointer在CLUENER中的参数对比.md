---
type: example
title: Efficient GlobalPointer在CLUENER中的参数对比
article_id: "8877"
article: [[spaces-8877-Efficient-GlobalPointer-少点参数-多点效果]]
section: 惊喜的实验
claim: Efficient GlobalPointer将实体识别解耦为共享的抽取投影和实体特定类别的分类投影
notation_mapping:
  M * 2 * d * D: M * 2 * d * D
steps:
  - 步骤1：设定 NER 任务的实体类别数 M（在 CLUENER 数据集中 M = 10）。
  - 步骤2：原始 GlobalPointer 在多分类场景下构建 M 组不同的 $q$ 和 $k$ 注意力权重投影层，使得参数冗余随 M 线性增长。
  - 步骤3：在 Efficient GlobalPointer 中，使 10 个实体类别共用同一组 Span 提取查询/键投影权重，仅引入 10 个低维拼接偏置分类权重 w。
  - 步骤4：比较训练收敛与显存开销，在 CLUENER 验证集上 F1 达到 80.66%（比原始版本提高约 0.6%），且参数量骤降至原版的几十分之一。
used_concepts:
  - [[GlobalPointer]]
  - [[Efficient GlobalPointer]]
source_span: ev::8877::参数分解
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-25-Efficient-GlobalPointer-少点参数-多点效果.md
source_ids:
  - "8877"
status: stable
updated: 2026-06-12
---

# Efficient GlobalPointer在CLUENER中的参数对比

本实例展示了 Efficient GlobalPointer（EGP）在解决多类别命名实体识别时的参数压缩和性能提升效果。

以 BERT-base（特征维度 $D=768$）和注意力特征维度 $d=64$ 为基本结构，当面对有 10 个实体类别的 CLUENER 数据集时，原始 GlobalPointer 需要配置 10 对独立的主投影矩阵，产生参数接近一千万，显存消耗较大且更新稀疏。切换至 EGP 后，通过对“提取”和“分类”两个过程的投影解耦，使 10 类实体共享单一通用 Span 提取层，每新增一个类别仅需要添加 256（即 $4d$）个偏置权重。模型参数规模被成功压缩至 30 万左右，且因避免了参数稀疏过拟合而在验证集与测试集上均录得更好的 F1 得分。
