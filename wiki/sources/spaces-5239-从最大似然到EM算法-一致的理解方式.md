---
type: article_summary
title: 从最大似然到EM算法：一致的理解方式
article_id: "5239"
source_url: https://spaces.ac.cn/archives/5239
date: 2018-03-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-03-15-从最大似然到EM算法-一致的理解方式.md
series:
  - "[[概率与统计模型]]"
topics:
  - "[[概率与统计推断]]"
concepts:
  - "[[最大似然]]"
  - "[[EM算法]]"
  - "[[KL散度]]"
  - "[[隐变量]]"
methods:
  - "[[KL散度交替最小化EM法]]"
evidence_spans:
  - "ev::5239::mle_to_em_kl_divergence"
  - "ev::5239::em_alternating_minimization"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-03-15-从最大似然到EM算法-一致的理解方式.md
source_ids:
  - "5239"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何从最大似然原理和最基础的KL散度出发，简洁自然地推导出EM算法的完整框架，包括E步的Q函数构造和M步的参数更新？

## 主要结论

1. 最大似然等价于最小化经验分布 $\tilde{p}(X)$ 与模型分布 $p_\theta(X)$ 之间的KL散度。
2. 对于含隐变量的模型，考虑联合分布的KL散度 $KL(\tilde{p}(X,Y)\|p_\theta(X,Y))$。
3. EM算法就是对联合KL散度的交替最小化：固定 $\tilde{p}(Y|X)$ 优化 $\theta$（M步），固定 $\theta$ 优化 $\tilde{p}(Y|X)$（E步）。
4. E步的解析解是贝叶斯后验 $\tilde{p}(Y|X)=p_\theta(Y|X)=p_\theta(Y)p_\theta(X|Y)/\sum_Y p_\theta(Y)p_\theta(X|Y)$。
5. Q函数自然出现为M步中需要最大化的部分：$\mathbb{E}_X[\sum_Y \tilde{p}(Y|X)\log p_\theta(Y)p_\theta(X|Y)]$。

## 推导结构

1. 从最大似然到KL散度
2. 有监督学习的最大似然（分类问题）
3. 隐变量问题与联合KL散度
4. EM算法的交替最小化推导
5. Q函数和EM流程的自然引出

## 关键公式

EM迭代：$\theta^{(r)} = \mathop{\text{argmax}}_\theta \mathbb{E}_X[\sum_Y \tilde{p}^{(r-1)}(Y|X)\log p_\theta(Y)p_\theta(X|Y)]$；$\tilde{p}^{(r)}(Y|X) = p_{\theta^{(r)}}(Y|X)$

## 体现的方法

- **KL散度交替最小化EM法**：通过交替固定隐变量后验分布和模型参数，最小化联合分布KL散度以求解含隐变量的最大似然问题。

## 所属系列位置

属于《概率与统计模型》系列的EM算法专题核心文章。

## 与其他文章的关系

- [[4277 梯度下降和EM算法：系出同源，一脉相承]]：姊妹篇，4277从近似曲线视角，5239从KL散度视角。
