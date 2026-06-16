---
type: example
title: 球面向量优化更新
article_id: 7063
article: JoSE：球面上的词向量和句向量
section: 梯度下降
claim: JoSE模型参数在单位球面约束下的梯度投影与步长余弦对齐修正更新步骤。
steps: 1. 约束 $\Vert \boldsymbol{x} \Vert = 1$。无约束函数为 $f(\boldsymbol{x})$，通过设置 $\boldsymbol{x} = \boldsymbol{\theta} / \Vert \boldsymbol{\theta} \Vert$ 展开为无约束优化形式。\n2. 对展开式关于无约束参数 $\boldsymbol{\theta}$ 求梯度：\n$\nabla_{\boldsymbol{\theta}} f\left(\frac{\boldsymbol{\theta}}{\Vert \boldsymbol{\theta}\Vert}\right) = \frac{1}{\Vert \boldsymbol{\theta} \Vert} (\boldsymbol{I} - \boldsymbol{x}\boldsymbol{x}^{\top}) \nabla_{\boldsymbol{x}} f(\boldsymbol{x})$。\n3. 将 $1/\Vert\boldsymbol{\theta}\Vert$ 标量整合进学习率中。\n4. 梯度更新公式：$\boldsymbol{x}_{t+1} = R_x(\boldsymbol{x}_t - \eta_t \boldsymbol{g}_t)$，其中投影梯度为 $\boldsymbol{g}_t = (\boldsymbol{I} - \boldsymbol{x}_t\boldsymbol{x}_t^{\top}) \nabla_{\boldsymbol{x}} f(\boldsymbol{x}_t)$。\n5. 引入余弦对齐调节因子 $\left(1 + \frac{\boldsymbol{x}_t^{\top}\nabla_{\boldsymbol{x}_t} f}{\Vert \nabla_{\boldsymbol{x}_t} f \Vert}\right)$ 修正切平面更新步长。
used_concepts: ["[[球面文本嵌入]]"]
notation_mapping: {"\\boldsymbol{x}": "球面向量特征", "\\boldsymbol{g}": "切平向投影梯度", "\\boldsymbol{\\theta}": "未归一化的代存变量"}
source_span: ev::7063::梯度投影
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2019-11-11-JoSE-球面上的词向量和句向量.md"]
source_ids: ["7063"]
status: stable
updated: 2026-06-12
---

# 球面向量优化更新

## 演示过程
本例演示了 JoSE 模型如何解决限制表示特征为单位向量（球投影约束）时的最速下降求导。

设 loss 函数为 $f(\boldsymbol{x})$ 满足 $\Vert \boldsymbol{x} \Vert = 1$。
定义无约束实数向量 $\boldsymbol{\theta}$ 并代换 $\boldsymbol{x} = \boldsymbol{\theta} / \Vert \boldsymbol{\theta} \Vert$，无约束导数求偏导：
$$
\frac{\partial f}{\partial \theta_i} = \sum_{j} \frac{\partial f}{\partial x_j} \frac{\partial x_j}{\partial \theta_i}
$$
其中：
$$
\frac{\partial x_j}{\partial \theta_i} = \frac{\delta_{ij}\Vert\boldsymbol{\theta}\Vert - \theta_j \frac{\theta_i}{\Vert\boldsymbol{\theta}\Vert}}{\Vert\boldsymbol{\theta}\Vert^2} = \frac{1}{\Vert\boldsymbol{\theta}\Vert}\left(\delta_{ij} - x_i x_j\right)
$$
写成矩阵矩阵积形式：
$$
\nabla_{\boldsymbol{\theta}} f = \frac{1}{\Vert\boldsymbol{\theta}\Vert}(\boldsymbol{I} - \boldsymbol{x}\boldsymbol{x}^{\top})\nabla_{\boldsymbol{x}} f
$$
利用切空间投影性质与标量学习率转换，沿用方向修正更新：
$$
\boldsymbol{x}_{t+1} = \frac{\boldsymbol{x}_t - \eta_t (\text{factor}) (\boldsymbol{I}-\boldsymbol{x}_t\boldsymbol{x}_t^\top)\nabla f}{\Vert \dots \Vert}
$$