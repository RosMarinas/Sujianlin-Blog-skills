---
type: concept
title: EM算法
aliases:
  - Expectation-Maximization
  - 最大期望算法
definition: EM算法是一种通过迭代交替优化（E步计算隐变量后验期望，M步最大化似然函数）来求解含隐变量概率模型参数的最大似然估计的通用方法。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-03-23-梯度下降和EM算法-系出同源-一脉相承.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-03-15-从最大似然到EM算法-一致的理解方式.md
source_ids:
  - "4277"
  - "5239"
prerequisites:
  - "[[最大似然]]"
  - "[[KL散度]]"
  - "[[隐变量]]"
related_methods:
  - "[[近似曲线迭代法]]"
  - "[[KL散度交替最小化EM法]]"
series:
  - "[[概率与统计模型]]"
evidence_spans:
  - "ev::4277::em_as_approximation_method"
  - "ev::5239::em_alternating_minimization"
status: draft
updated: 2026-06-13
---

**EM算法（Expectation-Maximization Algorithm）**是含隐变量概率模型参数估计的标准方法。其核心思想是通过交替执行E步（估计隐变量后验分布）和M步（最大化完整数据似然期望）来逐步逼近最优参数。

### 原理概述

EM算法可以从两个统一视角理解：

1. **近似曲线迭代视角**：EM与梯度下降同源，都是用简单代理函数局部逼近原目标函数。梯度下降用二次抛物线，EM为了满足概率约束使用线性化Q函数。

2. **KL散度交替最小化视角**：对联合分布 $KL(\tilde{p}(X,Y)\|p_\theta(X,Y))$ 交替优化——固定后验优化参数（M步），固定参数更新后验（E步），后验的解析解为贝叶斯公式。

### 典型应用

- pLSA主题模型参数估计
- GMM混合高斯模型聚类
- K-Means聚类（取光滑近似的极限）
- 隐马尔可夫模型（HMM）的Baum-Welch算法
