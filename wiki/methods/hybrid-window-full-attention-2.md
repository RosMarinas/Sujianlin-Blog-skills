---


type: method
operation_types:
  primary: Decompose / reduce dimension
  secondary: []
title: HWFA2 (HWFA + ReRoPE)
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
source_ids:
  - 9706
  - 9708
  - 9728
  - 9731
  - 9859
  - 9948
method_summary: HWFA2是HWFA（Hybrid Window-Full Attention）与ReRoPE的组合方案。
typical_structure: |
  1. 前L-1层使用Window Attention结合RoPE，设置适当窗口大小。
  2. 在深层（或中间部分层）插入f层Full Attention。
  3. 训练阶段，Full Attention层采用普通的RoPE位置编码。
  4. 推理阶段，Full Attention层无缝切换为ReRoPE以处理超长序列。
applicability: 需要兼顾大窗口长度外推能力与计算效率时，或者高维对象可以用低维结构近似时
examples:
  - [[article::9731]]
status: stable
updated: 2026-06-13
created: 2026-06-09
tags: 
related_articles: 
related_concepts: 
evidence_spans: 
  - ev::9731::原文提出HWFA与ReRoPE的组合“HWFA2”，即“L-1层Window RoPE Attention + f层Full RoPE/ReRoPE Attention”，并在实验部分指出 w64-f2 的组合能达到近乎最佳的长度外推效果且降低推理成本。
proposes: ""






---
## 适用问题
需要兼顾大窗口长度外推能力与计算效率时，或者高维对象可以用低维结构近似时。

## 核心变换
将全量注意力（Full Attention）的计算成本通过分解为“Window Attention + Full Attention”的混合层降低，并在训练和推理时切换不同位置编码（RoPE与ReRoPE），从而实现“训练低成本、推理长外推”的目标。

## 典型步骤
1. 前 $L-1$ 层使用 Window Attention 结合 RoPE，设置适当的窗口大小 $w$（例如 $N/L$ 的2~4倍）。
2. 在第 $L$ 层（或中间部分层）插入 $f$ 层 Full Attention（无窗口限制）。
3. 训练阶段，Full Attention 层采用普通的 RoPE 位置编码。
4. 推理阶段，Full Attention 层无缝切换为 ReRoPE，利用其优异的外推性质处理超长序列。

## 直觉
HWFA 的思路是通过局部窗口提取局部特征，而在个别全局层提取全局特征；ReRoPE 的特点是外推能力极强但推理计算成本高。将二者强强联合，大部分层（局部层）享受了 Window Attention 的极低计算成本，只有少数全局层引入 ReRoPE，既保留了全局长度外推能力，又削弱了额外推理开销。

## 边界
由于只在少部分层保留了 Full Attention，如果任务高度依赖每一层的全局信息交互，可能出现性能瓶颈；窗口大小 $w$ 需根据序列长度和层数的比例设置，存在超参调整的依赖。

## 例子
在长度 $N=512$ 和层数 $L=24$ 的模型中，最佳参数为 $w=64$ 且 $f=2$。其训练效果与不重复的外推效果均超过了原本单用的 ReRoPE。

## 证据
- ev::9731::原文提出HWFA与ReRoPE的组合“HWFA2”，即“训练阶段将HWFA原本的Full NoPE Attention换成Full RoPE Attention，然后推理阶段则改为Full ReRoPE Attention”，以及“Window Attention的感受野可以适当取大一些...得益于ReRoPE，长度外推能力并不会有所下降”。
