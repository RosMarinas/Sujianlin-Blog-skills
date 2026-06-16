---
type: concept
title: Tokenizer
aliases:
- 分词器
- 子词分词器
definition: 将原始文本转换为模型可处理的token序列的工具，包括BPE、Unigram、WordPiece等方法。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
- Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
source_ids:
- '9762'
- '9768'
prerequisites:
- - - concept::Unigram分词
- - - concept::Viterbi算法
related_methods:
- - - method::Viterbi Sampling
- - - method::Token Healing
status: draft
updated: '2026-06-12'
---

# Tokenizer

Tokenizer是将原始文本映射为离散token ID序列的工具。常见的实现包括BPE、Unigram、WordPiece等。在Unigram分词模型中，其通常的确定性输出依赖Viterbi算法在线性时间内找到最大概率的分词方案。假设$\boldsymbol{w}=(w_1,w_2,\cdots,w_k)$代表一个切分方案，对应的打分为$P(\boldsymbol{w})=p(w_1)p(w_2)\cdots p(w_k)$，$\Omega(S)$代表句子$S$所有可能的切分方案的集合，那么分词算法的数学描述为：
$$
\boldsymbol{w}^* = \mathop{\text{argmax}}_{\boldsymbol{w}\in \Omega(S)}P(\boldsymbol{w})
$$

## 大词表的优劣势与续写问题

对于LLM来说，增大Tokenizer的词表具有明显的优势：“增大词表 → 提高压缩率 → 缩短序列长度”。相同文本对应的tokens数变少使得解码速度获得实打实的提升，并且能够缓解Teacher Forcing带来的Exposure Bias问题，从而可能提升模型效果。

然而，过度增加词表的边界情况是它会“割裂token与token之间在字符层面之间的联系，从而可能会影响泛化”。这种割裂在续写任务上会导致严重的不符合期望的问题。具体案例包括：
1. **代码模型**：“import numpy as np”变成了一个独立的token。当用户仅输入“import numpy”单独出现时，模型无法续写出“ as np”。
2. **自然语言模型**：如果“广州的白云”被分词为“广州/的/白云”，但由于“白云机场”也是一个独立token，直接将分出的三个词转为id输入到模型中，将无法续写出“广州/的/白云机场”，因为Tokenizer无法提前预估未来的文本，导致遇到不完整前缀时的分词结果出错。

## 相关解决与改进对策

### 1. Token Healing（推断期前缀搜索）
针对续写问题，可以在不改变已有模型的前提下，引入基于词表的前缀搜索。在给定不完整输入时，分词器向后“回退一步”（比如拿“白云”去大词表搜索），获取所有匹配前缀的候选词集合（如“白云”、“白云机场”、“白云山”等）。然后用LLM运行一次输入，计算候选词的条件概率，例如：
$$
p(\text{白云机场}|\text{广州},\text{的})
$$
重新归一化后进行采样，以此解决输入前缀切断带来的无法续写问题。此回退操作通常只需在采样第一步进行。

### 2. 随机分词（训练期正则化）
在训练阶段使用带有随机性的tokenize算法（Subword Regularization），使得文本在训练时可能被分为整体也可能被分为子词，从而增强泛化和容错能力。

**Subword Regularization (SentencePiece实现)**
先搜索出$P(\boldsymbol{w})$最大的$n$个分词方案（$n$-best segmentations），然后构建如下分布对这$n$个方案进行依概率采样：
$$
p_i = \frac{P(\boldsymbol{w}^*_i)^{\alpha}}{\sum\limits_{j=1}^n P(\boldsymbol{w}^*_j)^{\alpha}}
$$
该方法的计算复杂度理论上是Viterbi解码的$n$倍，开启后分词速度极大幅度下降。

**Viterbi Sampling (BytePiece实现)**
为了得到复杂度与确定性Viterbi Decoding相近的轻量级随机采样算法，将Viterbi算法在保留当前最优得分路径时的比较替换为了类似于MCMC的接受率：
$$
r_i = \left\{\begin{aligned}&\,1\,, \,\, \varepsilon < \sigma(\alpha(s_i - s_{i-1})) \\
&\,0\,, \,\, \text{else}\end{aligned}\right.
$$
其中$\varepsilon\sim U[0,1]$是均匀随机数，$\alpha > 0$是超参数，$\sigma(t)=1/(1+e^{-t})$是Sigmoid函数，$s_i,s_{i-1}$分别是新旧切分方案的概率对数。当$s_i > s_{i-1}$时，新方案被分配更大概率，极大程度上保持了原最大概率切分的排序，并且在维持原本线性的高效率下引入了合理的分词随机性。
