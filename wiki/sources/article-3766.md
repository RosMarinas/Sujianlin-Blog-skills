---
type: article_summary
article_id: "3766"
source_url: https://spaces.ac.cn/archives/3766
date: 2016-06-09
category: Mathematics
series: [[路径积分系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-5-例子和综述.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-06-09-路径积分系列-5-例子和综述.md
source_ids:
  - "3766"
status: draft
updated: 2026-06-10
---

# article-3766: 路径积分系列：5.例子和综述

## 文章核心问题

通过股票价格模型这个具体案例展示路径积分方法在随机问题中的应用，并综述该系列的方法论意义和未来研究方向。

## 主要结论

1. 股票价格SDE $dS_t = S_t(\mu dt + \sigma dW_t)$ 可以通过对数变换 $x_t = \ln S_t$ 转化为标准SDE形式 $dx_t = (\mu - \frac{1}{2}\sigma^2)dt + \sigma dW_t$。
2. 该SDE对应的路径积分可精确求解（二次型作用量），结果为对数正态分布。
3. 路径积分方法源于量子力学，但应用不限于量子力学——量子金融（量子经济学）是将路径积分方法从量子力学领域推向金融领域的交叉学科。
4. 未来三个有价值的研究方向：高阶非线性随机场微分方程的路径积分、随机偏微分方程的路径积分、为随机偏微分方程寻找类似不对称随机游走的模型。

## 推导结构

1. **股票价格SDE**：写出一维股票价格SDE → 对数变换 → 转化为标准SDE形式
2. **路径积分求解**：写出等价的路径积分 → 二次型精确求解 → 归一化
3. **转换为原始变量**：通过对数变换逆变换 → 得到对数正态分布
4. **综述**：总结路径积分方法的应用范围，指出未来方向

## 关键公式

- 股票价格SDE：$dS_t = S_t(\mu dt + \sigma dW_t)$ (70)
- 对数变换：$dx_t = (\mu - \frac{1}{2}\sigma^2)dt + \sigma dW_t$ (71)
- 等价偏微分方程：$\sigma\frac{\partial P}{\partial t} = \frac{\sigma^2}{2}\frac{\partial^2 P}{\partial x^2} + (\mu - \frac{1}{2}\sigma^2)\frac{\partial P}{\partial x}$ (72)
- 路径积分形式：$\int_{x_a}^{x_b}\exp\left\{-\frac{1}{2\sigma}\int_{t_a}^{t_b}[\dot{x} - (\mu - \frac{1}{2}\sigma^2)]^2 dt\right\}\mathscr{D}x(t)$ (73)
- 精确解（对数正态分布）：$P(S_b) = \frac{1}{S_b\sqrt{2\pi\sigma T}}\exp\left\{-\frac{T}{2\sigma}\left[\frac{\ln(S_b/S_a)}{T} - (\mu - \frac{1}{2}\sigma^2)\right]^2\right\}$ (77)

## 体现的方法

- **SDE path integral calculation** → discrete ↔ continuous bridge: 展示如何对具体SDE应用路径积分求解
- **variable transformation in SDE** → rewrite / identity transform: 对数变换简化SDE
- 该方法与 [[把优化算法解释为动力系统离散化]] 共享 SDE 方法论基础

## 所属系列位置

路径积分系列第5篇（最终篇），以案例总结全系列。

## 与其他文章的关系

- [[article-3762]]（第4篇）：使用第4篇建立的SDE路径积分方法
- [[article-3750]]（第2篇）：股票价格SDE等价于不对称随机游走，对应偏微分方程(72)本质上就是(12)的形式
- 与[[SGD-SDE近似]]概念：共享SDE模型框架
- 该篇展示的路径积分-金融联系指向量子金融这一交叉领域

## 原文证据锚点

- ev::3766::股票SDE模型：公式(70)给出了股票价格的对数正态SDE
- ev::3766::对数变换：公式(71)展示了随机微积分的Ito变换
- ev::3766::精确解：公式(77)给出了股价的最终概率分布
- ev::3766::未来方向：列出了三个值得继续研究的方向
