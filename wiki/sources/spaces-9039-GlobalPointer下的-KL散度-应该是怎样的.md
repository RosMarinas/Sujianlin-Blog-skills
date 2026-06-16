---
type: article_summary
title: GlobalPointer下的"KL散度"应该是怎样的？
article_id: "9039"
source_url: https://spaces.ac.cn/archives/9039
date: 2022-04-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-04-15-GlobalPointer下的-KL散度-应该是怎样的.md
series:
  - [[多标签分类交叉熵]]
topics:
  - [[概率分布构建]]
concepts:
  - [[KL散度]]
  - [[对称KL散度]]
  - [[多标签分类损失]]
methods:
  - [[GlobalPointer对称KL散度]]
evidence_spans:
  - ev::9039::对称KL散度logits形式
  - ev::9039::GlobalPointer散度sigmoid构造
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-04-15-GlobalPointer下的-KL散度-应该是怎样的.md
source_ids:
  - "9039"
status: draft
updated: 2026-06-10
---

# article-9039: GlobalPointer下的"KL散度"应该是怎样的？

## 文章核心问题
GlobalPointer 的预测结果并非概率分布（其损失函数是多标签交叉熵），无法直接计算 KL 散度。如何在 GlobalPointer 中应用 R-Drop 或虚拟对抗训练等需要 KL 散度的正则化方法？

## 主要结论
1. 对于标准的 Softmax 分类，对称 KL 散度可以简化为 logits 层面的内积形式 $D(s, t) = \langle f(s) - f(t), s - t \rangle$，其中 $f$ 是 Softmax（即 onehot(argmax) 的光滑近似）。
2. 将这一视角类比到 GlobalPointer：其输出目标是所有 logits 大于 0 的类别，因此应将 Softmax 替换为 sigmoid 函数 $\sigma(x) = 1/(1+e^{-x})$（即"大于0置1、小于0置0"的光滑近似），得到 $D(s, t) = \langle \sigma(s) - \sigma(t), s - t \rangle$。
3. 该形式等价于将各维度视为独立的二分类问题，分别计算二元分布的 KL 散度后求和。这种等价性表明，虽然多标签分类中"拆分为多个二分类"会导致类别不平衡，但仅作为连续性评估的散度度量时不存在该问题。
4. 初步实验表明，使用此形式的 KL 散度将 R-Drop 应用到 GlobalPointer 中可带来轻微提升；而直接对 GlobalPointer 的 logits 做 Softmax 再算 KL 散度则效果不佳。

## 推导结构
- 从对称 KL 散度定义 $D(p,q) = KL(p\|q) + KL(q\|p)$ 出发，代入 $p_i = e^{s_i}/\sum_j e^{s_j}$，化简得到 logits 形式 $D(s,t) = \sum_i (p_i - q_i)(s_i - t_i)$
- 将 Softmax 视为 onehot(argmax) 的光滑近似，抽象出一般形式 $D(s,t) = \langle f(s) - f(t), s - t \rangle$
- 类比到 GlobalPointer：输出目标是所有 logits > 0 的类别，对应的光滑近似是 sigmoid
- 代入 sigmoid 得到 $D(s,t) = \langle \sigma(s) - \sigma(t), s - t \rangle$
- 验证该形式等价于各维度独立二分类 KL 散度之和：利用 $[\sigma(s_i), 1-\sigma(s_i)] = softmax([s_i, 0])$，代入前式即得

## 关键公式
- 对称 KL 散度：$D(p,q) = KL(p\|q) + KL(q\|p) = \sum_i (p_i - q_i)(\log p_i - \log q_i)$
- Softmax 下简化为 logits 形式：$D(s,t) = \sum_i (p_i - q_i)(s_i - t_i)$
- 抽象视角：$D(s,t) = \langle f(s) - f(t), s - t \rangle$，其中 $f = softmax$
- GlobalPointer 的 KL 散度：$D(s,t) = \langle \sigma(s) - \sigma(t), s - t \rangle$，其中 $\sigma(x) = 1/(1+e^{-x})$
- 等价性证明：$[\sigma(s_i), 1-\sigma(s_i)] = softmax([s_i, 0])$
