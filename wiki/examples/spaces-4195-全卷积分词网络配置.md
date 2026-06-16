---
type: example
title: 'spaces-4195: 全卷积分词网络配置'
article_id: '4195'
article:
- - wiki/sources/spaces-4195-中文分词全卷积.md
section: 模型
claim: 构建三层一维全卷积神经网络（保持SAME填充）对不定长字序列进行分类标注。
notation_mapping:
  x: x
  y: y
steps:
- step: 1
  description: 定义输入占位符以支持变长字 ID 矩阵：`x = tf.placeholder(tf.int32, shape=[None, None])`。
- step: 2
  description: 映射字 Embedding 矩阵：`embedded = tf.nn.embedding_lookup(embeddings, x)`，得到张量维度
    `[Batch, Length, 128]`。
- step: 3
  description: 连接一维卷积层 1，核窗口大小为 3，保留原长度：`y_conv1 = tf.nn.relu(tf.nn.conv1d(embedded,
    W_conv1, stride=1, padding='SAME') + b_conv1)`。
- step: 4
  description: 拼接一维卷积层 2，进一步提取上下文特征并将通道数压缩为 32 维：`y_conv2 = tf.nn.relu(tf.nn.conv1d(y_conv1,
    W_conv2, stride=1, padding='SAME') + b_conv2)`。
- step: 5
  description: 拼接卷积层 3，映射到 4 维分类边界：`y_logit = tf.nn.conv1d(y_conv2, W_conv3, stride=1,
    padding='SAME') + b_conv3`。
- step: 6
  description: 使用 Softmax 计算归一化标签概率：`y = tf.nn.softmax(y_logit)`，输出概率维度为 `[Batch,
    Length, 4]`，分别对应 SBME 四类标注。
used_concepts:
- - - concept::全卷积网络
- - - concept::字标注分词
used_methods:
- - - method::基于全卷积网络的字标注序列建模
source_span: ev::4195::FCN分词结构
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-01-13-中文分词系列-6-基于全卷积网络的中文分词.md
source_ids:
- '4195'
status: draft
updated: '2026-06-12'
---

# spaces-4195: 全卷积分词网络配置

本例展示了利用 TensorFlow 框架搭建 1D-CNN（全卷积无池化）模型，实现输入输出长度完全对齐的中文分词序列标注网络的搭建步骤。

不同于传统的基于 RNN（如 LSTM）的序列建模方案，本模型将一维卷积等价为 N-gram 模型，利用卷积操作天然的平移不变性（即权值共享特性）来提取文本的局部上下文特征。对于自然语言序列，插入多余的字符导致序列平移时，权值共享能够保证网络给出一致的特征响应。此外，全卷积网络（FCN）自始至终仅使用卷积层，摒弃了池化（Pooling）操作，从而在支持不定长文本输入的同时，严格保证了输出的标签序列长度与输入的中文字符序列长度完全一致。

该网络结构的具体计算流如下：

1. **输入与词嵌入表示**：首先，通过 `tf.placeholder(tf.int32, shape=[None, None])` 构建支持变长序列的二维输入张量（维度为 `[Batch, Length]`），并利用 `tf.nn.embedding_lookup` 将每个汉字 ID 映射为 128 维的词向量。
2. **多层一维卷积特征提取**：随后，接入第一层一维卷积，核大小为 3（等价于提取 3-gram 特征），并通过 `padding='SAME'` 约束确保序列长度在卷积后不产生任何缩减：`y_conv1 = tf.nn.relu(tf.nn.conv1d(embedded, W_conv1, stride=1, padding='SAME') + b_conv1)`。接着级联第二层具有相同 `SAME` 填充方式的卷积层，将特征通道数进一步压缩至 32 维：`y_conv2 = tf.nn.relu(tf.nn.conv1d(y_conv1, W_conv2, stride=1, padding='SAME') + b_conv2)`。
3. **字标注分类**：最终的输出层采用不带激活函数的 1D 卷积将 32 维特征映射到 4 维分类边界空间，再使用 `tf.nn.softmax(y_logit)` 计算归一化的标签概率，直接输出维度为 `[Batch, Length, 4]` 的张量。这四个维度分别对应经典的 SBME 字标注体系中的四个标签：`s`（单字）、`b`（词首）、`m`（词中）和 `e`（词尾）。

这种基于纯 FCN 且采用 `SAME` 填充的一维卷积分词网络架构，不仅去除了 RNN 的长距离时序计算依赖，充分发挥了 GPU 对卷积运算的并行加速能力，同时完美契合了字标注任务要求输入输出点对点严格对齐的特点。

以下是基于 TensorFlow 的全卷积网络（FCN）模型定义及训练代码片段的完整实现细节：

### 1. 模型搭建

使用了三层卷积叠起来，不指定输入长度，设为 `None`，设置 `padding='SAME'` 使得输入输出同样长度（基于这个目的，也不用池化），中间用 `relu` 激活，最后用 `softmax` 激活，用交叉熵作为损失函数。

