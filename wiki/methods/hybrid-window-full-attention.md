---


type: method
operation_types:
  primary: Decompose / reduce dimension
  secondary: []
title: Hybrid Window-Full Attention
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-12-Transformer升级之路-9-一种全局长度外推的新思路.md
source_ids:
  - 9603
method_summary: 混合窗口-全注意力机制：在浅层使用窗口注意力保持局部外推能力，在深层某一层使用无位置编码的全注意力捕获全局依赖，兼顾长度外推和序列建模质量。
typical_structure: |
  1. 将前 L-1 层设置为带有 RoPE 的 Window Attention。
  2. 约束窗口大小使得总感受野不超过训练文本长度。
  3. 将第 L 层设置为不带 RoPE 但带有 log n 缩放因子的 Full Attention。
  4. 训练并在长序列上直接进行推理。
applicability: 高维对象可以用低维结构近似时，特别是需要兼顾长序列外推与全局依赖的模型设计。
examples:
  - [[article::9603]]
status: stable
updated: 2026-06-13
evidence_spans: 
  - ev::9603::提出HWFA结构：“1、前面L-1层使用Window为w的‘Window Attention+RoPE’... 2、第L层使用带 \log n 因子的Full Attention，但是不使用RoPE。”
---





## 适用问题
高维对象可以用低维结构近似时，特别是需要兼顾长序列外推与全局依赖（如 In Context Learning）的自回归模型或双向编码器模型。

## 核心变换
将所有层的全量注意力（Full Attention）解耦为局部和全局层：浅层执行带 RoPE 的 Window Attention 提取局部特征，而在最深层执行不带 RoPE 的 Full Attention 聚合全局特征，并将全局感受野上限控制在训练长度之内。

## 典型步骤
1. 将前 $L-1$ 层设置为带有 RoPE 的 Window Attention，窗口大小设为 $w$。
2. 约束窗口大小，使得 $(w-1)(L-1)+1 \le \alpha N$（$N$为训练长度，$\alpha \le 1$），保证总感受野不超越训练长度。
3. 将第 $L$ 层设置为 Full Attention，去除 RoPE 位置编码，并加上 $\log n$ 缩放因子。
4. 使用标准训练过程并在超长序列上进行外推测试。

## 直觉
Window Attention 层总感受野不超过训练长度，这强制了注意力机制的平移不变性，使得特征不受绝对位置干扰（“独立同分布”的局部特征）；最后一层的 Full Attention 则像全局池化，对这些独立同分布特征进行全局的检索与聚合。由于该层不包含会受长度外推限制的绝对位置信号，它可以稳定地扩展到比训练长度长得多的序列上。

## 边界
在原版 HWFA 中，Window 感受野必须严格满足 $(w-1)(L-1)+1 \le \alpha N$ 的约束。这意味着当模型层数较多或者训练长度较短时，每层的窗口大小 $w$ 会变得非常小，这会一定程度上牺牲模型的拟合能力（训练准确率）。

## 例子
在长度 $N=512$ 和层数 $L=24$ 的模型中，将前 23 层设为 Window Attention 且 $w=16$，第 24 层使用无位置编码并带缩放的 Full Attention，结果在 4096 长度的测试中取得了优异的全局外推精度。

## 证据
- ev::9603::提出组合方式：“前面L-1层使用Window为w的‘Window Attention+RoPE’，满足约束...第L层使用带 \log n 因子的Full Attention，但是不使用RoPE。”
- ev::9603::提到其逻辑来源：“单层的Full Attention可以看作是某种‘检索’和‘融合’...单层（全）注意力可以通过增加 \log n 缩放因子来增强长度外推性”。
