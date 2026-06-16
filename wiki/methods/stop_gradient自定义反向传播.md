---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: stop_gradient自定义反向传播
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
  - 10373
method_summary: "使用stop_gradient(sg)将变量与前向表达式连接，将反向传播时的梯度强制替换为由解析公式给出的自定义梯度值。"
typical_structure: |
  1. 前向传播：使用数值求解器（例如二分查找）或其他复杂黑盒操作计算出目标输出 $Y$。
  2. 解析梯度：根据隐函数求导等数学推导，计算 $Y$ 对输入 $\boldsymbol{x}$ 的精确解析梯度 $\nabla_{\boldsymbol{x}}Y$。
  3. 梯度挂载：利用核心变换公式构造 $Y_{eff}$，并将 $Y_{eff}$ 用于后续的计算图中。
  4. 反向传播：框架自动进行反向传播，被 $\text{sg}$ 包裹的部分梯度为零，$\boldsymbol{x}$ 接收到的梯度自动等于 $\nabla_{\boldsymbol{x}}Y$。
applicability: "适用于无法在前向传播中直接追踪图梯度，但是其隐式导数可以被解析计算的任何自适应或隐式优化控制层。"
examples:
  - "[[spaces-10373-ThreTopK解析解推导]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::10373::公式及原理解释：“\\boldsymbol{x}\\cdot\\text{sg}[\\nabla_{\\boldsymbol{x}}\\lambda(\\boldsymbol{x})] + \\text{sg}[\\lambda(\\boldsymbol{x}) - \\boldsymbol{x}\\cdot\\nabla_{\\boldsymbol{x}}\\lambda(\\boldsymbol{x})]...前向传播时等价于\\text{sg}不存在...反向传播时被\\text{sg}的部份梯度都是零，所以梯度就是给定的\\nabla_{\\boldsymbol{x}}\\lambda(\\boldsymbol{x})”。"
---

# stop_gradient自定义反向传播

## 适用问题
在使用数值方法（如二分法、牛顿法）或者复杂的前向计算过程求解某个变量（如阈值 $\lambda(\boldsymbol{x})$）时，往往会丢失该变量关于输入 $\boldsymbol{x}$ 的自动微分图。但如果其隐式梯度可以解析求出，我们可以利用 `stop_gradient`（`sg`）技巧实现自定义的梯度回传，而无需编写底层自动求导插件（如 PyTorch 的 `autograd.Function`）。

## 核心变换
将原本通过复杂数值计算得到的前向变量 $Y(\boldsymbol{x})$（计算图已断开）替换为一个有效的计算表达式 $Y_{eff}$，使其保留原有的前向值，并挂载所需的解析梯度 $\nabla_{\boldsymbol{x}}Y$：

$Y_{eff} = \boldsymbol{x} \cdot \text{sg}[\nabla_{\boldsymbol{x}}Y(\boldsymbol{x})] + \text{sg}[Y(\boldsymbol{x}) - \boldsymbol{x} \cdot \nabla_{\boldsymbol{x}}Y(\boldsymbol{x})]$

此处 $\cdot$ 代表向量内积或对应元素相乘求和，$\text{sg}$ 表示截断梯度（如 PyTorch 中的 `.detach()`，JAX 中的 `jax.lax.stop_gradient`）。

## 典型步骤
1. 前向传播：使用数值求解器（例如二分查找）或其他复杂黑盒操作计算出目标输出 $Y$。
2. 解析梯度：根据隐函数求导等数学推导，计算 $Y$ 对输入 $\boldsymbol{x}$ 的精确解析梯度 $\nabla_{\boldsymbol{x}}Y$。
3. 梯度挂载：利用核心变换公式构造 $Y_{eff}$，并将 $Y_{eff}$ 用于后续的计算图中。
4. 反向传播：框架自动进行反向传播，被 $\text{sg}$ 包裹的部分梯度为零，$\boldsymbol{x}$ 接收到的梯度自动等于 $\nabla_{\boldsymbol{x}}Y$。

## 直觉
前向时，所有的 $\text{sg}$ 操作相当于不存在，所以 $Y_{eff} = \boldsymbol{x} \cdot \nabla_{\boldsymbol{x}}Y + Y - \boldsymbol{x} \cdot \nabla_{\boldsymbol{x}}Y = Y$。
反向时，求 $Y_{eff}$ 对 $\boldsymbol{x}$ 的偏导数。由于带有 $\text{sg}$ 的项都被视为常数项，后一项的导数为0，前一项的导数为其常数系数 $\text{sg}[\nabla_{\boldsymbol{x}}Y]$。因此完美地将反向梯度的值“伪造”成解析梯度，同时没有改变前向值。

## 边界
1. 需要确保解析梯度 $\nabla_{\boldsymbol{x}}Y$ 的计算是准确的，否则会导致训练方向出错。
2. 构造 $Y_{eff}$ 时涉及到向量内积或对应维度广播乘加，需要注意张量维度的对齐。
3. 如果前向计算 $Y$ 本身可以直接由自动微分框架支持，可能无需使用此方法，但本方法在处理隐式导数时特别简洁有效。

## 例子
在计算 Top-K 的光滑近似（ThreTopK）时，需要用二分法求解阈值 $\lambda(\boldsymbol{x})$。数值求解过程难以提供直接可用的计算图梯度，此时利用解析得到的 $\nabla_{\boldsymbol{x}}\lambda(\boldsymbol{x})$，通过此技巧组合出带梯度的 $\lambda(\boldsymbol{x})$ 用于后续损失计算。

## 证据
- ev::10373::公式及原理解释：“\boldsymbol{x}\cdot\text{sg}[\nabla_{\boldsymbol{x}}\lambda(\boldsymbol{x})] + \text{sg}[\lambda(\boldsymbol{x}) - \boldsymbol{x}\cdot\nabla_{\boldsymbol{x}}\lambda(\boldsymbol{x})]...前向传播时等价于\text{sg}不存在...反向传播时被\text{sg}的部份梯度都是零，所以梯度就是给定的\nabla_{\boldsymbol{x}}\lambda(\boldsymbol{x})”。
