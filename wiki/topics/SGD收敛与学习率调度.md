---
type: topic
title: "SGD收敛与学习率调度"
aliases:
  - "随机优化收敛"
  - "SGD learning-rate schedule"
scope: "SGD 收敛、终点损失、学习率调度，以及学习率与 Batch Size 尺度律。"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_ids:
  - "9902"
  - "11469"
  - "11480"
  - "11494"
  - "11530"
  - "11540"
  - "11260"
  - "11280"
  - "11285"
  - "11301"
series:
  - "[[让炼丹更科学一些]]"
  - "[[重新思考学习率与Batch Size]]"
concepts:
  - "[[SGD平均损失收敛]]"
  - "[[SGD终点损失收敛]]"
  - "[[梯度自适应学习率]]"
  - "[[学习率-Batch Size尺度律]]"
  - "[[平均场近似学习率分析]]"
  - "[[EMA等效批量放大]]"
formulas:
  - "[[SGD平均损失界]]"
  - "[[加权终点恒等式]]"
  - "[[Warmup-Decay最优学习率]]"
  - "[[二阶近似最优学习率公式]]"
  - "[[EMA等效Batch Size公式]]"
propositions:
  - "[[线性衰减实现终点最优速率]]"
  - "[[EMA等效放大Batch Size]]"
methods:
  - "[[通过恒等式重写优化轨迹]]"
  - "[[自上而下构造辅助序列]]"
  - "[[用平均场近似替代复杂期望计算]]"
  - "[[用等效Batch Size解释动量降噪]]"
problem_patterns:
  - "[[将经验学习率策略转化为收敛界优化问题]]"
  - "[[将优化器非线性更新转化为Batch Size尺度律问题]]"
reading_paths:
  - "[[SGD收敛与学习率调度阅读路径]]"
  - "[[学习率与Batch Size尺度律阅读路径]]"
open_questions:
  - "Adam 等自适应优化器的完整严格收敛理论暂不提升为稳定命题。"
status: draft
updated: "2026-06-10"
---

# SGD收敛与学习率调度

## 主题边界

本主题收录 SGD 收敛界、终点损失、学习率调度和学习率-Batch Size 尺度律。它仍不把非凸深度网络训练中的经验规律提升为严格稳定定理。

## 主题内对象

- 系列：[[让炼丹更科学一些]]、[[重新思考学习率与Batch Size]]
- 核心概念：[[SGD平均损失收敛]]、[[SGD终点损失收敛]]、[[学习率-Batch Size尺度律]]、[[平均场近似学习率分析]]、[[EMA等效批量放大]]
- 核心公式：[[SGD平均损失界]]、[[二阶近似最优学习率公式]]、[[SignSGD平均场学习率公式]]、[[EMA等效Batch Size公式]]

## 明确不在本 batch 内

- 非凸训练的严格收敛证明。
- Adam/RMSProp 的完整定理化推导。
- 外部论文的独立 article_summary 建模。
