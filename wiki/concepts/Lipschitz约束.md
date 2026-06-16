---
type: concept
title: Lipschitz约束
aliases: '["Lipschitz constraint", "L约束"]'
definition: 函数变化率的约束：存在常数C使得||f(x1)-f(x2)|| <= C||x1-x2||对所有x1,x2成立
standard_notation: '||f||_L, ||f(x1)-f(x2)|| <= C||x1-x2||'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
- Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
source_ids:
- '['
- '"'
- '6'
- '0'
- '5'
- '1'
- '"'
- ','
- '"'
- '8'
- '7'
- '5'
- '7'
- '"'
- ']'
related_methods: '[["谱归一化满足L约束"], ["梯度惩罚满足L约束"], ["梯度归一化满足L约束"]]'
related_formulas: '[["谱范数公式"]]'
evidence_spans: '[]'
series: '[]'
status: draft
updated: '2026-06-12'
---

# Lipschitz约束

## 定义

函数变化率的约束：存在常数C使得||f(x1)-f(x2)|| <= C||x1-x2||对所有x1,x2成立

## 激活场景

源文把 Lipschitz 约束解释为控制模型对输入扰动的敏感性：当 $\Vert x_1-x_2\Vert$ 很小时，也希望 $\Vert f_w(x_1)-f_w(x_2)\Vert$ 尽可能小。若存在只依赖参数、不依赖输入的常数 $C(w)$ 使不等式恒成立，就说明模型变化被一个线性上界控制住；$C$ 越小，模型对扰动越不敏感，通常更利于泛化。

## 关键关系

在 WGAN 中，Lipschitz 约束不只是正则偏好，而是目标定义的一部分。源文给出 WGAN 判别器的约束形式 $|f|_L=1$ 或 $\Vert D\Vert_L\le 1$，并讨论参数裁剪、梯度惩罚、谱归一化和梯度归一化等实现方式。梯度惩罚通过惩罚 $\Vert f'(x)\Vert$ 的偏离近似施加约束；谱归一化则通过控制每层参数的谱范数来构造满足有界 L 常数的网络。

## 标准符号

||f||_L, ||f(x1)-f(x2)|| <= C||x1-x2||

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md`
