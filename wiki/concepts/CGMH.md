---
type: concept
definition: CGMH (Constrained Generation by Metropolis-Hastings Sampling) 是一种利用MH采样进行无监督有约束文本生成的方法。通过增、删、改三种微调操作模拟人的写作润色过程，使得生成过程具有可解释性。
title: CGMH
aliases:
- Constrained Generation by Metropolis-Hastings
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-25-搜出来的文本-四-通过增-删-改来用词造句.md
source_ids:
- '8194'
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence
  binding is deferred.
status: draft
updated: '2026-06-12'
---


# CGMH

## Definition

CGMH (Constrained Generation by Metropolis-Hastings Sampling) 是一种利用MH采样进行无监督有约束文本生成的方法。通过增、删、改三种微调操作模拟人的写作润色过程，使得生成过程具有可解释性。

## Key Innovation

将MCMC方法中的转移概率设计为三种具体的文本编辑操作（增、删、改），使MH采样在文本领域变得实用且直观。任务特定的约束通过目标函数ρ(x,c)融入接受率中。

## Relation to Earlier Articles

- 第一篇（8062）提出了受限文本生成的形式化框架
- 第二篇（8084）介绍了MCMC/MH/Gibbs/模拟退火等算法基础
- 第三篇（8119）用BERT MLM实现了Gibbs采样
- 第四篇（8194）用MH + 增删改操作实现了通用的约束文本生成

## Related Pages
- [[MH采样]]
- [[受限文本生成]]
- [[增删改操作]]
- [[BERT MLM Gibbs采样]]