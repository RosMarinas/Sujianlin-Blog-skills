---
type: proposition
title: ID的核心难点是列子集选择
aliases: []
statement: 在 ID 中，固定骨架列后最优系数可由伪逆解析求得，因此主要难点是选择哪些列作为骨架；该列子集选择问题是 NP-Hard 的组合优化问题。
assumptions:
  - 采用 `M_{[:,S]}Z` 形式的 ID 近似。
  - 误差使用 Frobenius 范数。
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-10-30-低秩近似之路-四-ID.md
source_ids:
  - "10501"
requires:
  - "[[插值分解]]"
  - "[[伪逆]]"
proof_route: 文章在定义 ID 后直接用伪逆给出固定 `C` 时 `Z` 的最优解，并指出剩余 `S` 的优化是列选择组合优化，精确求解 NP-Hard。
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
limits:
  - 该命题不评价列驱 QR、随机投影、随机列采样谁在所有任务上更优。
examples: []
evidence_spans:
  - ev::10501::基本定义
  - ev::10501::提高精度
status: stable
updated: 2026-06-09
---

## 证明路线

固定 `C=M_{[:,S]}` 后，`Z=C^\dagger M` 给出连续部分的解析解。剩下的问题只剩索引集合 `S` 的选择，因此 ID 的难点从连续最小二乘转移为离散列子集选择。
