---

type: formula
title: AttnRes层间注意力公式
aliases:
- Attention Residuals Formula
latex: oldsymbol{y}_{t+1} = oldsymbol{f}_{t+1}\left(\sum_{s=0}^t a_{t+1,s}oldsymbol{y}_s
ight),
  \quad a_{t+1,s} \propto \exp(oldsymbol{w}_{t+1}\cdot \mathop{	ext{RMSNorm}}(oldsymbol{y}_s))
symbol_meanings:
  oldsymbol{y}_{t+1}: t+1 层的残差输出向量
  oldsymbol{f}_{t+1}: 第 t+1 层的前馈映射层（含In Norm）
  a_{t+1,s}: 层级注意力权重（归一化标量）
  oldsymbol{w}_{t+1}: 层特定的静态权重查询向量
standard_notation:
  convention: Follow AttnRes original paper. Static Q design (w_t is data-independent)
    is crucial for inference optimization.
conditions: RMSNorm使得加权求和与加权平均等价。a非负约束避免同向冲突。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-03-19-Attention-Residuals-回忆录.md
source_ids:
- '11664'
status: draft
updated: '2026-06-14'
appears_in:
- '11664'
---


# AttnRes层间注意力公式


## 概述

（待补充）

## 公式本体

```tex
oldsymbol{y}_{t+1} = oldsymbol{f}_{t+1}\left(\sum_{s=0}^t a_{t+1,s}oldsymbol{y}_s
ight), \quad a_{t+1,s} \propto \exp(oldsymbol{w}_{t+1}\cdot \mathop{	ext{RMSNorm}}(oldsymbol{y}_s))
```

## 成立条件

RMSNorm使得加权求和与加权平均等价。a非负约束避免同向冲突。

## 详细说明

AttnRes（Attention Residuals）层间注意力公式 $$oldsymbol{y}_{t+1} = oldsymbol{f}_{t+1}\left(\sum_{s=0}^t a_{t+1,s}oldsymbol{y}_s
ight)$$ 是一种对传统 Transformer 残差连接结构（Residuals）进行根本性升级的激进架构设计。与常规残差通过等权累加先前所有层输出的模式不同，AttnRes 引入了一个基于注意力的加权归一化系数 $a_{t+1,s}$，它由带有层级独立权重向量 $oldsymbol{w}_{t+1}$（充当静态 Query）与经过 $\mathop{	ext{RMSNorm}}$ 处理的 $oldsymbol{y}_s$（充当 Key/Value）的内积并经过指数映射决定。对注意力矩阵的非负性限制确保了底层输入信息能够沿着残差路径以同向的姿态传播至顶层；同时静态 Q 策略消除了前向查询时带来的冗余计算。在诸如 mHC 或 Block AttnRes 机制下，该层间密集连接不仅可避免梯度的过度消散，还能提供相比于恒等映射更为广阔的模型深层协同潜力。
