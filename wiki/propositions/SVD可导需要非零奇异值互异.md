---
type: proposition
title: SVD可导需要非零奇异值互异
aliases: []
statement: SVD 的一般可导条件要求全体非零奇异值两两不等；相等奇异值会破坏分解唯一性。
assumptions:
  - 只考虑源文讨论的可微区域
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
  - "10878"
requires:
  - [[SVD奇异值微分公式]]
proof_route: 由源文局部推导抽取；公式细节见 requires。
methods:
  - [[用等效前向表达保留SVD梯度]]
limits:
  - 早期 SVD 系列偏解释性，严格定理仍以低秩近似系列为准。
examples: []
evidence_spans:
  - ev::10878::一般结果
status: stable
updated: 2026-06-10
---

# SVD可导需要非零奇异值互异

## 命题

SVD 的一般可导条件要求全体非零奇异值两两不等；相等奇异值会破坏分解唯一性。

## 证据

- `ev::10878::一般结果`
