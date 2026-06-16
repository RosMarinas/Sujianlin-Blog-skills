---
type: example
title: spaces-10831-RMSNorm对角雅可比微分方程求解
article_id: 10831
article:
- - spaces-10831-寻找Normalization替代品
section: DyT现！
claim: 通过解保留 RMSNorm 雅可比矩阵对角分量的微分方程，可以推导并构造出逐元素自适应激活函数 Dynamic Tanh (DyT)
notation_mapping:
  y_i: y_i (输出特征向量第 i 维元素)
  x_i: x_i (输入特征向量第 i 维元素)
  rho: rho (特征模长参数，假设在小区间内为常数)
steps:
- 提取 RMSNorm Jacobian 矩阵的对角分量，构造常微分方程： dy_i / dx_i = (1 / rho) * (1 - y_i^2 / d)
- 应用分离变量法： dy_i / (1 - y_i^2 / d) = (1 / rho) * dx_i
- 对两端进行积分，其中左端可利用双曲正切导数： sqrt(d) * arctanh(y_i / sqrt(d)) = x_i / rho + C
- 代入初值条件 y_i(0) = 0，确定常数项 C = 0
- 反解 y_i 的表达式，可求得： y_i = sqrt(d) * tanh(x_i / (rho * sqrt(d)))
- 将外侧系数与分母因子替换为可训练超参数，即得到了 DyT 形式： y_i = gamma_i * tanh(alpha_i * x_i) + beta_i
used_concepts:
- - - Dynamic Tanh
used_formulas:
- - - RMSNorm雅可比矩阵公式
used_methods:
- - - 对角雅可比梯度近似法
source_span: ev::10831::DyT现！
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
source_ids:
- 10831
status: stable
updated: '2026-06-12'
---

## 问题

源文“DyT现！”一节从 RMSNorm 的雅可比矩阵出发，问一个逐元素函数 $f(\boldsymbol{x})=[f(x_1),\ldots,f(x_d)]$ 能否保留 RMSNorm 的主要梯度行为。

## 推导

RMSNorm 梯度先被写成
$$
\nabla_{\boldsymbol{x}}\boldsymbol{y}=\frac{1}{\Vert\boldsymbol{x}\Vert_{RMS}}\left(\boldsymbol{I}-\frac{\boldsymbol{y}\boldsymbol{y}^{\top}}{d}\right).
$$
逐元素函数的雅可比必须是对角阵，所以源文只保留上式的对角线部分：
$$
\frac{dy_i}{dx_i}=\frac{1}{\Vert\boldsymbol{x}\Vert_{RMS}}\left(1-\frac{y_i^2}{d}\right).
$$
进一步假设 $\rho=\Vert\boldsymbol{x}\Vert_{RMS}$ 为常数，并取初值 $y_i(0)=0$，直接求解该微分方程，得到
$$
y_i=\sqrt{d}\tanh\left(\frac{x_i}{\rho\sqrt{d}}\right).
$$

## 方法与证据

这个 Example 的方法是“从多维归一化层的雅可比中抽取对角近似，再解一维微分方程”。证据来自 `ev::10831::DyT现！`：源文明确说明 DyT 的 $\tanh$ 正是由该对角微分方程和常数 RMS 假设推出。
