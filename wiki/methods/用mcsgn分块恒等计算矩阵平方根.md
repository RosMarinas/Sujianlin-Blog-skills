---


type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 用mcsgn分块恒等计算矩阵平方根
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-矩阵符号函数mcsgn能计算什么.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-07-19-矩阵平方根和逆平方根的高效计算.md
source_ids:
  - 11158
method_summary: 构造反对角分块矩阵并计算 mcsgn，从收敛分块中读取矩阵平方根和逆平方根。
typical_structure: |
  1. 将半正定矩阵 $\boldsymbol{P}$ 缩放到使得其特征值落在 $[0,1]$ 区间内。
  2. 构造一个形如 $\begin{bmatrix}\boldsymbol{0} & \boldsymbol{P} \\ \boldsymbol{I} & \boldsymbol{0}\end{bmatrix}$ 的 $2n \times 2n$ 分块反对角阵 $\boldsymbol{M}$。
  3. 通过 Newton-Schulz 等迭代算法对该分块矩阵求解矩阵符号函数 $\text{mcsgn}(\boldsymbol{M})$。
  4. 利用分块反对角阵的特性，直接从迭代收敛的极限矩阵中读取右上角和左下角的分块，分别得到 $\boldsymbol{P}^{1/2}$ 和 $\boldsymbol{P}^{-1/2}$。
applicability: 在需要同时或单独快速计算矩阵（尤其是深度学习中的协方差阵或预条件矩阵）的算术平方根和逆平方根时，避免高代价的特征值分解。
examples:
  - [[article::11158]]
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::11158::介绍了基于 mcsgn 符号函数和特定的分块反对角恒等式来同时迭代计算矩阵的平方根和逆平方根的方法（Lines 51-100）。
---

# 用mcsgn分块恒等计算矩阵平方根

## 适用问题

通常计算矩阵的平方根与逆平方根需要做 $O(N^3)$ 的完整 SVD 或特征值分解，这在现代机器学习（比如某些二阶优化器或白化层）中不可接受。需要一种仅靠矩阵乘法且能高度并行化的快速逼近算法。

## 核心变换

$$ \mathop{\text{mcsgn}}\left(\begin{bmatrix}\boldsymbol{0} & \boldsymbol{P} \\ \boldsymbol{I} & \boldsymbol{0}\end{bmatrix}\right)=\begin{bmatrix}\boldsymbol{0} & \boldsymbol{P}^{1/2} \\ \boldsymbol{P}^{-1/2} & \boldsymbol{0}\end{bmatrix} $$
将“求方根”这个非线性且依赖谱分解的操作，转换为对特定增广分块矩阵求“矩阵符号函数（mcsgn）”的操作。由于符号函数可以通过只包含加法和乘法的牛顿迭代进行，原问题也就转化为了纯乘法迭代计算。

## 典型步骤

1. **预处理缩放**：给定特征值非负的矩阵 $\boldsymbol{P}$，通常将其除以 $\text{tr}(\boldsymbol{P})$ 或谱范数的上界，以保证其特征值全部压缩在 $[0, 1]$ 内。
2. **初始化分块**：构建分块对角矩阵 $\boldsymbol{Y}_0 = \boldsymbol{P}$, $\boldsymbol{Z}_0 = \boldsymbol{I}$（为了避免零奇异值导致逆方根爆炸，可以稍作修改只跟踪 $\boldsymbol{P}^{1/2}$，即令 $\boldsymbol{Y}_0\boldsymbol{Z}_0 = \boldsymbol{P}$）。
3. **分步迭代**：反复执行基于 Newton-Schulz 方法（或带高阶加速项的方法）推导出的解耦迭代式：
   $$ \boldsymbol{Y}_{t+1} = (a\boldsymbol{I} + b\boldsymbol{Y}_t\boldsymbol{Z}_t + c(\boldsymbol{Y}_t\boldsymbol{Z}_t)^2)\boldsymbol{Y}_t $$
   $$ \boldsymbol{Z}_{t+1} = \boldsymbol{Z}_t(a\boldsymbol{I} + b\boldsymbol{Y}_t\boldsymbol{Z}_t + c(\boldsymbol{Y}_t\boldsymbol{Z}_t)^2) $$
4. **提取结果**：当迭代收敛时（即 $\boldsymbol{Y}_t\boldsymbol{Z}_t \to \boldsymbol{I}$ 或差值极小），$\boldsymbol{Y}_t$ 将收敛于 $\boldsymbol{P}^{1/2}$，$\boldsymbol{Z}_t$ 将收敛于 $\boldsymbol{P}^{-1/2}$。

## 直觉

怎么不用开平方键就能算出 $\sqrt{x}$？我们可以用牛顿迭代法不停地做加法和乘法逼近它。但在矩阵里，直接套用 $\sqrt{\boldsymbol{P}}$ 的标量迭代公式很容易因为数值不稳定而崩溃。而 mcsgn （矩阵符号函数）本质上就是把矩阵往单位阵拉扯。当我们把 $\boldsymbol{P}$ 和 $\boldsymbol{I}$ 一上一下放到一个矩阵对角线外的时候，算法试图“磨平”它，一顿操作下来，就把 $\boldsymbol{P}$ 掰成了两半 $\sqrt{\boldsymbol{P}}$ 和 $1/\sqrt{\boldsymbol{P}}$ 放在两边了。

## 边界

- 矩阵 $\boldsymbol{P}$ 必须是半正定或其特征值严格非负，如果存在复数或负特征值，所求平方根的意义与收敛性会改变。
- 如果矩阵存在趋近于 $0$ 的奇异值，同时计算逆平方根 $\boldsymbol{P}^{-1/2}$ 会导致极度数值不稳定；此时需使用专门的仅跟踪 $\boldsymbol{Y}_t$ 的修改版迭代。

## 例子

在自适应学习率优化算法或高阶分布调整中，若要计算维度为 $1000 \times 1000$ 的协方差矩阵的平方根以执行空间白化（Whitening），可以调用基于上述原理的 5 阶 Newton-Schulz 迭代算子，在 GPU 上仅需十数次纯矩阵乘法即可达到极高精度。

## 证据

- ev::11158::介绍了基于 mcsgn 符号函数和特定的分块反对角恒等式来同时迭代计算矩阵的平方根和逆平方根的方法（Lines 51-100）。
