---
type: article_summary
title: "【外微分浅谈】4. 微分不微"
article_id: "4059"
source_url: https://spaces.ac.cn/archives/4059
date: 2016-11-05
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-4-微分不微.md
series:
  - "[[外微分浅谈]]"
concepts:
  - "[[微分形式]]"
  - "[[外微分]]"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-05-外微分浅谈-4-微分不微.md
source_ids:
  - "4059"
status: draft
updated: 2026-06-11
---

## 概述
本文正式定义了高维空间中的微分形式（Differential Forms）与外微分（Exterior Derivative）。作者首先将坐标的微元 $dx^\mu$ 视为基底，在反对称外积的基础上建立了 $p$-形式微分，并定义了外微分算子 $d$。文章着重推导并阐述了外微分算子的两个核心性质：零幂性（$d^2\omega = 0$）与外微分的 Leibniz 乘积法则。最后，文章展示了一个立竿见影的代数应用，即利用微分形式的外积判定多维空间中向量组的线性相关性。

## 关键内容
1. **微分形式与外积基底**：
   - 0-形式：普通的标量函数 $f$。
   - 1-形式：以 $dx^\mu$ 为基底的线性组合 $\omega_\mu dx^\mu$。
   - $p$-形式：以反对称积 $dx^{\mu_1} \land \dots \land dx^{\mu_p}$ 为基底构成的代数式。
2. **外微分算子 $d$**：
   - 定义为提升形式阶数的微分运算：
     $$d\left(\omega_{\mu_1 \dots \mu_p} dx^{\mu_1}\land \dots\land dx^{\mu_p}\right) = \frac{\partial \omega_{\mu_1 \dots \mu_p}}{\partial x^{\mu_{p+1}}} dx^{\mu_{p+1}}\land dx^{\mu_1}\land \dots\land dx^{\mu_p}$$
3. **外微分的关键性质**：
   - 零幂性质：对于任意微分形式 $\omega$，始终满足：
     $$d^2 \omega = 0$$
   - Leibniz 法则：如果 $\alpha$ 是 $p$-形式而 $\beta$ 是 $q$-形式，则：
     $$d(\alpha\land \beta)=d\alpha\land \beta + (-1)^p \alpha\land d\beta$$
4. **判定向量组线性相关**：
   - 设 $k$ 个向量的分量为 $\alpha^1, \dots, \alpha^k$，构造其对应的 1-形式。则这 $k$ 个向量线性相关，当且仅当它们的外积为 0：
     $$(\alpha_{\mu}^1 dx^{\mu}) \land (\alpha_{\mu}^2 dx^{\mu}) \land \dots \land (\alpha_{\mu}^k dx^{\mu})=0$$
