---
type: article_summary
title: FlatNCE：小批次对比学习效果差的原因竟是浮点误差？
article_id: 8586
source_url: https://spaces.ac.cn/archives/8586
date: 2021-07-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md"]
source_ids: ["8586"]
status: draft
updated: 2026-06-12
---

# FlatNCE：小批次对比学习效果差的原因竟是浮点误差？

## 文章核心问题
探究标准的对比学习损失函数（InfoNCE）在小 batch_size（小 $K$）情况下，训练效果发生剧烈退化的数学及计算精度根源。

## 主要结论
传统的对比学习高度依赖大 batch_size。根本原因在于：当正负样本对得分拉开之后，$e^{s_i-s_t} \\to 0$，导致 InfoNCE 损失值逼近 0。对于自适应优化器如 Adam，微小的损失和导数在归一化梯度更新时，其计算下溢误差（浮点误差）会远超真实梯度，使得更新方向沦为随机噪声。提出 FlatNCE 损失，通过一阶近似和 stop_gradient 调整，将分子除以常数算子阻断分母下溢，并证明其在导数层面完全等价于损失函数 $\\log\\left(\\sum_{i\\neq t} e^{s_i}\\right) - s_t$。这成功消成了分母中正样本得分，极大地平抑了浮点噪声，使小 batch_size 也能获得大批次的对比度。

## 推导结构
1. 分析小批次下 InfoNCE 损失逼近 0 时，Adam 优化器的梯度放大效应和浮点数精度限制。
2. 提出以 $\\xi/\\text{sg}(\\xi)$ 作为缩放因子阻断精度偏差。
3. 证明该带 `stop_gradient` 算子的表示其梯度流等于无约束的对数负得分和减去正得分。
4. 展示 FlatCLR 在图像任务中对小 batch_size 的鲁棒实验。

## 关键公式
- 常规分类损失：$\\log \\left(1 + \\sum_{i\\neq t} e^{s_i - s_t}\\right)$
- FlatNCE 缩放模型：$\\frac{\\xi}{\\text{sg}(\\xi)}$
- FlatNCE 等价非约束损失：$\\log\\left(\\sum\\limits_{i\\neq t} e^{s_i}\\right) - s_t$

## 体现的方法
- [[FlatNCE损失计算]]：通过重写对比计算过程消除由于损失接近 0 产生的下溢阶。

## 与其他文章的关系
- 其对于小 batch 对比度优化的尝试，与通过 [[对比学习可以使用梯度累积吗？]] 进行空间置换的计算路线形成对比。

## 原文证据锚点
- `ev::8586::FlatNCE等效`：对应原文中关于小批次对比学习由于损失过小导致 Adam 梯度归一化后浮点噪声主导的机理分析，以及通过 stop_gradient 算子推导得到等价损失函数的数学步骤。