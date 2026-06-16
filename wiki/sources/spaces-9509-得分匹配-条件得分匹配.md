---
type: article_summary
title: 生成扩散模型漫谈（十八）：得分匹配 = 条件得分匹配
article_id: "9509"
source_url: https://spaces.ac.cn/archives/9509
date: 2023-02-28
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-02-28-生成扩散模型漫谈-十八-得分匹配-条件得分匹配.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[得分匹配]]"
  - "[[条件得分匹配]]"
evidence_spans:
  - ev::9509::得分匹配
  - ev::9509::条件得分
  - ev::9509::不等关系
  - ev::9509::等价关系
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-02-28-生成扩散模型漫谈-十八-得分匹配-条件得分匹配.md
source_ids:
  - "9509"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文证明了扩散模型中"得分匹配"（Score Matching）与"条件得分匹配"（Conditional Score Matching）之差是一个与模型参数无关的常数，因此两者在优化意义上是完全等价的——尽管它们的统计量性质不同（有偏vs无偏估计）。

## 核心问题

在扩散模型文献中，"得分匹配"和"条件得分匹配"这两个概念常被混用。第16篇已证明条件得分匹配是得分匹配的上界，但它们之间是否存在更深层的等价关系？两者的实际区别是什么？

## 关键结论

1. **等价性（主结果）**：得分匹配与条件得分匹配之差为$\mathbb{E}_{\boldsymbol{x}_t}[\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\|\nabla \log p_t(\cdot|\boldsymbol{x}_0)\|^2] - \|\nabla \log p_t\|^2]$，该量仅依赖数据分布和扩散过程，与模型参数$\boldsymbol{\theta}$无关。
2. **上下界关系的深化**：第16篇仅证明了条件得分匹配 $\geq$ 得分匹配（上界关系），本文证明了更强的等价关系——两者仅差一个常数，因此最小化任一目标都得到相同的最优参数。
3. **有偏vs无偏的鸿沟**：尽管理论上等价，实际统计量性质不同——得分匹配的估计器涉及两个期望的除法，是有偏估计且依赖大batch_size；条件得分匹配是直接可用的无偏估计，不需要大batch_size。等价性仅在无限样本极限下成立。
4. **历史溯源**：该等价结果最早出现在Vincent (2011)的论文"A Connection Between Score Matching and Denoising Autoencoders"中。

## 核心推导

推导通过将两个目标展开后逐项对比来完成：

**步骤1**：展开得分匹配(SM)：
$$\text{SM} = \mathbb{E}_{\boldsymbol{x}_t}[\|\nabla\log p_t\|^2] + \mathbb{E}_{\boldsymbol{x}_t}[\|\boldsymbol{s}_{\boldsymbol{\theta}}\|^2] - 2\mathbb{E}_{\boldsymbol{x}_t}[\boldsymbol{s}_{\boldsymbol{\theta}}\cdot\nabla\log p_t]$$

**步骤2**：展开条件得分匹配(CSM)，利用联合分布$p(\boldsymbol{x}_0,\boldsymbol{x}_t)=p(\boldsymbol{x}_t)p(\boldsymbol{x}_0|\boldsymbol{x}_t)$：
$$\text{CSM} = \mathbb{E}_{\boldsymbol{x}_t}[\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\|\nabla\log p_t(\cdot|\boldsymbol{x}_0)\|^2]] + \mathbb{E}_{\boldsymbol{x}_t}[\|\boldsymbol{s}_{\boldsymbol{\theta}}\|^2] - 2\mathbb{E}_{\boldsymbol{x}_t}[\boldsymbol{s}_{\boldsymbol{\theta}}\cdot\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\nabla\log p_t(\cdot|\boldsymbol{x}_0)]]$$

**步骤3**：应用关键恒等式$\nabla\log p_t = \mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\nabla\log p_t(\cdot|\boldsymbol{x}_0)]$，两个目标的$\|\boldsymbol{s}_{\boldsymbol{\theta}}\|^2$项和交叉项完全相同。

**步骤4**：差值仅剩$\|\text{target}\|^2$项之差：$\text{CSM} - \text{SM} = \mathbb{E}_{\boldsymbol{x}_t}[\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\|\nabla\log p_t(\cdot|\boldsymbol{x}_0)\|^2] - \|\nabla\log p_t\|^2]$，该项与$\boldsymbol{\theta}$无关。

## 关键公式

**得分匹配（SM）**：
$$\mathbb{E}_{\boldsymbol{x}_t\sim p_t(\boldsymbol{x}_t)}\left[\left\Vert\nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t) - \boldsymbol{s}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)\right\Vert^2\right]$$

**条件得分匹配（CSM）**：
$$\mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_t\sim p_0(\boldsymbol{x}_0)p_t(\boldsymbol{x}_t|\boldsymbol{x}_0)}\left[\left\Vert\nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) - \boldsymbol{s}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)\right\Vert^2\right]$$

**关键恒等式**：
$$\nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t) = \mathbb{E}_{\boldsymbol{x}_0\sim p_t(\boldsymbol{x}_0|\boldsymbol{x}_t)}\left[\nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t|\boldsymbol{x}_0)\right]$$

**等价比率**（与$\boldsymbol{\theta}$无关的常数）：
$$\text{CSM} - \text{SM} = \mathbb{E}_{\boldsymbol{x}_t}\left[\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}\left[\|\nabla\log p_t(\cdot|\boldsymbol{x}_0)\|^2\right] - \|\nabla\log p_t\|^2\right]$$

## 实验或案例

本文为纯理论分析，没有实验验证。作者在文末特别澄清了一个重要的实践认识：尽管理论上等价，但直接从公式(score-1)估计$\nabla\log p_t$来做得分匹配仍是有偏的、依赖大batch_size的方法，这与条件得分匹配的无偏估计性质不同。等价性只在样本数趋于无穷时才严格成立。

## 系列定位

本文是系列中一篇短小精悍的补充性理论文章。它在第16篇（证明了CSM是SM的上界）的基础上进一步发现了两者之间的等价关系，澄清了文献中一个容易混淆的基本问题。通过揭示这两个训练目标的确切关系，本文为理解扩散模型训练目标的本质提供了关键的微观理论基础。
