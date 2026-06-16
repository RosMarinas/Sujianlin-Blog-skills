---
type: article_summary
title: Google新搜出的优化器Lion：效率与效果兼得的“训练狮”
article_id: "9473"
source_url: https://spaces.ac.cn/archives/9473
date: 2023-02-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-02-16-Google新搜出的优化器Lion-效率与效果兼得的-训练狮.md
series: []
topics:
  - "[[优化器稳定性与自适应机制]]"
concepts:
  - "[[Lion优化器]]"
  - "[[直通估计器]]"
methods:
  - "[[用符号函数重写优化器更新方向]]"
problem_patterns: []
evidence_spans:
  - ev::9473::Lion更新公式
  - ev::9473::Lion与AdamW对比
  - ev::9473::Lion与SIGNUM关系
  - ev::9473::Amos炼丹策略应用
  - ev::9473::Lion噪声与平坦度
  - ev::9473::Lion小batch缺点
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-02-16-Google新搜出的优化器Lion-效率与效果兼得的-训练狮.md
source_ids:
  - "9473"
status: draft
updated: 2026-06-12
---

# Google新搜出的优化器Lion：效率与效果兼得的“训练狮”

## 文章核心问题

如何通过符号发现（Symbolic Discovery）算法自动寻找并设计超越主流AdamW的深度学习优化器，从而在提高收敛速度和泛化性能的同时，降低显存开销与计算复杂度。

## 主要结论

- **Lion优化器**（EvoLved Sign Momentum）通过符号函数将更新量的模长限制为常数，比AdamW少缓存一组二阶动量参数，显著降低显存开销。
- **与SIGNUM的关系**：SIGNUM是Lion的特例（$\beta_1 = \beta_2$ 且 $\lambda_t = 0$），但SIGNUM在泛化性上没有取得优势；Lion通过错位动量更新（动量更新在参数更新后）和超参微调，在多种生成与理解任务上表现优于AdamW。
- **超参规律**：Lion的学习率 $\eta$ 通常需要比AdamW缩小10倍以上（因为更新方向模长是 1），权重衰减率 $\lambda$ 需相应放大10倍以上以保持衰减幅度。
- **平坦度与泛化性**：$\text{sign}$ 操作引入了额外的噪声，促使模型进入损失函数更加平坦的区域，从而获得更好的泛化性能。
- **限制**：Lion在 Batch Size 小于 64 时效果不如AdamW，且在参数设置不当时可能发生数值发散，需要引入或增加 Warmup 步数。

## 推导结构

1. **提出更新公式**：给出Lion优化器状态更新方程，引入符号函数 $\text{sign}$。
2. **算法对比分析**：将Lion、AdamW和SIGNUM的数学更新机制进行比对，说明Lion省去二阶动量、除法和开根号所带来的内存与计算节省。
3. **推导超参方案**：参考Amos优化器理论，给出相对学习率与权重衰减率的自适应计算方案，通过 $\alpha_0$（初始参数相对更新量）与参数尺度 $\sigma$ 自适应匹配 $\eta$ 与 $\lambda$。
4. **探究泛化机制**：讨论 $\text{sign}$ 引入的梯度方向噪声对极值点平坦度的影响。
5. **局限性讨论**：指出小 Batch Size 下噪声叠加导致的性能恶化。

## 关键公式

- **Lion更新规则**：
  $$
  \left\{\begin{aligned}
  &\boldsymbol{u}_t = \text{sign}\big(\beta_1 \boldsymbol{m}_{t-1} + (1 - \beta_1) \boldsymbol{g}_t\big) \\
  &\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t (\boldsymbol{u}_t + \lambda_t \boldsymbol{\theta}_{t-1}) \\
  &\boldsymbol{m}_t = \beta_2 \boldsymbol{m}_{t-1} + (1 - \beta_2) \boldsymbol{g}_t
  \end{aligned}\right.
  $$
- **Amos炼丹参数组合**：
  $$
  \eta_t \approx \frac{\alpha_0\sigma}{\kappa t + 1},\quad \lambda_t = \frac{\alpha_0}{2\sigma}
  $$

## 体现的方法

- **用符号函数重写优化器更新方向**：丢弃传统的浮点梯度幅值，通过符号函数提取梯度的多维象限方向进行参数步长约束。
- **超参对齐与自适应**：通过参数初始化方差 $\sigma^2$ 反推最优学习率与权重衰减率的比例关系。

## 所属系列位置

独立研究文章，属于深度学习优化器理论和自适应机制的探讨。

## 与其他文章的关系

- 前置超参计算框架依赖于 [Amos优化器炼丹策略](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Amos优化器炼丹策略.md) (9344)。
- 与后续的 [Tiger优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Tiger优化器.md) (9512) 属于同一个 sign 动量优化器家族，并在 [Embedding异常分析](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Embedding过度更新.md) (9736) 中暴露了相同的梯度稀疏更新缺陷。

## 原文证据锚点

- **ev::9473::Lion更新公式**: 第23-28行，详细说明了Lion的更新状态转移方程。
- **ev::9473::Lion与AdamW对比**: 第30-41行，对比了Lion与AdamW的运算速度和内存缓存占用。
- **ev::9473::Lion与SIGNUM关系**: 第43-51行，分析了Lion与SIGNUM的等价条件及差异。
- **ev::9473::Amos炼丹策略应用**: 第70-84行，展示了利用Amos理论反推学习率和权重衰减比例的数学简化过程。
- **ev::9473::Lion噪声与平坦度**: 第92-96行，探讨了符号函数所产生的随机噪声与泛化极值点平坦度的因果假说。
- **ev::9473::Lion小batch缺点**: 第97-98行，讨论了小 Batch 规模下噪声过大导致发散的实验局限。
