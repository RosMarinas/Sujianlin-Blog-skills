---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: XPOS
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
source_ids:
  - 8373
  - 9431
method_summary: 在 RoPE 旋转位置编码基础上为查询和键引入不对称的指数衰减因子，使得长距离注意力自动趋近于零，大幅增强语言模型的长度外推能力。
typical_structure: |
  1. 将输入序列映射为查询（Query）和键（Key）向量 $\boldsymbol{q}_m, \boldsymbol{k}_n$。
  2. 根据当前词的绝对位置 $m$ 和 $n$，计算对应的旋转变换矩阵 $\boldsymbol{\mathcal{R}}_m, \boldsymbol{\mathcal{R}}_n$。
  3. 定义一个标量超参数 $\xi \in (0, 1)$。
  4. 对 Query 施加正向指数缩放：$\boldsymbol{q}_m\to \boldsymbol{\mathcal{R}}_m\boldsymbol{q}_m \xi^m$。
  5. 对 Key 施加反向指数缩放：$\boldsymbol{k}_n\to \boldsymbol{\mathcal{R}}_n\boldsymbol{k}_n \xi^{-n}$。
  6. 在自注意力点乘计算中，两项相乘得到只依赖相对距离的带衰减的注意力分数：$\boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n \xi^{m-n}$。
applicability: 单向自回归语言模型（如 GPT 架构）需要获得超越训练序列长度的长文本泛化（外推）能力时。
evidence_spans:
  - ev::9431::"单从“绝对位置实现相对位置”角度来看，并没有必要限制两者的变换格式一致，比如XPOS考虑的是...总的结果依然是只依赖于相对位置m-n的"
  - ev::9431::"XPOS的机智之处是它选择了跟很多相关工作一样选定了场景——只关注单向语言模型——这样一来我们只会用到m>=n部分的注意力！此时只需要选择xi in (0,1)，就可以实现随着相对距离衰减的效果"
examples:
  - [[article::9431]]
status: stable
updated: 2026-06-13
---

# XPOS

## 适用问题

在基于 Transformer 的大型语言模型中，直接使用绝对位置编码或 RoPE（旋转位置编码）在面对超过训练长度的长文本（长度外推）时，性能往往会断崖式下降。模型在长序列中产生的无序注意力熵过大，需要一种手段能够“局部化”注意力，使得模型自发忽略遥远的历史，仅对临近上下文保持高关注。

## 核心变换

将 RoPE 原本严格对称的“查询-键”旋转操作，变换为非对称的“旋转加指数放缩”映射。由于单向语言模型天然满足 $m \geq n$（只能看历史），通过强行引入随相对距离 $m-n$ 单调递减的指数因子 $\xi^{m-n}$，将注意力计算强行打入“局部关注”的几何范畴。

## 典型步骤

1. **分离旋转与缩放**：继承 RoPE 的核心思想，利用二维平面旋转矩阵 $\boldsymbol{\mathcal{R}}$ 来注入位置信息。
2. **施加非对称底数**：选取一组小于 1 的底数向量 $\xi \in (0, 1)$。
3. **Query 变基**：对当前步 $m$ 产生的 $\boldsymbol{q}_m$，除了乘上 $\boldsymbol{\mathcal{R}}_m$ 外，再乘上衰减系数 $\xi^m$。
4. **Key 变基**：对历史步 $n$ 产生的 $\boldsymbol{k}_n$，除了乘上 $\boldsymbol{\mathcal{R}}_n$ 外，再乘上反向衰减系数 $\xi^{-n}$。
5. **内积计算**：当两者做点积操作 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$ 时，不仅旋转矩阵合成为只依赖相对距离的 $\boldsymbol{\mathcal{R}}_{m-n}$，两者的衰减系数也恰好消去位置基数，合并为单纯的相对衰减因子 $\xi^{m-n}$。

## 直觉

我们希望远处的 Token 对当前计算注意力的影响微乎其微。既然模型只做因果预测（即当前词位置 $m$ 肯定大于等于历史词位置 $n$），那 $m-n$ 一定是个非负数。如果我们在算 $Q$ 的时候强行压小（乘以很小的小数 $\xi^m$），在算 $K$ 的时候强行放大（除以同一个小数 $\xi^{-n}$），最终做乘法时，多出来的部分正好是 $\xi^{m-n}$。相对距离 $m-n$ 越大，这个数就越接近零，相当于我们顺滑地给远处的历史套上了一层“近视滤镜”，这就巧妙达到了局部注意力的效果。

## 边界

- **无法用于双向模型**：XPOS 的核心前提是 $m \geq n$，若用在类似 BERT 的双向注意力机制中，由于未来词 $m < n$，指数项 $\xi^{m-n}$ 将变为负幂次从而产生严重发散问题。
- **溢出风险**：由于 Key 是乘以 $\xi^{-n}$ 也就是一个随位置指数增长的巨大数，当序列长度 $n$ 达到上万时，若 $\xi$ 控制不当极易导致数值溢出（FP16下更明显），工程实现中需要特殊的数值稳定性处理。

## 例子

在语言模型外推任务中，我们将长文本预测任务的 Attention Score 设计为 $\boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n \xi^{m-n}$。如果 $\xi = 0.99$，那么对于仅相隔 1 个字的上下文，乘数为 $0.99^1 \approx 0.99$，几乎不受影响；而对于相隔 1000 个字的上下文，乘数变为 $0.99^{1000} \approx 0.00004$，此时 $K$ 提供的信息在 softmax 之前被极大压制，模型只用专注于近处的逻辑，从而实现了比原版 RoPE 长得多的外推能力。

## 证据

- ev::9431::"单从绝对位置实现相对位置角度来看，并没有必要限制两者的变换格式一致，比如XPOS考虑的是...总的结果依然是只依赖于相对位置m-n的"
- ev::9431::"XPOS的机智之处是它选择了跟很多相关工作一样选定了场景——只关注单向语言模型——这样一来我们只会用到m>=n部分的注意力！此时只需要选择xi in (0,1)，就可以实现随着相对距离衰减的效果"
