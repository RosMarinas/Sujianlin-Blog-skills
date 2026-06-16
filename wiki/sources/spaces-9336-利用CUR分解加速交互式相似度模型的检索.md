---
type: article_summary
title: 利用CUR分解加速交互式相似度模型的检索
article_id: 9336
source_url: https://spaces.ac.cn/archives/9336
date: 2022-11-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-11-02-利用CUR分解加速交互式相似度模型的检索.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-11-02-利用CUR分解加速交互式相似度模型的检索.md"]
source_ids: ["9336"]
status: draft
updated: 2026-06-12
---

# 利用CUR分解加速交互式相似度模型的检索

## 文章核心问题
如何在大规模检索场景下，加速计算复杂度为 $\\mathcal{O}(N)$ 且特征无法离线缓存的双向交互式匹配相似度模型（Cross-Encoder）。

## 主要结论
提出了 ANNCUR 检索方案。基于打分矩阵在宏观上的低秩属性，利用 CUR 矩阵分解，将 Cross-Encoder 计算打分 $s(q,k)$ 近似表示为：query 先与 key 的代表集 $\\mathcal{U}$ 交互，key 先与 query 的代表集 $\\mathcal{V}$ 交互，再通过两者交集矩阵的伪逆进行加权。这样所有的检索代表与全库 key 的交互结果都可以离线缓存，检索时仅需算 $|\\mathcal{U}|$ 次交互式打分并执行一次向量-矩阵乘法，计算量大幅下降，且召回后再配合重排序（Re-rank）可实现又快又好。

## 推导结构
1. 对比特征式（Bi-Encoder）和交互式（Cross-Encoder）匹配的优劣及检索瓶颈。
2. 提出用降秩表示重写打分矩阵，并与 SVD 比较。
3. 建立 CUR 分解的直观几何关系：从行列中选出真实子集作代表基底，通过公共交集的 Moore-Penrose 伪逆重建大矩阵。
4. 阐述 ANNCUR 在向量乘法和 Faiss 检索加速中的硬件离线缓存优化设计。

## 关键公式
- CUR 矩阵分解：$\\boldsymbol{S} \\approx \\boldsymbol{F} (\\boldsymbol{F}\\cap \\boldsymbol{H})^{\\dagger}\\boldsymbol{H}$，其中 $\\boldsymbol{F}=\\boldsymbol{S}_{:,\\mathcal{U}}$，$\\boldsymbol{H}=\\boldsymbol{S}_{\\mathcal{V},:}$。
- 近似打分公式：$s(q,k) \\approx \\sum_{u\\in\\mathcal{U},v\\in\\mathcal{V}} s(q, u) g(u, v) s(v, k)$，其中 $g(u, v) = (\\boldsymbol{F}\\cap \\boldsymbol{H})^{\\dagger}_{u,v}$。

## 体现的方法
- [[ANNCUR检索加速]]：在表示层基于行列质心子集与伪逆变换拟合非线性双塔矩阵。

## 与其他文章的关系
- 使用矩阵分解做线性化的另一应用见 [[Nyströmformer：基于矩阵分解的线性化Attention方案]]。
- 是 [[CoSENT（二）：特征式匹配与交互式匹配有多大差距？]] 弥补性能与延迟帕累托边界的重要工作。

## 原文证据锚点
- `ev::9336::ANNCUR原理`：对应原文中利用 CUR 分解将 Cross-Encoder 的两两相似度打分转化为局部代表打分加伪逆加权矩阵乘法的公式定义与检索加速流程。