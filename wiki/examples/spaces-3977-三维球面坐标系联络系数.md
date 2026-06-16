---
type: example
title: 三维球面坐标系联络系数
article_id: '3977'
article: '[[spaces-3977-理解黎曼几何-3-测地线]]'
section: 有力的计算工具
claim: 利用变分 Euler-Lagrange 方法，高效推导球坐标系下的全部非零联络系数。
notation_mapping:
  r: r
  \theta: \theta
  \phi: \phi
  \Gamma^i_{jk}: \Gamma^i_{jk}
steps:
- 1. 根据球坐标系的三维线元 $ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$，选取坐标分量 $x^1
  = r, x^2 = \theta, x^3 = \phi$。
- "2. 构建无根号的能量泛函变分拉格朗日量：\n   L = \\frac{1}{2}\\left[\\dot{r}^2 + r^2 \\dot{\\theta}^2\
  \ + r^2 \\sin^2\\theta \\dot{\\phi}^2\\right]"
- "3. 对 $r$ 建立 Euler-Lagrange 方程：\n   \\frac{d}{ds}(\\dot{r}) - \\frac{\\partial L}{\\\
  partial r} = 0 \\implies \\ddot{r} - r\\dot{\\theta}^2 - r\\sin^2\\theta \\dot{\\\
  phi}^2 = 0"
- "4. 对 $\\theta$ 建立 Euler-Lagrange 方程：\n   \\frac{d}{ds}(r^2 \\dot{\\theta}) - r^2\
  \ \\sin\\theta \\cos\\theta \\dot{\\phi}^2 = 0 \\implies r^2 \\ddot{\\theta} + 2r\\\
  dot{r}\\dot{\\theta} - r^2 \\sin\\theta \\cos\\theta \\dot{\\phi}^2 = 0\n   整理为最高阶项系数为\
  \ 1 的形式：\\ddot{\\theta} + \\frac{2}{r}\\dot{r}\\dot{\\theta} - \\sin\\theta \\cos\\\
  theta \\dot{\\phi}^2 = 0"
- "5. 对 $\\phi$ 建立 Euler-Lagrange 方程：\n   \\frac{d}{ds}(r^2 \\sin^2\\theta \\dot{\\\
  phi}) = 0 \\implies r^2 \\sin^2\\theta \\ddot{\\phi} + 2r\\sin^2\\theta \\dot{r}\\\
  dot{\\phi} + 2r^2 \\sin\\theta \\cos\\theta \\dot{\\theta}\\dot{\\phi} = 0\n   化简整理为：\\\
  ddot{\\phi} + \\frac{2}{r}\\dot{r}\\dot{\\phi} + \\frac{2\\cos\\theta}{\\sin\\theta}\\\
  dot{\\theta}\\dot{\\phi} = 0"
- "6. 对照测地线方程标准式 $\\ddot{x}^\\mu + \\Gamma^\\mu_{\\alpha\\beta} \\dot{x}^\\alpha \\\
  dot{x}^\\beta = 0$，直接读取非零联络系数：\n   - 从 $r$-方程得到：$\\Gamma^1_{22} = -r$ 且 $\\Gamma^1_{33}\
  \ = -r \\sin^2\\theta$\n   - 从 $\\theta$-方程（将 $2\\dot{r}\\dot{\\theta}/r$ 分拆为两个对称项）得到：$\\\
  Gamma^2_{12} = \\Gamma^2_{21} = \\frac{1}{r}$ 且 $\\Gamma^2_{33} = -\\sin\\theta\
  \ \\cos\\theta$\n   - 从 $\\phi$-方程得到：$\\Gamma^3_{13} = \\Gamma^3_{31} = \\frac{1}{r}$\
  \ 且 $\\Gamma^3_{23} = \\Gamma^3_{32} = \\cot\\theta$"
