---
type: article_summary
title: 斯特灵(stirling)公式与渐近级数
article_id: "3731"
source_url: https://spaces.ac.cn/archives/3731
date: 2016-04-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-04-15-斯特灵-stirling-公式与渐近级数.md
series:
  - "[[渐近分析]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[斯特灵公式]]"
  - "[[渐近级数]]"
  - "[[伽马函数]]"
methods:
  - "[[拉普拉斯方法/鞍点法]]"
  - "[[参数量纲引入法]]"
evidence_spans:
  - "ev::3731::stirling_derivation_laplace"
  - "ev::3731::asymptotic_series_divergence_explanation"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-04-15-斯特灵-stirling-公式与渐近级数.md
source_ids:
  - "3731"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何通过拉普拉斯方法直接从伽马函数的积分定义推导斯特灵公式和斯特灵级数，并解释渐近级数发散的根本原因？

## 主要结论

1. 从 $\Gamma(x+1)=\int_0^\infty e^{-t}t^x dt$ 出发，通过变量代换 $t=xs$ 和 $s=e^u$，将积分化为适合拉普拉斯方法的标准形式。
2. 主贡献来自 $u=0$ 附近的高斯积分 $\int_{-\infty}^\infty e^{-xu^2/2}du=\sqrt{2\pi/x}$，直接得到斯特灵公式 $\Gamma(x+1)\approx\sqrt{2\pi x}(x/e)^x$。
3. 通过人工引入参数 $q$ 实现逐项展开积分，得到斯特灵级数 $\Gamma(x+1)=\sqrt{2\pi x}(x/e)^x(1+\frac{1}{12x}+\frac{1}{288x^2}+\cdots)$。
4. 渐近级数发散的根本原因：复合函数泰勒展开在无穷远处失效——被积函数在无穷远处的贡献虽被高斯核压制，但无穷多个弱项叠加后发散。

## 推导结构

1. 伽马函数的积分表示和变量变换
2. 拉普拉斯方法求主项 → 斯特灵公式
3. 引入参数 $q$ 做级数展开 → 斯特灵级数
4. 以 $I(\varepsilon)=\int_{-\infty}^\infty e^{-x^2-\varepsilon x^4}dx$ 为例说明渐近发散原因

## 关键公式

$$\Gamma(x+1)=\sqrt{2\pi x}\left(\frac{x}{e}\right)^x\left(1+\frac{1}{12x}+\frac{1}{288x^2}+\cdots\right)$$

## 体现的方法

- **拉普拉斯方法/鞍点法**：利用积分主要贡献来自被积函数极值点附近的事实，将复杂积分近似为高斯积分。
- **参数量纲引入法**：通过人工引入参数 $q$ 来辨明展开式中各项的阶，实现系统化的逐项积分。

## 所属系列位置

属于《渐近分析》系列的核心文章，建立渐近展开的标准方法论。

## 与其他文章的关系

- [[3696 一个非线性差分方程的隐函数解]]：共享渐近级数主题和参数 $q$ 技术。
- [[3108 伽马函数的傅里叶变换之路]]：同为伽马函数的不同推导路径。
