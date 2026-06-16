---


type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: KERPLE
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
source_ids:
  - 9431
method_summary: KERPLE 是一种核化相对位置编码方法，它推广了 ALIBI，通过引入可训练参数使距离惩罚呈幂律或对数形式，以增强 Transformer 的局部注意力约束和长度外推能力。
typical_structure: |
  1. 在计算 Attention 的 Softmax 之前，对注意力分数减去一个基于距离的偏置项。
  2. 使用可训练参数 $r_1, r_2$ 定义惩罚函数。
  3. 惩罚函数可设计为幂律形式：$r_1|m - n|^{r_2}$。
  4. 或对数形式：$r_1\log(1+r_2|m - n|)$。
applicability: 需要提升 Transformer 长度外推能力，且认为简单的线性距离惩罚（如 ALIBI）不足以提供最佳注意力局部性退化速度的情况。
examples:
  - [[article::9431]]
status: stable
updated: 2026-06-13
evidence_spans: 
  - ev::9431::苏剑林指出 KERPLE 实质上就是 ALIBI 的简单推广，它引入了两个训练参数 r_1, r_2 来一般化衰减项。
---





## 适用问题
在 Transformer 架构中提升模型对长序列的泛化外推能力，尤其是改进基于简单线性偏置（ALIBI）的注意力惩罚方案，以期寻找更优的相对距离衰减率。

## 核心变换
在计算 Attention Score 时，改变 ALIBI 将查询和键之间距离绝对值作为线性偏置减去的做法，转而引入包含可训练参数的**非线性核化惩罚**（Kernelized relative positional embedding），例如幂律（Power-law）或对数（Logarithmic）距离惩罚。

## 典型步骤
1. 计算查询和键的标准内积注意力分数 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$。
2. 定义带可训练参数 $r_1, r_2$ 的核惩罚函数（确保 $r_1, r_2 > 0$）：
   - 幂律形式：$f(m, n) = r_1|m - n|^{r_2}$，其中 $r_2 \leq 2$；
   - 对数形式：$f(m, n) = r_1\log(1+r_2|m - n|)$。
3. 在进行 Softmax 归一化之前，将上述分数减去核惩罚项。
4. 在训练过程中让模型自动学习 $r_1, r_2$ 以决定不同头部对距离的敏感度衰减速率。

## 直觉
对于语言模型，距离较远的 Token 提供的相关性信息通常较低，因此 ALIBI 提出随着距离增加按比例减少注意力分数。但“线性衰减”未必是真实语言依赖的最优形式。KERPLE 通过引入对数或指数的形式并增加可训练缩放系数，让模型自我寻找一种衰减速度的“甜蜜点”，这本质上是用非线性放宽了 ALIBI 的严格局部化假设。

## 边界
虽然引入了参数使模型更具普适性并获得了指标上的略微提升，但这也增加了训练过程的微小成本。此外，与 ALIBI 一样，对于依赖纯双向注意力（无需严格左右区分）且确实需要极其长程依赖的任务，依然存在由于惩罚导致丢失全局信息的风险。

## 例子
单向语言模型在采用 KERPLE 对数惩罚形式进行训练后，模型能推断比训练时长度长得多的输入序列而不发生困惑度的灾难性崩溃。

## 证据
- ev::9431::文章提到：“KERPLE...实质上就是ALIBI的简单推广，它引入了两个训练参数 $r_1,r_2$ 来一般化”。
- ev::9431::引用了其公式形式：“$\boldsymbol{q}_m^{\top}\boldsymbol{k}_n - r_1|m - n|^{r_2}$”和“$\boldsymbol{q}_m^{\top}\boldsymbol{k}_n - r_1\log(1+r_2|m - n|)$”。
