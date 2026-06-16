---
type: concept
definition: KL散度的对称化形式：D(p,q) = KL(p||q) + KL(q||p) = Σ(pi - qi)(log pi - log qi)。
aliases:
- Symmetric KL Divergence
- Jeffreys Divergence
status: draft
updated: '2026-06-12'
title: 对称KL散度
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# 对称KL散度

KL散度的对称化形式：D(p,q) = KL(p||q) + KL(q||p) = Σ(p_i - q_i)(log p_i - log q_i)。

## Logits层面的简洁形式

当 p, q 由 Softmax 得到：p_i = e^{s_i}/Z, q_i = e^{t_i}/Z'，对称KL散度化简为：
D(p,q) = Σ(p_i - q_i)(s_i - t_i)

这为R-Drop、虚拟对抗训练等正则化方法提供了直接可用的散度形式。

## GlobalPointer推广

对于多标签分类（GlobalPointer），Softmax应替换为Sigmoid：
D(s,t) = Σ(σ(s_i) - σ(t_i))(s_i - t_i)
等价于每个logits分别作为二分类的KL散度之和。

## 相关概念

- [[KL散度]]
- [[多标签分类损失]]
- [[GlobalPointer对称KL散度]]