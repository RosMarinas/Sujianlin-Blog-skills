---
type: concept
title: f-divergence
definition: "f散度是衡量两个概率分布差异的广义指标度量，涵盖KL散度、JS散度及皮尔逊散度等变体。"
sources:
  - wiki/sources/spaces-6016-f-GAN.md
source_ids:
  - "6016"
status: draft
updated: 2026-06-12
---
# f散度 (f-divergence)

## Definition
f散度是KL散度的一般化: D_f(P||Q) = ∫ q(x) f(p(x)/q(x)) dx, 其中f为凸函数且f(1)=0。

## Common f-divergences
| Name | f(u) |
|------|------|
| KL散度 | u log u |
| 逆KL散度 | -log u |
| JS散度 | -(u+1)/2 log((1+u)/2) + u/2 log u |
| Pearson χ² | (1-u)²/u |
| Hellinger距离 | (√u - 1)² |

## Key Property
凸共轭（Fenchel对偶）: f(u) = max_t { t u - g(t) }

## Related Methods
- [[methods/f-GAN]]
- [[sources/spaces-6016-f-GAN]]
