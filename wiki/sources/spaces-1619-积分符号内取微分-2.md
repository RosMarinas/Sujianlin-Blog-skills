---
type: article_summary
title: 费曼积分法——积分符号内取微分(2)
article_id: "1619"
source_url: https://spaces.ac.cn/archives/1619
date: 2012-06-12
category: 数学研究
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2012-06-12-费曼积分法-积分符号内取微分-2.md
series:
  - 费曼积分法
concepts:
  - 含参变量积分
  - 变限积分
  - 积分符号内取微分
methods:
  - 积分符号内取微分法
evidence_spans:
  - ev::1619::一般原理
  - ev::1619::莱布尼茨法则
  - ev::1619::例子1
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-12-费曼积分法-积分符号内取微分-2.md
source_ids:
  - "1619"
status: draft
updated: 2026-06-10
---

# 费曼积分法——积分符号内取微分(2)

## 摘要

本文推导了"积分符号内取微分"的一般原理——含参变量积分的 Leibniz 法则，并通过第一个实例展示了该方法的操作步骤。文章指出费曼积分法的核心在于引入合适的参数，使得求导后积分变得简单。

## 公式

### Leibniz 法则（变限积分）

$$
G(a)=\int_{m(a)}^{n(a)} f(x,a)dx
$$

$$
G'(a)=\int_{m(a)}^{n(a)} \frac{\partial f(x,a)}{\partial a} dx + f(n(a),a)\cdot n'(a)-f(m(a),a)\cdot m'(a)
$$

当积分限为常数时简化为：

$$
G'(a)=\int_{m}^{n} \frac{\partial f(x,a)}{\partial a} dx
$$

### 例 1：∫₀^{π/2} x/tan(x) dx

$$
G(a)=\int_0^{\pi/2} \frac{\arctan(a\tan x)}{\tan x}dx
$$

求导、积分、再积分的结果：

$$
G(a)=\frac{\pi}{2}\ln(1+a), \quad G(1)=\frac{\pi}{2}\ln 2
$$
