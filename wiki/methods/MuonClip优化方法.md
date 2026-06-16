---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: MuonClip优化方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-02-27-Muon续集-为什么我们选择尝试Muon.md
source_ids:
  - 11126
method_summary: 将 Muon 谱范数最速下降优化器（包含动量、Update RMS 对齐及 Weight Decay）与 QK-Clip 权重局部裁剪相结合，构成大规模多模态/大语言模型的高稳定训练更新规则。
typical_structure: |
  1. 在每一步优化器（例如Muon）更新参数后，监控每一层、每个Attention Head的MaxLogit $S_{max}^{(l,h)}$。
  2. 若某个Head的MaxLogit超过设定的阈值 $\tau$（如100），则对引发该爆炸的 $\boldsymbol{Q}, \boldsymbol{K}$ 权重实施裁剪。
  3. 对于参与乘积的 $W_{qc}, W_{kc}$，分别乘以 $\sqrt{\tau / S_{max}}$。对于单侧相关的 $W_{qr}$，直接乘以 $\tau / S_{max}$。
  4. 继续训练，通过持续的QK-Clip抵消优化器导致的谱范数扩张，直到模型自身稳定。
applicability: 适用于追求极高收敛速度但极易在大参数量发生注意力谱范数（MaxLogit）爆炸的多模态及大语言模型预训练阶段。
examples:
  - [[article::11126]]
evidence_spans:
  - ev::11126::提出了通过事后监控MaxLogit并直接按比例裁剪Q、K权重（QK-Clip）来避免Muon在Scaleup时导致的MaxLogit爆炸问题。
status: stable
updated: 2026-06-12
---

# MuonClip优化方法

## 适用问题
适用于追求极高收敛速度但极易在大参数量发生注意力谱范数（MaxLogit）爆炸的多模态及大语言模型预训练阶段。传统降低LR或增加Weight Decay会导致性能惩罚，而softcap不能根本压制权重谱范数。

## 核心变换
将对Loss的常规梯度下降与针对模型状态监控信号（MaxLogit）的硬性重标定（Weight Scaling）组合，形成一种拉锯式的鲁棒更新轨道。

## 典型步骤
1. 在每一步优化器（例如Muon）更新参数后，监控每一层、每个Attention Head的MaxLogit $S_{max}^{(l,h)}$。
2. 若某个Head的MaxLogit超过设定的阈值 $\tau$（如100），则定位该Head负责投影的 $\boldsymbol{Q}, \boldsymbol{K}$ 权重实施裁剪。
3. 对于参与特征点积的权重 $W_{qc}, W_{kc}$，分别乘上缩放系数 $\sqrt{\tau / S_{max}}$；对于无需配对的 $W_{qr}$，直接乘上 $\tau / S_{max}$。
4. 继续训练循环。QK-Clip通过拉锯战阻止模型前期的过度发散，后期随着Weight Decay的积累模型主动回落，Clip机制自然退出。

## 直觉
既然MaxLogit是由Q和K的矩阵相乘产生的极大内积，且容易在像Muon这种全秩极分解驱动下导致奇异值过大（谱范数爆炸），与其在优化器层面盲猜参数调整，不如当发现MaxLogit触及报警红线时，直接把底层的相关权重砍掉一个比例（“哪里不稳Clip哪里”），这就好比吃了立竿见影的“抗生素”。

## 边界
在分布式训练下，由于注意力权重的切分（如Tensor Parallelism），要进行精细的 Per-Head Clip 会引发一定的通信与实现复杂度；它仅在参数规模巨大的LLM上才表现出强烈的必须性。

## 例子
万亿参数模型 Kimi K2 的训练中，通过融合Muon的 0.2 Update RMS 和阈值设为100的 QK-Clip 构成 MuonClip，在70k steps前双方处于激烈拉锯抗衡，之后自然平息，免除了模型发散危机。

## 证据
- ev::11126::提出了通过事后监控MaxLogit并直接按比例裁剪Q、K权重（QK-Clip）来避免Muon在Scaleup时导致的MaxLogit爆炸问题。