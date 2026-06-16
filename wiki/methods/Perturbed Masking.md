---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Perturbed Masking
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
  - 7476
method_summary: 通过比较MLM模型在不同mask方案下的输出差异，计算token间相关度，用于无监督分词和句法分析
typical_structure: |
  1. 指定目标 token $x_i$，通过模型计算将其替换为 `[MASK]` 时的表示 $H(\boldsymbol{x}\backslash \{x_i\})_i$。
  2. 指定上下文中的另一 token $x_j$，将 $x_i$ 和 $x_j$ 同时替换为 `[MASK]` 得到表示 $H(\boldsymbol{x}\backslash \{x_i, x_j\})_i$。
  3. 计算这两个表示之间的距离（如欧氏距离），以此衡量 $x_j$ 对 $x_i$ 的依赖影响程度，构成相关矩阵。
  4. 利用生成的相关矩阵执行聚类等操作，进行无监督的边界切分或层级结构生成。
applicability: 无监督分词、无监督句法分析、BERT内部机制的可解释性探测等任务。
tools: 
related_methods: 
examples:
  - [[article::7476]]
status: stable
updated: 2026-06-12
problem_patterns: 
evidence_spans: 
  - ev::7476::"我们将其定义为$f(x_i, x_j)=d\big(H(\boldsymbol{x}\backslash \{x_i\})_i, H(\boldsymbol{x}\backslash \{x_i, x_j\})_i\big)$...可以用两者的距离代表着$x_j$对$x_i$的“影响力”"
---

# Perturbed Masking

## 适用问题

期望直接使用已训练好的掩码语言模型（MLM，如BERT）在无监督、不微调的情况下进行词法分析（分词）或抽取树状层级的句法结构，同时也是探测或解释语言模型内部如何理解 token 之间关联的一种方法。

## 核心变换

将“评估 token 间的依存关系”这一目标转换为“控制变量的特征距离计算”：即通过掩码掉部分上下文（Perturbation），观察目标预测位置的编码向量所产生的偏离（Distance），以此定量评估 token 间的影响力。

## 典型步骤

1. **单目标掩码编码**：将待分析句中的第 $i$ 个 token 替换为 `[MASK]`，提取 MLM 模型在这个位置输出的上下文编码特征 $H(\boldsymbol{x}\backslash \{x_i\})_i$。
2. **双目标联合掩码编码**：同时将第 $i$ 和第 $j$ 个 token 都替换为 `[MASK]`，提取 MLM 此时在第 $i$ 个位置的特征 $H(\boldsymbol{x}\backslash \{x_i, x_j\})_i$。
3. **距离计算**：计算上述两个特征的差异距离（如欧几里得距离），得到 $x_j$ 对 $x_i$ 的影响度矩阵。
4. **扩展 Span 级影响**：如果研究对象是词或 Span，取 Span 内部特征的平均值再行距离对比。
5. **结构解码**：基于获得的影响度关联矩阵，设定阈值进行无监督的连续分词，或利用有序神经元递归聚类方法抽取无监督层级树状句法结构。

## 直觉

MLM的本质是通过周围所有的“未掩盖词”去猜被“掩盖”的那个词。当目标词已经被掩盖后，如果我再悄悄把句子里的另一个词也掩盖掉，导致模型猜测目标词时所依赖的特征发生了巨大的变动，这就说明被二次掩盖的这个词非常重要，两者之间存在强依赖关联。

## 边界

- **非对称性**：$x_j$ 对 $x_i$ 的影响不一定等同于 $x_i$ 对 $x_j$ 的影响。在某些简单分词中需要作对称化平均处理。
- **长序列代价**：由于每次评估都需要运行一次包含掩蔽的模型前向计算，构建全局 $T \times T$ 矩阵需要大量的推理调用，时间开销会随句子长度平方级增长。

## 例子

- **BERT无监督中文分词**：使用欧氏距离作为 token 关联衡量，基于相邻 token 的影响度得分均值，通过设定一个阈值直接切分中文句子。在未使用分词任务微调的 BERT 模型下，达到了非常合理的成词效果。
- **Span层次结构抽取**：结合聚类思路，不断递归二分句子以使类内特征关联度最大、类间特征关联度最小，成功无监督析出了“欧拉是一名数学家”等语句的依存句法树状结构。

## 证据

- ev::7476::"按照“mask越多、预测越不准“直观想法，我们有理由相信$H(\boldsymbol{x}\backslash \{x_i\})_i$比$H(\boldsymbol{x}\backslash \{x_i, x_j\})_i$能更准确地预测$x_i$，而$H(\boldsymbol{x}\backslash \{x_i, x_j\})_i$跟$H(\boldsymbol{x}\backslash \{x_i\})_i$相比就是去掉了$x_j$的信息，所以可以用两者的距离代表着$x_j$对$x_i$的“影响力”。"
- ev::7476::"有了相关矩阵之后，分词是一个很自然的应用...设定一个阈值，然后把相关度小于这个阈值的两个token切开，大于等于这个阈值的两个token拼接"
