---
type: article_summary
title: 从马尔科夫过程到主方程（推导过程）
article_id: "4598"
source_url: https://spaces.ac.cn/archives/4598
date: 2017-10-06
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-10-06-从马尔科夫过程到主方程-推导过程.md
series:
  - "[[随机过程与主方程]]"
topics:
  - "[[概率与统计推断]]"
concepts:
  - "[[马尔可夫过程]]"
  - "[[主方程]]"
  - "[[跃迁概率]]"
methods:
  - "[[主方程推导法]]"
evidence_spans:
  - "ev::4598::master_equation_derivation"
  - "ev::4598::master_equation_practical_form"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-10-06-从马尔科夫过程到主方程-推导过程.md
source_ids:
  - "4598"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何从马尔科夫过程的积分方程形式 $p(x,\tau)=\int p(x,\tau|y,t)p(y,t)dy$ 严格推导出主方程（Master Equation）的微分形式，并解释为何主方程采用最终的对称形式？

## 主要结论

1. 从马尔科夫过程定义出发，令 $\tau=t+\epsilon$ 并取 $\epsilon\to 0$ 得 $\partial_t p(x,t)=\int \tilde{W}(x,y,t)p(y,t)dy$。
2. 但该形式不便建模，因为 $\tilde{W}(x,y,t)$ 必须满足 $\int\tilde{W}(x,y,t)dx=0$，难以直接构造。
3. 通过引入技巧 $\tilde{W}(x,y,t)=W(x,y,t)-\int\delta(y-x)W(z,x,t)dz$，自动满足约束，得到主方程的标准形式：
   $$\frac{\partial p(x,t)}{\partial t} = \int\Big[W(x,y,t)p(y,t)-W(y,x,t)p(x,t)\Big]dy$$
4. 这种形式对 $W(x,y,t)$ 无附加约束，方便建模；$W(x,y,t)$ 的物理意义是"从 $y$ 到 $x$ 的跃迁率"。

## 推导结构

1. 马尔科夫过程的积分方程
2. $\epsilon$ 展开推导主方程雏形
3. 归一化约束与 $\tilde{W}$ 的条件
4. 技巧变换得到实用形式

## 关键公式

$$\frac{\partial p(x,t)}{\partial t} = \int\Big[W(x,y,t)p(y,t)-W(y,x,t)p(x,t)\Big]dy$$

## 体现的方法

- **主方程推导法**：通过ϵ展开和约束自动满足技巧，将马尔科夫过程的积分方程转化为便于建模的微分-积分主方程形式。

## 所属系列位置

属于《随机过程与主方程》系列的基础推导文章。

## 与其他文章的关系

- [[5239 从最大似然到EM算法：一致的理解方式]]：同为概率模型中的方法论文章。
