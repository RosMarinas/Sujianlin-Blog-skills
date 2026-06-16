---
type: article_summary
title: 当概率遇上复变：从二项分布到泊松分布
article_id: "3188"
source_url: https://spaces.ac.cn/archives/3188
date: 2015-01-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2015-01-13-当概率遇上复变-从二项分布到泊松分布.md
series:
  - "[[当概率遇上复变]]"
topics:
  - "[[解析概率]]"
concepts:
  - "[[概率生成函数]]"
methods:
  - "[[通过母函数做分布极限近似]]"
problem_patterns: []
evidence_spans:
  - ev::3188::泊松分布推导
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-01-13-当概率遇上复变-从二项分布到泊松分布.md
source_ids:
  - "3188"
status: draft
updated: 2026-06-11
---

# 当概率遇上复变：从二项分布到泊松分布

## 文章核心问题
通过生成函数（母函数）方法推导二项分布在稀有大样本试验下的泊松分布极限形式，展示母函数在概率分布近似推导中的优美与高效。

## 主要结论
1. 泊松分布常用于描述单位时间内随机事件发生的次数，也是小概率二项分布的近似。
2. 二项分布的母函数 $(1-p+px)^n$，在 $\lambda = pn$ 保持适中、 $n \to \infty$ 的极限下，可以完美近似为 $e^{\lambda(x-1)}$。
3. 极限近似后的函数 $e^{\lambda(x-1)}$ 依然自动满足概率生成函数归一性条件（即在 $x=1$ 处值为 1），不需要额外的修正因子。
4. 将特征母函数展开为泰勒幂级数：$e^{\lambda x - \lambda} = e^{-\lambda} \sum \frac{\lambda^k}{k!} x^k$，可以直接读出泊松分布概率公式：$P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$。

## 推导结构
1. 概念引入：介绍泊松分布的适用场景和传统二项近似证明的繁琐。
2. 母函数表示：引入二项分布母函数 $(q+px)^n$，并将其表示为带均值参数 $\lambda$ 的形式：$\left(1+\frac{\lambda}{n}(x-1)\right)^n$。
3. 极限逼近：利用重要极限公式 $\lim_{n\to\infty}(1+x/n)^n = e^x$，推导出泊松母函数 $e^{\lambda(x-1)}$。
4. 归一性验证：验证近似后的母函数在 $x=1$ 时等于 1，肯定其是一件“非常漂亮的巧合”。
5. 级数展开：展开 $e^{\lambda x-\lambda}$，导出泊松分布概率分布公式。并推荐了各种概率分布之间演变关系的经典框架图。

## 关键公式
- 二项分布母函数参数化：$\left(1+\frac{\lambda}{n}(x-1)\right)^n$
- 泊松分布母函数（极限形式）：$e^{\lambda x-\lambda}$
- 泊松分布概率公式：$P(X=k)=e^{-\lambda}\frac{\lambda^k}{k !}$

## 体现的方法
- [[通过母函数做分布极限近似]]

## 所属系列位置
- [[当概率遇上复变]] 系列第 4 篇，用母函数做二项到泊松的渐进推导。

## 与其他文章的关系
- 回应了第一篇《当概率遇上复变：解析概率》中建立的离散母函数和二项母函数公式；展示了母函数相比于茆诗松教材中传统的微积分代数证明更具简洁美。

## 原文证据锚点
- `ev::3188::泊松分布推导`: 原文第18行至第48行，通过二项分布母函数在 $\lambda=pn$ 条件下取 $n\to\infty$ 极限推导泊松分布母函数及概率公式的过程。
