---
type: proposition
title: SquarePlus凸性与恒大于条件
aliases:
  - SquarePlus convexity
  - SquarePlus dominance over SoftPlus
statement: SquarePlus 函数 $\text{SquarePlus}(x) = (x + \sqrt{x^2+b})/2$ 是凸函数（二阶导数恒正），当且仅当 $b \geq 4\log^2 2$ 时恒大于 SoftPlus（即 $\text{SquarePlus}(x) \geq \text{SoftPlus}(x)$）。
assumptions:
  - "$b > 0$"
  - "$x \in \mathbb{R}$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-29-SquarePlus-可能是运算最简单的ReLU光滑近似.md
source_ids:
  - "8833"
requires:
  - "formula::SquarePlus公式"
proof_route: |
  凸性：$\frac{d^2}{dx^2}\text{SquarePlus}(x) = b/[2(x^2+b)^{3/2}] > 0$。恒大于条件：由不等式 $\text{SquarePlus}(x) \geq \text{SoftPlus}(x)$ 推导出 $b \geq 4\log(e^x+1)\log(e^{-x}+1)$，右端最大值在 $x=0$ 处取值为 $4\log^2 2$，通过 $\log\log(e^x+1)$ 的凹性和詹森不等式证明。
methods: []
limits: 恒大于条件保证SquarePlus处处不小于SoftPlus，但最小化误差时最优参数 $b \approx 1.5238$ 并不满足此条件。
examples:
  - "example::SquarePlus最佳参数逼近SoftPlus"
evidence_spans: []
status: draft
updated: 2026-06-12
---

## 命题

SquarePlus函数 $\text{SquarePlus}(x) = (x + \sqrt{x^2+b})/2$ 是严格凸函数，其二阶导数处处为正：
$$
\frac{d^2}{dx^2}\text{SquarePlus}(x) = \frac{b}{2(x^2+b)^{3/2}} > 0
$$

SquarePlus恒大于等于SoftPlus的充要条件是参数 $b \geq 4\log^2 2$：
$$
\text{SquarePlus}(x) \geq \text{SoftPlus}(x) \iff b \geq 4\log^2 2
$$

恒大于条件的证明利用了 $\log(e^x+1)\log(e^{-x}+1)$ 在 $x=0$ 处取得最大值 $4\log^2 2$ 的性质，通过函数凹性和Jensen不等式完成。值得注意的是，最小化L2逼近误差的最优参数 $b \approx 1.5238$ 并不满足此条件，说明"总体最佳近似"与"处处更优"是不同的设计目标。
