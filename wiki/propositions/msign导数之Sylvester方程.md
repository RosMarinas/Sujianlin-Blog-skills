---
type: proposition
title: msign导数之Sylvester方程
statement: '对矩阵符号函数前向算子 $\boldsymbol{O} = \text{msign}(\boldsymbol{M})$ 的求导，其微分算子可等价映射为求解一个以 $\boldsymbol{M}\boldsymbol{O}^\top$ 和 $\boldsymbol{O}^\top\boldsymbol{M}$ 为系数的 Sylvester 方程，并利用分块特征值符号函数 $\text{mcsgn}$ 进行 GPU 友好的解析求解。'
assumptions:
  - '$\boldsymbol{M} \in \mathbb{R}^{n \times m}$，其前向 msign 输出满足恒等关系 $\boldsymbol{M} = \boldsymbol{O}\boldsymbol{M}^\top\boldsymbol{O}$，且反向传播梯度 $\boldsymbol{C} = \nabla_{\boldsymbol{O}}\mathcal{L}$ 物理良置。'
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-13-msign的导数.md
source_ids:
  - "11025"
requires:
  - "[[msign导数求解公式]]"
  - "[[矩阵符号函数(msign)]]"
proof_route: |
  1. 对恒等式 $\boldsymbol{M} = \boldsymbol{O}\boldsymbol{M}^\top\boldsymbol{O}$ 两边求微分，得到：
     $d\boldsymbol{M} = (d\boldsymbol{O})\boldsymbol{M}^\top\boldsymbol{O} + \boldsymbol{O}(d\boldsymbol{M}^\top)\boldsymbol{O} + \boldsymbol{O}\boldsymbol{M}^\top(d\boldsymbol{O})$。
  2. 运用迹技巧（Trace Trick），乘上与 $\boldsymbol{M}$ 形状相同的矩阵 $\boldsymbol{X}^\top$ 后求迹，移位化简得出微分转换方程组：
     $\boldsymbol{X} - \boldsymbol{O}\boldsymbol{X}^\top\boldsymbol{O} = \nabla_{\boldsymbol{M}}\mathcal{L}$ 且 $\boldsymbol{X}\boldsymbol{O}^\top\boldsymbol{M} + \boldsymbol{M}\boldsymbol{O}^\top\boldsymbol{X} = \nabla_{\boldsymbol{O}}\mathcal{L}$。
  3. 定义 $\boldsymbol{A} = \boldsymbol{M}\boldsymbol{O}^\top$ 和 $\boldsymbol{B} = \boldsymbol{O}^\top\boldsymbol{M}$，将第二个方程改写为标准的 Sylvester 方程：$\boldsymbol{A}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} = \nabla_{\boldsymbol{O}}\mathcal{L}$。
  4. 构造分块上三角矩阵 $\begin{bmatrix} \boldsymbol{A} & -\boldsymbol{C} \\ \boldsymbol{0} & -\boldsymbol{B} \end{bmatrix}$ 并求其矩阵特征值符号函数 $\text{mcsgn}$。
  5. 依据其相似不变性及分块对角阵正定性质，得出右上角分块对应于 $-2\boldsymbol{X}$，从而在添加奇异值微小正扰动 $\epsilon \boldsymbol{I}$ 使得方程良置后，解析求得 $\boldsymbol{X}$。
  6. 将 $\boldsymbol{X}$ 代回首个方程，得到参数矩阵的精确梯度 $\nabla_{\boldsymbol{M}}\mathcal{L}$。
evidence_spans:
  - "ev::11025::推导过程"
status: draft
updated: 2026-06-11
---

## 优越性

传统的矩阵函数求导通常依赖于奇异值分解（SVD），而在反向传播中对 SVD 进行求导不仅计算复杂，且在 GPU 上的并行效率极低。

本命题提出的 Sylvester 方程求解方案，利用矩阵特征值符号函数 $\text{mcsgn}$ 的分块矩阵性质，把微分运算巧妙转换为针对分块三角矩阵计算 $\text{mcsgn}$。由于 $\text{mcsgn}$ 可以通过 Newton-Schulz 迭代进行纯矩阵乘法的高效计算，因此本命题提供了一种在 GPU 上完全避免 SVD 运算的、高效可微分的 $\text{msign}$ 求导方法。
