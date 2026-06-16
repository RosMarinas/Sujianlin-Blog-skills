---
type: article_summary
title: GELU的两个初等函数近似是怎么来的
article_id: "7309"
source_url: https://spaces.ac.cn/archives/7309
date: 2020-03-26
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
series: []
topics:
  - 激活函数
  - 函数逼近论
concepts:
  - GELU
  - erf函数
  - tanh近似
methods:
  - 局部拟合
  - 全局拟合
  - 混合拟合
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
source_ids:
  - "7309"
status: draft
updated: 2026-06-10
---

## 总结

本文拆解GELU激活函数 $\text{GELU}(x)=x\Phi(x)$ 的两个常见初等近似的数学推导过程。核心是用 $\tanh$ 函数局部拟合（泰勒展开匹配低阶项）和全局拟合（min-max误差优化）来逼近 $\text{erf}(x/\sqrt{2})$，得到近似形式 $\frac{1}{2}x[1+\tanh(\sqrt{2/\pi}(x+0.044715x^3))]$。

## 关键思想

- $ \Phi(x) = \frac{1}{2}[1+\text{erf}(x/\sqrt{2})]$，故逼近 $\Phi$ 等价于逼近 $\text{erf}$
- $\text{erf}$ 是奇函数、单调有界，适合用 $\tanh$ 拟合
- 局部拟合：在 $x=0$ 处泰勒展开匹配前两项系数
- 全局拟合：固定一阶项，用 scipy 优化 min-max 误差 $\min_b \max_x |\text{erf}(x/\sqrt{2})-\tanh(ax+bx^3)|$
- 第二种近似 $\Phi(x)\approx\sigma(1.702x)$ 直接用 sigmoid 全局逼近累积正态分布

## 所属系列

[[激活函数理论]] — [[函数逼近论]]
