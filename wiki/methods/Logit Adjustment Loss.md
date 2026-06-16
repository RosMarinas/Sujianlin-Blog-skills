---
type: method
title: "Logit Adjustment Loss"
aliases:
  - "logit调整损失"
operation_types:
  primary: "Align / calibrate by invariance"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-19-通过互信息思想来缓解类别不平衡问题.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-31-再谈类别不平衡问题-调节权重与魔改Loss的对比联系.md
source_ids:
  - "7615"
  - "7708"
method_summary: "在logits中加入先验分布log p(y)项，使模型拟合互信息而非条件概率，缓解长尾分类问题。"
typical_structure: |
  1. 从训练集统计类别先验分布 p(y)
  2. 将最后一层 bias 初始化为 τ·log p(y)，或在 loss 中显式加上 τ·log p(y)
  3. Softmax 归一化后计算标准交叉熵
  4. 推理时根据目标指标选择决策规则：整体准确率用 argmax(f_y + τ·log p(y))，各类别均衡准确率用 argmax(f_y)
applicability: "长尾分布分类问题，训练集类别频率 p(y) 已知且与测试分布一致"
tools:
  - 先验分布
  - 互信息
related_methods:
  - [[Focal Loss]]
  - [[Dice Loss]]
  - [[用三角不等式指导Margin设计]]
examples:
  - [[article::7615]]
  - [[article::7708]]
status: draft
updated: 2026-06-14
---

## 适用问题

长尾分布下的单标签多分类问题。训练集中某些类别样本极少，标准交叉熵训练会导致模型忽略低频类别。该方法通过在 logits 中注入类别先验，使模型直接拟合互信息 $I(X;Y)$ 而非条件概率 $p(y|x)$，让低频类别获得与其先验频率匹配的补偿。

## 核心变换

**输入**：标准 logits $f_y(x;\theta)$ + 类别先验分布 $p(y)$
**输出**：经先验校准的损失函数

标准交叉熵建模 $p_\theta(y|x) = \text{softmax}(f_y)$，Logit Adjustment 改为建模互信息：

$$
\log \frac{p_\theta(y|x)}{p(y)} \sim f_y(x;\theta)
\quad\Rightarrow\quad
p_\theta(y|x) = \frac{e^{f_y(x;\theta) + \tau \log p(y)}}{\sum_i e^{f_i(x;\theta) + \tau \log p(i)}}
$$

对应的损失函数（$\tau=1$ 通常最优）：

$$
-\log p_\theta(y|x) = \log\left[1 + \sum_{i\neq y} \left(\frac{p(i)}{p(y)}\right)^\tau e^{f_i - f_y}\right]
$$

## 典型步骤

1. **估计先验**：从训练集统计各类别频率 $p(y)$
2. **注入偏置**：将分类层 bias 初始化为 $\tau \cdot \log p(y)$（最简单实现），或在 loss 中显式将 logits 加 $\tau \cdot \log p(y)$
3. **标准训练**：使用普通交叉熵训练，无需修改优化器或采样策略
4. **选择推理规则**：
   - 追求整体准确率 → $y^* = \arg\max_y [f_y(x) + \tau \log p(y)]$（输出条件概率最大者）
   - 追求各类别均衡准确率 → $y^* = \arg\max_y f_y(x)$（输出互信息最大者）

## 直觉

核心思想：**能靠先验解决的就靠先验，先验解决不了的本质部分才由模型学习**。

从互信息视角，$I(X;Y) = \log \frac{p(y|x)}{p(y)}$ 揭示了 $X$ 和 $Y$ 之间的本质关联，剥离了类别先验带来的偏移。标准交叉熵让模型同时学习"各类别的自然频率"和"输入与类别的本质关联"两件事，而在长尾分布下前者会主导梯度。加上 $\log p(y)$ 偏置后，模型被"告知"先验信息，可以将容量集中在学习本质关联上。

从几何视角（article 7708）：这等价于为每个类别设置与样本数相关的 margin $m_y = -\tau \log p(y)$。低频类别获得更大的 margin，使得每个稀有类样本在特征空间中"一个顶十个"，从而在类别地盘之争中不落下风。

## 边界

- 仅适用于**单标签多分类**场景；多标签问题需另用 GlobalPointer + 多标签交叉熵
- 假设训练集和测试集的类别分布相同；若分布偏移（如测试时类别频率变化），需调整或去掉 $\log p(y)$ 项
- $\tau=1$ 在多数实验中效果最优，但极端不均衡（如 $p(y) < 10^{-4}$）可能需要调小 $\tau$
- 该方法与类别加权交叉熵、Focal Loss 属于同一家族：本质上都是在调节梯度，区别在于 Logit Adjustment 在 $\log$ **之前**调权，而传统方法在 $\log$ **之后**调权

## 例子

- CIFAR-10/100-LT、ImageNet-LT、iNaturalist 等长尾基准上达到 SOTA（2020），显著优于重采样和类别加权基线
- Keras 实现：`y_pred = y_pred + tau * K.constant(np.log(prior + 1e-8))`，然后调用 `categorical_crossentropy(y_true, y_pred, from_logits=True)`
- 可与 Focal Loss、Dice Loss 等方法组合使用，进一步调节难易样本的梯度贡献

## 证据

- ev::7615::Logit Adjustment 互信息推导：从 $p(y|x) \propto e^{f_y}$ 到 $p(y|x) \propto p(y) e^{f_y}$ 的完整推导
- ev::7615::两种推理决策规则：整体准确率 vs 各类均衡准确率的 argmax 选择
- ev::7708::几何 margin 视角：$r_y = -\tau \log p(y)$ 将 Logit Adjustment 与 AM-Softmax 建立联系
- ev::7708::梯度分析：从光滑准确率到交叉熵的梯度对比，揭示魔改 loss 本质是梯度调节
