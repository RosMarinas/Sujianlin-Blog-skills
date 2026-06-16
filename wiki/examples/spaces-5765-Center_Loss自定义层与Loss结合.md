---
type: example
title: spaces-5765-Center_Loss自定义层与Loss结合
article_id: '5765'
article: '[[spaces-5765-让Keras更酷一些-精巧的层与花式的回调]]'
section: 层与loss的结合
claim: 在自定义层中将可训练权重（中心表示）与 Loss 计算结合，使得复杂 Loss 能够像标准 Dense 层一样通过网络输出和底层标签直接进行端到端优化。
notation_mapping:
  L_{total}: crossentropy + lamb * center_loss (返回值)
  L_{crossentropy}: crossentropy
  L_{center}: center_loss
  \lambda: lamb
  \boldsymbol{W}: self.kernel
  \boldsymbol{b}: self.bias
  \boldsymbol{C}: self.centers
steps:
- 1. 定义自定义层类 `Dense_with_Center_loss(Layer)`，在其 `build` 方法中声明普通 Dense 的可训练权重 `kernel`
  与 `bias`，并额外注册类别特征中心权重 `centers`。
- 2. 在 `call` 中，前向传播仅计算普通的矩阵线性映射并加上偏置：`K.dot(inputs, self.kernel) + self.bias`，但将输入特征缓存于层属性
  `self.inputs` 中。
- 3. 在自定义层中编写 `.loss(y_true, y_pred, lamb)` 方法：利用真实标签 `y_true` 在 `self.centers` 中使用
  `K.gather` 检索出其对应的特征中心 $\boldsymbol{c}_i$。
- 4. 计算当前输入特征与中心的 L2 距离作为 Center Loss：`center_loss = K.sum(K.square(centers - self.inputs),
  axis=1)`。
- 5. 计算常规的交叉熵损失 `crossentropy = K.sparse_categorical_crossentropy(y_true, y_pred,
  from_logits=True)`。
- 6. 返回加权总损失：`crossentropy + lamb * center_loss`。
- 7. 构建模型并执行 `model.compile(loss=dense_center.loss, optimizer='adam')`，传入真实标签直接进行微调训练。
used_concepts:
- '[[梯度累积]]'
source_span: ev::5765::Center_Loss
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-08-06-让Keras更酷一些-精巧的层与花式的回调.md
source_ids:
- '5765'
status: draft
updated: '2026-06-12'
---

## 核心实现代码

```python
class Dense_with_Center_loss(Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(Dense_with_Center_loss, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_shape[1], self.output_dim),
                                      initializer='glorot_normal',
                                      trainable=True)
        self.bias = self.add_weight(name='bias',
                                    shape=(self.output_dim,),
                                    initializer='zeros',
                                    trainable=True)
        self.centers = self.add_weight(name='centers',
                                       shape=(self.output_dim, input_shape[1]),
                                       initializer='glorot_normal',
                                       trainable=True)

    def call(self, inputs):
        self.inputs = inputs
        return K.dot(inputs, self.kernel) + self.bias

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)

    def loss(self, y_true, y_pred, lamb=0.5):
        y_true = K.cast(y_true, 'int32')
        crossentropy = K.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)
        centers = K.gather(self.centers, y_true[:, 0])
        center_loss = K.sum(K.square(centers - self.inputs), axis=1)
        return crossentropy + lamb * center_loss
```