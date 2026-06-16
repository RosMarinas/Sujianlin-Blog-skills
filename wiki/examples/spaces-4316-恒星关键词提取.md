---
type: example
title: spaces-4316-恒星关键词提取
aliases: []
article_id: '4316'
article: '[[spaces-4316-不可思议的Word2Vec-3-提取关键词]]'
section: 实践为上
claim: 用 Word2Vec 提取 '太阳是一颗恒星' 的关键词
notation_mapping:
  s: 太阳是一颗恒星
  w_i: 恒星 | 太阳 | 一颗 | 是
steps:
- '对输入文本 ''太阳是一颗恒星'' 进行分词，得到词序列: [''太阳'', ''是'', ''一颗'', ''恒星'']。'
- 排除词表中不存在的词（此处全部保留）。
- 对每个词 w_i，在整个分词序列上计算转移概率 sum_u log P(u | w_i)。其中 P(u|w_i) 由 Skip-Gram + Huffman Softmax
  预训练模型进行计算。
- 根据计算出的条件概率对数进行降序排列，得分最高者即为关键词。排名前两位的词为 '恒星' (-27.90) 和 '太阳' (-28.11)。
used_concepts:
- '[[Word2Vec]]'
- '[[Skip-Gram]]'
- '[[Hierarchical Softmax]]'
used_formulas:
- '[[基于点互信息PMI的相关词度量]]'
used_methods:
- '[[基于Word2Vec的无监督关键词提取]]'
source_span: ev::4316::分词实践
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-04-07-不可思议的Word2Vec-3-提取关键词.md
source_ids:
- '4316'
status: draft
updated: '2026-06-12'
---

# spaces-4316-恒星关键词提取

演示了利用 $P(s|w_i)$ 条件概率对一句话抽取关键词的计算流向。为了估算词与词之间的转移概率 $p(w_k|w_i)$，模型使用了 Skip-Gram + Huffman Softmax 的预训练模型对概率对数进行计算，节点向量和输入词向量的内积化简过程如下：

$$
\begin{aligned}&\log \left(\frac{1}{1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}}\right)^{1-d}\left(1-\frac{1}{1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}}\right)^{d}\\
=&-(1-d)\log (1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}) - d \log (1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}) - d \boldsymbol{x}^{\top} \boldsymbol{\theta}\\
=&-\log (1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}) - d \boldsymbol{x}^{\top} \boldsymbol{\theta}\end{aligned}
$$

考虑到官方的 score_sg_pair 函数实际实现，其化简过程为：

$$
\begin{aligned}&-\log (1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}}) - d \boldsymbol{x}^{\top} \boldsymbol{\theta}\\
=&-\log \bigg[e^{d \boldsymbol{x}^{\top}\theta}(1+e^{-\boldsymbol{x}^{\top} \boldsymbol{\theta}})\bigg]\\
=&-\log \bigg(e^{d \boldsymbol{x}^{\top}\theta}+e^{(d-1)\boldsymbol{x}^{\top} \boldsymbol{\theta}}\bigg)\\
=&-\log \bigg(1+e^{-(-1)^d \boldsymbol{x}^{\top}\theta}\bigg)\end{aligned}
$$

实践中的具体计算代码流向如下：

```python
import numpy as np
import gensim
from collections import Counter
import pandas as pd
import jieba

model = gensim.models.word2vec.Word2Vec.load('word2vec_wx')

def predict_proba(oword, iword):
    iword_vec = model[iword]
    oword = model.wv.vocab[oword]
    oword_l = model.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot) 
    return lprob

def keywords(s):
    s = [w for w in s if w in model]
    ws = {w:sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()

s = u'太阳是一颗恒星'
pd.Series(keywords(jieba.cut(s)))
```

输出结果是：
> 0 (恒星, -27.9013707845)
> 
> 1 (太阳, -28.1072913493)
> 
> 2 (一颗, -30.482187911)
> 
> 3 (是, -36.3372344659)
