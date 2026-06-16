---
type: article_summary
article_id: "1794"
source_url: https://spaces.ac.cn/archives/1794
date: 2012-11-30
category: Mathematics
series: [[算子与线性常微分方程系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2012-11-30-算子与线性常微分方程-下.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-11-30-算子与线性常微分方程-下.md
source_ids:
  - "1794"
status: draft
updated: 2026-06-10
---

# article-1794: 算子与线性常微分方程(下)

## 文章核心问题

探讨算子方法推广到变系数线性常微分方程时遇到的本质困难——算子的非对易性，并通过对易子分析揭示可分解的条件。

## 主要结论

1. [D,x]=1 是求导算子与乘法算子的基本对易关系。
2. 由于算子不可交换，变系数方程不能像常系数那样直接求根分解。
3. 对于 [D²+g(x)]y=f(x) 形式的方程，可尝试分解为 [D-a(x)][D+a(x)]，这要求 a 满足 Riccati 方程 -a²+a'=g(x)。
4. Riccati 方程本身又可转化为二阶线性方程，形成循环依赖。
5. 已知齐次方程的一个特解即可求得非齐次方程的通解——局部性质决定全局。

## 推导结构

- 计算对易子 [D,x] = Dx - xD = 1
- 计算 (D-x)(D+x) = D²-x²+1（非 D²-x²）
- 对方程 [D²+g(x)]y=f(x)，尝试算符分解 [D-a(x)][D+a(x)]
- 展开得 D²-a²+a'，要求 -a²+a'=g(x)（Riccati 方程）
- 通过 a = -u'/u 将 Riccati 方程化为 u''+g(x)u=0

## 关键公式

- [D,x] = 1（对易子）
- (D-x)(D+x) = D²-x²+1
- -a²(x)+a'(x)=g(x)（Riccati 方程）
- u''+g(x)u=0（Riccati 方程的线性化）

## 体现的方法

- **算子分解法** → 尝试将二阶变系数算子分解为两个一阶算子的复合
- **对易子分析** → 通过计算算子间的对易关系理解可交换性

## 所属系列位置

算子与线性常微分方程系列第2篇（下），讨论变系数情形和非对易性。

## 与其他文章的关系

- [[article-1791]]（上篇）建立算子框架和常系数解法
- [[article-1878]] 摄动法简介中常数变易法与摄动法的思想关联

## 原文证据锚点

- ev::1794::对易子计算：[D,x]y = D(xy)-xDy = y，所以 [D,x]=1
- ev::1794::Riccati循环：变系数算子分解导致 Riccati 方程，Riccati 方程本身又等价于原二阶方程的死循环
- ev::1794::局部决定全局：齐次方程的一个特解即可推出非齐次方程的通解
