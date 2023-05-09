# 布朗桥（Brownian Bridges）

在建立某个随机动力过程时，我们虽然希望其随机性尽可能大，但又要防止它的范围过分扩张。通过使用合适的约束手段，我们可以达到这一目的，Brownian bridge 是其中之一。

本文的开源代码可见我的 ObservableHQ 笔记本

[Brownian Bridges](https://observablehq.com/@listenzcc/brownian-bridges)

---
- [布朗桥（Brownian Bridges）](#布朗桥brownian-bridges)
  - [Brownian Bridges 基础原理和特性](#brownian-bridges-基础原理和特性)
  - [Brownian Bridges 的形象绘图](#brownian-bridges-的形象绘图)


## Brownian Bridges 基础原理和特性

布朗桥（Bronian Bridges）的特性在下文中介绍得比较清楚，可以理解为在随机游走过程中，每隔一段时间 $T$ 就回归到零点的路径的集合。注意到英文中的 Bridges 了吗，这个复数的格就代表一段连续的随机游走路径中，可以存在无数的在特定时间长度后，“恰好”回归到零点的路径片段，这些片段统称为布朗桥。

> A Brownian bridge can be defined as standard Brownian motion conditioned on hitting zero at a fixed future time *T*, or as any continuous process with the same distribution as this. Rather than conditioning, a slightly easier approach is to subtract a linear term from the Brownian motion, chosen such that the resulting process hits zero at the time *T*. This is equivalent, but has the added benefit of being independent of the original Brownian motion at all later times.
> 

[Brownian Bridges](https://almostsuremath.com/2021/03/29/brownian-bridges/)

![Untitled](%E5%B8%83%E6%9C%97%E6%A1%A5%EF%BC%88Brownian%20Bridges%EF%BC%89%208e4c2fe13c9745d388ecd5aa066fb329/Untitled.png)

布朗桥的较严谨的数学表达式如下

$$
B_t = X_t - \frac{t}{T}X_T
$$

其中，$t, T$分别代表某一个时刻和时间片段的总时间，$X_t$ 代表服从特定分布的随机变量，不同时刻之间的随机变量相互独立。进一步地，它还具有比较好的特性，那就是在不同桥上的随机游走过程相互独立

$$
\mathbb{E}(B_s, X_t) = 0,
\forall s \le T \le t
$$

在证明过程中，我们用到了这样一个结论，那就是随机游走过程的方差随时间增长而不断变大，并且正比于经过的时间长度

$$
\mathbb{E}(B_s, X_t)
= \mathbb{E}(X_s X_t)
- \frac{s}{T} \mathbb{E}(X_T X_t)
= s - \frac{s}{T} T = 0

$$

证明毕。$\square$

## Brownian Bridges 的形象绘图

我在 ObservableHQ 上提供了相应的样例，在绘制时间序列图的基础上还进行了 PCA 分析。

[Brownian Bridges](https://observablehq.com/@listenzcc/brownian-bridges)

![时间序列图](%E5%B8%83%E6%9C%97%E6%A1%A5%EF%BC%88Brownian%20Bridges%EF%BC%89%208e4c2fe13c9745d388ecd5aa066fb329/Untitled%201.png)

时间序列图

PCA 分析的方法是将各个时间段看作是同一对象的不同维度，以下图为例，我将整个序列切分为 $17$ 段，每段包含 $1000$ 个时间点，将每一段看作是一座布朗桥，对它们进行排列成为 $1000 \times 17$ 的矩阵。接下来对该矩阵进行 PCA 分解。由于其前两个主成分的能量分别占总能量的 $41\%, 24\%$，由于其占比较大，因此选择前两个主成分对全部 $1000$ 个样本进行表示，按照时间先后进行染色绘制 PCA 对比图，从图中可以看到，与原始随机游走相比（上图）布朗桥方法（下图）有效地限制了随机游走的动态范围。

![对比图](%E5%B8%83%E6%9C%97%E6%A1%A5%EF%BC%88Brownian%20Bridges%EF%BC%89%208e4c2fe13c9745d388ecd5aa066fb329/Untitled%202.png)

对比图

![对比图-PCA](%E5%B8%83%E6%9C%97%E6%A1%A5%EF%BC%88Brownian%20Bridges%EF%BC%89%208e4c2fe13c9745d388ecd5aa066fb329/Untitled%203.png)

对比图-PCA