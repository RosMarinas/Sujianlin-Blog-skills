---
title: IGN示例：判别生成合一的GAN变种
type: example
status: draft
notation_mapping:
  G_φ(x): 幂等生成器，输入输出同大小
  δ_φ(x) = ||G_φ(x) - x||²: 重构损失作为判别器
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
article_id: （待从源文章提取）
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# IGN示例

## Architecture
- 生成器G_φ使用自编码器结构（输入=输出维度）
- 判别器由重构损失 δ_φ(x) = ||G_φ(x) - x||² 替代
- 通过stop_gradient实现单loss训练

## Training Objective
min_φ δ_φ(x) - δ_φ(G_{φ'}(z)) + δ_{φ'}(G_φ(z))

## Related Sources
- [[sources/spaces-9969-IGN]]