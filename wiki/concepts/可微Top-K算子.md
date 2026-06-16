---
type: concept
title: 可微Top-K算子
definition: 一种将输入向量映射到多热（multi-hot）向量（其中最大k个分量为1，其余为0）的离散Top-K算子的连续且光滑的近似算子，能够提供有效的梯度。
standard_notation: \mathcal{ST}_k(\boldsymbol{x})
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
- '10373'
prerequisites:
- - - softmax
status: draft
updated: '2026-06-13'
---

# 可微Top-K算子

## 定义

可微Top-K算子是硬 Top-k 多热映射 `T_k(x)` 的光滑近似。源文先定义 `T_k: R^n -> {0,1}^n`，其中最大 `k` 个分量对应位置为 1；由于硬指派不连续且不能提供有效梯度，需要构造 `ST_k(x): R^n -> Delta_k^{n-1}`。

## 激活场景

它用于需要把 Top-k 选择嵌入端到端训练的模型。目标输出向量每个分量落在 `[0,1]`，总和为 `k`，并尽量满足单调性、平移不变性和温度趋零时收敛到硬 Top-k。

## 关键关系

源文给出两条构造路径：GradTopK 把 Top-k 指示向量看成“最大 k 个分量之和”的梯度，再用 logsumexp 光滑化；ThreTopK 则选取单调函数 `f`，通过求阈值 `lambda(x)` 使 `sum_i f(x_i-lambda)=k`。当 `k=1` 时，这些构造应退化或对应到 Softmax。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md`
