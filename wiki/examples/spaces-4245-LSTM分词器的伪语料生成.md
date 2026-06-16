---
type: example
title: 'spaces-4245: LSTM分词器的伪语料生成'
article_id: '4245'
article:
- - wiki/sources/spaces-4245-中文分词只需词典.md
section: 随机组合就可以
claim: 仅使用一个词频词典，按词频概率进行加权采样随机拼接成句子并生成对应的 SBME 字标注伪标签。
notation_mapping:
  elements: elements (词表中的词语列表)
  weights: weights (各词对应的出现频数权重)
steps:
- step: 1
  description: 载入带频数词典 `dict.txt`。对频数相近的词语进行预合并，以减少随机选择的权重分组数量。
- step: 2
  description: 构建加权选择类 `Random_Choice`，计算权重的累加分布（CDF）：`weights = np.cumsum(weights)/sum(weights)`。
- step: 3
  description: 在数据生成器中，随机决定当前段落所含词数 $n \sim \text{Uniform}(1, 16)$。
- step: 4
  description: 循环 $n$ 次，每次通过随机数落在 CDF 区间的位置，随机抽取词语：`seq = [wc.choice() for i in range(n)]`。
- step: 5
  description: 遍历 `seq`，若词长为 1，赋予标签 `s`；若词长 $L \ge 2$，赋予 `b + 'm'*(L-2) + 'e'`。将词语拼接为完整文本，同步拼接生成字标签序列
    `tag`。
- step: 6
  description: 将字转换成字表 ID，对长度不足最大句长 48 的部分后补 0，并将 SBME 标签映射为 one-hot 编码，填充位赋予特殊的掩码类别
    `[0,0,0,0,1]`。
used_concepts:
- - - concept::中文分词
- - - concept::字标注分词
used_methods:
- - - method::基于词表随机组合语料训练
source_span: ev::4245::伪语料生成
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-03-06-中文分词系列-7-深度学习分词-只需一个词典.md
source_ids:
- '4245'
status: draft
updated: '2026-06-12'
---

# spaces-4245: LSTM分词器的伪语料生成

为了解决深度学习分词器训练对大规模高质量标注语料的依赖问题，本例展示了如何仅利用带频词典加权随机采样，自动拼凑变长汉字序列伪语料并生成对应的 SBME 标注。这种无监督/半监督的方案证明了，即使拼接出的语料不完全符合自然语言语法，只要按词频加权组合，也能训练出效果优异的分词模型。

具体生成机制包含以下核心技术与参数细节：

1. **加权随机采样与 CDF 分组加速**：首先载入包含词频的 `dict.txt`。为了解决直接在全体词表上进行随机加权采样的性能瓶颈，代码采用对词频相近词语“扎堆”预合并的策略（例如将出现 10001、10002 次的词统一归为 10000），大大减少权重分组数量。加权选择类 `Random_Choice` 将按词频计算各组权重的累积分布函数（CDF）：`weights = np.cumsum(weights).astype(np.float64)/sum(weights)`。采样时，通过随机数 $r \sim [0, 1)$ 在 CDF 区间定位到对应权重组，再从组内作均匀随机选择。

以下是相应的核心代码实现：
```python
import numpy as np
import pandas as pd

class Random_Choice:
    def __init__(self, elements, weights):
        d = pd.DataFrame(zip(elements, weights))
        self.elements, self.weights = [], []
        for i,j in d.groupby(1):
            self.weights.append(len(j)*i)
            self.elements.append(tuple(j[0]))
        self.weights = np.cumsum(self.weights).astype(np.float64)/sum(self.weights)
    def choice(self):
        r = np.random.random()
        w = self.elements[np.where(self.weights >= r)[0][0]]
        return w[np.random.randint(0, len(w))]
```

2. **动态句长拼接**：在批量数据生成器中，每一条伪语料所包含的词数 $n$ 由离散均匀分布 $n \sim \text{Uniform}(1, 16)$ 随机决定（对应代码中的 `np.random.randint(1, 17)`），之后循环 $n$ 次从 CDF 中抽取词语拼接成完整的汉字序列 `seq`。
3. **4-Tag (SBME) 标签映射**：对拼接得到的每个词生成对应字标签：若词长为 $1$，赋予单字标签 `'s'`；若词长 $L \ge 2$，则赋予 `'b' + 'm'*(L-2) + 'e'`。
4. **长度截断与 One-Hot 编码填充**：全局定义最大句长 `maxlen = 48`。生成的序列若长度超过 48 则直接丢弃；若不足 48，则字特征序列用 `0` 补充至长度 48。SBME 字标签被映射为 5 维的 One-Hot 编码表示：`'s':[1,0,0,0,0], 'b':[0,1,0,0,0], 'm':[0,0,1,0,0], 'e':[0,0,0,1,0]`，而对应补充的填充字符位置（Padding），则赋予第五维特定的掩码（Mask）类别：`[0,0,0,0,1]`。

