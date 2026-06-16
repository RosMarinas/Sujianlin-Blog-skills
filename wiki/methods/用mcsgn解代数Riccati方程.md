---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 用mcsgn解代数Riccati方程
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-矩阵符号函数mcsgn能计算什么.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-07-19-矩阵平方根和逆平方根的高效计算.md
  - Data/wiki/sources/spaces-10648-从谱范数梯度到新式权重衰减的思考.md
  - Data/wiki/sources/spaces-10795-高阶MuP-更简明但更高明的谱条件缩放.md
  - Data/wiki/sources/spaces-11056-矩阵符号函数mcsgn能计算什么.md
  - Data/wiki/sources/spaces-11175-矩阵r次方根和逆r次方根的高效计算.md
source_ids:
  - 11056
method_summary: 把代数 Riccati 方程嵌入哈密顿分块矩阵的 mcsgn 恒等式中，从分块结果反解矩阵解。
typical_structure: |
  1. 将代数 Riccati 方程的系数矩阵组装成一个 $2n \times 2n$ 的哈密顿分块矩阵 $H = \begin{bmatrix}\boldsymbol{A} & \boldsymbol{C} \\ \boldsymbol{D} & \boldsymbol{B}\end{bmatrix}$。
  2. 对矩阵 $H$ 利用纯矩阵乘法（例如 Newton-Schulz 迭代）计算它的矩阵符号函数 $\mathop{\text{mcsgn}}(H)$。
  3. 将求得的 $\mathop{\text{mcsgn}}(H)$ 表示成 $2 \times 2$ 分块矩阵 $\begin{bmatrix} W_{11} & W_{12} \\ W_{21} & W_{22} \end{bmatrix}$。
  4. 利用分块等式（类似于 $-X Y - I = W_{11}$, $-Y = W_{21}$）反解出 Riccati 方程的目标解 $X$。
applicability: 用于在线性控制系统（如LQR设计、卡尔曼滤波）、最优控制问题中需要免去复杂特征值分解来高效求解代数 Riccati 方程的数值计算。
examples:
  - [[article::11056]]
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::11056::展示了代数Riccati方程 $\boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = 0$ 如何通过构建分块矩阵取 mcsgn 函数进而提取出解 $\boldsymbol{X}$ 的解析推导（Lines 40-85）。
---

# 用mcsgn解代数Riccati方程

## 适用问题

在控制理论和动力系统中，大量优化问题会归结为求解代数 Riccati 方程（ARE）：$\boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = \boldsymbol{0}$。如果利用传统的 Schur 分解寻找解，速度慢且难以利用深度学习框架中的 GPU 矩阵乘法单元（Tensor Cores）进行并行加速。

## 核心变换

$$ \boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = \boldsymbol{0} \iff \mathop{\text{mcsgn}}\left(\begin{bmatrix}\boldsymbol{A} & \boldsymbol{C} \\ \boldsymbol{D} & \boldsymbol{B}\end{bmatrix}\right) = \text{特定分块矩阵} $$
将解二次矩阵方程的问题，等效转化为对由系数组成的增广分块矩阵执行 mcsgn 运算，然后通过局部块结构的代数关系直接抽取出解 $\boldsymbol{X}$。

## 典型步骤

1. **构造系统矩阵**：提取代数 Riccati 方程中的四个系数矩阵 $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}, \boldsymbol{D}$，组装成一个 $2n \times 2n$ 的大分块矩阵 $\boldsymbol{H} = \begin{bmatrix}\boldsymbol{A} & \boldsymbol{C} \\ \boldsymbol{D} & \boldsymbol{B}\end{bmatrix}$。
2. **计算符号函数**：对 $\boldsymbol{H}$ 使用并行的 Newton-Schulz 迭代法求解推广的矩阵符号函数 $\boldsymbol{W} = \mathop{\text{mcsgn}}(\boldsymbol{H})$。
3. **块矩阵解析**：根据 Riccati 方程解存在的性质，$\boldsymbol{W}$ 在特定块可以表示为 $\begin{bmatrix}-\boldsymbol{X}\boldsymbol{Y}-\boldsymbol{I} & 2\boldsymbol{X} + \boldsymbol{X}\boldsymbol{Y}\boldsymbol{X} \\ -\boldsymbol{Y} & \boldsymbol{Y}\boldsymbol{X} + \boldsymbol{I}\end{bmatrix}$（以特定特殊情境为例）。
4. **提取结果**：从块对应位置直接读取或使用极轻量的逆操作（如知道 $-\boldsymbol{Y} = \boldsymbol{W}_{21}$，即可顺次推算得 $\boldsymbol{X}$）。

## 直觉

要解 $ax^2 + bx + c = 0$，我们背熟了求根公式；但矩阵版的 $xDx + xB - Ax - C = 0$ 是没有简单的求根公式的，里面还牵扯到矩阵乘法的不可交换性。数学家巧妙地构建了一个大号的二元一次方程组对应的矩阵，只要对这个矩阵施加一个类似于“变号”的操作（mcsgn），它就会由于内在的对称性坍缩成一个携带了 $X$ 信息的特定格式。我们只要像开盲盒一样掀开这个大矩阵左下角的盖子，就能直接把 $X$ 取出来。

## 边界

- 只有在特定的系统稳定性假设下，构建的分块矩阵的特征谱才是可分的，此时矩阵符号函数 $\mathop{\text{mcsgn}}$ 能够良好收敛到包含解的形式。
- 对于极端奇异的系统参数，$\mathop{\text{mcsgn}}$ 迭代中可能发生数值不稳定（如中途求逆矩阵或者对特征值缩放不当时）。

## 例子

在求解最简单的 Riccati 形式 $\boldsymbol{X}^2 = \boldsymbol{C}$ 时（即 $\boldsymbol{A}=\boldsymbol{B}=\boldsymbol{0}, \boldsymbol{D}=\boldsymbol{I}$），我们对 $\begin{bmatrix}\boldsymbol{0} & \boldsymbol{C} \\ \boldsymbol{I} & \boldsymbol{0}\end{bmatrix}$ 取 mcsgn，利用块恒等式立即推导出其结果为 $\begin{bmatrix}\boldsymbol{0} & \boldsymbol{C}^{1/2} \\ \boldsymbol{C}^{-1/2} & \boldsymbol{0}\end{bmatrix}$，右上角的块就是我们的解 $\boldsymbol{X} = \boldsymbol{C}^{1/2}$。

## 证据

- ev::11056::展示了代数Riccati方程 $\boldsymbol{X}\boldsymbol{D}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} - \boldsymbol{A}\boldsymbol{X} - \boldsymbol{C} = 0$ 如何通过构建分块矩阵取 mcsgn 函数进而提取出解 $\boldsymbol{X}$ 的解析推导（Lines 40-85）。
