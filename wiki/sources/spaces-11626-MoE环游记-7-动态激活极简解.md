---
type: article_summary
title: MoE环游记：7. 动态激活极简解
article_id: "11626"
source_url: https://spaces.ac.cn/archives/11626
date: 2026-02-23
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
source_html: Data/Spaces_ac_cn/raw/articles/11626/page.html
series:
  - "[[MoE环游记]]"
topics:
  - "[[MoE路由与负载均衡]]"
concepts:
  - "[[动态专家激活]]"
  - "[[Quantile Balancing]]"
methods:
  - "[[用分位数求解负载均衡偏置]]"
problem_patterns:
  - "[[将路由选择转化为约束分配问题]]"
evidence_spans:
  - ev::11626::动态激活
  - ev::11626::一步求解
  - ev::11626::专家选择
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-02-23-MoE环游记-7-动态激活极简解.md
source_ids:
  - "11626"
status: draft
updated: 2026-06-09
---

# MoE环游记：7. 动态激活极简解

## 文章核心问题

本文去掉“每个 Token 恰好激活 `k` 个 Expert”的约束，只保留每个 Expert 总负载约束，从而得到动态激活版 QB 的一步分位数解。

## 主要结论

- 平均每个 Token 激活 `k` 个 Expert 与每个 Expert 负载均衡已经足以表达 MoE 预算目标。
- 动态激活形式由对偶目标自然推出：只要 `s_ij - beta_j > 0` 就激活 Expert。
- `beta_j` 的最优解是第 `mk/n+1` 大元素，也就是 `1-k/n` 分位数。
- 用旧 `beta` 路由、再用当前 batch 更新 `beta` 是避免信息泄漏的必要顺序。

## 推导结构

1. 从第六篇的最优分配问题中去掉行约束。
2. 对列约束做 max-min 对偶化。
3. 将每个 `beta_j` 的优化分解为独立分位数问题。
4. 用 Expert Choice 解释分位数阈值，并指出 Bias 形式如何修复因果和训推一致问题。

## 关键公式

- [[QB分位数偏置公式]]：动态版是一阶分位数阈值，不再需要交替迭代。

## 体现的方法

- [[用分位数求解负载均衡偏置]]：用一维分位数阈值控制 Expert 负载和平均预算。

## 所属系列位置

这是系列第七篇，把第六篇 QB 简化为动态激活的闭式阈值形式。

## 与其他文章的关系

- continues: `article::11619`
- precedes: `article::11760`
- derives: `concept::动态专家激活`

## 原文证据锚点

- `ev::11626::动态激活`：第 16-23 行说明去掉每 Token 固定 `k` 约束后的目标。
- `ev::11626::一步求解`：第 48-68 行推出 `beta` 的一步分位数最优解。
- `ev::11626::专家选择`：第 95-105 行解释 Bias 形式如何把 Expert Choice 改写为因果的 Token Choice。
