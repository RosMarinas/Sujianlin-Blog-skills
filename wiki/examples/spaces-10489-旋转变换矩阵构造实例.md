---
type: example
title: spaces-10489-旋转变换矩阵构造实例
article_id: 10489
article:
- - spaces-10489-VQ旋转技巧
section: 旋转
claim: 已知连续特征向量 z 和最近邻量化编码向量 q，可以通过解析正交矩阵 R 构造出精确旋转缩放矩阵 G
notation_mapping:
  z: z (连续特征向量)
  q: q (量化向量)
  G: G (包含旋转缩放的估计矩阵)
  R: R (正交旋转矩阵)
steps:
- 对向量 z 和 q 进行 L2 归一化： tilde_z = z / ||z||, tilde_q = q / ||q||
- 计算单位向量的夹角余弦值 cos_theta = tilde_z . tilde_q
- 利用正交变换解析解构建 R： R = I + 2*tilde_q*tilde_z^T - 2 * (tilde_q + tilde_z)*(tilde_q +
  tilde_z)^T / ||tilde_q + tilde_z||^2
- 使用模长之比进行缩放对齐得到最终的 G = (||q||/||z||) * R
- 验证特征映射关系： G * z = q
used_concepts:
- - - 旋转技巧
used_formulas:
- - - 旋转变换矩阵公式
used_methods:
- - - VQ旋转直通估计法
source_span: ev::10489::旋转
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-10-24-VQ的旋转技巧-梯度直通估计的一般推广.md
source_ids:
- 10489
status: stable
updated: '2026-06-12'
---

## 问题

源文“旋转”一节要为 VQ 的广义直通估计器选择矩阵 $G$。目标是在前向仍得到量化向量 $q$ 的同时，让反向梯度不再简单假设 $\partial q/\partial z=I$，而是反映 $z$ 到 $q$ 的几何关系。

## 推导

源文从
$$
z_q=\mathrm{sg}[G]z+\mathrm{sg}[q-Gz]
$$
出发，考虑 $Gz=q$ 的情形。先令 $\tilde{z}=z/\Vert z\Vert$、$\tilde{q}=q/\Vert q\Vert$，构造把 $\tilde{z}$ 旋转到 $\tilde{q}$ 的正交矩阵
$$
R=I+2\tilde{q}\tilde{z}^{\top}-2\left(\frac{\tilde{q}+\tilde{z}}{\Vert\tilde{q}+\tilde{z}\Vert}\right)\left(\frac{\tilde{q}+\tilde{z}}{\Vert\tilde{q}+\tilde{z}\Vert}\right)^{\top}.
$$
由 $\tilde{q}=R\tilde{z}$ 得到
$$
q=\frac{\Vert q\Vert}{\Vert z\Vert}Rz,\qquad G=\frac{\Vert q\Vert}{\Vert z\Vert}R.
$$

## 方法与证据

该例体现“先构造单位向量间正交变换，再补上模长缩放”的方法。证据来自 `ev::10489::旋转`：源文明确说明 $G$ 使梯度夹角和模长比与 $q$ 相对于 $z$ 的几何性质一致，并提醒实现时要对 $\tilde{q},\tilde{z},\Vert q\Vert/\Vert z\Vert$ 停梯度。
