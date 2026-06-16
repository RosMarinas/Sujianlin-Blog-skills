---


type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: Leaky ReRoPE分段线性外推方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
  - Data/（待从源文章提取）
source_ids:
  - 9708
  - 9728
  - 9948
method_summary: Leaky ReRoPE是ReRoPE的一般化，在局部窗口w内保持标准相对位置步长1，在窗口外使用更小的步长1/k进行相对位置压缩，实现了受控的、性能较优的长度外推。
typical_structure: |
  1. 定义参数 $w$（通常取训练长度的 $1/4$）作为局部窗口大小，定义 $k$ 决定窗口外的压缩步长。
  2. 计算标准相对位置矩阵（步长=1）的第一注意力分量 $a^{(1)}_{i,j}$。
  3. 计算窗口外压缩位置矩阵（步长=1/k）的第二注意力分量 $a^{(2)}_{i,j}$。
  4. 进行分段合并：在 $i-j < w$ 时取 $a^{(1)}$，在 $i-j \ge w$ 时取 $a^{(2)}$。
applicability: 在使用 RoPE 的 LLM 中进行长序列外推测试，既希望兼顾 ReRoPE 优异的局部精确性，又希望利用可控的位置内插压缩更长范围的长距离语义的情况。
examples:
  - [[article::9708]]
  - [[article::9728]]
status: stable
updated: 2026-06-13
created: 2026-06-09
tags: 
related_articles: 
related_concepts: 
evidence_spans: 
  - ev::9708::提出将窗口外的位置差异不再固定为常数而是按比例映射（即类比 Leaky ReLU），引入了参数 $k$。
  - ev::9708::对比实验证明 Leaky ReRoPE w128-k16+log n 在 4096 测试达到极高精度。
---






## 适用问题
基于 RoPE 的大型语言模型要在不重新训练、免微调（Zero-shot）的前提下，实现超出训练长度的大幅度长度外推，同时解决纯 ReRoPE 无法区分极远距离 Token 相对先后顺序的局限。

## 核心变换
将 ReRoPE 里面“超出窗口长度 $w$ 后距离强制截断固定”的平坦设计（类似 ReLU 截断部分），重写为带有小斜率**分段线性位置映射**的设计（类似 Leaky ReLU）。使得超出 $w$ 之外的相对位置，以 $1/k$ 的微小步长继续被计算和区分。

## 典型步骤
1. **参数配置**：选定局部窗口阈值 $w$（建议等于训练长度 $L_{train}/4$），以及步长收缩倍数 $k$。$k$ 的设置经验是：使得最大预测范围 $w + (L_{test}-1-w)/k$ 的结果不超过 $L_{train}/2$。
2. **算子一计算**：使用正常相对位置差 $j-i$（即步长 1），计算标准的 RoPE Attention 矩阵 $a^{(1)}_{i,j} = q_i^\top R_{j-i} k_j$。
3. **算子二计算**：对所有的相对位置施加压缩，新的相对位置定义为 $(j-i-w)/k + w$。计算压缩后的 Attention 矩阵 $a^{(2)}_{i,j}$。
4. **按条件拼装**：构建掩码（Mask）进行硬拼接。对于相对距离 $< w$ 的区域，取 $a^{(1)}_{i,j}$ 的值；对于相对距离 $\ge w$ 的区域，取 $a^{(2)}_{i,j}$ 的值。
5. 最后再正常地计算 Softmax 与 Value 乘积输出。

## 直觉
在语言阅读理解中，附近的词汇（$w$ 范围内）对我们具有极强的逐字位置敏感性，不能有丝毫变形；而很久以前发生的事（$w$ 范围外），我们通常只记得其宽泛的轮廓和彼此间的粗略前后顺序，不需要像近距离那样精确。Leaky ReRoPE 就是赋予了模型这种认知逻辑：近处依然是 1 倍分辨率（不糊），远处缩放成 1/16 分辨率（有损但位置不至于完全越界和停滞）。它通过分段线性映射把整个超长文本的相对关系都挤进了模型本来就认识的训练长度“盒子”里。

## 边界
不同于 ReRoPE 在理论上宣称的“无尽头外推”，Leaky ReRoPE 由于引入了随距离增长的 $1/k$ 斜率，因此当输入极端长的时候，压缩后的值终究会越界（超过训练期间见过的最大位置），导致效果断崖式下跌。它需要预先预估并设置 $k$ 来应对给定的目标测试长度。此外，推理阶段仍然需要算两次 Attention 分量并进行拼接，没有解决 ReRoPE 拖慢推理计算的工程实现难点。

## 例子
对于训练长度 512 的模型，想要它不微调就能阅读 4096 长度的文档。设置 $w=128, k=16$。那么对于距离它 100 的 token，模型使用距离 100 进行注意力交互；对于距离它 4000 的 token，模型会把它的有效相对距离计算为 $128 + (4000-128)/16 \approx 370$。这让模型觉得 4000 远处的 token 只是在这个 512 框架里的第 370 个位置，从而能平稳调用注意力，准确率依然可维持在 49% 以上。

## 证据
- ev::9708::提出将窗口外的位置差异保留：“就像ReLU和Leaky ReLU的区别那样...超出w的部分，我们不用全部强制等于w，而是将它们的差异以小步长保留下来，即按比例压缩”。
- ev::9708::明确了参数指导思想：“如果为了得到更好的外推效果，我们需要保证$w+(L-1-w)/k$不超过$L_{train}/2$左右”。
- ev::9708::对比实验证明有效性：“w128-k16+log n 在 4096 测试达到 49.10%”，超越纯粹的位置截断。
