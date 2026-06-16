---
type: concept
definition: MLA（Multi-head Latent Attention）是DeepSeek-V2提出的Attention变体，通过"双重投影"设计实现MHA训练与MQA解码的自由切换，在保持效果的同时大幅降低KV
  Cache。
title: Multi-head Latent Attention (MLA)
status: draft
created: '2026-06-09'
tags:
- Attention
- KV Cache
- MHA
- GQA
- Partial RoPE
related_articles:
- 10907
- 11111
- 10862
related_concepts:
- partial-rope
- vo-rope
- rotary-position-embedding
evidence_spans:
- 10907-观察
- 10907-实验
- 11111-部分旋转
- 11111-键值共享
- 11111-双重投影
- 11111-总而言之
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

MLA（Multi-head Latent Attention）是DeepSeek-V2提出的Attention变体，通过"双重投影"设计实现MHA训练与MQA解码的自由切换，在保持效果的同时大幅降低KV Cache。

核心思想是：先将输入投影到一个低维共享向量c_i（维度d_c），再通过独立的升维投影矩阵为每个头生成K、V。推理时利用Attention的恒等变换将升维矩阵吸收到Q和O投影中，退化为KV共享的MQA。

## 关键性质

1. **双重投影**：
   - 训练/Prefill: c_i → 各头的k_i^(s)和v_i^(s)（表现为MHA）
   - Decoding: 吸收升维矩阵后退化为KV共享的MQA
   - 实现Prefill和Decoding的"双向奔赴"

2. **KV Cache极致压缩**：
   - MLA的KV Cache=576（512+64），vs 标准MHA=4096（head_dims=128, 16 heads）
   - 在Loss持平的前提下将KV Cache降至MHA的1/7

3. **Partial RoPE拼接**：
   - K、V的NoPE部分（512维）共享，RoPE部分（64维）仅用于K
   - 暗合Partial RoPE设计，兼顾位置与语义

4. **训练效率**：
   - head_dims=(128+64)的MHA配置
   - 参数效率高，MLA-256（head_dims=192+64）可进一步提升效果

## 为什么有效

从理论角度看，MLA成功的关键在于：
1. 大前提：Partial RoPE效果不逊于RoPE，使NoPE部分可承担主要计算
2. Decoding视角：给定KV Cache下，head_dims=KV Cache、KV共享的MQA是理论最优
3. Training视角：给定head_dims下，MHA是理论最优
4. MLA的双重投影巧妙调和了以上两个冲突的需求
5. 拼接RoPE同时增加了head_dims并实现了Partial RoPE——"一箭双雕"

## 实验表现

- MLA (894M): Loss=2.721, Cache=576
- GQA1-256-PR (943M): Loss=2.711, Cache=512（略超MLA但参数量更大）
- GQA2-(192+64)-S2 (943M): Loss=2.708, Cache=512（引入VO-RoPE超过MLA）
- MLA-256 (989M): Loss=2.705, Cache=576

## 出现位置

- [第20篇](/archives/10907) 全文实验分析
- [第21篇](/archives/11111) 全文理论分析
- [第19篇](/archives/10862) 提及与VO-RoPE的兼容性问题

## 原文证据

- 原文10907"观察"节：列出MLA三大特点（训练MHA、解码MQA、Partial RoPE）
- 原文10907 Part I-V：详尽消融实验数据
- 原文11111"键值共享"节：分析NoPE背景下最优Attention的理论形式
- 原文11111"双重投影"节：给出MLA训练/解码的双重公式
- 原文11111"总而言之"节：总结MLA为"NoPE+LoRA+MHA+MQA的魔术秀"