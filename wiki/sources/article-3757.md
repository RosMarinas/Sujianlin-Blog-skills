---
type: article_summary
article_id: "3757"
source_url: https://spaces.ac.cn/archives/3757
date: 2016-06-02
category: Mathematics
series: [[路径积分系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-06-02-路径积分系列-3-路径积分.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-06-02-路径积分系列-3-路径积分.md
source_ids:
  - "3757"
status: draft
updated: 2026-06-10
---

# article-3757: 路径积分系列：3.路径积分

## 文章核心问题

从随机游走问题出发，给出路径积分的一个简明而直接的介绍，展示如何将抛物型偏微分方程问题转化为路径积分形式。

## 主要结论

1. 路径积分是求偏微分方程Green函数的一种方法，只需无穷小时刻的Green函数即可构造。
2. 布朗运动的路径概率泛函为 $P[x(t)] = \exp(-\frac{1}{2\alpha}\int \dot{x}^2 dt)$，路径积分即对所有路径的该泛函求和。
3. 含势函数$V(x)$的抛物型方程 $\alpha\frac{\partial\phi}{\partial t} = \frac{\alpha^2}{2}\frac{\partial^2\phi}{\partial x^2} + V\phi$ 对应的路径积分泛函为 $K[x(t)] = \exp[-\frac{1}{\alpha}\int(\frac{1}{2}\dot{x}^2 - V(x))dt]$。
4. 路径积分与偏微分方程等价——可由偏微分方程写出路径积分，也可由路径积分推导出偏微分方程。
5. 路径积分的最可能路径问题自然地引出变分原理，$\delta S[x(t)]=0$ 给出 $\ddot{x} = -\partial V/\partial x$。
6. 二次型作用量的路径积分可精确求解，涉及van Vleck-Pauli-Morette行列式；非二次型可用微扰展开。

## 推导结构

1. **从点的概率到路径的概率**：将时间等分 → 各段概率相乘 → 取连续极限 → 布朗运动的路径概率泛函
2. **对路径进行求和**：离散化路径 → 对所有中间位置积分 → 无穷维路径积分定义
3. **抛物方程的路径积分**：含V的方程 → 无穷小时间Green函数 → 组合成路径积分
4. **从路径积分到偏微分方程**：逆向推导的等价性说明
5. **算例**：最可能路径（变分原理）、二次型作用量（精确解）、微扰展开

## 关键公式

- 布朗运动路径概率：$P[x(t)] = \exp\left(-\frac{1}{2\alpha}\int\dot{x}^2 dt\right)$ (26)
- 路径积分定义：$P(x_0,0;x_n,T) = \int_{x_0}^{x_n} \exp\left(-\frac{1}{2\alpha}\int_0^T \dot{x}^2 dt\right) \mathscr{D}x(t)$ (28)
- 含势函数的路径泛函：$K[x(t)] = \exp\left[-\frac{1}{\alpha} \int \left(\frac{1}{2}\dot{x}^2 - V(x)\right)dt\right]$ (40)
- 路径积分与传播子关系：$P(x_b,t_b;x_a,t_a) = \int_{x_a}^{x_b} \exp\left[-\frac{1}{\alpha}\int_{t_a}^{t_b}(\frac{1}{2}\dot{x}^2 - V(x))dt\right] \mathscr{D}x(t)$ (41)
- 二次型精确解：$P(b,a) = (\frac{1}{2\pi\hbar})^{D/2} \sqrt{-\det(\frac{\partial^2 S_{cl}}{\partial x_a \partial x_b})} \exp(-\frac{1}{\hbar}S_{cl})$ (46)
- 微扰展开：$P(b,a) = P_0(b,a) + (-\frac{1}{\hbar})\int P(b,c)V(c)P(c,a)d\tau_c + \dots$ (47)

## 体现的方法

- **path integral formulation** → discrete ↔ continuous bridge: 通过离散化路径再取无穷维极限构造路径积分
- **变分法** → 辅助推理: 最可能路径由一阶变分为零决定
- **微扰展开** → estimate/sample: 非精确可解路径积分的近似计算
- 该方法与 [[把优化算法解释为动力系统离散化]] 和 [[ODE直接推导法]] 共享 discrete ↔ continuous bridge 操作类型

## 所属系列位置

路径积分系列第3篇，核心概念篇，正式引入路径积分定义。

## 与其他文章的关系

- [[article-3750]]（第2篇）提供了随机游走基础，本文在此之上构造路径积分
- [[article-3762]]（第4篇）将路径积分方法扩展到随机微分方程
- [[article-3766]]（第5篇）给出路径积分在金融等领域的应用案例
- 与[[Fokker-Planck方程]]概念相关——路径积分提供了Fokker-Planck方程的Green函数构造方法

## 原文证据锚点

- ev::3757::布朗运动路径概率：公式(26)给出了路径概率泛函的形式
- ev::3757::路径积分定义：公式(28)正式定义了路径积分
- ev::3757::含势路径泛函：公式(40)给出了含势函数的路径泛函
- ev::3757::二次型精确解：公式(46)展示了可精确求解的路径积分
- ev::3757::最可能路径变分：$\delta S=0$ 导出 $\ddot{x} = -\partial V/\partial x$
