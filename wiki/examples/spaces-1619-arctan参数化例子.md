---
type: example
title: 反函数参数化求 ∫₀^{π/2} x/tan(x) dx
aliases:
- arctan参数化示例
notation_mapping:
  G(a): 含参变量积分
  a: 人工参数
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-06-12-费曼积分法-积分符号内取微分-2.md
source_ids:
- '1619'
evidence_spans: []
article_id: '1619'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

# 反函数参数化求 ∫₀^{π/2} x/tan(x) dx

## 问题

求 $\displaystyle I = \int_0^{\pi/2} \frac{x}{\tan x}dx$.

## 参数化

对 $\int x/f(x)dx$ 形式，采用反函数参数化：

$$
G(a) = \int_0^{\pi/2} \frac{\arctan(a\tan x)}{\tan x}dx
$$

原积分 $I = G(1)$.

## 求导

$$
\frac{\partial}{\partial a}\frac{\arctan(a\tan x)}{\tan x} = \frac{1}{a^2\tan^2 x+1}
$$

改写后积分：

$$
G'(a) = \frac{1}{1-a^2}\int_0^{\pi/2}\left[1-\frac{2a^2}{(1+a^2)+(1-a^2)\cos 2x}\right]dx
$$

利用 $\int \frac{dx}{a+b\cos x}$ 类型的积分公式：

$$
G'(a) = \frac{\pi}{2(1+a)}
$$

## 还原

$$
G(a) = \frac{\pi}{2}\ln(1+a) + C
$$

由 $G(0)=0$ 得 $C=0$，故：

$$
I = G(1) = \frac{\pi}{2}\ln 2
$$

## 关键技巧

- 反函数参数化：将 $x$ 替换为 $\arctan(a\tan x)$
- 求导后出现 $\frac{1}{a^2\tan^2 x+1}$ 形式，可通过三角恒等式化为 $\frac{1}{a+b\cos 2x}$ 类型
- 利用已知积分公式 $\int \frac{dx}{a+b\cos x}$ 完成第一次积分