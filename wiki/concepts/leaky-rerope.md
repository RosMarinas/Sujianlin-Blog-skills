---
type: concept
definition: Leaky ReRoPE是ReRoPE的一般化形式，它在窗口w内使用标准RoPE步长1（保持局部不失真），在窗口外使用更小的步长1/k进行位置内插（压缩远处不越界），从而实现免微调的长度外推。
title: Leaky ReRoPE
status: draft
created: '2026-06-09'
tags:
- RoPE
- 长度外推
- 位置编码
- 分段线性
related_articles:
- 9708
- 9728
- 9731
- 9948
related_concepts:
- rerope
- length-extrapolation
- rotary-position-embedding
- inv-leaky-rerope
evidence_spans:
- 9708-融合
- 9728-回顾
- 9948-保近压远
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

Leaky ReRoPE是ReRoPE的一般化形式，它在窗口w内使用标准RoPE步长1（保持局部不失真），在窗口外使用更小的步长1/k进行位置内插（压缩远处不越界），从而实现免微调的长度外推。

Leaky ReRoPE与ReRoPE的关系，类似于Leaky ReLU与ReLU的关系——前者在"负区间"使用一个非零斜率（1/k），后者直接截断为0（对应ReRoPE截断为w）。

## 关键性质

1. **分段线性**：相对位置在窗口内线性增长（步长1），窗口外线性增长但更缓慢（步长1/k），形成分段线性结构。
2. **k的可调性**：k控制可处理的最大长度。一般情况下，使得 w + (L-1-w)/k 不超过训练长度的一半为佳。
3. **w的可调性**：窗口w的最佳取值约为训练长度的1/4到1/2。
4. **理论上限**：与ReRoPE不同，k取有限值时存在最大可处理长度上限（当窗口外位置编码超出训练范围时效果下降）。
5. **精调潜力**：经过精调的Leaky ReRoPE有机会超过ReRoPE，但提升很微弱。

## 数学定义

设训练长度为L_train，窗口大小为w，内压缩因子为k，则位置m和n之间的相对位置编码为：

- 若 |m-n| < w：相对位置 = |m-n|（标准RoPE）
- 若 |m-n| ≥ w：相对位置 = w + (|m-n|-w)/k（内插版本）

## 出现位置

- [第12篇](/archives/9708) "融合"节首次提出
- [第12篇](/archives/9708) "实验"节与ReRoPE对比
- [第13篇](/archives/9728) "回顾"节作为逆用的基础
- [第16篇](/archives/9948) "保近压远"节全面讨论

## 原文证据

- 原文9708"融合"节给出了Leaky ReRoPE的完整矩阵定义（eq:leaky-rerope），并指出它与ReLU/Leaky ReLU的类比关系
- 原文9708"实验"节的对比表显示Leaky ReRoPE与ReRoPE性能接近（如w128-k16+log n在4096不重复测试中达49.10%）
- 原文9728"回顾"节重述了Leaky ReRoPE的数学定义

## 变体

- **InvLeaky ReRoPE**：在训练阶段逆用Leaky ReRoPE（窗口外步长>1），推理阶段退回标准RoPE，保持推理速度不变
- **Self-Extend**：外部工作，在Leaky ReRoPE基础上加入Round运算