used_concepts:
- '[[concept::联络]]'
used_formulas:
- '[[formula::测地线方程]]'
used_methods:
- '[[method::变分求解联络系数法]]'
source_span: ev::3977::球坐标联络计算
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2016-10-15-理解黎曼几何-3-测地线.md
source_ids:
- '3977'
status: draft
updated: '2026-06-12'
---

## 概述
本例完整展示了如何利用变分控制方程快速解耦计算三维球坐标系下的 Christoffel 符号。测地线是与一切坐标变换都无关的客观实体（即两点间的最短线），通过变分法求解距离积分 $\delta s = \delta \int \sqrt{g_{\mu\nu} dx^{\mu} dx^{\nu}} = 0$ 的极值，可以直接得到测地线方程，进而读取出对应的联络系数。相较于直接代入求和公式，变分法展示出了无可比拟的简洁性。

## 详细计算过程

根据三维球坐标系的线元 $ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$，我们选取坐标分量 $x^1 = r, x^2 = \theta, x^3 = \phi$。

为了简化变分计算，我们构建无根号的能量泛函变分拉格朗日量：
$$
L = \frac{1}{2}\left[\dot{r}^2 + r^2 \dot{\theta}^2 + r^2 \sin^2\theta \dot{\phi}^2\right]
$$

接下来分别对三个坐标分量建立 Euler-Lagrange 方程 $\frac{d}{ds}\left(\frac{\partial L}{\partial \dot{x}^i}\right) - \frac{\partial L}{\partial x^i} = 0$：

1. **对 $r$ 的变分**：
   $$ \frac{d}{ds}(\dot{r}) - \frac{\partial L}{\partial r} = 0 \implies \ddot{r} - r\dot{\theta}^2 - r\sin^2\theta \dot{\phi}^2 = 0 $$

2. **对 $\theta$ 的变分**：
   $$ \frac{d}{ds}(r^2 \dot{\theta}) - r^2 \sin\theta \cos\theta \dot{\phi}^2 = 0 \implies r^2 \ddot{\theta} + 2r\dot{r}\dot{\theta} - r^2 \sin\theta \cos\theta \dot{\phi}^2 = 0 $$
   将其整理为最高阶项系数为 1 的形式：
   $$ \ddot{\theta} + \frac{2}{r}\dot{r}\dot{\theta} - \sin\theta \cos\theta \dot{\phi}^2 = 0 $$

3. **对 $\phi$ 的变分**：
   $$ \frac{d}{ds}(r^2 \sin^2\theta \dot{\phi}) = 0 \implies r^2 \sin^2\theta \ddot{\phi} + 2r\sin^2\theta \dot{r}\dot{\phi} + 2r^2 \sin\theta \cos\theta \dot{\theta}\dot{\phi} = 0 $$
   化简整理为：
   $$ \ddot{\phi} + \frac{2}{r}\dot{r}\dot{\phi} + \frac{2\cos\theta}{\sin\theta}\dot{\theta}\dot{\phi} = 0 $$

最后，我们将上述三组方程对照测地线方程的标准形式 $\ddot{x}^\mu + \Gamma^\mu_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta = 0$，可以直接读取出非零的联络系数（注意交叉项需要分拆为两个对称项）：
- 从 $r$-方程得到：$\Gamma^1_{22} = -r$ 且 $\Gamma^1_{33} = -r \sin^2\theta$
- 从 $\theta$-方程得到（将 $2\dot{r}\dot{\theta}/r$ 分拆为两个对称项）：$\Gamma^2_{12} = \Gamma^2_{21} = \frac{1}{r}$ 且 $\Gamma^2_{33} = -\sin\theta \cos\theta$
- 从 $\phi$-方程得到：$\Gamma^3_{13} = \Gamma^3_{31} = \frac{1}{r}$ 且 $\Gamma^3_{23} = \Gamma^3_{32} = \cot\theta$

利用这一方法，绕开了繁琐的度规求导与指标求和，高效且直观地求得了球坐标系下全部的非零联络系数。
