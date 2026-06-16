---
type: method
operation_types:
  primary: Decompose / reduce dimension
  secondary: []
title: 用结构约束线性化Attention计算
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
source_ids:
  - 6853
  - 7546
  - 8180
method_summary: 通过稀疏模式、核函数分解、低秩投影或Nyström三矩阵近似，避免显式构造全量n×n注意力矩阵。
typical_structure: |
  1. 识别计算瓶颈：标准的n×n的Q K^T自注意力点乘计算
  2. 引入结构化约束打破复杂度：定义稀疏化连接、核函数特征映射剥除Softmax或利用Nystrom进行低秩分解
  3. 执行可替换计算顺序的乘法（如先算K^T V，或计算小规模矩阵池化等近似解）
  4. 恢复所需语义并确保无显著表现退化
applicability: 适用于超长序列建模等自注意力复杂度由二次增长导致显存和计算时间不可接受的场景（如高维对象可以用低维结构近似时）。
related_methods: 
examples:
  - [[article::6853]]
  - [[article::7546]]
  - [[article::8180]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::6853::Sparse Attention引入局部和空洞稀疏约束避免计算全量自注意力
  - ev::7546::Linear Attention提出剥离Softmax并利用结合率先算K^TV来达成线性复杂度
  - ev::8180::Nyströmformer使用基于地标的自适应池化和低秩矩阵分解构造线性Attention
---

# 用结构约束线性化Attention计算

## 适用问题

标准的Transformer中的Scaled-Dot Attention在序列长度 $n$ 较大时，时间和空间复杂度呈 $\mathcal{O}(n^2)$ 增长，导致显存不足和运算过慢。当需要处理长文本或生成长序列时，必须通过有效结构替换来将复杂度降低至线性级 $\mathcal{O}(n)$。

## 核心变换

抛弃直接计算 $n \times n$ 的完整注意力相关度矩阵，转而引入“先验结构约束”。通过稀疏连接约束屏蔽非必要交互，或者通过代数结构的拆解（去掉或替换非线性Softmax操作使得矩阵乘法可结合、利用Nyström矩阵近似做低秩分解），从而改变计算顺序缩小计算规模。

## 典型步骤

1. **定位瓶颈对象**：确定完整 $n \times n$ 注意力矩阵为时间与空间的瓶颈。
2. **选择约束策略**：
   - **拓扑稀疏约束**：保留局部窗口或间隔式（Atrous）相关性。
   - **核方法约束**：移除Softmax，将Attention定义为两个经过激活函数映射的特征矩阵点乘。
   - **低秩矩阵分解约束**：使用 Nyström / CUR 方法，利用少量 Landmark 点逼近原矩阵。
3. **改变计算顺序**：
   - 若是代数分解：利用矩阵乘法结合律，优先计算 $d \times d$ 等较小维度矩阵。
   - 若是稀疏矩阵：跳过被Mask的零点。
4. **误差控制与语义对齐**：验证对齐语义，记录近似带来的潜在误差，确保方法模拟原始的长程相关度。

## 直觉

矩阵乘法在引入非线性的 Softmax 后被锁定为必须先算巨大的二元交互矩阵；只要能设计函数代替 Softmax 维持非负与概率特性，或者找到足够低维的信息枢纽（Landmark），即可利用矩阵乘法结合律，以 $\mathcal{O}(n)$ 的代价完成全局融合。

## 边界

- 稀疏约束通常会切断长程连续依赖，且没有底层CUDA算子优化往往无法实际加速。
- 采用低维聚类或下采样近似由于揉合了区间信息，会使得因果掩码（Causal Masking）失效，难以应用于自回归生成任务。
- 仅仅实现高效CUDA内核融合（如Flash Attention）不属于结构约束线性化方法。

## 例子

- **Sparse Transformer (OpenAI)**：结合带孔自注意力和局部自注意力，使得计算具备“局部紧密、远程稀疏”结构。
- **Linear Attention**：利用核函数替代指数形式保证内积非负性，通过结合率提前计算 $K^T V$，变为线性复杂度。
- **Nyströmformer**：将序列做自适应平均池化作为 Landmark，通过三个较小矩阵相乘实现 Nyström 近似，变成线性复杂度。

## 证据

- ev::6853::《为节约而生：从标准Attention到稀疏Attention》详细推演了利用带孔（Atrous）和局部（Local）自注意力组合，避开大量关联项的计算。
- ev::7546::《线性Attention的探索：Attention必须有个Softmax吗？》提出去除Softmax后能够使自注意力转变为 O(n) 的三矩阵序列连乘问题。
- ev::8180::《Nyströmformer：基于矩阵分解的线性化Attention方案》论述了依靠自适应池化聚类构造 Nyström 矩阵分解形式，以较小代价获得全局注意力近似。
