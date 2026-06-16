---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Attention Residuals层间注意力方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-03-19-Attention-Residuals-回忆录.md
source_ids:
  - 11664
method_summary: "把残差流中的等权层间累加推广为对历史层状态的 Attention 加权求和，用层间注意力替代固定 residual 汇聚。"
typical_structure: |
  1. 计算当前层或当前块的候选输出特征。
  2. 对历史层的所有特征应用 RMSNorm。
  3. 使用固定的静态权重向量与所有历史层的特征进行内积操作，计算相应的层间注意力权重。
  4. 基于计算出的注意力权重，将所有历史层和当前层的特征进行加权求和，取代简单的残差等权相加。
  5. 可选：对网络层进行分块（Block），块内求和压缩，块间进行注意力加权以降低显存和计算开销。
applicability: "在极深网络中，传统残差连接不足以提供最有的层间信息流动，或者期望进一步通过增强特征复用以换取性能提升时。"
examples:
  - "[[article::11664]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::11664::一个自然的推广就是换成加权求和：y_{t+1} = f_{t+1}( \\sum_{s=0}^t a_{t+1,s}y_s ) ... 终版的AttnRes形式 a_{t+1,s} \\propto \\exp(w_{t+1}\\cdot RMSNorm(y_s))。"
---

# Attention Residuals层间注意力方法

## 适用问题
在深层网络中，如何通过替换传统的残差连接（Residuals）来提供更灵活和自适应的层间历史信息复用，进而获得更强的模型表达能力？

## 核心变换
将传统的残差等权相加 $\boldsymbol{x}_t = \boldsymbol{x}_{t-1} + \boldsymbol{f}_t(\boldsymbol{x}_{t-1})$ 重写为历史状态输出的加权求和形式，并使用层间注意力计算这些权重：
$$ \boldsymbol{y}_{t+1} = \boldsymbol{f}_{t+1}\left(\sum_{s=0}^t a_{t+1,s}\boldsymbol{y}_s\right), \quad a_{t+1,s} \propto \exp(\boldsymbol{w}_{t+1}\cdot \mathop{\text{RMSNorm}}(\boldsymbol{y}_s)) $$
其中 $\boldsymbol{w}_{t+1}$ 为可训练的静态 Q 向量。

## 典型步骤
1. 计算当前层或当前块的候选输出特征。
2. 对历史层的所有特征应用 RMSNorm。
3. 使用固定的静态权重向量与所有历史层的特征进行内积操作，计算相应的层间注意力权重。
4. 基于计算出的注意力权重，将所有历史层和当前层的特征进行加权求和，取代简单的残差等权相加。
5. 可选：对网络层进行分块（Block），块内求和压缩，块间进行注意力加权以降低显存和计算开销。

## 直觉
传统残差连接等价于所有历史层输出等权求和。通过层间 Attention，模型可以自适应地选择关注哪些历史层的特征。为了确保对历史层输出复用的同向性和计算的稳定性，要求这些注意力系数必须非负并且加和为 1。使用静态参数代替动态 $Q$ 还能实现推理阶段注意力系数的提前计算，优化显存。

## 边界
完整版（Full AttnRes）在网络很深时会大幅度增加通信量和显存开销，由于涉及到跨所有前面层的计算，这对 Infra 也是挑战。而即便通过分块压缩降低了开销，也会牺牲极少部分的精度提升，其超参数（如分多少个 Block）也需要调试。

## 例子
将模型按照深度的每 $m$ 层作为一个 Block。在每个 Block 内特征通过简单的加权求和进行压缩，然后使用预训练的静态向量作为 Q，跨越不同的 Block 进行注意力计算并融合结果送入下一个阶段。

## 证据
- 11664 提到，AttnRes 将等权求和推广为加权求和，其终版形式通过引入静态 $\boldsymbol{w}_{t+1}$ 来充当 Q 计算注意力 $\exp(\boldsymbol{w}_{t+1}\cdot \mathop{\text{RMSNorm}}(\boldsymbol{y}_s))$，并在 Block AttnRes 版中将层分组降低开销。
