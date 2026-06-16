---
type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用Householder变换构造向量变换的正交矩阵
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-06-05-从一个单位向量变换到另一个单位向量的正交矩阵.md
  - Data/wiki/sources/spaces-11563-DeltaNet的核心逆矩阵的元素总是在-1-1-内.md
  - Data/wiki/sources/spaces-8453-从一个单位向量变换到另一个单位向量的正交矩阵.md
source_ids:
  - 8453
method_summary: "用两个单位向量的差向量构造 Householder 反射矩阵，得到将一个单位向量精确映射到另一个单位向量的显式正交变换。"
typical_structure: |
  1. 获取需要对齐的两个高维单位向量 $\boldsymbol{a}$ 和 $\boldsymbol{b}$。
  2. 计算它们的差向量 $\boldsymbol{a} - \boldsymbol{b}$。
  3. 以 $\boldsymbol{a} - \boldsymbol{b}$ 作为正交法向量（镜面），利用 Householder 变换公式构造正交矩阵 $\boldsymbol{T}$。
  4. 应用矩阵 $\boldsymbol{T}$ 实现从 $\boldsymbol{a}$ 到 $\boldsymbol{b}$ 的保模长旋转/反射映射。
applicability: "在多维空间中，需要寻求一个显式且简单的正交矩阵来将一个给定单位向量精确映射为另一个给定单位向量的场合。"
examples:
  - "[[article::8453]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8453::介绍了利用目标差向量构造Householder变换矩阵，实现一个单位向量到另一个单位向量正交映射的方法（Lines 86-91）。"
---

# 用Householder变换构造向量变换的正交矩阵

## 适用问题

寻找高维空间中能够将已知单位向量 $\boldsymbol{a}$ 转换到另一已知单位向量 $\boldsymbol{b}$ 的正交矩阵 $\boldsymbol{T}$，且要求构造形式足够简单解析，避免复杂的特征值分解或高维旋转角参数化计算。

## 核心变换

$$ \boldsymbol{T} = \boldsymbol{I} - 2 \frac{(\boldsymbol{a} - \boldsymbol{b})(\boldsymbol{a} - \boldsymbol{b})^\top}{\|\boldsymbol{a} - \boldsymbol{b}\|^2} $$
利用纯镜像对称（Householder变换）直接构造保内积、保模长的目标转移正交矩阵。

## 典型步骤

1. 输入两个需要对齐的等长列向量（通常均已标准化为单位向量）$\boldsymbol{a}$ 和 $\boldsymbol{b}$。
2. 计算它们的向量差 $\boldsymbol{v} = \boldsymbol{a} - \boldsymbol{b}$，该向量表示连接两个向量端点的弦。
3. 利用差向量 $\boldsymbol{v}$ 的归一化形式构造 Householder 矩阵：$ \boldsymbol{T} = \boldsymbol{I} - 2\frac{\boldsymbol{v}\boldsymbol{v}^\top}{\boldsymbol{v}^\top \boldsymbol{v}} $。
4. （可选验证）易证 $\boldsymbol{T}$ 是对称正交阵且满足 $\boldsymbol{T}\boldsymbol{a} = \boldsymbol{b}$。由于 Householder 矩阵本身是其自身的逆，也可以作为双向对合变换。

## 直觉

想象在一个三维（甚至高维）空间里，你要把一根手指（向量a）指向另一根手指（向量b）的方向，而不改变手臂的长度。最简单的办法不是去思考怎么在复杂的空间里绕来绕去地旋转它，而是在两根指尖中间立一面垂直于两指尖连线的镜子。原来那根手指在镜子里的影像，正好就与目标手指的位置一模一样。Householder 变换就是这面“镜子”。

## 边界

- 只适用于等长（同范数）向量之间的变换。如果两向量模长不等，需分别除以各自模长转化为单位向量处理。
- 当 $\boldsymbol{a} = \boldsymbol{b}$ 时，除数为 $0$，需作为特例返回单位阵 $\boldsymbol{I}$。
- 该变换是一个反射操作（行列式为 -1），不是一个单纯的“旋转”（行列式为 +1）。若强求必须为纯旋转矩阵，此方法构造的 $\boldsymbol{T}$ 无法直接满足。

## 例子

在二维子平面分解中，通过计算夹角 $\theta$ 和单位向量分解可推导出一个正交基形式的解。经过坐标系和代数合并化简，其最终等价为以 $(\boldsymbol{a}-\boldsymbol{b})$ 为对称轴的一个标准的镜像反射 Householder 变换矩阵。

## 证据

- ev::8453::介绍了利用目标差向量构造Householder变换矩阵，实现一个单位向量到另一个单位向量正交映射的方法（Lines 86-91）。
