---
type: concept
title: FlatNCE
definition: 一种改进的对比学习损失函数，旨在突破 InfoNCE 损失在小 batch_size 时的下溢和梯度噪声问题。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md"]
source_ids: ["8586"]
aliases: ["FlatNCE Loss", "FlatCLR"]
status: stable
updated: 2026-06-12
---

# FlatNCE

## 定义
FlatNCE 是一种从导数结构上进行数值缩放校正的对比学习优化损失函数，专门解决批次规模有限时的梯度精度受损问题。

## 梯度噪声分析
在经典的 InfoNCE 交叉熵中，随着训练深入正负得分迅速拉开，损失逼近 0。对于自适应优化器如 Adam，微小的损失和导数在通过均方根归一化时，计算精度的浮点噪声会占主导地位并被过度放大，导致模型参数更新失效。 FlatNCE 在导数公式中用 `stop_gradient` 算子阻断分母下溢的影响，转换为非约束的对数差值损失，极大释放了小批次下的表示学习潜力。