---
type: concept
definition: 第二类旋转位置编码（VO-RoPE）是RoPE的一种互补用法，它在Value向量上施加正向旋转、在Output向量上施加逆向旋转，从而实现对Value的相对位置编码：
title: 第二类旋转位置编码 (VO-RoPE)
status: draft
created: '2026-06-09'
tags:
- RoPE
- Value编码
- 相对位置
- 理论完备性
related_articles:
- 10862
- 10907
- 11111
related_concepts:
- rotary-position-embedding
- mla
- partial-rope
evidence_spans:
- 10862-新的用法
- 10862-简单实验
- 10862-相关工作
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

第二类旋转位置编码（VO-RoPE）是RoPE的一种互补用法，它在Value向量上施加正向旋转、在Output向量上施加逆向旋转，从而实现对Value的相对位置编码：

o_i = R_i^T Σ_j a_{i,j} R_j v_j = Σ_j a_{i,j} R_{j-i} v_j

对应的标准RoPE（QK-RoPE）则是作用于Query和Key。二者形式对称但效果不同。

## 关键性质

1. **Value端的相对位置**：VO-RoPE是第一个在Value上实现相对位置编码的方案，补全了"RoPE能否加在V上"的理论空白。
2. **效果中等**：1B模型实验显示VO-RoPE（Loss=2.770）优于NoPE（2.795）但不如QK-RoPE（2.712），与QK-RoPE叠加无增益（QKVO-RoPE Loss=2.719）。
3. **连接线性RNN**：当Attention权重取特定形式 a_{i,j} = γ^{i-j} 时，VO-RoPE退化为复数Decay的线性RNN：

o_i = Σ (γ e^{-Iθ})^{i-j} v_j

这提供了从Attention到复线性RNN（LRU、RetNet）的中间桥梁。

## 与其他方案的关系

- **QK-RoPE**：标准RoPE，施加于Q和K，用于提取位置相关的注意力权重
- **VO-RoPE**：第二类，施加于V和O，用于位置相关的Value聚合
- **QKVO-RoPE**：四者全加，效果与QK-RoPE接近（Loss=2.719 vs 2.712）

## 潜在应用

VO-RoPE可解决MLA中的K、V共享与RoPE不兼容问题。在MLA中，若对共享的c_j直接加RoPE：若加在Value侧则失去相对位置编码；若不加则K、V不完全共享（KV Cache翻倍）。VO-RoPE的方案是对c_j加RoPE作为Value，再在Output侧加逆向RoPE，实现K、V完全共享且保持相对位置编码。

## 出现位置

- [第19篇](/archives/10862) 全文提出
- [第20篇](/archives/10907) 用于GQA2-(192+64)-S2实验
- [第21篇](/archives/11111) 作为MLA理论分析的补充讨论

## 原文证据

- 原文10862"新的用法"节给出VO-RoPE的核心公式(eq:vo-rope)
- 原文10862"简单实验"节：1B模型Loss对比表，QK-RoPE=2.712, VO-RoPE=2.770, NoPE=2.795
- 原文10862"相关工作"节：与复线性RNN的联系推导
- 原文10907 Part V：GQA2-(192+64)-S2（引入VO-RoPE）Loss=2.708，优于GQA1-256-PR的2.711