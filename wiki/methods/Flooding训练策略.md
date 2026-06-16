---
type: method
title: "Flooding训练策略"
aliases:
  - "洪泛训练"
  - "Flooding"
operation_types:
  primary: "Discrete / continuous bridge"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-31-我们真的需要把训练集的损失降低到零吗.md
source_ids:
  - "7643"
method_summary: "损失函数降到阈值b后改为|L(theta)-b|+b，交替梯度下降和上升，等效于梯度惩罚正则化。"
typical_structure: |
  1. 设定阈值b
  2. L(theta)>b时正常梯度下降
  3. L(theta)<b时变为梯度上升
  4. 等效于最小化||grad L(theta)||^2
applicability: "提高模型泛化性，防止过拟合"
tools:
  - 阈值b
  - 梯度惩罚
related_methods: []
examples:
  - [[article::7643]]
status: draft
updated: 2026-06-13
---

## 适用问题

提高神经网络泛化能力，防止过拟合。当训练损失已经降至较低水平时，通过交替梯度下降和梯度上升推动参数走向更平滑的区域。

## 核心变换

**输入**：原始损失函数 $\mathcal{L}(\theta)$
**输出**：修改后的损失函数 $\tilde{\mathcal{L}}(\theta)$

$$
\tilde{\mathcal{L}}(\theta)=|\mathcal{L}(\theta) - b|+b
$$

其中$b$为预设阈值。当$\mathcal{L}(\theta) > b$时，$\tilde{\mathcal{L}}(\theta)=\mathcal{L}(\theta)$，执行标准梯度下降；当$\mathcal{L}(\theta) < b$时，$\tilde{\mathcal{L}}(\theta)=2b-\mathcal{L}(\theta)$，损失变号，执行梯度上升。

## 典型步骤

1. **设定阈值$b$**：根据验证集调整，通常设为略低于期望的最终训练损失
2. **修改损失函数**：在原有损失$\mathcal{L}(\theta)$上加`loss = abs(loss - b) + b`
3. **正常训练**：当损失高于$b$时梯度下降；低于$b$时自动切换为梯度上升
4. **观察验证集**：监视验证集损失是否出现"二次下降"（double descent）现象
5. **调整$b$**：根据验证集性能微调阈值（实验表明对$b$的选择较为鲁棒）

## 直觉

当训练损失低于阈值后，交替梯度下降和梯度上升的净效果等价于最小化梯度范数$\|\nabla_\theta \mathcal{L}(\theta)\|^2$（学习率为$\varepsilon^2/2$）。推导如下：
$$
\theta_{n+1} \approx \theta_{n-1} - \frac{\varepsilon^2}{2}\nabla_\theta\|\nabla_\theta \mathcal{L}(\theta_{n-1})\|^2
$$
推动参数走向"平坦"区域——即损失函数曲面的底部尽量平滑的地方。平坦极小值通常具有更好的泛化性能（对参数扰动更不敏感），与添加随机噪声、对抗训练的本质一致。

## 边界

- $b$需要根据验证集调整，虽然实验表明较鲁棒，但选择不当（过高或过低）仍会损害性能
- Flooding不会在所有任务上都有提升，效果因数据集和模型而异
- 等价于在损失足够低后增加梯度惩罚正则化，与直接加梯度惩罚相比不一定更优
- 交替训练策略有更通用的形式（$\varepsilon_1 > \varepsilon_2$的不对称学习率），但经验上不如直接加梯度惩罚

## 例子

- 原论文实验：在多个图像/NLP任务上，Flooding使验证集损失出现"二次下降"，最终效果优于不加Flooding的基线
- 实现只需一行代码：`loss = K.abs(loss - b) + b`（Keras后端）
- 与梯度惩罚、对抗训练等正则化技术有深层联系，可组合使用

## 证据

- ev::7643::Flooding损失函数定义：$\tilde{\mathcal{L}}(\theta)=|\mathcal{L}(\theta)-b|+b$，低于阈值后梯度上升
- ev::7643::梯度范数推导：交替升降的净效果等价于最小化$\|\nabla_\theta \mathcal{L}(\theta)\|^2$
- ev::7643::二次下降现象：验证集损失在Flooding后出现double descent
