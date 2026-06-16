---


type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 基于Word2Vec计算相关词
aliases: 
sources:
  - Data/Spaces_ac_cm/markdown/Big-Data/2020-08-20-最小熵原理-六-词向量的维度应该怎么选择.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-01-不可思议的Word2Vec-4-不一样的-相似.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-一-simpler-glove.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-二-对语言进行建模.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-五-有趣的结果.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-六-代码-分享与结语.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-02-最小熵原理-四-物以类聚-之从图书馆到词向量.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
source_ids:
  - 4368
  - 4669
  - 4675
method_summary: 利用 Word2Vec 模型预测的条件概率 log P(y|x) 扣减词频边际分布项 log P(y) 来衡量词之间的点互信息(PMI)相关性。
typical_structure: |
  1. 预先在大规模语料库上训练一个基于 Skip-Gram 的 Word2Vec 模型。
  2. 获取训练好的模型中词的频率边际分布 $P(w)$ 以及模型能预测给定的中心词生成上下文词的条件概率 $P(w_j|w_i)$。
  3. 通过 $\\log P(w_j|w_i) - \\alpha \\log P(w_j)$ 计算点互信息，其中 $\\alpha$ 可略小于1（如0.9）以增强高频词的相关性。
  4. 对某个查询词 $w_i$，将词表内其他词按互信息降序排列，排在前面的即为最强“相关词”。
applicability: 需要召回地理、文化等外部关联词（如地标、机构）而非词法层面的同义词（余弦相似）时使用，常用于搜索推荐与语义关联分析。
examples:
  - [[spaces-4368-广州相关词计算]]
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::4368::这种“相似”，准确来说是“相关”，应该怎么描述呢？答案是互信息...这个也完全可以由Word2Vec中的Skip-Gram+Huffman Softmax模型来完成。"
  - "ev::4675::对于像“的”、“了”这些几乎没有意义的词语...模长会自动接近于0，所以我们说词向量的模长能在一定程度上代表词的重要程度。"
---






## 适用问题

需要基于大规模语料寻找词语的强关联词汇（如“广州”关联“白云机场”、“小蛮腰”等具备现实伴随关系的词汇），而不仅仅是语义同义词或可替换词（如“广州”替换为“深圳”）时。常用于搜索引擎推荐、场景实体联想等。

## 核心变换

将“基于词向量余弦距离寻找相似词”的任务，转换为“计算词间点互信息（PMI）来寻找经常共同出现的搭配词”。利用 Word2Vec 模型内置的条件生成概率取代传统统计学中低效的全量共现计数。

## 典型步骤

1. 预先在大规模语料库上训练一个基于 Skip-Gram 的 Word2Vec 模型（含 Huffman Softmax 等）。
2. 从模型参数和词频统计中提取出目标词 $w_i$ 对上下文候选词 $w_j$ 的生成概率对数 $\log P(w_j|w_i)$ 以及边缘词频概率对数 $\log P(w_j)$。
3. 利用两者的差值计算点互信息（PMI）：$\log \frac{P(w_j, w_i)}{P(w_j)P(w_i)} \approx \log P(w_j|w_i) - \log P(w_j)$。为了防止过分偏好低频词，可引入惩罚系数 $\alpha$：$\log P(w_j|w_i) - \alpha \log P(w_j)$。
4. 将目标词与其他词的相关度从大到小排列，选取 Top-K 作为最终的相关词集合。

## 直觉

普通的余弦相似度代表的是“两个词在句子中能否互相替换而保持句子语法合理”，因为它们周边通常环绕着相同的上下文；而互信息（PMI）代表的是“两个词是否经常在同一句话中成对出现”，比如“飞机”和“机场”。Word2Vec 内部恰恰是依靠共现概率来训练的，稍微改造一下输出层概率预测公式，就能把隐藏在参数中的“相关性”提炼出来。

## 边界

- 提取相关词需要遍历一次词表中的 Huffman 树概率，在极大词表下计算成本比直接算余弦相似度略高。
- 对于极端低频词，互信息的估计方差很大，可能造成异常相关，因此往往需要 $\alpha$ 衰减参数来压制。

## 例子

查询词：“广州”。
- 找余弦相似词（替换关系）：东莞、深圳、佛山、惠州（都能做“__是广东的城市”的填空）。
- 找互信息相关词（伴随出现关系）：福中路、白云机场、第十甫路、光孝寺（都是在广州场景下高频出现的实体地标）。

## 证据

- ev::4368::这种“相似”，准确来说是“相关”，应该怎么描述呢？答案是互信息...这个也完全可以由Word2Vec中的Skip-Gram+Huffman Softmax模型来完成。
- ev::4671::因为词与词的相关程度用相关度来描述... 从形式上看类似对互信息矩阵的SVD分解。
- ev::4675::对于像“的”、“了”这些几乎没有意义的词语...模长会自动接近于0，所以我们说词向量的模长能在一定程度上代表词的重要程度。
