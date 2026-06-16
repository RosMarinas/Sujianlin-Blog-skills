---
title: EAE示例：自编码器到生成模型
type: example
status: draft
notation_mapping:
  E(x): 编码器,将x映射到隐变量z
  D(z): 解码器,将z映射回x
  N(·): BN层(无beta/gamma)
  H(Z): 隐变量熵,通过k邻近估计
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

# EAE示例

## Pipeline
1. 编码器E将x映射到隐变量z
2. BN层标准化z（均值为0、方差为1）
3. 解码器D重构x̂ = D(N(E(x)))
4. 重构损失 + 最大熵正则项

## Loss Components
- 重构损失: ||x - D(N(E(x)))||²
- 熵正则: -λ H(Z) ≈ -λ · d/n Σ log ε(i)

## Related Sources
- [[sources/spaces-7343-EAE]]