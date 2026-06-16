---
type: method
title: "Focal Loss损失函数"
aliases:
  - "Focal Loss"
operation_types:
  primary: "Discrete / continuous bridge"
  secondary:
    - "Generalize from special cases"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-12-25-从loss的硬截断-软化到focal-loss.md
source_ids:
  - "4733"
method_summary: "通过(1-y_hat)^gamma调节因子降低易分类样本的loss贡献，使模型聚焦于难分类样本。"
typical_structure: |
  1. 标准交叉熵损失
  2. 添加(1-y_hat)^gamma调制因子
  3. 可选alpha平衡权重
applicability: "类别不平衡的分类任务，目标检测，NLP序列标注"
tools:
  - 调制因子gamma
  - 平衡权重alpha
related_methods: []
examples:
  - [[article::4733]]
status: draft
updated: 2026-06-13
---

## 适用问题

类别不平衡的分类任务，即某些类别样本远少于其他类别。常见于目标检测（前景vs背景）、NLP序列标注（实体vs非实体）等场景。

## 核心变换

**输入**：标准交叉熵损失 $L_{ce} = -y\log \hat{y} - (1-y)\log(1-\hat{y})$
**输出**：调制后的Focal Loss $L_{fl}$

$$
L_{fl} = \begin{cases}
-(1-\hat{y})^\gamma \log \hat{y}, & y=1 \\
-\hat{y}^\gamma \log(1-\hat{y}), & y=0
\end{cases}
$$

其中$\gamma \geq 0$为调制因子（典型值$\gamma=2$）。可选加入类别平衡权重$\alpha$：
$$
L_{fl} = \begin{cases}
-\alpha(1-\hat{y})^\gamma \log \hat{y}, & y=1 \\
-(1-\alpha)\hat{y}^\gamma \log(1-\hat{y}), & y=0
\end{cases}
$$

## 典型步骤

1. **选择$\gamma$**：通常设为2。$\gamma=0$退化为标准交叉熵
2. **添加调制因子**：在交叉熵基础上乘以$(1-\hat{y})^\gamma$（正样本）或$\hat{y}^\gamma$（负样本）
3. **（可选）加$\alpha$平衡**：为少数类别增加权重（经验值$\alpha=0.25$，$\gamma=2$）
4. **训练**：标准梯度下降，调制因子自动降低易分类样本的梯度贡献

## 直觉

Focal Loss的核心思想是"聚焦于难样本"。对正样本而言，当$\hat{y}$接近1（易分类）时，$(1-\hat{y})^\gamma$接近0，loss权重极小；当$\hat{y}$很小（难分类）时，$(1-\hat{y})^\gamma$接近1，loss权重保留。从平滑化的视角看，Focal Loss等价于从"硬截断"loss（只更新预测错误的样本）经过sigmoid光滑化后的结果。当$\hat{y}=\sigma(x)$时，Focal Loss可写为：
$$
L_{fl} = -\sigma^\gamma(-x)\log\sigma(x) \quad (y=1)
$$
与"阶跃函数→sigmoid"的软化路径一致（$K=\gamma$时两者等价）。

## 边界

- $\gamma$和$\alpha$相互影响，需联合调参。Kaiming团队推荐$\alpha=0.25,\gamma=2$（在其目标检测任务上）
- Focal Loss不能完全替代重采样等类别不平衡处理方法，某些场景下需组合使用
- 多分类版本：$L_{fl} = -(1-\hat{y}_t)^\gamma \log \hat{y}_t$，其中$\hat{y}_t$为目标类别的softmax输出
- 调制因子本质上是在调节梯度贡献，与类别加权交叉熵属于同一家族（区别在于调权位置不同）

## 例子

- 目标检测：RetinaNet使用Focal Loss解决正负样本极度不平衡（1:1000+），达到单阶段检测器SOTA
- 命名实体识别：基于序列标注的NER中实体与非实体比例严重失衡，Focal Loss可带来微小提升
- 二分类中调制因子的梯度分析：易分正样本（$\hat{y}\to 1$）的梯度几乎为0，难分正样本（$\hat{y}\to 0$）保留完整梯度

## 证据

- ev::4733::Focal Loss定义：$(1-\hat{y})^\gamma$调制因子在二分类交叉熵上的应用
- ev::4733::硬截断→软化→Focal Loss推导：从$\theta(0.5-\hat{y})$阶跃函数到$\sigma(-Kx)$光滑化的完整推理链
- ev::4733::Focal Loss与软化loss的等价性：$K=\gamma=1$时两者完全等价
- ev::4733::多分类推广：$L_{fl}=-(1-\hat{y}_t)^\gamma\log\hat{y}_t$，基于softmax输出
