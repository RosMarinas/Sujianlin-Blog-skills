---
type: article_summary
title: "生成扩散模型漫谈（十二）：“硬刚”扩散ODE"
article_id: "9280"
source_url: "https://spaces.ac.cn/archives/9280"
date: "2022-09-28"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2022-09-28-生成扩散模型漫谈-十二-硬刚-扩散ODE.md"
series:
  - "[[生成扩散模型漫谈]]"
topics: []
concepts:
  - "[[概率守恒]]"
  - "[[连续方程]]"
  - "[[得分匹配]]"
methods:
  - "[[ODE直接推导法]]"
problem_patterns: []
evidence_spans:
  - "ev::9280::微分方程"
  - "ev::9280::雅可比行列式"
  - "ev::9280::泰勒近似"
  - "ev::9280::热传导方程"
  - "ev::9280::求解分布"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2022-09-28-生成扩散模型漫谈-十二-硬刚-扩散ODE.md"
source_ids:
  - "9280"
status: draft
updated: "2026-06-09"
---

# 生成扩散模型漫谈（十二）：“硬刚”扩散ODE

## 文章核心问题

能否不经过SDE/FP方程的"迂回"路线，直接从ODE出发推导出扩散模型所需的概率变换条件？最终ODE扩散模型应满足什么方程、对应什么形式的解？

## 主要结论

1. ODE扩散模型可以直接从一阶ODE + 雅可比行列式 + 泰勒展开推导出来，无需经过SDE或Fokker-Planck方程。
2. ODE的漂移项 $\boldsymbol{f}_t$ 必须满足连续性方程 $\frac{\partial}{\partial t} p_t = -\nabla_{\boldsymbol{x}_t}\cdot(\boldsymbol{f}_t p_t)$，这是一个不定方程（1个方程，$d$个未知数），具有极大灵活性。
3. 采用得分参数化 $\boldsymbol{f}_t = -D_t \nabla_{\boldsymbol{x}_t}\log p_t$ 后将代入连续性方程得到扩散方程；在位置无关标量 $D_t$ 的假设下，扩散方程退化为热传导方程。
4. 热传导方程的解是高斯混合分布 $p_t(\boldsymbol{x}_t) = \int \mathcal{N}(\boldsymbol{x}_t; \boldsymbol{x}_0, \sigma_t^2 \boldsymbol{I}) p_0(\boldsymbol{x}_0) d\boldsymbol{x}_0$，其中 $\sigma_t^2 = 2\int_0^t D_s ds$。
5. 最终ODE为 $\frac{d\boldsymbol{x}_t}{dt} = -\dot{\sigma}_t \sigma_t \nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t)$，其中得分函数可通过条件得分匹配学习。

## 推导结构

1. **ODE定义**：设 $\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{f}_t(\boldsymbol{x}_t)$，描述从 $\boldsymbol{x}_0$ 到 $\boldsymbol{x}_T$ 的可逆变换。
2. **雅可比行列式**：根据概率守恒 $p_t d\boldsymbol{x}_t = p_{t+\Delta t} d\boldsymbol{x}_{t+\Delta t}$ 和雅可比行列式近似，得到 $\log p_{t+\Delta t} - \log p_t \approx -\nabla_{\boldsymbol{x}_t}\cdot \boldsymbol{f}_t \Delta t$。
3. **泰勒展开匹配**：将 $\log p_{t+\Delta t}(\boldsymbol{x}_{t+\Delta t})$ 一阶泰勒展开并与雅可比结果匹配，得到 $\boldsymbol{f}_t$ 的约束方程，整理为连续性方程。
4. **得分参数化**：设 $\boldsymbol{f}_t = -D_t \nabla_{\boldsymbol{x}_t}\log p_t$，代入后得到热传导方程 $\frac{\partial}{\partial t}p_t = D_t \nabla^2 p_t$。
5. **傅里叶变换求解**：利用傅里叶变换求解热传导方程，得到高斯混合解，最终确定完整 ODE 形式。

## 关键公式

- **ODE定义**: $\frac{d\boldsymbol{x}_t}{dt} = \boldsymbol{f}_t(\boldsymbol{x}_t)$
- **概率守恒（对数差异）**: $\log p_{t+\Delta t}(\boldsymbol{x}_{t+\Delta t}) - \log p_t(\boldsymbol{x}_t) \approx -\nabla_{\boldsymbol{x}_t}\cdot \boldsymbol{f}_t(\boldsymbol{x}_t) \Delta t$
- **连续性方程**: $\frac{\partial}{\partial t} p_t(\boldsymbol{x}_t) = - \nabla_{\boldsymbol{x}_t}\cdot\Big(\boldsymbol{f}_t(\boldsymbol{x}_t) p_t(\boldsymbol{x}_t)\Big)$
- **得分参数化**: $\boldsymbol{f}_t(\boldsymbol{x}_t) = - \boldsymbol{D}_t(\boldsymbol{x}_t)\,\nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t)$
- **热传导方程**: $\frac{\partial}{\partial t}p_t(\boldsymbol{x}_t) = D_t \nabla_{\boldsymbol{x}_t}^2 p_t(\boldsymbol{x}_t)$
- **高斯混合解**: $p_t(\boldsymbol{x}_t) = \int \frac{1}{(2\pi\sigma_t^2)^{d/2}}\exp\left(-\frac{\Vert \boldsymbol{x}_t - \boldsymbol{x}_0\Vert^2}{2\sigma_t^2}\right)p_0(\boldsymbol{x}_0) d \boldsymbol{x}_0$
- **最终生成ODE**: $\frac{d\boldsymbol{x}_t}{dt} = -\dot{\sigma}_t \sigma_t \nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t)$

## 实验或案例

本文为纯理论推导，未提供实验。

## 所属系列位置

本文是系列第12篇，提供一个"自上而下"的ODE扩散模型推导，绕开了SDE→ODE的间接路线。它与第5篇（SDE框架）、第6篇（Fokker-Planck方程）和第4篇（DDIM）存在联系，但采用更直接的方法。同时，它为后续第13篇（PFGM）和第14/15篇（一般ODE构建框架）提供了核心数学工具——连续性方程。

## 与其他文章的关系

- builds_on: [[生成扩散模型漫谈（四）：DDIM = 高观点DDPM]]
- builds_on: [[生成扩散模型漫谈（五）：一般框架之SDE篇]]
- builds_on: [[生成扩散模型漫谈（六）：一般框架之ODE篇]]
- precedes: [[生成扩散模型漫谈（十三）：从万有引力到扩散模型]]
- belongs_to: [[生成扩散模型漫谈]]

## 原文证据锚点

- `ev::9280::微分方程`
- `ev::9280::雅可比行列式`
- `ev::9280::泰勒近似`
- `ev::9280::热传导方程`
- `ev::9280::求解分布`
