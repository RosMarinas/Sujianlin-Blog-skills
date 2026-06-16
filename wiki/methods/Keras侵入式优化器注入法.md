---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Keras侵入式优化器注入法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-08-让Keras更酷一些-小众的自定义优化器.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-08-用时间换取效果-Keras梯度累积优化器.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-08-让Keras更酷一些-小众的自定义优化器.md
source_ids:
  - 5879
method_summary: 通过直接覆盖 Keras 模型的 `model.train_function` 计算图，将单步训练拆分为多个顺序执行的子更新步骤（K.function），从而实现需要多次计算梯度的复杂优化算法（如 Heun 方法）。
typical_structure: |
  1. 继承 Keras Optimizer 基类，但不使用传统的 get_updates 返回单一计算图算子。
  2. 实现一个 get_grouped_updates 方法，分阶段计算不同阶段的梯度与状态变量。
  3. 定义 inject() 方法获取模型的底层输入/目标占位符。
  4. 利用 K.function 将分组的更新步骤编译为多个分离的前向-反向操作函数，并覆盖覆盖 model.train_function 使其按顺序执行。
applicability: 当需要实现类似二阶或多阶 ODE 求解器更新规则的优化算法（如 Heun, RK23, RK45），这类算法需要在单步参数更新中重新针对更新后的状态计算二次或多次梯度，因而超出了传统单步 `get_updates` 优化器结构限制的场景。
examples:
  - [[article::5879]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::5879::文中指出可以通过覆盖底层执行入口来实现多步梯度更新计算：“通过在外部将单次 sess.run 分拆编译为多个顺序的 K.function 级联...并覆盖 Keras 底层的 train_function”。
---





## 适用问题
需要实现高级微积分数值解法式的优化算法（如 Heun方法、Runge-Kutta 法等），这些算法要求在一次训练迭代（单 batch）中，先用初步梯度走一小步，然后在新的参数位置上再次计算梯度，从而超出了框架默认优化器仅调用一次 `get_updates`（单次 `sess.run`）的局限。

## 核心变换
将 Keras 默认的单步执行入口 `model.train_function`，使用“侵入式（注入）”手段强行覆盖重写：把原来仅被编译成一个大计算图的流程，拆解为**顺序调用的多个 `K.function` 级联**，使得系统可以完成多次“获取当前参数 -> 计算梯度 -> 部分更新”的往复动作。

## 典型步骤
1. 继承 Keras 的 `Optimizer` 基类创建自定义优化器，放弃常规的 `get_updates` 实现。
2. 提供获取分步更新列表的接口（如 `get_grouped_updates`），其中为每一小步（如探路步、微调步）定义其特定的前向计算与梯度更新。
3. 定义核心的 `inject(model)` 拦截方法：
   - 提取目标模型的输入层、目标张量和样本权重信息。
   - 使用 `K.function` 将每一小步独立编译成执行单元（如 `train_function_1`，`train_function_2`）。
4. 将原本的 `model.train_function` 封装替换为一个在调用时会按顺序执行所有独立编译函数的 Python 闭包。
5. 在用户代码中，正常 `model.compile` 后立即调用 `optimizer.inject(model)` 进行注入，然后调用 `fit` 训练即可。

## 直觉
通常的优化器就像司机闭着眼睛踩一脚油门，开一段路才睁开眼睛看位置（计算一次梯度并更新一次）；而高级的优化方法要求司机半路上睁开一次眼睛，评估一下这半路的风向，然后再决定接下来踩多深的油门（在一步之间计算二次梯度）。通过“侵入式注入”，我们给底层的执行函数开了一个“外挂”，强行拆分了原本打包在一起的自动驾驶引擎。

## 边界
这种方法非常底层，依赖于 Keras `Model` 内部 API（如 `_feed_inputs` 等下划线方法），在 Keras/TensorFlow 版本更迭时极容易失效。并且此类高阶（多步计算梯度）优化器本身通常会让每一步训练的计算量加倍，在深度学习实际运用中往往效果不如动量加速版的 SGD 或 Adam 明显，性价比低。

## 例子
实现二阶 Heun 方法时，第一次 `K.function` 求原位置梯度并前进一步到临时点，保存旧梯度；第二次 `K.function` 在临时点求新梯度，并以此对第一次步伐进行修正。结果是模型能够在一个 batch 训练中完成对复杂抛物线轨道的更好拟合。

## 证据
- ev::5879::文中详细介绍了因为 Heun 方法需两步梯度而带来的计算困境：“在第二步计算梯度...必须先在第一步将参数变为 $\tilde{p}_{i+1}$...前面的优化器定义中get_updates这个方法却只能执行一步”。
- ev::5879::给出了强行替换属性的证明：“`model.train_function = F`...其实下面的大部分代码，都是直接抄自keras的源码...也就是keras中的_make_train_function函数”。
