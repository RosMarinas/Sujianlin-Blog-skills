---
type: article_summary
title: "[欧拉数学]黎曼ζ函数"
article_id: "1505"
source_url: https://spaces.ac.cn/archives/1505
date: 2011-11-18
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2011-11-18-欧拉数学-黎曼ζ函数.md
series:
  - [[wiki/series/欧拉数学.md]]
concepts:
  - [[concept::黎曼ζ函数]]
methods:
  - [[method::基于生成函数的欧拉乘积展开]]
evidence_spans:
  - ev::1505::黎曼函数定义
  - ev::1505::埃氏筛法推导
  - ev::1505::金钥匙公式
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2011-11-18-欧拉数学-黎曼ζ函数.md
source_ids:
  - "1505"
status: draft
updated: 2026-06-11
---

# [欧拉数学]黎曼ζ函数

本文探讨了数论中的黎曼 $\zeta$ 函数，重点介绍其级数形式，并采用类比“埃拉托色尼筛法”的方式，初等且极其美妙地推导出了连接自然数与素数的欧拉乘积公式（即“金钥匙”）。

## 核心内容

- **黎曼 $\zeta$ 函数定义**：定义为无限级数：
  $$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \dots$$
- **类埃氏筛法推导**：
  1. 写出级数形式：$\zeta(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots$
  2. 乘以第一个素数项：$\frac{1}{2^s}\zeta(s) = \frac{1}{2^s} + \frac{1}{4^s} + \dots$。两者作差，消去所有分母为 2 的倍数的项：
     $$(1 - \frac{1}{2^s})\zeta(s) = 1 + \frac{1}{3^s} + \frac{1}{5^s} + \frac{1}{7^s} + \dots$$
  3. 重复这一消去步骤，依次乘以 $(1 - \frac{1}{p^s})$，其中 $p$ 为下一个素数。
  4. 当 $s > 1$ 时，随着素数 $p \to \infty$，右端乘积后只剩下第一项 1：
     $$\dots (1 - p^{-s}) \dots (1 - 3^{-s})(1 - 2^{-s})\zeta(s) = 1$$
- **欧拉乘积公式（金钥匙）**：
  $$\zeta(s) = \prod_{p} (1 - p^{-s})^{-1}$$
  该公式建立起自然数（左侧求和项）与所有素数（右侧乘积项）之间的桥梁，是解析数论的基石。
