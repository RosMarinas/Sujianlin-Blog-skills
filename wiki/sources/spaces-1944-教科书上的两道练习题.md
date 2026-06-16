---
type: article_summary
title: 费曼积分法(6)：教科书上的两道练习题
article_id: "1944"
source_url: https://spaces.ac.cn/archives/1944
date: 2013-03-24
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-6-教科书上的两道练习题.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1944::No1
  - ev::1944::No2
  - ev::1944::对称性解法
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-6-教科书上的两道练习题.md
source_ids:
  - "1944"
status: draft
updated: 2026-06-10
---

# 费曼积分法(6)：教科书上的两道练习题

## 摘要

本文用费曼积分法解决《数学分析》教科书上的两道练习题。第一题 $\int_0^1 \ln(1+x)/(1+x^2)dx$ 通过引入参数 $a$ 后求导化为有理分式积分；第二题 $\int_0^\pi x\sin x/(1+\cos^2 x)dx$ 巧妙地利用 $\arccos(a\cos x)$ 参数化与对称性。

## 公式

### 例 1

$$
F(a)=\int_0^1 \frac{\ln(1+ax)}{1+x^2}dx, \quad F(1)=\frac{\pi}{8}\ln 2
$$

### 例 2

$$
\int_0^\pi \frac{x\sin x}{1+\cos^2 x}dx = \frac{\pi^2}{4}
$$

求解中利用 $\arccos(a\cos x)$ 参数化求导后发现积分值为常数，巧妙地简化了问题。
