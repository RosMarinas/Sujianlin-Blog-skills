---
type: problem_pattern
title: "将优化器非线性更新转化为Batch Size尺度律问题"
aliases:
pattern_summary: "把非线性随机更新量的统计分析转化为 Batch Size 显式依赖，再解释学习率尺度律。"
trigger_questions:
  - "更新量是否非线性依赖随机梯度？"
  - "是否要比较不同 Batch Size 的最优学习率？"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_ids:
  - "11260"
  - "11280"
  - "11285"
  - "11301"
activates_methods:
  - "[[用平均场近似替代复杂期望计算]]"
  - "[[用等效Batch Size解释动量降噪]]"
typical_prerequisites:
  - "[[二阶近似最优学习率公式]]"
examples:
  - "[[spaces-11280-SignSGD平均场期望推导]]"
  - "[[spaces-11301-EMA等效Batch放大推导]]"
failure_modes:
  - "忽略平均场近似条件"
  - "把近似尺度律误读为严格非凸收敛定理"
evidence_spans:
  - "ev::11260::困难分析"
  - "ev::11280::方法大意"
status: stable
updated: "2026-06-10"
---

# 将优化器非线性更新转化为Batch Size尺度律问题

## 模式

当优化器更新量非线性依赖随机梯度时，直接分析学习率-Batch Size 关系很难；可先把更新量统计量近似成 Batch Size 的显式函数，再代回二阶最优学习率公式。

## 触发问题

- 更新量是否包含 sign、softsign、msign、EMA 或 Adam 分母？
- 目标是否是比较不同 Batch Size 下的最优学习率？
- 是否只需要主导尺度关系，而不是完整分布积分？

## 常见失败模式

把经验 scaling law 当作已证明定理，或忽略平均场/缓变/独立性假设。
