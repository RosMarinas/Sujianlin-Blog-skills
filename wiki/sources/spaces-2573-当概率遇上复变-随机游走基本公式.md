---
type: article_summary
title: 当概率遇上复变：随机游走基本公式
article_id: "2573"
source_url: https://spaces.ac.cn/archives/2573
date: 2014-04-30
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-04-30-当概率遇上复变-随机游走基本公式.md
series:
  - "[[当概率遇上复变]]"
topics:
  - "[[解析概率]]"
concepts:
  - "[[随机游走]]"
methods:
  - "[[通过连续极限推导离散过程的极限分布]]"
problem_patterns: []
evidence_spans:
  - ev::2573::离散随机游动
  - ev::2573::连续极限与正态分布
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-04-30-当概率遇上复变-随机游走基本公式.md
source_ids:
  - "2573"
status: draft
updated: 2026-06-11
---

# 当概率遇上复变：随机游走基本公式

## 文章核心问题
使用生成函数及其连续极限方法推导一维离散随机游走粒子位置的概率分布，并建立随机游走与正态分布（维纳过程）的本源联系。

## 主要结论
1. 一维离散网格上粒子每步向前（+1）或向后（-1）概率为 $1/2$，试验 $n$ 次的概率分布可用生成函数 $\frac{1}{2^n}(z + z^{-1})^n$ 描述。
2. 在时间步 $\Delta t \to 0$、空间步 $\Delta s \to 0$ 且满足标度关系 $\Delta s^2 = \alpha \Delta t$ 的连续极限下，随机游走概率分布的特征函数趋于 $\exp(-\frac{\omega^2 \alpha t}{2})$。
3. 对极限特征函数进行傅里叶反变换，得到粒子在 $t$ 秒后位于坐标 $x$ 处的概率密度为正态分布：$P(x) = \frac{1}{\sqrt{2\pi \alpha t}} \exp(-\frac{x^2}{2\alpha t})$。
4. 随机游走是许多物理现象（如布朗运动、误差累积）的数学基础。极限下蕴含的 $\Delta t \propto \Delta s^2$ 意味着瞬时移动速度为无穷大。

## 推导结构
1. 离散醉汉走路：将每次行走的概率定义为 $\frac{1}{2}(z+z^{-1})$，则 $n$ 秒后位置的概率分布由 $\frac{1}{2^n}(z+z^{-1})^n$ 的系数给出。
2. 细致随机行走：设时间步 $\Delta t$，空间步 $\Delta s$，写出母函数 $\frac{1}{2^{t/\Delta t}}\left(z^{\Delta s}+z^{-\Delta s}\right)^{t/\Delta t}$。
3. 极限变换：用 $e^{-i\omega}$ 代替 $z$，利用欧拉公式化简母函数为 $\cos^{t/\Delta t}(\omega \Delta s) \approx (1 - \frac{\omega^2 \Delta s^2}{2})^{t/\Delta t}$。
4. 约束关系：设定 $\Delta s^2 = \alpha \Delta t$，在 $\Delta t \to 0$ 下将其极限表示为指数形式 $\exp(-\frac{\omega^2 \alpha t}{2})$。
5. 反变换：进行傅里叶逆变换，解出极限概率密度函数 $P(x)$ 满足高斯/正态分布。

## 关键公式
- 离散母函数：$\frac{1}{2^n}(z+z^{-1})^n$
- 连续特征函数极限：$\lim_{\Delta t\to 0}\cos^{t/\Delta t}(\omega \Delta s) = \exp\left(\frac{- \omega^2 \alpha t }{2}\right)$ (其中 $\Delta s^2 = \alpha \Delta t$)
- 随机游走极限PDF：$P(x)=\frac{1}{\sqrt{2\pi \alpha t}}\exp\left(-\frac{x^2}{2\alpha t }\right)$

## 体现的方法
- [[通过连续极限推导离散过程的极限分布]]

## 所属系列位置
- [[当概率遇上复变]] 系列第 2 篇，通过生成函数连续极限推导维纳过程基本公式。

## 与其他文章的关系
- 本篇导出的高斯密度核 $P(x)$ 是第三篇《当概率遇上复变：随机游走与路径积分》构建路径积分表示的基础。

## 原文证据锚点
- `ev::2573::离散随机游动`: 原文第16行至第25行，讨论一维网格上的离散粒子游走，给出以二项分布为背景的母函数表达式。
- `ev::2573::连续极限与正态分布`: 原文第26行至第58行，展示从特征函数逼近、引出 $\Delta s^2 = \alpha \Delta t$ 极限条件到反变换出正态分布 PDF 这一核心数学物理推导。
