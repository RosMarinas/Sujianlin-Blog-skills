---
type: proposition
title: Tiger优化器无感梯度累积等价性
statement: Tiger优化器通过对滑动平均衰减率 beta 和学习率进行分段指示函数调制，在不分配任何额外显存空间的情况下，数学上精确等价于标准的梯度累积动量迭代算法。
assumptions:
  - 梯度累积步数为 $k$。
  - 标准梯度累积缓存并平均这 $k$ 步梯度，即 $\bar{\boldsymbol{g}} = \frac{1}{k}\sum_{i=1}^k \boldsymbol{g}_{T+i}$，随后在大更新步执行动量与参数滚动。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
source_ids:
  - "9512"
proof_route: |
  1. 设定指示函数 $\chi_{t/k}$，当 $t$ 能被 $k$ 整除时为 1，否则为 0。
  2. 考虑参数 $\boldsymbol{\theta}$ 在子更新步 $t = T+i$ ($1 \le i < k$) 时的行为。由于 $\chi_{t/k} = 0$，故有 $\boldsymbol{\theta}_{T+i} = \boldsymbol{\theta}_{T+i-1}$，即权重保持不变。
  3. 考虑动量 $\boldsymbol{m}_t$ 在子更新步的行为：
     - 若 $t-1 \equiv 0 \pmod k$，即上一步刚刚完成了大更新，有 $\chi_{(t-1)/k} = 1$。动量更新为：
       \boldsymbol{m}_{T+1} = \beta \boldsymbol{m}_T + \frac{1}{k}(1-\beta)\boldsymbol{g}_{T+1}
     - 若 $t-1 \not\equiv 0 \pmod k$，即处于累积中间段，有 $\chi_{(t-1)/k} = 0$。动量滚动仅作加累加：
       \boldsymbol{m}_{T+i} = \boldsymbol{m}_{T+i-1} + \frac{1}{k}(1-\beta)\boldsymbol{g}_{T+i} \quad (2 \le i \le k)
  4. 展开第 $T+k$ 步的最终动量值：
     \boldsymbol{m}_{T+k} = \boldsymbol{m}_{T+1} + \sum_{i=2}^k \frac{1}{k}(1-\beta)\boldsymbol{g}_{T+i}
     = \beta \boldsymbol{m}_T + \frac{1}{k}(1-\beta)\boldsymbol{g}_{T+1} + \sum_{i=2}^k \frac{1}{k}(1-\beta)\boldsymbol{g}_{T+i}
     = \beta \boldsymbol{m}_T + (1-\beta) \left[ \frac{1}{k} \sum_{i=1}^k \boldsymbol{g}_{T+i} \right]
     这与标准梯度累积更新得到的动量状态完全等价。
  5. 此时 $t = T+k$ 满足整除，有 $\chi_{t/k} = 1$，参数触发大步更新：
     \boldsymbol{\theta}_{T+k} = \boldsymbol{\theta}_T - \eta_{T+k}\left[\text{sign}(\boldsymbol{m}_{T+k}) + \lambda_{T+k}\boldsymbol{\theta}_T\right]
     这与利用 $\bar{\boldsymbol{g}}$ 执行 Standard 累积的一步更新完全同构。
evidence_spans:
  - ev::9512::Tiger梯度累积
status: draft
updated: 2026-06-12
---

# Tiger优化器无感梯度累积等价性

## 命题陈述

Tiger优化器在修改滑动平均率 $\beta$ 与步长系数后，无需分配额外显存用于存储累加的浮点梯度，就能在数学上等价实现包含梯度累积的自适应优化动作。

## 物理意义

这一特性是 Tiger 的核心优势。由于 Lion 和 Adam 在更新量中混杂了当前的即时梯度，无法在不缓存梯度的前提下将累积作用折算进一阶状态中。Tiger 仅使用动量驱动更新，从而能够以“修改滑动平均率的插值”实现真正的零开销梯度累积。
