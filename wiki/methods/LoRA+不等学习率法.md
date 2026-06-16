---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: LoRA+不等学习率法
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-02-27-配置不同的学习率-LoRA还能再涨一点.md
  - Data/wiki/sources/spaces-10001-配置不同的学习率-LoRA还能再涨一点.md
  - Data/wiki/sources/spaces-10226-对齐全量微调-这是我看过最精彩的LoRA改进-一.md
  - Data/wiki/sources/spaces-10266-对齐全量微调-这是我看过最精彩的LoRA改进-二.md
  - Data/wiki/sources/spaces-9590-梯度视角下的LoRA-简介-分析-猜测及推广.md
source_ids:
  - 10001
method_summary: 基于网络层初始化的数值稳定性与梯度贡献度理论分析，通过对 LoRA 的降维矩阵 A 和升维矩阵 B 分配不等比例的学习率（B 远大于 A），优化模型训练的收敛速度和效果。
typical_structure: |
  1. 获取原全连接层的维度 $n \times m$ 以及 LoRA 的秩参数 $r$。
  2. 使用常规方法初始化矩阵 A（方差为 $1/n$）和矩阵 B（方差为 $1/r$ 或全零）。
  3. 配置参数分组，将矩阵 B 分配较大的学习率 $\eta_B$，将矩阵 A 分配较小的学习率 $\eta_A$。
  4. 推荐保持最优学习率比例 $\eta_B / \eta_A \approx \mathcal{O}(\sqrt{n})$。
applicability: 利用 LoRA 方法对大型预训练模型（如 LLM）进行参数高效微调，并希望突破默认对称优化配置带来的性能瓶颈时。
examples:
  - [[article::10001]]
status: stable
updated: 2026-06-13
source_id: 10001
tags: 
evidence_spans:
  - ev::10001::文章给出了结论推导：“为了使得 $\Delta \mathcal{L}_A$ 与 $\Delta \mathcal{L}_B$ 的大小相当，那么应该有近似... $\frac{\eta_B}{\eta_A} = \mathcal{O}(\sqrt{n})$”。
---




# LoRA+不等学习率法

## 适用问题
在基于 LoRA (Low-Rank Adaptation) 方法对大型深度学习模型进行微调时，希望通过修正默认的“对称等价配置”（即对 A 和 B 使用相同的超参数优化）来挖掘进一步提升收敛指标的潜力。

## 核心变换
在优化器参数更新逻辑中，不将 $A, B$ 两个小矩阵一视同仁，而是强行引入**学习率阶层差异**（$B$ 的学习率 $\eta_B$ 显著高于 $A$ 的学习率 $\eta_A$），这源于它们在矩阵连乘分解中的不对称几何地位。

## 典型步骤
1. 定义微调层结构，其中 $W = W_0 + AB$（其中 $A \in \mathbb{R}^{n \times r}, B \in \mathbb{R}^{r \times m}$）。
2. 为了数值稳定性与方差一致性，将矩阵 A 的初始化方差设定为 $1/n$，B 设置为 $1/r$（实际中即便 B 为了恒等性被设为全零，这种内在属性也依旧发挥作用）。
3. 分拆模型参数为多组供优化器调用。
4. 为包含 $A$ 矩阵参数的分组绑定基础学习率 $\eta_A$。
5. 为包含 $B$ 矩阵参数的分组绑定增幅学习率 $\eta_B$，通常遵循推荐值 $\frac{\eta_B}{\eta_A} \approx 2^4 = 16$ （约为 $\mathcal{O}(\sqrt{n})$ 量级）。
6. 用标准的优化算法（如 AdamW）在异构学习率下启动训练。

## 直觉
由于 LoRA 的中间维度 $r \ll n$，矩阵 $A$ 从 $n$ 维投影到极小的 $r$ 维时，就像一个极其宽大的漏斗，导致 $A$ 矩阵的单点微小变化，乘过网络后就会产生巨变（敏感）。相反，矩阵 $B$ 只是把极小维度 $r$ 变回 $m$ 维，对输出的影响比较平滑。为了让这对组合在降低损失这件工作上“贡献出相等的力气”（而不是让 $A$ 一个人拼死微调，$B$ 磨洋工），我们需要给对输出影响迟缓的 $B$ 赋予更大的学习速度（步伐跨度大），给超级敏感的 $A$ 赋予极小的学习速度，从而取得最佳的协调同步。

## 边界
这套理论依据“前向网络每一层输出方差应该不变的数值稳定原则”与“SignSGD 两矩阵贡献对等原则”粗略推演而得，因此实际工程中，最优倍率仍会在 $\mathcal{O}(\sqrt{n})$ 周围随具体任务有所震荡，并不是绝对刚性的公式常数；同时，该调优虽然理论优美，但在极大的数据量微调下其相比良好 Tuning 过超参的标准 LoRA 的绝对提升往往只是零点几个百分点的“锦上添花”。

## 例子
对于一个 $n=768$，$r=8$ 的网络，在优化器配置时，如果 A 设置学习率 `5e-5`，那么应当把 B 的学习率设置为 `8e-4` (即 $16 \times \text{5e-5}$)。实验证明在这个配置下，测试集的 Perplexity（困惑度）比 A,B 都为 `5e-5` 时下降得更多更快。

## 证据
- ev::10001::详细阐明了原因在于打破对称性：“A,B 表面上是对称的，但实际上它们有着固有的不对称性...不管选择 A 还是 B 来全零初始化，结论都是 B 的学习率要大于 A”。
- ev::10001::展示了基于方差与梯度的定性推演：“为了 $\Delta \mathcal{L}_A$ 与 $\Delta \mathcal{L}_B$ 的大小相当，那么应该有近似... $\frac{\eta_B}{\eta_A} \approx \frac{n}{m}\sqrt{\frac{n}{r}}$”。
