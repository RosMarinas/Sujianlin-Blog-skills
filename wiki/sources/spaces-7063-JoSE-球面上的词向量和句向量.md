---
type: article_summary
title: JoSE：球面上的词向量和句向量
article_id: 7063
source_url: https://spaces.ac.cn/archives/7063
date: 2019-11-11
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-11-11-JoSE-球面上的词向量和句向量.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2019-11-11-JoSE-球面上的词向量和句向量.md"]
source_ids: ["7063"]
status: draft
updated: 2026-06-12
---

# JoSE：球面上的词向量和句向量

## 文章核心问题
如何在单位超球面上联合训练词向量和句向量（JoSE模型），以保持文本方向相似性度量并克服多基底和模长不一致带来的优化困难。

## 主要结论
通过将所有词与句向量模长强制归一化（$\\Vert \\boldsymbol{x}\\Vert=1$），并引入 Hinge Loss，能使“词-词-句”打分明显高于“词-随机词-句”打分。同时，将受等式约束的黎曼流形最小化问题转化为在切空间投影方向上的梯度下降，并基于余弦对齐修正步长，能够在无约束框架下实现高效求解。

## 推导结构
1. 定义球面投影 Hinge Loss 优化目标。
2. 将带约束的流形优化等价转化为无约束更新公式，求导得到切空间投影算子。
3. 发现同一投影梯度对应不同的原梯度方向，由此引入负梯度与原向量夹角的余弦修正因子调节更新步长。

## 关键公式
- 优化目标：$\\max(0, m - \\boldsymbol{v}^{\\top}\\boldsymbol{u} - \\boldsymbol{d}^{\\top}\\boldsymbol{u} + \\boldsymbol{v}^{\\top} \\boldsymbol{u}' + \\boldsymbol{d}^{\\top} \\boldsymbol{u}')$
- 投影修正梯度公式：$\\boldsymbol{g} = \\left(\\boldsymbol{I} - \\boldsymbol{x}\\boldsymbol{x}^{\\top}\\right)\\nabla_{\\boldsymbol{x}} f\\left(\\boldsymbol{x}\\right)$
- 最终迭代更新公式：$\\boldsymbol{x}_{t+1} = \\frac{\\boldsymbol{x}_{t} - \\eta_t\\left(1+\\frac{\\boldsymbol{x}_t^{\\top}\\nabla_{\\boldsymbol{x}_t}\\,f\\left(\\boldsymbol{x}_t\right)}{\\left\\Vert \\nabla_{\\boldsymbol{x}_t}\\,f\\left(\\boldsymbol{x}_t\\right)\\right\\Vert}\\right)\\boldsymbol{g}}{\\left\\Vert \\boldsymbol{x}_{t} - \\eta_t\\left(1+\\frac{\\boldsymbol{x}_t^{\\top}\\nabla_{\\boldsymbol{x}_t}\\,f\\left(\\boldsymbol{x}_t\right)}{\\left\\Vert \\nabla_{\\boldsymbol{x}_t}\\,f\\left(\\boldsymbol{x}_t\\right)\\right\\Vert}\\right)\\boldsymbol{g}\\right\\Vert}$

## 体现的方法
- [[球面向量梯度更新修正]]：利用切空间投影与余弦方向修正更新球面上向量。

## 与其他文章的关系
- 是超球面约束优化的具体应用，其切空间投影与 [[流形上的最速下降]] 的几何投影机制一致。

## 原文证据锚点
- `ev::7063::优化目标`：对应原文中对 JoSE Hinge 损失和归一化约束的定义。
- `ev::7063::梯度投影`：对应原文中切空间投影矩阵与更新量方向修正调节梯度的详细几何推导。