---
type: concept
title: LoRA
definition: "一种参数高效微调方法，通过将预训练权重矩阵的更新量分解为两个低秩矩阵的乘积，从而在微调期间仅训练少量的低秩旁路参数。"
sources:
  - wiki/sources/spaces-10226-对齐全量微调-这是我看过最精彩的LoRA改进-一.md
  - wiki/sources/spaces-10266-对齐全量微调-这是我看过最精彩的LoRA改进-二.md
  - wiki/sources/spaces-10001-配置不同的学习率-LoRA还能再涨一点.md
  - wiki/sources/spaces-9590-梯度视角下的LoRA-简介-分析-猜测及推广.md
source_ids:
  - "10226"
  - "10266"
  - "10001"
  - "9590"
status: draft
updated: 2026-06-12
---
# LoRA (Low-Rank Adaptation)

## Definition

低秩适应（Low-Rank Adaptation, LoRA）是一种参数高效微调（PEFT）技术。它通过冻结预训练模型的权重矩阵 $\boldsymbol{W}_0 \in \mathbb{R}^{d \times k}$，并引入两个低秩矩阵的乘积来近似权重的更新量 $\Delta \boldsymbol{W} = \boldsymbol{B}\boldsymbol{A}$，其中 $\boldsymbol{B} \in \mathbb{R}^{d \times r}$ 且 $\boldsymbol{A} \in \mathbb{R}^{r \times k}$，秩 $r \ll \min(d, k)$。

## Mathematical Formulation

对于输入 $\boldsymbol{x}$，模型的前向传播修改为：
$$
\boldsymbol{h} = \boldsymbol{W}_0\boldsymbol{x} + \Delta\boldsymbol{W}\boldsymbol{x} = \boldsymbol{W}_0\boldsymbol{x} + \frac{\alpha}{r}\boldsymbol{B}\boldsymbol{A}\boldsymbol{x}
$$
其中：
- $\boldsymbol{A}$ 通常使用高斯随机初始化 $\mathcal{N}(0, \sigma^2)$，$\boldsymbol{B}$ 初始化为 $0$，从而保证在训练开始时 $\Delta\boldsymbol{W} = 0$。
- $\alpha$ 是一个常数缩放因子，用于调整低秩适配器输出的权重。

## Optimization and Learning Rates

1. **LoRA+ (不等学习率)**：研究表明，在使用极大初始学习率时，$\boldsymbol{A}$ 和 $\boldsymbol{B}$ 的特征流是不对称的。为优化信息流动，LoRA+ 建议对矩阵 $\boldsymbol{B}$ 设置比矩阵 $\boldsymbol{A}$ 更高的学习率（即 $\eta_B / \eta_A = \gamma > 1$）。
2. **LoRA-GA (梯度近似)**：通过优化初始梯度方向来对齐全量微调的初始状态。
3. **LoRA-Pro**：在微调期间优化参数的投影。

## References

- 苏剑林. "对齐全量微调：这是我看过最精彩的LoRA改进（一）". 科学空间, 2024. [spaces-10226]
- 苏剑林. "对齐全量微调：这是我看过最精彩的LoRA改进（二）". 科学空间, 2024. [spaces-10266]
- 苏剑林. "配置不同的学习率，LoRA还能再涨一点". 科学空间, 2023. [spaces-10001]
- 苏剑林. "梯度视角下的LoRA：简介、分析、猜测及推广". 科学空间, 2023. [spaces-9590]
