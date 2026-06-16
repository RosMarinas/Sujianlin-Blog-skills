---
type: method
title: 动态残差缩放稳定收敛法
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-21-RoFormerV2-自然语言理解的极限探索.md
source_ids:
  - "8998"
method_summary: 通过在残差分支的加法合并前引入一个动态更新的标量系数 $\alpha$，在预训练初始阶段将其设为 0，使模型主要由恒等映射主导以稳定反向梯度流，随后随着训练进度的推进线性缓慢增加至 1.0，从而成功解决超深 Post-Norm 架构模型在不使用 Warmup 调度下无法收敛的难题。
typical_structure: |
  1. 在层连接中设计带权残差：$\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + \alpha F(\boldsymbol{x}_t))$
  2. 声明 $\alpha$ 为一个依赖于训练迭代步数（step）的标量系数：$\alpha(step) = \min(1.0, \frac{step}{warmup\_steps})$
  3. 在模型预训练最初的数千步内，$\alpha$ 由 0 缓慢且线性地增长到 1.0
  4. 当 $\alpha$ 达到 1.0 后，在后续训练中保持为 1.0，使网络完全恢复为标准的 Post-Norm 计算方式
applicability: 在构建超深或精简版 Post-Norm Transformer 神经网络进行从零开始的大规模无监督预训练时，当遇到因底层梯度不平衡导致模型初始化极难收敛、不加学习率 Warmup 就会直接出现 Loss 溢出或梯度爆炸时激活此方法。
tools:
  - 动态残差缩放
  - Post-Norm 稳定训练
related_methods:
  - [[ReZero]]
  - [[DeepNet]]
  - [[Pre-Norm vs Post-Norm 收敛难度分析]]
examples:
  - [[article::8998]]
status: draft
updated: 2026-06-14
---

## 适用问题

超深 Post-Norm Transformer（如 RoFormerV2）在从零开始大规模预训练时，底层梯度由于残差路径上的多层累积而极度不平衡，导致模型不借助学习率 Warmup 就无法收敛，直接出现 Loss 溢出或梯度爆炸。该方法专为此类场景设计，在不引入额外网络模块的前提下，通过动态残差缩放稳定训练过程。

## 核心变换

**输入**：Post-Norm 残差连接 $\boldsymbol{x}_{t} + F(\boldsymbol{x}_{t})$
**输出**：带动态系数的残差连接 $\boldsymbol{x}_{t} + \alpha F(\boldsymbol{x}_{t})$
**参数**：标量系数 $\alpha$，其值随训练步数变化

标准 Post-Norm 残差连接：
$$
\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + F(\boldsymbol{x}_t))
$$

动态残差缩放引入系数 $\alpha$：
$$
\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + \alpha F(\boldsymbol{x}_t))
$$

$\alpha$ 的调度策略（线性 warmup）：
$$
\alpha(step) = \min\left(1.0, \frac{step}{warmup\_steps}\right)
$$

在训练初始阶段 $\alpha = 0$，残差路径退化为纯恒等映射 $\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t)$，梯度可直接无损地回传到底层。随着训练进行，$\alpha$ 线性增长到 1，模型逐渐恢复完整的 Post-Norm 表达能力。

## 典型步骤

1. **定义 $\alpha$ 调度器**：将 $\alpha$ 声明为依赖于训练迭代步数的标量，预热步数 $warmup\_steps$ 通常设为数千步
2. **改造残差连接**：在每一层中，将标准残差加法 $\boldsymbol{x}_t + F(\boldsymbol{x}_t)$ 替换为 $\boldsymbol{x}_t + \alpha F(\boldsymbol{x}_t)$
3. **正常训练**：使用标准优化器训练，$\alpha$ 从 0 开始线性增长
4. **恢复标准结构**：当 $\alpha$ 达到 1.0 后，网络完全恢复为标准 Post-Norm 计算方式，此后的训练行为与普通 Post-Norm 一致

## 直觉

核心思想：**先让梯度畅通无阻，再逐步激活变换能力**。

深层 Post-Norm 难以收敛的本质原因是：多层残差叠加后，底层参数的梯度需要穿越多个非线性变换层，信号在回传过程中极易爆炸或消失。将残差分支权重 $\alpha$ 从 0 开始，意味着模型初始状态下完全跳过所有子层变换，梯度通过恒等映射直达底层。由于恒等映射的雅可比是单位矩阵，梯度在各层间无损传播。随着训练进行，$\alpha$ 缓慢增加，变换分支逐渐介入，但此时底层参数已经初步适应，不会因大幅度梯度变化而崩溃。

这种方法比 ReZero 更为优雅：ReZero 使用可学习的零初始化标量，而动态残差缩放使用确定的调度策略，无需引入额外的可学习参数，且在实验中被证明效果更优。

## 边界

- 仅适用于 **Post-Norm** 架构；Pre-Norm 本身已有稳定的梯度路径，无需此方法
- $\alpha$ 的预热步数需要根据模型深度和总训练步数调参，过短会丧失稳定性优势，过长会延迟模型收敛
- 该方法不能完全替代学习率 Warmup，但在不依赖学习率 Warmup 的情况下也能稳定训练，提供了额外的收敛保障
- 与 DeepNet 相比，该方法不改变初始化方式，更轻量但效果略逊于 DeepNet 的初始化缩放

## 例子

- RoFormerV2 使用该技术，在去除所有 Bias 和简化 Layer Norm 后仍能稳定训练，训练吞吐量提升 1.2x~1.3x
- 超深 Post-Norm 模型（24 层以上）在 $\alpha$ 调度下，可在无 Warmup 情况下成功收敛，实验表明梯度回传的方差显著降低

## 证据

- ev::8998::动态残差缩放公式：$\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + \alpha F(\boldsymbol{x}_t))$，$\alpha$ 从 0 线性递增到 1
- ev::8998::与 ReZero 的对比实验：动态残差缩放效果更优，且无需引入额外的可学习参数
- ev::8998::RoFormerV2 中的应用：去除 Bias + 简化 Layer Norm 后使用该方法成功稳定训练
