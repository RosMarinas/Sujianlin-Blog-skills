---
type: concept
title: KL散度
aliases:
  - KL Divergence
  - Kullback-Leibler Divergence
definition: KL散度衡量两个概率分布之间的差异程度，定义为 KL(p||q) = sum p(x) log(p(x)/q(x))。其值为非负，当且仅当两个分布相同时为0。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-03-15-从最大似然到EM算法-一致的理解方式.md
source_ids:
  - "5239"
related_methods:
  - "[[KL散度交替最小化EM法]]"
status: draft
updated: 2026-06-13
---

**KL散度**是信息论和统计推断中的核心概念。KL散度衡量两个概率分布 $p$ 和 $q$ 之间的差异程度，定义为 $KL(p\|q) = \sum p(x) \log(p(x)/q(x))$，其值非负，当且仅当 $p=q$ 时为零。最大似然估计等价于最小化经验分布与模型分布之间的KL散度。在EM算法中，通过交替最小化联合分布的KL散度 $KL(\tilde{p}(X,Y)\|p_\theta(X,Y))$，自然地导出了E步（固定参数优化后验）和M步（固定后验优化参数）的迭代格式，Q函数也自然地作为M步的优化目标出现。
