---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: NTK-aware Scaled RoPE
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-06-Transformer升级之路-10-RoPE是一种β进制编码.md
source_ids:
  - 9675
method_summary: 借用进制编码和NTK理论的直觉，通过改变RoPE的基数（Base），使得高频基向量保持外推，低频基向量近似内插，从而实现LLM免微调的长文本窗口扩展。
typical_structure: |
  1. 计算目标扩展倍数 $k$。
  2. 根据公式 $\lambda = k^{2/(d-2)}$ 得到伸缩因子 $\lambda$。
  3. 将原始RoPE的底数 $\beta$ 缩放为 $\beta \lambda$（或直接换为 $\beta \cdot k^{2/d}$）。
  4. 将原本的频率 $\frac{n}{\beta^i}$ 替换为 $\frac{n}{(\beta \lambda)^i}$ 进行后续的位置编码计算。
applicability: 需要强制系统满足某种变换不变性（如缩放、旋转）以稳定训练时，特别是扩展大语言模型上下文长度且无长文本微调资源时。
examples:
  - [[article::9675]]
evidence_spans:
  - ev::9675::指出RoPE本质是一种β进制编码，介绍了如何通过改变进制底数实现“高频外推、低频内插”的NTK-aware Scaled RoPE机制。
status: stable
updated: 2026-06-12
---

# NTK-aware Scaled RoPE

## 适用问题
需要强制系统满足某种变换不变性（如缩放、旋转）以稳定训练时，特别是扩展大语言模型上下文长度且无长文本微调资源时。标准的截断外推会引发未训练位置崩溃，而全局内插破坏了临近语义距离的微观尺度。

## 核心变换
将进制编码机制下的底数放大，把单纯在外部空间的硬裁切转换为“高频保持绝对差异（外推），低频压缩绝对距离（内插）”的频率融合缩放变换。

## 典型步骤
1. 计算目标扩展倍数 $k$。
2. 根据公式 $\lambda = k^{2/(d-2)}$ 得到伸缩因子 $\lambda$。
3. 将原始RoPE的底数 $\beta$ 缩放为 $\beta \lambda$（或近似等价地直接换为 $\beta \cdot k^{2/d}$）。
4. 将原本的频率 $\frac{n}{\beta^i}$ 替换为 $\frac{n}{(\beta \lambda)^i}$ 进行后续的位置编码计算。

## 直觉
RoPE本质上是将位置 $n$ 进行一种 $\beta$ 进制编码。如果要表示更大的范围，最优雅的办法不是挤压原本的数字分布（纯内插），也不是增加新的不熟悉的数位（纯外推），而是稍微调大使用的“进制基底”。这使得靠近个位（高频）的表示变化极小，能够维持原本学到的精细局部比较；而越靠近高位（低频），缩放效应叠加越明显，从而将庞大的大数字塞回熟悉的训练范围内。

## 边界
免微调虽然能解决崩溃和长度泛化，但模型长距离的注意力可能不够集中，外加微调效果更佳；对于极端倍数的扩充（如100倍），仅仅调整底数可能导致中低频重叠紊乱。

## 例子
模型原本支持 1000 长度。想要提升到 8000 ($k=8$) 且不微调。只要将 RoPE 算法里的 base $10000$ 更新为 $10000 \cdot \lambda \approx 10000 \cdot 8^{2/d}$ 就能让旧模型直接理解新长度。

## 证据
- ev::9675::指出RoPE本质是一种β进制编码，介绍了如何通过改变进制底数实现“高频外推、低频内插”的NTK-aware Scaled RoPE机制。
