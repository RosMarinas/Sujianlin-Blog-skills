---
type: article_summary
title: Tiger：一个“抠”到极致的优化器
article_id: "9512"
source_url: https://spaces.ac.cn/archives/9512
date: 2023-03-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
series: []
topics:
  - "[[优化器稳定性与自适应机制]]"
concepts:
  - "[[Tiger优化器]]"
  - "[[Lion优化器]]"
methods:
  - "[[用符号函数重写优化器更新方向]]"
  - "[[通过矩阵块自适应缩放学习率]]"
problem_patterns: []
evidence_spans:
  - ev::9512::Tiger更新公式
  - ev::9512::Tiger超参设置
  - ev::9512::Tiger梯度累积
  - ev::9512::Tiger半精度训练
  - ev::9512::Tiger防止NaN
  - ev::9512::Tiger退化思想
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
source_ids:
  - "9512"
status: draft
updated: 2026-06-12
---

# Tiger：一个“抠”到极致的优化器

## 文章核心问题

如何通过对Lion优化器进行进一步的数学简化（将滑动平均率统一为 $\beta_1=\beta_2$），从而在不降低甚至能优化模型泛化性的前提下，实现“无感且零显存开销”的内置梯度累积。

## 主要结论

- **Tiger优化器**：在Lion的基础上令 $\beta_1=\beta_2=\beta$。其状态更新仅依赖于单组动量和当前权重本身，是更极简的符号优化器。
- **无感梯度累积**：由于Tiger更新不显式使用当前批梯度（而是只用动量 $\boldsymbol{m}_t$），因此可以在需要梯度累积时直接修改滑动衰减率 $\beta$ 和学习率 $\eta_t$，从而无需像Adam或Lion那样额外开辟显存来缓存历史梯度。
- **自适应块学习率**：对偏置和归一化参数，学习率设置为全局相对学习率的一半；对于主要的权重矩阵，将学习率乘以其自身的均方根（RMS），即 $\eta_t = \alpha_t \times \text{RMS}(\boldsymbol{\theta})$，从而解耦了参数的初始化模长和相对更新幅度。
- **全半精度（FP16）训练**：在混合精度或纯FP16下，由于 $\text{sign}$ 操作更新幅度总是常数，只要学习率不小于 $6\times 10^{-8}$ 即可确保不会下溢出，从而支持完全在FP16范畴内执行状态转移。
- **防NaN收缩策略**：当检测到梯度出现 $\text{NaN}$ 时，跳过当前更新并将权重向其初始化中心方向以 $s=0.99$ 的收缩率做轻微收缩，防止训练崩溃。

## 推导结构

1. **基本定义**：给出Tiger更新公式，并将Tiger、Lion、AdamW的计算开销和动量机制对齐。
2. **块级超参微调**：提出将bias、beta、gamma与kernel矩阵进行分类，设计基于参数 $\text{RMS}$ 缩放的学习率自适应分配方法。
3. **无感梯度累积推导**：通过指示函数 $\chi_{t/k}$ 展开，将梯度累积行为等价嵌入到滑动平均动力学中，求得修改后的等效 $\beta$ 和学习率。
4. **全FP16溢出分析**：从符号函数输出恒为 $\pm 1$ 以及动量界限出发，分析为何Tiger天然免疫FP16数值下溢。
5. **梯度异常处理**：设计出现 NaN 时动量保留与权重中心化收缩的鲁棒机制。

## 关键公式

- **Tiger更新公式**：
  $$
  \left\{\begin{aligned}
  &\boldsymbol{m}_t = \beta \boldsymbol{m}_{t-1} + (1 - \beta) \boldsymbol{g}_t \\
  &\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t \left[\text{sign}(\boldsymbol{m}_t) + \lambda_t \boldsymbol{\theta}_{t-1}\right]
  \end{aligned}\right.
  $$
- **无感梯度累积公式**：
  $$
  \left\{\begin{aligned}
  &\boldsymbol{m}_t = \big[(\beta - 1)\chi_{(t-1)/k} + 1\big] \boldsymbol{m}_{t-1} + \frac{1}{k}(1 - \beta) \boldsymbol{g}_t \\
  &\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \chi_{t/k}\eta_t \left[\text{sign}(\boldsymbol{m}_t) + \lambda_t \boldsymbol{\theta}_{t-1}\right]
  \end{aligned}\right.
  $$
- **参数收缩防NaN公式**（在 $\boldsymbol{g}_t = \text{NaN}$ 时激活）：
  $$
  \left\{\begin{aligned}
  &\boldsymbol{m}_t = \boldsymbol{m}_{t-1} \\
  &\boldsymbol{\theta}_t = (\boldsymbol{\theta}_{t-1} - c)\times s + c
  \end{aligned}\right.
  $$

## 体现的方法

- **用符号函数重写优化器更新方向**：通过符号化动量过滤幅度差异，加速极值收敛。
- **通过矩阵块自适应缩放学习率**：在局部子层根据权重 $\text{RMS}$ 矩阵模长动态校准步长，解耦跨网络尺度调参。
- **优化步长与状态收缩**：在梯度发生数值异常时通过主动的状态流形中心收缩替代单纯抛弃梯度。

## 所属系列位置

独立研究文章，属于深度学习优化器理论和自适应机制的探讨。

## 与其他文章的关系

- 自适应步长调节继承了 [Amos优化器炼丹策略](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Amos优化器炼丹策略.md) (9344) 与 [LAMB优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/AdaFactor优化器.md) (7094)。
- 与 [Lion优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) (9473) 存在继承和特化关系，并同样会导致 [Embedding过度更新异常](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Embedding过度更新.md) (9736)。

## 原文证据锚点

- **ev::9512::Tiger更新公式**: 第24-32行，描述了Tiger的最小化参数状态转移关系。
- **ev::9512::Tiger超参设置**: 第66-100行，阐述了自适应块学习率和偏置项不进行权重衰减的先验理论。
- **ev::9512::Tiger梯度累积**: 第101-118行，利用示性函数推导将梯度累积完全整合进 $\beta$ 调度，避免历史梯度缓存显存开销。
- **ev::9512::Tiger半精度训练**: 第119-124行，分析了符号函数对于低精度量化下溢出的鲁棒性。
- **ev::9512::Tiger防止NaN**: 第125-139行，提出在梯度出现 $\text{NaN}$ 时对权重进行常数中心化收缩的防御动作。
- **ev::9512::Tiger退化思想**: 第169-188行，提出了使优化器随着训练推进从Tiger（$sign$ 驱动）逐渐退化为SGDM的自适应插值设想。