```python
import tensorflow as tf

embedding_size = 128
keep_prob = tf.placeholder(tf.float32)

embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
x = tf.placeholder(tf.int32, shape=[None, None])
embedded = tf.nn.embedding_lookup(embeddings, x)
embedded_dropout = tf.nn.dropout(embedded, keep_prob)
W_conv1 = tf.Variable(tf.random_uniform([3, embedding_size, embedding_size], -1.0, 1.0))
b_conv1 = tf.Variable(tf.random_uniform([embedding_size], -1.0, 1.0))
y_conv1 = tf.nn.relu(tf.nn.conv1d(embedded_dropout, W_conv1, stride=1, padding='SAME') + b_conv1)
W_conv2 = tf.Variable(tf.random_uniform([3, embedding_size, embedding_size/4], -1.0, 1.0))
b_conv2 = tf.Variable(tf.random_uniform([embedding_size/4], -1.0, 1.0))
y_conv2 = tf.nn.relu(tf.nn.conv1d(y_conv1, W_conv2, stride=1, padding='SAME') + b_conv2)
W_conv3 = tf.Variable(tf.random_uniform([3, embedding_size/4, 4], -1.0, 1.0))
b_conv3 = tf.Variable(tf.random_uniform([4], -1.0, 1.0))
y = tf.nn.softmax(tf.nn.conv1d(y_conv2, W_conv3, stride=1, padding='SAME') + b_conv3)

y_ = tf.placeholder(tf.float32, shape=[None, None, 4])
cross_entropy = - tf.reduce_sum(y_ * tf.log(y + 1e-20))
train_step = tf.train.AdamOptimizer().minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 2), tf.argmax(y_, 2))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
```

### 2. 训练循环与进度反馈

利用 tqdm 来辅助显示进度（实时显示进度、速度、精度）：

```python
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
nb_epoch = 300

for i in range(nb_epoch):
    d = tqdm(data(), desc=u'Epcho %s, Accuracy: 0.0'%(i+1))
    k = 0
    accs = []
    for xxx,yyy in d:
        k += 1
        if k%100 == 0:
            acc = sess.run(accuracy, feed_dict={x: xxx, y_: yyy, keep_prob:1})
            accs.append(acc)
            d.set_description('Epcho %s, Accuracy: %s'%(i+1, acc))
        sess.run(train_step, feed_dict={x: xxx, y_: yyy, keep_prob:0.5})
    print u'Epcho %s Mean Accuracy: %s'%(i+1, np.mean(accs))

saver = tf.train.Saver()
saver.save(sess, './ckpt/cw.ckpt')
```

### 3. Viterbi 解码与人工干预（硬解码）

在最后的解码阶段加入硬解码（人工干预解码）。利用词表对各个标签的概率进行调整，然后再使用 Viterbi 算法得到最优路径：

```python
trans_proba = {'ss':1, 'sb':1, 'bm':1, 'be':1, 'mm':1, 'me':1, 'es':1, 'eb':1}
trans_proba = {i:np.log(j) for i,j in trans_proba.iteritems()}

add_dict = {}
if os.path.exists('add_dict.txt'):
    with open('add_dict.txt') as f:
        for l in f:
            a,b = l.split(',')
            add_dict[a.decode('utf-8')] = np.log(float(b))
    

def viterbi(nodes):
    paths = nodes[0]
    for l in range(1,len(nodes)):
        paths_ = paths.copy()
        paths = {}
        for i in nodes[l].keys():
            nows = {}
            for j in paths_.keys():
                if j[-1]+i in trans_proba.keys():
                    nows[j+i]= paths_[j]+nodes[l][i]+trans_proba[j[-1]+i]
            k = np.argmax(nows.values())
            paths[nows.keys()[k]] = nows.values()[k]
    return paths.keys()[np.argmax(paths.values())]

def simple_cut(s):
    if s:
        nodes = [dict(zip('sbme', np.log(k)))
                 for k in sess.run(y, feed_dict={x:[[word2id[i] for i in s]], keep_prob:1})[0]
                ]
        for w,f in add_dict.iteritems():
            for i in re.finditer(w, s):
                if len(w) == 1:
                    nodes[i.start()]['s'] += f
                else:
                    nodes[i.start()]['b'] += f
                    nodes[i.end()-1]['e'] += f
                    for j in range(i.start()+1, i.end()-1):
                        nodes[j]['m'] += f
        tags = viterbi(nodes)
        words = [s[0]]
        for i in range(1, len(s)):
            if tags[i] in ['s', 'b']:
                words.append(s[i])
            else:
                words[-1] += s[i]
        return words
    else:
        return []

def cut_words(s):
    i = 0
    r = []
    for j in re.finditer('['+stops+' ]'+'|[a-zA-Z\d]+', s):
        r.extend(simple_cut(s[i:j.start()]))
        r.append(s[j.start():j.end()])
        i = j.end()
    if i != len(s):
        r.extend(simple_cut(s[i:]))
    return r
```
