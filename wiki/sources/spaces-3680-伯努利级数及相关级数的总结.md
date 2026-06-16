---
type: article_summary
title: "[欧拉数学]伯努利级数及相关级数的总结"
article_id: "3680"
source_url: https://spaces.ac.cn/archives/3680
date: 2016-03-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-03-20-欧拉数学-伯努利级数及相关级数的总结.md
series:
  - "[[欧拉数学]]"
topics:
  - "[[数学分析与级数]]"
concepts:
  - "[[伯努利级数]]"
  - "[[连乘积展开]]"
  - "[[韦达定理推广]]"
methods:
  - "[[欧拉无穷韦达定理法]]"
evidence_spans:
  - "ev::3680::euler_basel_problem"
  - "ev::3680::euler_infinite_product"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-03-20-欧拉数学-伯努利级数及相关级数的总结.md
source_ids:
  - "3680"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何利用欧拉开创的大胆类比方法——将有限阶多项式的韦达定理推广到无穷级数——来求解伯努利级数 $\sum\frac1{n^2}$、更一般的级数 $\sum\frac1{n^2\pm\omega^2}$ 以及连乘积 $\prod(1\pm\frac{\omega^2}{n^2})$？

## 主要结论

1. 欧拉将韦达定理推广到无穷：将 $\frac{\sin\sqrt{x}}{\sqrt{x}}$ 视为无限次"多项式"，其根为 $n^2\pi^2$，由韦达定理得 $\sum_{n=1}^\infty\frac1{n^2}=\frac{\pi^2}{6}$。
2. 同样得到连乘积公式：$\frac{\sin x}{x} = \prod_{n=1}^\infty (1-\frac{x^2}{n^2\pi^2})$。
3. 推广得到 $\sum_n\frac1{n^2-\omega^2} = \frac{1-\pi\omega\cot\pi\omega}{2\omega^2}$ 及双曲版本 $(\omega\to i\omega)$。

## 推导结构

1. 伯努利级数 $\sum 1/n^2$ 的欧拉解法
2. 从韦达定理到无穷连乘积展开
3. 推广到含参级数 $\sum 1/(n^2\pm\omega^2)$ 和双曲版本

## 关键公式

$$\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}$$ $$\frac{\sin x}{x} = \prod_{n=1}^\infty\left(1-\frac{x^2}{n^2\pi^2}\right)$$ $$\sum_{n=1}^\infty\frac{1}{n^2-\omega^2} = \frac{1-\pi\omega\cot\pi\omega}{2\omega^2}$$

## 体现的方法

- **欧拉无穷韦达定理法**：将有限维代数定理（韦达定理）大胆推广到无穷维解析函数，将函数的零点与展开系数联系起来。

## 所属系列位置

属于《欧拉数学》系列，展示 18 世纪欧拉风格的创造性级数运算。

## 与其他文章的关系

- [[3018 算符的艺术：差分、微分与伯努利数]]：共享伯努利数这一核心主题，3018 从算符角度理解伯努利数。
