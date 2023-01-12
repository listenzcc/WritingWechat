# 后验概率的暴力计算

本文提供一种后验概率的暴力计算思路，但很遗憾，暴力计算解的精度低于解析解，这也许就是数据驱动的机器学习和数据分析之间的差距。

本文的开源代码可见我前端代码库

[Simulation of Maximized Posterior Probabilities](https://observablehq.com/@listenzcc/simulation-of-maximized-posterior-probabilities "Simulation of Maximized Posterior Probabilities")

---
- [后验概率的暴力计算](#后验概率的暴力计算)
  - [坦克问题](#坦克问题)
  - [暴力模拟](#暴力模拟)
  - [计算结果](#计算结果)
    - [样例1](#样例1)
    - [样例2](#样例2)


## 坦克问题

本文选择的是德国坦克数量估计问题，该问题简化为从N个元素中随机选择M个元素，但N值是未知的，我们的目的是找到最可能的N值。问题描述如下

> 我相信有N辆坦克，但其值未知。如果我随机选择了其中的M辆，并记录它们的序列号，我如何以此为基础估计出真实的N值？
>

[The German Tank Problem Explained: AP® Statistics Review](https://www.albert.io/blog/german-tank-problem-explained-ap-statistics-review/ "The German Tank Problem Explained: AP® Statistics Review")

这个问题是有解析解的，它就是

$$
\begin{aligned}  \hat{\mathbb{N}} = k + k/\mathbb{M} -1\end{aligned}
$$

其中，$k$是观测到的最大的序列号。

## 暴力模拟

本文通过暴力计算的方法对正向过程的模拟达到求解的目的。

> 如果有N辆坦克，我从中随机选择M辆，那么我能得到什么呢？
>

选择过程重复R次，以构建相当大的数据集以获得全局分布。在每次选择中，我使用不放回的方式从样本中随机选择M个元素，所选出的值按照升序排序。之后将选择出的值与排序后的观测目标值逐一进行比较，并计算这些序列的差异

$$
\begin{aligned}  d_n = \sum_{i=1}^{\mathbb{M}} (t_i - s_{in})^2\end{aligned}
$$

其中，t和s指的是相应的目标和选择值，n指的是潜在的N值的全部可能。差异最小的n被认为是潜在的N值。

$$
\begin{aligned}  \hat{\mathbb{N}} = argmin_n d_n\end{aligned}
$$

目标值是从真实世界中获得的，例如，它指的是坦克的序列号。因此，计算的最终结果能够估计出目标序列的N值。

## 计算结果

下图是暴力模拟的结果，图中的纵坐标是差异值，差异值是前文所述的模拟和目标序列之间的差异；图中的横坐标代表模拟时使用的 N 值。模拟结果表明，估计值总是有偏差的。无论执行多少模拟都是如此，说明估计值本身有偏。另一方面，数学解更接近目标N值，可以说它能够提供更高精度的答案。

---

### 样例1

![Setup](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled.png)

Setup

![Mean Curve](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled%201.png)

Mean Curve

![All Simulation](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled%202.png)

All Simulation

---

### 样例2

![Setup 2](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled%203.png)

Setup 2

![Mean Curve 2](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled%204.png)

Mean Curve 2

![All Simulation](%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E7%9A%84%E6%9A%B4%E5%8A%9B%E8%AE%A1%E7%AE%97%20d9a81e5c15ec4a4c89127fccd1e4deea/Untitled%205.png)

All Simulation