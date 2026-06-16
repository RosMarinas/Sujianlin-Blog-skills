---
type: article_summary
title: ReLU/GeLU/Swish的一个恒等式
article_id: "11233"
source_url: https://spaces.ac.cn/archives/11233
date: 2025-08-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-08-16-ReLU-GeLU-Swish的一个恒等式.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-08-16-ReLU-GeLU-Swish的一个恒等式.md
source_ids:
  - "11233"
status: draft
updated: 2026-06-11
---

# ReLU/GeLU/Swish的一个恒等式

本文介绍并证明了 ReLU、GeLU 和 Swish 激活函数所满足的一个有趣且简单的恒等式，并探讨了该恒等式对神经网络结构的意义。

## 主要内容

1. **基本结果**：
   - 对于 $\text{relu}(x) = \max(x, 0)$，由于其提取正负分量的性质，显然成立：
     $$x = \text{relu}(x) - \text{relu}(-x)$$

2. **一般性结论**：
   - 设 $\phi(x)$ 是任意奇函数（即满足 $\phi(-x) = -\phi(x)$），且定义函数：
     $$f(x) = \frac{1}{2}(\phi(x) + 1)x$$
     则恒等式 $x = f(x) - f(-x)$ 恒成立。
   - 对于常用激活函数：
     - **Swish**：$\phi(x) = \tanh(\frac{x}{2})$，满足奇函数性质。
     - **GeLU**：$\phi(x) = \text{erf}(\frac{x}{\sqrt{2}})$，同样满足奇函数性质。
     因此，Swish 和 GeLU 均完全适用并满足该恒等式。

3. **意义思考**：
   - 恒等式可以表示为矩阵乘法形式：
     $$x = f(x) - f(-x) = f\left(\begin{bmatrix}x & -x\end{bmatrix}\right)\begin{bmatrix}1 \\ -1\end{bmatrix}$$
   - 这表明以 ReLU、GeLU、Swish 为激活函数时，两层神经网络天生具有退化为一层的能力（即表示恒等映射）。这使得网络能够自适应地调节其实际深度，与 ResNet 的残差连接工作原理异曲同工，这也解释了为何这些激活函数优于传统的 Tanh 或 Sigmoid。
