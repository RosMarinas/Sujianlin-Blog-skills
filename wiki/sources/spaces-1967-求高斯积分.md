---
type: article_summary
title: 费曼积分法(8)：求高斯积分
article_id: "1967"
source_url: https://spaces.ac.cn/archives/1967
date: 2013-04-14
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-04-14-费曼积分法-8-求高斯积分.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1967::参数置于积分区间
  - ev::1967::f_x构造
  - ev::1967::高斯积分结果
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-04-14-费曼积分法-8-求高斯积分.md
source_ids:
  - "1967"
status: draft
updated: 2026-06-10
---

# 费曼积分法(8)：求高斯积分

## 摘要

本文展示了如何利用费曼积分法求高斯积分 $\int_0^\infty e^{-x^2}dx = \sqrt{\pi}/2$。核心技巧是将参数置于积分区间中：构造 $f(x)=\big(\int_0^x e^{-t^2}dt\big)^2$，对 $x$ 求导后通过变量代换 $t=ux$ 将二重积分化为单重积分，最终取 $x\to\infty$ 得到结果。

## 公式

### 构造方法

$$
f(x)=\left(\int_0^x e^{-t^2}dt\right)^2
$$

求导得：

$$
f'(x)=2\int_0^x e^{-t^2}dt \cdot e^{-x^2}=2\int_0^x e^{-(t^2+x^2)}dt
$$

作代换 $t=ux$：

$$
f'(x)=\int_0^1 2x e^{-(1+u^2)x^2}du
$$

### 结果

$$
f(x)=-\int_0^1 \frac{e^{-(1+u^2)x^2}}{1+u^2}du + \frac{\pi}{4}
$$

取 $x\to\infty$：

$$
f(\infty)=\frac{\pi}{4}, \quad \int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}
$$
