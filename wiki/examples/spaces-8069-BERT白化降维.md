---
type: example
title: BERT白化降维
article_id: 8069
article: 你可能不需要BERT-flow：一个线性变换媲美BERT-flow
section: 降维效果还能更好
claim: 使用BERT-whitening白化校正并利用SVD特征值降维截断的计算步骤。
steps: 1. 读入大批无监督提取句向量，大小为 $[N, d]$；\n2. 计算每一维度的均值 $\boldsymbol{\mu}$ 及对称正定协方差 $\boldsymbol{\Sigma}$；\n3. 对协方差做 SVD 特征分解：$\boldsymbol{\Sigma} = \boldsymbol{U}\boldsymbol{\Lambda}\boldsymbol{U}^{\top}$，其中对角线值自动从大到小对齐；\n4. 计算转换矩阵 $\boldsymbol{W} = \boldsymbol{U}\sqrt{\boldsymbol{\Lambda}^{-1}}$；\n5. 设定剪裁维度为 $k$（如 $k=256$），仅截取前 $k$ 列得到大小为 $[d, k]$ 的 $\boldsymbol{W}[:,:k]$；\n6. 转化得到降维后的各项同性表示向量 $\tilde{\boldsymbol{x}}_i = (\boldsymbol{x}_i - \boldsymbol{\mu})\boldsymbol{W}[:,:k]$。
used_concepts: ["[[BERT-whitening]]", "[[句向量各向异性]]"]
notation_mapping: {"\\boldsymbol{\\Sigma}": "总体特征协方差矩阵", "\\boldsymbol{W}": "对称去相关核"}
source_span: ev::8069::白化操作
sources: ["Data/Spaces_ac_cn/markdown/Mathematics/2021-01-11-你可能不需要BERT-flow-一个线性变换媲美BERT-flow.md"]
source_ids: ["8069"]
status: stable
updated: 2026-06-12
---

# BERT白化降维

## 演示过程
本例演示如何通过 SVD 求解无参白化核，并直接进行主成分降维（PCA）截断。

我们估计句向量协方差为 $\boldsymbol{\Sigma}$，对其做奇异值分解：
$$
\boldsymbol{\Sigma} = \boldsymbol{U} \boldsymbol{\Lambda} \boldsymbol{U}^{\top}
$$
满足 $\boldsymbol{U}^{\top}\boldsymbol{U} = \boldsymbol{I}$，$\boldsymbol{\Lambda} = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_d)$ 且自大至小排布。
取变换 $\boldsymbol{W} = \boldsymbol{U} \boldsymbol{\Lambda}^{-1/2}$。
则变换后特征的协方差为：
$$
\tilde{\boldsymbol{\Sigma}} = \boldsymbol{W}^{\top} \boldsymbol{\Sigma} \boldsymbol{W} = \boldsymbol{\Lambda}^{-1/2} \boldsymbol{U}^{\top} \boldsymbol{U} \boldsymbol{\Lambda} \boldsymbol{U}^{\top} \boldsymbol{U} \boldsymbol{\Lambda}^{-1/2} = \boldsymbol{I}
$$
若需要压缩维度至 $k < d$，取特征排序前 $k$ 个：
$$
\boldsymbol{W}_{d \times k} = \boldsymbol{U}[:, :k] \text{diag}(\lambda_1^{-1/2}, \dots, \lambda_k^{-1/2})
$$
计算投影映射后，句向量相似度在压缩空间内仍然得以保真甚至净化。