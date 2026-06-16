---
type: article_summary
article_id: "3750"
source_url: https://spaces.ac.cn/archives/3750
date: 2016-05-30
category: Mathematics
series: [[路径积分系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-05-30-路径积分系列-2-随机游走模型.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-05-30-路径积分系列-2-随机游走模型.md
source_ids:
  - "3750"
status: draft
updated: 2026-06-10
---

# article-3750: 路径积分系列：2.随机游走模型

## 文章核心问题

建立对称和非对称随机游走模型，推导其概率分布和对应的偏微分方程，提出通过随机游走模拟求解偏微分方程的数值方法。

## 主要结论

1. 对称随机游走取连续极限后得到扩散方程 $\frac{\partial P}{\partial t} = \frac{\alpha}{2} \frac{\partial^2 P}{\partial x^2}$，概率分布为正态分布 $P(x,t) = \frac{1}{\sqrt{2\pi\alpha t}}\exp(-\frac{x^2}{2\alpha t})$。
2. 非对称随机游走（有偏随机游走）对应的偏微分方程为 $\frac{\partial P}{\partial t} = \frac{\alpha}{2}\frac{\partial^2 P}{\partial x^2} - \frac{\partial}{\partial x}(pP)$，其中$p(x,t)$表示偏移速度。
3. 通过变换 $P(x,t)=\phi(x,t)\xi(x,t)$ 可消去一阶偏导项，得到与量子力学薛定谔方程类似的形式 $\alpha\frac{\partial\phi}{\partial t} = \frac{\alpha^2}{2}\frac{\partial^2\phi}{\partial x^2} + V\phi$。
4. 随机游走容易通过计算机模拟，因此可以作为一种求解偏微分方程的数值方法。

## 推导结构

1. **对称随机游走**：走格子模型 → 母函数法 → 傅里叶变换 → 连续极限 → 扩散方程
2. **非对称随机游走**：引入位置依赖的非对称概率 → 母函数近似 → 傅里叶变换 → Fokker-Planck型方程（含 drift 项）
3. **简化形式**：变量代换 $P = \phi\xi$ → 消去一阶偏导 → 薛定谔型方程
4. **计算机模拟**：利用随机游走模拟求解偏微分方程

## 关键公式

- 对称随机游走的概率分布：$P(x,t) = \frac{1}{\sqrt{2\pi \alpha t}}\exp\left(-\frac{x^2}{2\alpha t}\right)$ (7)
- 非对称随机游走的偏微分方程：$\frac{\partial P}{\partial t} = \frac{\alpha}{2}\frac{\partial^2 P}{\partial x^2} - \frac{\partial}{\partial x}(pP)$ (12)
- 简化后的薛定谔型方程：$\alpha\frac{\partial \phi}{\partial t} = \frac{\alpha^2}{2}\frac{\partial^2 \phi}{\partial x^2} + V\phi$ (19)，其中 $V = -\frac{1}{2}(\alpha\frac{\partial p}{\partial x} + p^2) - \int\frac{\partial p}{\partial t}dx$

## 体现的方法

- **random walk → diffusion limit** → discrete ↔ continuous bridge: 通过取 $\Delta t,\Delta s\to 0$ 且 $\Delta s^2 = \alpha\Delta t$ 的极限，将离散随机游走转化为连续扩散方程
- **Fourier transform method** → rewrite / identity transform: 利用傅里叶变换将母函数转化为概率分布
- 该方法与 [[把优化算法解释为动力系统离散化]] 共享 discrete ↔ continuous bridge 操作类型——都是将离散过程取连续极限得到连续方程

## 所属系列位置

路径积分系列第2篇，为后续路径积分和SDE的讨论奠定随机游走基础。

## 与其他文章的关系

- [[article-3749]]（第1篇）概述本文的框架位置
- [[article-3757]]（第3篇）从随机游走路径概率出发构建路径积分
- [[article-3762]]（第4篇）证明随机微分方程与非对称随机游走模型的等价性
- 与系列[[从动力学角度看优化算法]]中的 [[SGD-SDE近似]] 共享"离散→连续"的极限方法；与 [[把优化算法解释为动力系统离散化]] 共享相同的操作类型

## 原文证据锚点

- ev::3750::对称随机游走分布：公式(7)给出了对称随机游走的正态分布结果
- ev::3750::非对称随机游走方程：公式(12)给出了非对称随机游走的Fokker-Planck型方程
- ev::3750::简化形式：公式(19)将方程化简为薛定谔型
- ev::3750::连续极限条件：$\Delta s^2 = \alpha \Delta t, \Delta t \to 0$ 是离散→连续的关键标度关系
