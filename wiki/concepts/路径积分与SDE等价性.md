---
type: concept
title: 路径积分与SDE等价性
aliases:
- Path Integral and SDE Equivalence
- SDE Path Integral Equivalence
definition: 随机微分方程 $dx(t) = p(x,t)dt + \sqrt{\alpha}dW_t$ 与不对称随机游走模型在路径积分意义下完全等价——两者的路径概率泛函和对应的偏微分方程完全相同，路径积分是实现三者相互转化的纽带。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-4-随机微分方程.md
source_ids:
- '3762'
prerequisites:
- 路径积分
- 随机游走扩散极限
- 布朗运动路径概率
equivalent_forms:
- 不对称随机游走的Fokker-Planck方程 $\frac{\partial P}{\partial t} = \frac{\alpha}{2}\frac{\partial^2
  P}{\partial x^2} - \frac{\partial}{\partial x}(pP)$
- 路径概率泛函 $P[x(t)] = \exp\left[-\frac{1}{\alpha}\int(\frac{1}{2}\dot{x}^2-V)dt\right]\exp\left(\frac{1}{\alpha}\int_{x_a}^{x_b}pdx\right)$
direct_consequences:
- SDE ↔ PDE转化
- 量子金融
related_formulas:
- V(x,t) = -\frac{1}{2}(\alpha\frac{\partial p}{\partial x}+p^2)-\int\frac{\partial
  p}{\partial t}dx
- \mathcal{J}[x(t)] = \exp\left(-\frac{1}{2}\int\frac{\partial p}{\partial x}dt\right)  (雅可比行列式)
related_methods:
- '[[把优化算法解释为动力系统离散化]]'
- '[[Fokker-Planck方程推导法]]'
series:
- '[[路径积分系列]]'
evidence_spans:
- ev::3762::等价性结论
- ev::3762::非线性雅可比行列式
- ev::3762::SDE路径泛函
status: draft
updated: '2026-06-12'
---

# 路径积分与SDE等价性

## 定义

随机微分方程 $dx(t) = p(x,t)dt + \sqrt{\alpha}dW_t$ 与不对称随机游走模型在路径积分意义下完全等价——两者的路径概率泛函和对应的偏微分方程完全相同。

## 等价性证明

1. 从SDE出发，将路径积分测度从Wiener过程变换到$x(t)$过程：
   $P[x(t)]\mathscr{D}x(t) = P[W(t)]\mathscr{D}W(t)$
2. 代入布朗运动路径概率，用SDE将$\dot{W}$表达为$\dot{x}$和$p$：
   $\exp\left(-\frac{1}{2\alpha}\int[\dot{x}-p(x,t)]^2 dt\right)$
3. 计算测度变换的雅可比行列式：
   $\mathcal{J}[x(t)] = \exp\left(-\frac{1}{2}\int\frac{\partial p}{\partial x}dt\right)$
4. 组合得到路径概率泛函，与不对称随机游走的结果完全一致。

## 意义

这一等价性意味着SDE、随机游走和抛物型PDE三者可以通过路径积分相互转化。这为实际应用提供了多种视角和工具：
- 从离散随机游走模拟SDE（数值方法）
- 从SDE直接写出等价的PDE（分析方法）
- 从路径积分进行理论分析（解析方法）