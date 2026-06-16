---
type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: MathJax公式自适应窗口大小缩放方案
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-10-15-让MathJax的数学公式随窗口大小自动缩放.md
source_ids:
  - 10474
method_summary: 通过JS在MathJax渲染完成后，测量公式本身的宽度与上级或祖父容器的宽度，根据超出的比例动态设置其font-size以达到公式自适应窗口大小自动缩放的效果。
typical_structure: |
  1. 在MathJax配置中去掉自动换行配置(`linebreaks: {automatic: true}`)。
  2. 在MathJax的队列任务中添加渲染完成后的回调函数。
  3. 遍历所有的MathJax公式元素，获取其自身的offsetWidth和上级(或祖父)容器的offsetWidth。
  4. 若公式宽度超过容器宽度，则根据两者的比例计算对应的百分比，并将其赋给公式的font-size。
applicability: 适用于网页公式在移动端窄屏下超出页面边界的排版自适应优化。
examples:
  - [[spaces-10474-网页数学公式自适应窗口缩放]]
evidence_spans:
  - ev::10474::提出了通过JS在MathJax渲染完毕后读取元素宽度并动态缩放font-size，从而使长公式能像图片一样自适应父容器。
status: stable
updated: 2026-06-12
---

# MathJax公式自适应窗口大小缩放方案

## 适用问题
网页中包含较长且不可分割的数学公式时，在移动端窄屏下往往会超出页面边界导致显示不全或排版混乱。传统的自动换行策略会破坏公式原有结构。

## 核心变换
不依赖原生的CSS max-width，而是通过后处理脚本探测元素实际宽度，将其等效为一个缩放比例并应用在CSS font-size上。

## 典型步骤
1. 在MathJax配置中去掉自动换行配置(`linebreaks: {automatic: true}`)。
2. 在MathJax的队列任务中添加渲染完成后的回调函数。
3. 遍历所有的MathJax公式元素（比如找 `id` 以 `MathJax-Element` 开头的span）。
4. 获取公式自身的 `offsetWidth`，并根据公式类型（行内/块级）获取其父级或祖父级的宽度 `offsetWidth`。
5. 若公式宽度超过容器宽度，计算容器宽与公式宽的比例（例如乘上100），并动态将其设为该公式的 `font-size`。

## 直觉
数学公式既然渲染为文本块，就可以像普通图片受限于max-width一样缩小。我们只需要把缩放的动作转换为调整字体大小，如果公式内容长过容器，那么按等比缩小字体，使得排版恰好能放入容器。

## 边界
如果公式过长且屏幕过窄，缩放后的字体可能过小导致难以阅读；此操作需要在公式首次完全排版并占用DOM后执行，有短暂的闪烁。

## 例子
一段超长方程式：`\begin{equation}一个超长的数学公式\end{equation}` 在手机屏幕上会被JS动态将其字体大小设为譬如`75%`以完美贴合。

## 证据
- ev::10474::提出了通过JS在MathJax渲染完毕后读取元素宽度并动态缩放font-size，从而使长公式能像图片一样自适应父容器。
