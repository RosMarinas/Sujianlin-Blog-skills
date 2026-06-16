---
type: article_summary
title: 用热传导方程来指导自监督学习
article_id: "9359"
source_url: https://spaces.ac.cn/archives/9359
date: 2022-11-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-11-30-用热传导方程来指导自监督学习.md
concepts:
  - [[QB-Heat]]
  - [[特征图拉普拉斯先验]]
methods:
  - [[用拉普拉斯方程一阶离散化特征预测的自监督学习]]
formulas:
  - [[离散拉普拉斯特征预测公式]]
examples:
  - [[spaces-9359-QB-Heat特征重建]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-11-30-用热传导方程来指导自监督学习.md
source_ids:
  - "9359"
status: stable
updated: 2026-06-12
---

# 用热传导方程来指导自监督学习

## 摘要
本文介绍了基于物理热传导方程（更准确地说是拉普拉斯方程）指导图像领域自监督学习特征表示的方法，即“QB-Heat”。该方法认为，图像经过Encoder得到的特征图（Feature Map）在局部邻近位置上应当满足各向异性的拉普拉斯方程（二阶偏微分方程）。为了在离散特征网格上应用该约束，作者利用辅助矩阵将二阶拉普拉斯方程分解为一阶偏微分方程组，并采用一阶欧拉差分近似实现特征预测。在自监督学习框架中，QB-Heat每次仅向Encoder输入图像的一小部分，然后利用该离散化递推关系预测被遮蔽的四周特征，并由Decoder重建完整图像。最后，作者脱离物理幌子，指明该方法本质上是通过连续性和线性性假设为特征表示引入隐式正则化约束，从而增强模型的泛化能力。
