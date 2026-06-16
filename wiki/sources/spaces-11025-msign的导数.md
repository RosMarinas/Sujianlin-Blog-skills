---
type: article_summary
title: msign的导数
article_id: "11025"
source_url: https://spaces.ac.cn/archives/11025
date: 2025-06-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-06-13-msign的导数.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-13-msign的导数.md
source_ids:
  - "11025"
status: draft
updated: 2026-06-11
---

# msign的导数

本文推导了 $\text{msign}$ 算子的解析求导公式，并提出了一种不需要 SVD、可高效在 GPU 上利用 Newton-Schulz 迭代计算其导数的方法。该方法对于在模型前向传播中包含 $\text{msign}$ 操作（如结合 TTT 与 Muon）的反向传播具有重要作用。

## 主要内容

1. **基本定义**：
   - 对于 $\boldsymbol{M} \in \mathbb{R}^{n \times m}$，有 $\text{msign}(\boldsymbol{M}) = \boldsymbol{U}_{[:,:r]} \boldsymbol{V}_{[:,:r]}^\top$，等价于 $(\boldsymbol{M}\boldsymbol{M}^\top)^{-1/2}\boldsymbol{M}$。
   - 区分维基百科的方阵符号函数 $\text{mcsgn}(\boldsymbol{M}) = \boldsymbol{M}(\boldsymbol{M}^2)^{-1/2}$。

2. **同一计算**：
   - 均采用 Newton-Schulz 迭代计算。对于特征值为实数的分块三角矩阵，$\text{mcsgn}$ 亦可复用 $\text{msign}$ 的迭代系数。

3. **求导公式推导（迹技巧）**：
   - 从恒等式 $\boldsymbol{M} = \boldsymbol{O}\boldsymbol{M}^\top\boldsymbol{O}$ （其中 $\boldsymbol{O} = \text{msign}(\boldsymbol{M})$）出发，两边求微分。
   - 利用迹技巧（trace trick）建立 $\nabla_{\boldsymbol{M}}\mathcal{L}$ 与 $\nabla_{\boldsymbol{O}}\mathcal{L}$ 之间的关系，由以下方程组描述：
     $$
     \begin{aligned}
     \boldsymbol{X} - \boldsymbol{O}\boldsymbol{X}^\top\boldsymbol{O} =& \nabla_{\boldsymbol{M}}\mathcal{L} \\
     \boldsymbol{X}\boldsymbol{O}^\top\boldsymbol{M} + \boldsymbol{M}\boldsymbol{O}^\top\boldsymbol{X} =& \nabla_{\boldsymbol{O}}\mathcal{L}
     \end{aligned}
     $$

4. **GPU 友好的高效求解（Sylvester 方程）**：
   - 核心难点在于求解第二个方程。引入 $\boldsymbol{A} = \boldsymbol{M}\boldsymbol{O}^\top, \boldsymbol{B} = \boldsymbol{O}^\top\boldsymbol{M}, \boldsymbol{C} = \nabla_{\boldsymbol{O}}\mathcal{L}$，它可写成 Sylvester 方程形式：$\boldsymbol{A}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} = \boldsymbol{C}$。
   - 利用特征值在分块三角矩阵上的性质，通过求解分块矩阵的 $\text{mcsgn}$ 来解析求得 $\boldsymbol{X}$：
     $$
     \boldsymbol{X} = -\frac{1}{2} \left[ \lim_{\epsilon\to 0} \text{mcsgn}\left( \begin{bmatrix} \boldsymbol{A} + \epsilon\boldsymbol{I} & -\boldsymbol{C} \\ \boldsymbol{0} & -\boldsymbol{B} - \epsilon\boldsymbol{I} \end{bmatrix} \right) \right]_{[:n, n:]}
     $$
     其中 $\epsilon$ 为添加的奇异值扰动项（例如取 $\epsilon=10^{-3}$）。由此解得的 $\boldsymbol{X}$ 代入第一个方程即可得到最终的梯度 $\nabla_{\boldsymbol{M}}\mathcal{L}$，整个过程仅需 Newton-Schulz 迭代，不需要 SVD。
