---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Short Conv键值异源化方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
  - 11320
method_summary: 在线性Attention的K（以及Q/V）前加Short Conv（kernel_size=2），将TTT框架中(K,V)配对从"预测自己"(k_t,v_t)转化为NTP式"预测周围"(k_{t-1},v_t)，解决键值同源导致的表达能力瓶颈。
typical_structure: |
  1. 在计算注意力机制前，获得输入序列的特征映射表示序列。
  2. 对 Key 的特征序列（也可包含 Query 和 Value）应用一个核大小为2的短卷积（Short Conv）。
  3. 通过短卷积，将当前步的 $k_t$ 与前一步的 $k_{t-1}$ 混合，形成具备历史视野的新 Key。
  4. 将混合后的新 Key 与当前步的 Value 组成配对 $(k'_{t}, v_t)$，输入 TTT 等线性模型框架进行在线学习更新，从而将任务转化为"用历史/周围信息预测当前值"。
applicability: 适用于构建基于在线学习（Test Time Training, RNN 等）的线性注意力模型，解决由于 Q, K, V 同源导致在线回归模型缺乏有效学习信号而退化（恒等映射）的问题。
evidence_spans:
  - ev::11320::"在TTT中我们也可以考虑NTP，比如$(k_{t-1},v_t)$来构建语料对...进一步的想法是把$k_{t-1}$和$k_t$以某种方式混合起来...这不就相当于kernel_size=2的Conv嘛！"
  - ev::11320::"给K加Short Conv，是将TTT的训练目标从“预测自己”转化为NTP"
  - ev::11320::"给Q,V加Short Conv，则完全是顺带的...给Q,V加虽然也有一点作用，但远不如给K加Short Conv带来的提升"
examples:
  - [[article::11320]]
status: stable
updated: 2026-06-12
created: 2026-06-10
tags: 
related_articles: 
related_concepts: 
proposes: 
---

# Short Conv键值异源化方法

## 适用问题

在设计线性注意力（Linear Attention）和状态空间模型（如基于 Test Time Training 的 DeltaNet、GDN 等）时，模型将 Key 和 Value 视为在线学习的训练集配对。由于标准的 Transformer 机制中 $k_t$ 和 $v_t$ 均是由同一个输入 $x_t$ 线性投影而来，两者高度同源。如果直接让模型学习 $v_t = f(k_t)$，会导致学习目标退化为近乎无意义的恒等映射（“自己预测自己”），大大限制了模型的表达能力与压缩效率。

## 核心变换

改变在线回归/记忆的配对形式，通过在 Key 序列之前插入一个小卷积核（通常为 `kernel_size=2`）的 1D 卷积（Short Conv），将记忆配对从同时间步的同源预测 $(k_t, v_t)$ 重写（变换）为融合了前序上下文的错位预测 $(Mix(k_{t-1}, k_t), v_t)$。这使得内部的压缩机制转变为“预测周围/Next Token Prediction”，打破了同源带来的平凡解瓶颈。

## 典型步骤

1. 在计算注意力机制的投影层之后，获得输入序列的 $K$（以及可选的 $Q, V$）表示。
2. 对 $K$ 的特征序列沿时间维度应用一个核大小为 2 的 1D 短卷积（Short Conv），在计算第 $t$ 步时融合第 $t-1$ 步与第 $t$ 步的信息。
3. 利用得到的具有“周围”信息的混合 $k'_t$ 与 $v_t$ 组成训练配对 $(k'_t, v_t)$。
4. 将该配对送入 TTT 框架（在线优化器或 RNN 迭代），使得隐藏状态 $S_t$ 的更新变成一个用前文线索回归当前值的实质性学习任务。
5. （可选）对 $Q$ 和 $V$ 施加同样的短卷积以保持特征空间尺度的对齐。

## 直觉

我们可以把 TTT 框架下的线性注意力想象成一个一边阅读一边自我训练的小网络，它要用当前的 $k$ 去记住 $v$。如果 $k$ 和 $v$ 是一对龙凤胎（同源），小网络只要“照镜子”就能完成任务，它什么都没学到。要让它真正学到语言的规律并压缩到状态里，就必须像 Word2Vec 或 GPT 的 Next Token Prediction 一样，让它用“前一个词的样子”去猜“这个词的样子”。加一个窗口为 2 的短卷积，就是把前一个词的信息揉进当前词里，强迫小网络利用上下文去建立联系。

## 边界

- **因果约束限制**：短卷积必须是因果卷积（Causal Conv），即第 $t$ 步只能看到 $t$ 及其之前的特征，否则在自回归生成时会泄露未来信息。
- **算力分配不对等**：实验发现，对 Key 加入 Short Conv 的收益是决定性的，因为它是破除“恒等回归”的关键；而对 Query 和 Value 加入 Short Conv 收益微弱且可能徒增显存开销和推理延迟。

## 例子

在 DeltaNet 中，如果将 $\boldsymbol{K} = \boldsymbol{V}$，此时内部在线模型的最佳解直接就是单位矩阵 $I$，网络无需更新状态即可最小化误差，模型失效。但如果在 $\boldsymbol{K}$ 上应用了因果的核大小为2的短卷积（例如：$k'_t = 0.5 k_t + 0.5 k_{t-1}$），此时由于需要用包含 $k_{t-1}$ 的特征去预测 $v_t$（等于 $k_t$），在线学习任务就从“自己猜自己”变成了“用昨天和今天猜明天”，模型必须在状态矩阵 $S_t$ 中切实记忆序列间的转移模式，从而恢复并提升了线性注意力的建模能力。

## 证据

- ev::11320::"给K加Short Conv，是将TTT的训练目标从“预测自己”转化为NTP，让TTT至少有能力学出一个n-gram模型。"
- ev::11320::"在TTT中我们也可以考虑NTP，比如$(k_{t-1},v_t)$来构建语料对...把$k_{t-1}$和$k_t$以某种方式混合起来...相当于kernel_size=2的Conv"
- ev::11320::"根据飞来阁（FLA群）的消息，给$Q,V$加虽然也有一点作用，但远不如给$K$加Short Conv带来的提升"
