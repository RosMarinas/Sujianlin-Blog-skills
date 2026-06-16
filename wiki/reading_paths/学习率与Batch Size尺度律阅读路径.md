---
type: reading_path
title: "学习率与Batch Size尺度律阅读路径"
aliases:
  - "learning-rate batch-size reading path"
goal: "从二阶近似出发，理解 SGD、SignSGD、Muon 和 EMA/Adam 的学习率-Batch Size 尺度律。"
audience: "了解梯度下降、Hessian、期望和协方差的读者。"
ordered_nodes:
  - "article::11260"
  - "article::11280"
  - "article::11285"
  - "article::11301"
source_ids:
  - "11260"
  - "11280"
  - "11285"
  - "11301"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
prerequisites:
  - "[[二阶近似最优学习率公式]]"
checkpoints:
  - "写出最优学习率比值公式"
  - "解释平均场近似"
  - "解释 Muon 与 SignSGD 的关系"
  - "解释 EMA 有效批量"
next_paths:
  - "[[SGD收敛与学习率调度阅读路径]]"
  - "[[Muon与矩阵优化阅读路径]]"
status: draft
updated: "2026-06-10"
---

# 学习率与Batch Size尺度律阅读路径

## 读者状态

适合已经熟悉 SGD 更新式、二阶 Taylor 展开和基本期望/协方差计算的读者。

## 阅读顺序

1. 读 11260，建立二阶近似最优学习率公式和 SGD 基线。
2. 读 11280，理解平均场如何把 SignSGD 的复杂积分压缩成 Batch Size 标量依赖。
3. 读 11285，观察同一平均场动作如何迁移到 Muon 的矩阵符号函数。
4. 读 11301，理解 EMA/动量为什么可解释为有效 Batch Size 放大。

## 检查点

- 能写出二阶近似最优学习率的通用比值形式。
- 能说明平均场近似保留了哪个 Batch Size 因子。
- 能解释 Muon 与 SignSGD 的尺度律为何相似。
- 能说明 EMA 的有效 Batch Size 放大因子来自协方差计算。