数据生成器的完整构建逻辑如下：
```python
import pickle
words = pd.read_csv('dict.txt', delimiter='\t', header=None, encoding='utf-8')
words[0] = words[0].apply(unicode)
words = words.set_index(0)[1]

try:
    char2id = pickle.load(open('char2id.dic'))
except:
    from collections import defaultdict
    print u'fail to load old char2id.'
    char2id = pd.Series(list(''.join(words.index))).value_counts()
    char2id[:] = range(1, len(char2id)+1)
    char2id = defaultdict(int, char2id.to_dict())
    pickle.dump(char2id, open('char2id.dic', 'w'))

word_size = 128
maxlen = 48
batch_size = 1024

def word2tag(s):
    if len(s) == 1:
        return 's'
    elif len(s) >= 2:
        return 'b'+'m'*(len(s)-2)+'e'

tag2id = {'s':[1,0,0,0,0], 'b':[0,1,0,0,0], 'm':[0,0,1,0,0], 'e':[0,0,0,1,0]}

def data_generator():
    wc = Random_Choice(words.index, words)
    x, y = [], []
    while True:
        n = np.random.randint(1, 17)
        seq = [wc.choice() for i in range(n)]
        tag = ''.join([word2tag(i) for i in seq])
        seq = [char2id[i] for i in ''.join(seq)]
        if len(seq) > maxlen:
            continue
        else:
            seq = seq + [0]*(maxlen-len(seq))
            tag = [tag2id[i] for i in tag]
            tag = tag + [[0,0,0,0,1]]*(maxlen-len(tag))
            x.append(seq)
            y.append(tag)
        if len(x) == batch_size:
            yield np.array(x), np.array(y)
            x, y = [], []
```

最终生成器将序列和标签按照 `batch_size = 1024` 的大小产出 Numpy 数组，供 LSTM 模型进行批次训练。

## 结合动态规划输出 (Viterbi 解码)

模型在推理阶段直接输出每个位置五分类的 softmax 概率分布。为了结合约束输出合法的字标注序列并得到最优切分，这里进一步引入了 Viterbi 算法的解码步骤。

```python
zy = {'be':0.5,
      'bm':0.5,
      'eb':0.5,
      'es':0.5,
      'me':0.5,
      'mm':0.5,
      'sb':0.5,
      'ss':0.5
     }

zy = {i:np.log(zy[i]) for i in zy.keys()}

def viterbi(nodes):
    paths = {'b':nodes[0]['b'], 's':nodes[0]['s']}
    for l in range(1,len(nodes)):
        paths_ = paths.copy()
        paths = {}
        for i in nodes[l].keys():
            nows = {}
            for j in paths_.keys():
                if j[-1]+i in zy.keys():
                    nows[j+i]= paths_[j]+nodes[l][i]+zy[j[-1]+i]
            k = np.argmax(nows.values())
            paths[nows.keys()[k]] = nows.values()[k]
    return paths.keys()[np.argmax(paths.values())]

def simple_cut(s):
    if s:
        s = s[:maxlen]
        r = model.predict(np.array([[char2id[i] for i in s]+[0]*(maxlen-len(s))]), verbose=False)[0][:len(s)]
        r = np.log(r)
        nodes = [dict(zip(['s','b','m','e'], i[:4])) for i in r]
        t = viterbi(nodes)
        words = []
        for i in range(len(s)):
            if t[i] in ['s', 'b']:
                words.append(s[i])
            else:
                words[-1] += s[i]
        return words
    else:
        return []
```

## 原理思考：为什么随机拼凑能起效？

为何不具备自然语法结构、完全随机组合出的伪句也能够训练出一个很棒的分词器出来？原因在于，在构建传统基于词典的分词算法时，就是天然基于“句子是由词随机组合起来的”这一 Unigram 假设。在此假设下，对目标字符串切分的过程，等价于寻找一种切分方案，使得序列中各词产生概率乘积达到全局最大：

$$
p(w_1)p(w_2)\dots p(w_n)
$$

当我们按照实际词频分布来采样合成语料时，正是复现了这一语言模型假设。高频词语组合出现得多，低频词语组合出现得少，LSTM 等深度网络在这样的数据分布上经过大量迭代训练后，实际上隐式地学到了基于独立概率最大化（动态规划）的过程。这种半监督方法能够使得神经网络分词器对生词和复杂组合歧义产生良好的切分效果。
