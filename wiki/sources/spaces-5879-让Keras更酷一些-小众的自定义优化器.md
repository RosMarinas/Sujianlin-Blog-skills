---
type: article_summary
title: “让Keras更酷一些！”：小众的自定义优化器
article_id: "5879"
source_url: https://spaces.ac.cn/archives/5879
date: 2018-09-08
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-09-08-让Keras更酷一些-小众的自定义优化器.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-08-让Keras更酷一些-小众的自定义优化器.md
source_ids:
  - "5879"
status: draft
updated: 2026-06-11
---

# “让Keras更酷一些！”：小众的自定义优化器

本文介绍了在 Keras 中如何自定义优化器，包括符合 Keras 规范的标准写法以及一种用于特殊场景的“侵入式”外挂写法。

## 主要内容

1. **标准自定义优化器**：
   - 继承自 `Optimizer` 父类，重写 `get_updates(self, loss, params)` 以及 `get_config(self)`。
   - 在 `get_updates` 中通过 `self.get_gradients(loss, params)` 获取当前梯度，并通过 `K.update` 或 `K.update_add` 来定义参数和内部变量（如迭代次数 `iterations`）的更新。
   - 本文尝试编写了“软 batch”（即梯度累积）的优化器，但作者在 2019 年更新中指出本文的 `K.switch` 方案有误（因为其不能阻止分支评估），并在文章 [6794](/archives/6794) 中给出了修正方案。

2. **侵入式优化器（外挂写法）**：
   - 传统优化器的 `get_updates` 在单步训练（对应 TensorFlow 的单次 `sess.run`）中仅能执行一次梯度计算，无法实现需要多次计算梯度的优化算法（例如微分方程的二阶 Heun 方法）。
   - 通过在 Keras `model.compile` 后执行注入函数，直接覆盖和重构模型的 `model.train_function`。
   - `model.train_function` 本质上是一个 `K.function`。侵入式写法通过创建多个 `K.function`，并定义一个组合包装函数（例如先计算临时梯度并走一步，再在此基础计算新梯度并微调），从而在单次训练迭代中实现多次梯度评估。
   - 实例：`HeunOptimizer`。
