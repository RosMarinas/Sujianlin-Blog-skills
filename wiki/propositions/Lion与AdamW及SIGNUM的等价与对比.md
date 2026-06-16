---
type: proposition
title: Lion与AdamW及SIGNUM的等价与对比
statement: Lion优化器在计算与内存开销上显著优于AdamW，且泛化表现优于SIGNUM；在特定条件下，SIGNUM可以视为Lion优化器的特殊退化版本。
assumptions:
  - 优化更新在多维浮点数参数向量空间中进行。
  - 权重衰减机制均采用解耦的Weight Decay方式。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-02-16-Google新搜出的优化器Lion-效率与效果兼得的-训练狮.md
source_ids:
  - "9473"
proof_route: |
  1. 对比Lion与AdamW公式：Lion更新量为 \text{sign}(\beta_1 \boldsymbol{m}_{t-1} + (1-\beta_1)\boldsymbol{g}_t)，没有二阶矩 \boldsymbol{v}_t 及其开根号除法，因此节省了一半动量内存空间（AdamW缓存m和v，Lion只缓存m）。
  2. 对比SIGNUM公式：SIGNUM的更新矢量为 \text{sign}(\boldsymbol{m}_t)，其中 \boldsymbol{m}_t = \beta \boldsymbol{m}_{t-1} + (1-\beta)\boldsymbol{g}_t。
  3. 代数对比：若设 Lion 的超参数满足 \beta_1 = \beta_2 = \beta 且权重衰减 \lambda_t = 0，则 Lion 的更新矢量 u_t 变为 \text{sign}(\beta \boldsymbol{m}_{t-1} + (1-\beta)\boldsymbol{g}_t) = \text{sign}(\boldsymbol{m}_t)，这与 SIGNUM 完全等价。故 SIGNUM 是 Lion 在 \beta_1=\beta_2 和无权重衰减下的特例。
evidence_spans:
  - ev::9473::Lion与AdamW对比
  - ev::9473::Lion与SIGNUM关系
status: draft
updated: 2026-06-12
---

# Lion与AdamW及SIGNUM的等价与对比

## 命题陈述

Lion优化器通过去除二阶动量状态，相比 AdamW 节省了大量的计算操作与显存开销。同时，虽然 SIGNUM 在数学上可以视为 Lion 的退化特例（即 $\beta_1=\beta_2$ 且 $\lambda_t=0$），但 SIGNUM 在大模型上未能取得良好泛化，而 Lion 凭借错位更新（先执行 `sign` 更新参数，再更新本步动量）与超参独立调整展现出了相比 AdamW 更好的泛化性能。

## 局限与边界条件

尽管 Lion 效率与效果表现优异，但在 Batch Size 较小（如小于 64）时，由于 `sign` 函数引入的方向噪声无法在样本中被充分平均，会造成更新发散或重构损失上升，在此限制下其收敛表现差于 AdamW。
