---
type: article_summary
article_id: "3762"
source_url: https://spaces.ac.cn/archives/3762
date: 2016-06-09
category: Mathematics
series: [[路径积分系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-4-随机微分方程.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-4-随机微分方程.md
source_ids:
  - "3762"
status: draft
updated: 2026-06-10
---

# article-3762: 路径积分系列：4.随机微分方程

## 文章核心问题

将路径积分方法应用于随机微分方程（SDE），建立SDE与不对称随机游走模型之间的等价性，实现随机游走、SDE和抛物型偏微分方程三者的相互转化。

## 主要结论

1. 线性SDE $dx(t) = x(t)dt + \sqrt{\alpha}dW_t$ 可通过布朗运动的路径概率泛函和变量代换直接构造路径积分，线性变换的雅可比行列式为常数。
2. 非线性SDE $dx(t) = p(x(t),t)dt + \sqrt{\alpha}dW_t$ 的路径积分需要计算从Wiener过程到$x(t)$的雅可比行列式，结果为 $\mathcal{J}[x(t)] = \exp\left(-\frac{1}{2}\int\frac{\partial p}{\partial x}dt\right)$。
3. 非线性SDE的路径概率泛函为：
   $$P[x(t)] = \exp\left[-\frac{1}{\alpha}\int\left(\frac{1}{2}\dot{x}^2 - V(x,t)\right)dt\right]\exp\left(\frac{1}{\alpha}\int_{x_a}^{x_b}p(x,t)dx\right)$$
   其中 $V(x,t) = -\frac{1}{2}(\alpha\frac{\partial p}{\partial x} + p^2) - \int\frac{\partial p}{\partial t}dx$。
4. **核心等价性**：随机微分方程 $dx(t) = p(x,t)dt + \sqrt{\alpha}dW_t$ 与不对称随机游走模型的结果完全一致——两者的路径积分泛函完全相同，对应的偏微分方程也完全相同（公式(12)）。
5. 路径积分是实现随机游走、SDE、偏微分方程三者相互转化的纽带。

## 推导结构

1. **线性SDE**：写出SDE → 由布朗运动路径泛函 + 变量代换 → 路径概率泛函 → 高斯型路径积分精确求解
2. **非线性SDE雅可比行列式**：离散化SDE → 计算有限维雅可比矩阵 → 取连续极限 → $\mathcal{J} = \exp(-\frac{1}{2}\int\frac{\partial p}{\partial x}dt)$
3. **路径概率泛函**：组合布朗运动泛函和雅可比行列式 → 化简为路径积分标准形式
4. **等价性证明**：将结果与第2篇不对称随机游走的结果对比 → 完全一致

## 关键公式

- 一般SDE：$dx(t) = p(x(t),t)dt + \sqrt{\alpha}dW_t$ (48)
- 路径积分变量代换：$P[x(t)]\mathscr{D}x(t) = P[W(t)]\mathscr{D}W(t)$ (50)
- 非线性SDE的雅可比行列式：$\mathcal{J}[x(t)] = \exp\left(-\frac{1}{2}\int_{t_a}^{t_b}\frac{\partial p(x)}{\partial x}dt\right)$ (64)
- 非线性SDE的路径概率泛函：$P[x(t)] = \exp\left\{-\frac{1}{2\alpha}\int[(\dot{x}-p)^2 + \alpha\frac{\partial p}{\partial x}]dt\right\}$ (66)
- 化简为标准形式：$P[x(t)] = \exp\left[-\frac{1}{\alpha}\int(\frac{1}{2}\dot{x}^2 - V)dt\right]\exp\left(\frac{1}{\alpha}\int_{x_a}^{x_b}p dx\right)$ (68)
- 势函数：$V(x,t) = -\frac{1}{2}(\alpha\frac{\partial p}{\partial x}+p^2)-\int\frac{\partial p}{\partial t}dx$ (69)，与第2篇公式(18)完全一致

## 体现的方法

- **SDE path integral method** → discrete ↔ continuous bridge: 从SDE离散化构造路径积分，核心是雅可比行列式计算
- **variable transformation with Jacobian** → rewrite / identity transform: 在路径积分测度变换中计算雅可比行列式
- 该方法与 [[把优化算法解释为动力系统离散化]] 共享 discrete ↔ continuous bridge 操作类型——SGD → SDE 和 SDE → path integral 都是离散↔连续的桥梁方法
- **关键连接**：本文证明的等价性连接了 [[SGD-SDE近似]] 概念中的 SDE 与 [[把优化算法解释为动力系统离散化]] 方法中的离散→连续操作

## 所属系列位置

路径积分系列第4篇，建立SDE与路径积分、随机游走的等价性，是整个系列的理论核心。

## 与其他文章的关系

- [[article-3750]]（第2篇）：本文的结果与第2篇不对称随机游走的偏微分方程完全一致，验证了等价性
- [[article-3757]]（第3篇）：本文使用第3篇定义的路径积分概念，将其应用于SDE
- [[article-3766]]（第5篇）：第5篇以股票价格SDE为例展示了路径积分计算
- 与[[Fokker-Planck方程]]概念：本文的方程(12)实质上就是Fokker-Planck方程
- 与[[SGD-SDE近似]]概念：本文处理的SDE形式与SGD的SDE近似格式同源
- 与系列[[从动力学角度看优化算法]]共享SDE方法论基础

## 原文证据锚点

- ev::3762::线性SDE路径积分：公式(55)给出了线性SDE的路径概率泛函
- ev::3762::非线性雅可比行列式：公式(64)是关键的技术贡献
- ev::3762::SDE路径泛函：公式(66)是非线性SDE路径积分的一般形式
- ev::3762::等价性结论：公式(68)(69)与第2篇公式(18)(19)完全一致，验证了等价性
- ev::3762::离散化中点规则：公式(60)中对$p(x,t)$取平均的技术细节确保了离散化的精度
