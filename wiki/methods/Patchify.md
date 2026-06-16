---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Patchify
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-02-21-闭门造车-之多模态思路浅谈-一-无损输入.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-07-08-闭门造车-之多模态思路浅谈-二-自回归.md
source_ids:
  - 10197
  - 9984
method_summary: Patchify是将图像从 $w\times h\times 3$ 的连续像素数组变换为 $s\times t\times d$ 的特征数组的过程。
typical_structure: |
  1. 接收原始连续型输入（如 $w \times h \times 3$ 的图像像素数组）。
  2. 根据设定的Patch尺寸将输入分割。
  3. 执行变形和转置操作，将其转化为序列化的特征数组。
applicability: 需要将连续的高维像素空间或空间特征序列化、分块表示，以接入Transformer或处理离散序列模型时的图像预处理阶段。
tools: 
related_methods: 
examples:
  - [[article::9984]]
  - [[article::10197]]
status: stable
updated: 2026-06-12
belongs_to: null
problem_patterns: 
evidence_spans: 
  - ev::10197::"将图像从 $w\times h \times 3$的数组变成$s\times t\times d$（其中$s < w, t < h$）的数组，我们都可以称为广义的“Patchify”"
---

# Patchify

## 适用问题

视觉模型（如Vision Transformer或自回归图像生成模型）由于需要进行序列建模，直接将单个像素作为Token序列过长且计算不可行，因此需要将原始图像或连续特征阵列转化为合理的短序列表示。

## 核心变换

空间离散化与变形（Spatial Discretization and Reshaping）：将二维网格上的原始像素数组转换为若干块独立的特征表示向量（Token），建立图像的空间序列化。

## 典型步骤

（以狭义Patchify为例，即将 $w\times h\times 3$ 的像素数组转为一维特征）：
1. **尺寸切分**：将原始像素按步长 $s, t$ 变形，转化为 $s\times (w/s) \times t\times (h/t)\times 3$ 的五维张量。
2. **转置聚合**：通过矩阵转置操作汇聚同一个块内的像素，得到 $s\times t\times (w/s)\times (h/t)\times 3$。
3. **展平压缩**：将每个块内的数据展平，形成 $s\times t\times (3wh/st)$ 的特征数组（序列）。

## 直觉

图像的本质是连续像素阵列，但这不适合语言模型习惯的一维离散序列处理方式。既然单个像素信息量太低且计算量爆炸，那就把相邻的一小块像素“打包”当作一个单词来看待，既降低了长度，又保留了局部的空间关联性。

## 边界

- **信息损失**：对于基于 VQ 的广义 Patchify，离散化带来的信息损失往往是严重且不可逆的（如极致压缩到32个Token）。即便是狭义的无损变形 Patchify，也打破了图像在块边缘的连续空间关联。
- **二维到一维的映射歧义**：图像本身并不包含严格的一维时间顺序，不同排序方式（如从左到右、Z字型、螺旋型）都会对模型的自回归学习产生不同影响。

## 例子

- **Vision Transformer**：使用基于线性投影的狭义 Patchify 处理图像，使其能够套用自注意力机制进行图像分类。
- **图像自回归生成**：广义 Patchify 包括将图像通过 Encoder 映射为 Latent 空间的分块，甚至使用 VQ-Tokenizer 得到离散的 ID，作为自回归生成的输入序列。

## 证据

- ev::10197::"将图像从 $w\times h \times 3$的数组变成$s\times t\times d$（其中$s < w, t < h$）的数组，我们都可以称为广义的“Patchify”。不同的Patchify可能会有不同程度的信息损失"
- ev::10197::"狭义的Patchify就是对像素数组的简单变形和转置，即将$w\times h\times 3$的数组先变形为$s\times (w/s) \times t\times (h/t)\times 3$，然后转置为$s\times t\times (w/s)\times (h/t)\times 3$，最后变形为$s\times t\times (3wh/st)$"
