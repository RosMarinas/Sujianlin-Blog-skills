---
type: example
title: spaces-11267-Adam更新RMS数值模拟
article_id: '11267'
article: '[[spaces-11267-为什么Adam的Update-RMS是0-2]]'
section: 数值模拟
claim: 通过纯高斯噪声模拟 Adam 优化器在进入正式训练后的稳态更新均方根，可复现约 0.225 的 RMS 观测值。
notation_mapping:
  \|\boldsymbol{u}_t\|_{RMS}: rms
  \boldsymbol{m}_t: m
  \boldsymbol{v}_t: v
  \beta_1: beta1
  \beta_2: beta2
  \boldsymbol{g}_t: g
steps:
- 1. 设置模拟参数：参数维度 $N = 10000$，迭代步数 $T = 2000$，超参数 $\beta_1 = 0.9, \beta_2 = 0.95$。
- 2. 初始化动量一阶矩 $m = 0$，二阶矩 $v = 0$。
- 3. 在每一步迭代中，模拟生成纯噪声梯度 $g \sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{I})$。
- 4. 依据更新方程迭代滑动平均：$m = \beta_1 m + (1-\beta_1)g$ 和 $v = \beta_2 v + (1-\beta_2)g^2$。
- 5. 计算当前步的更新量 $u = m / \sqrt{v}$（省略微小偏置项 $\epsilon$）。
- 6. 迭代结束后，计算 $u$ 的均方根值 `rms = (u**2).mean()**0.5`，得出结果约为 0.225。
used_concepts:
- '[[Adam更新RMS]]'
used_formulas:
- '[[Adam更新均方根公式]]'
source_span: ev::11267::数值模拟
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
- '11267'
status: draft
updated: '2026-06-12'
---

## 模拟代码

```python
import numpy as np

N, T = 10000, 2000
beta1, beta2 = 0.9, 0.95
m, v = 0, 0
for t in range(1, T + 1):
    g = np.random.randn(N)
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g**2
    u = m / v**0.5

rms = (u**2).mean()**0.5
print(rms)  # 约 0.225
```