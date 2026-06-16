---
type: article_summary
title: MoE环游记：6. 最优分配促均衡
article_id: "11619"
source_url: https://spaces.ac.cn/archives/11619
date: 2026-02-22
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
source_html: Data/Spaces_ac_cn/raw/articles/11619/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[Quantile Balancing]]"
  - "[[Loss-Free偏置]]"
methods:
  - "[[用分位数求解负载均衡偏置]]"
  - "[[用对偶偏置改写路由约束]]"
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
evidence_spans:
  - ev::11619::线性规划
  - ev::11619::交替迭代
  - ev::11619::小心陷阱
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
source_ids:
  - "11619"
status: draft
updated: 2026-06-09
---

# MoE环游记：6. 最优分配促均衡

## 文章核心问题

本文把 MoE 负载均衡写成等式约束下的最优分配问题，并推导 Quantile Balancing 作为无 Aux Loss、无学习率的偏置求解方案。

## 主要结论

- 固定 Top-k 与每个 Expert 激活 `mk/n` 次可以写成整数规划；其线性松弛与原问题在最优解上等价。
- 对偶变量 `alpha` 和 `beta` 给出路由偏置视角，其中推理只需要固定维度的 `beta`。
- 交替取分位数可以求解 `beta`，因此 QB 可被看作更准确的 Loss-Free bias 更新。
- 必须先用旧偏置完成当前 batch 的路由，再更新偏置，避免信息泄漏和训练推理不一致。

## 推导结构

1. 从 Aux Loss 和 Loss-Free 的局限进入。
2. 建立带行列约束的最优分配线性规划。
3. 交换 max-min 得到对偶变量。
4. 推出交替分位数更新和实际使用流程。
5. 讨论 BIP 的不等式版本、截断问题与近似梯度下降。

## 关键公式

- [[QB分位数偏置公式]]：记录 Top-k 版 QB 的交替分位数更新。

## 体现的方法

- [[用分位数求解负载均衡偏置]]：将排序约束的偏置求解转化为分位数问题。
- [[用对偶偏置改写路由约束]]：对偶变量给出只影响分配的偏置解释。

## 所属系列位置

这是系列第六篇，给出负载均衡的最优分配主线，是第七篇动态 QB 与第八篇 MQB 的数学基础。

## 与其他文章的关系

- continues: `article::10945`
- precedes: `article::11626`
- derives: `concept::Quantile Balancing`

## 原文证据锚点

- `ev::11619::线性规划`：第 36-50 行将负载均衡写成整数规划和线性松弛。
- `ev::11619::交替迭代`：第 96-125 行给出 QB 的交替分位数求解流程。
- `ev::11619::小心陷阱`：第 127-157 行说明先路由后更新偏置的因果顺序和 QB 优势。
