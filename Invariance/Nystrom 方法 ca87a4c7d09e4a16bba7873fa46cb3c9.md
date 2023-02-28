# Nystrom 方法

本文尝试说明核函数与特征映射之间的关系，并借此介绍 Nystrom 的核函数加速方法。

---
- [Nystrom 方法](#nystrom-方法)
  - [核函数与特征映射](#核函数与特征映射)
  - [概率密度的经验近似](#概率密度的经验近似)
  - [矩阵的特征分解](#矩阵的特征分解)
  - [Nystrom 方法](#nystrom-方法-1)


## 核函数与特征映射

输入向量经过 feature map 的映射成为特征 $\phi_i(x)$，而特征之间的内积称为核函数

$$
K(x, y) = \sum_{i=1}^{N} \lambda_i \phi_i(x) \phi_i(y)
$$

其中，$N \le \infty$，这说明特征维度可以无限多； $\lambda_i \in R$，称为特征值；$\phi_i(\cdot) \in R$，代表一种特征映射，它将输入映射成一个值。 不同的特征映射彼此具有耦合关系，作为特征映射的约束，一种典型的约束称为 p-正交（p-orthogonal）

$$
\int \phi_i(x) \phi_j(x) p(x) dx = \delta_{ij}
$$

其中，$p(x)$代表输入向量出现的概率函数，我们要求特征之间依概率正交。 正交条件虽然严格，但由于概率密度函数的存在，我们不再需要“过度”关注那些小概率事件。 另外，由以上两式，我们可以立即得到下式

$$
\int K(y, x) \phi_i(x) p(x) dx = \lambda_i \phi_i(y)
$$

上式反映了核函数与特征映射之间的关系。

## 概率密度的经验近似

由于输入向量的概率密度函数几乎不可知，因此我们可以采取经验原则使用平均分布对它进近似， 即认为所有输入向量的出现与否都是“等可能”的

$$
X \sim Uniform
$$

反映在 p-正交约束上，它近似为

$$
\frac{1}{q} \sum_{k=1}^{q} \phi_i(x_k) \phi_j(x_k) \approx \delta_{ij}
$$

核函数与特征映射之间的关系式近似为

$$
\frac{1}{q} \sum_{k=1}^{q} K(y, x_k) \phi_i(x_k) \approx \lambda_i \phi_i(y)
$$

其中，*q* 代表输入向量的采样数量。

## 矩阵的特征分解

接下来，我将不加证明地给出矩阵分解式，再建立矩阵分解与核函数特征映射之间的关系。 之所以使用这么拧巴的逻辑，是因为我实在没想明白，要怎么从正方向把这个东西给推导出来， 因此我现在只能认为这是个巧合。

首先，将矩阵分解式列写如下

$$
K \cdot U = U \cdot \Lambda
$$

其中，$K \in R^{q \times q}$ 代表变换方阵； $U = [U_1, U_2, \dots, U_q]$ 代表列向量组成的矩阵，且$U_i \in R^q$； $\Lambda$ 为对角实矩阵。 另外，我们认为 $*U*$ 的各列满足标准正交关系

$$
U_i^T \cdot U_j = \delta_{ij}
$$

下面让我们发挥想象力地开始类比，首先是整个矩阵 $U$

$$
U \rightarrow [\phi_1, \phi_2, \dots, \phi_q]^T \cdot  [x_1, x_2, \dots, x_q]
$$

之后是该矩阵的每一列 $U_k$

$$
U_k \rightarrow [\phi_1(x_k), \phi_2(x_k), \dots, \phi_q(x_k)]^T
$$

这样，我们就构建了矩阵的特征分解与核函数特征映射之间的关系。 为了将映射关系进行量化，我们首先计算映射函数，即特征向量。 计算过程主要利用到特征向量之间的正交关系， 以及矩阵 $U$ 的单位正交性质。

$$
\begin{cases}\begin{gather*}\frac{1}{q} \sum_{k=1}^{q} \phi_i(x_k) \phi_j(x_k) &\approx \delta_{ij} \\U_i^T \cdot U_j &= \delta_{ij} \\\phi(x_j) &\approx \sqrt{q} \cdot U_j \\\phi_i(x_j) &\approx \sqrt{q} \cdot U_{i, j}\end{gather*}\end{cases}
$$

之后计算特征值。 在计算过程中我们分别将每一行进行计算， 发现在任意行中都有等式关系成立， 因此将每行推广到全部行后，可得比例关系。

$$
\begin{cases}\begin{gather*}\sum_{k=1}^{q} K(y, x_k) \phi_i(x_k) & \approx \lambda_i \phi_i(y) \cdot q \\\sum_{k=1}^{q} K_{i, k} \cdot U_k & = \sum_{k=1}^{q}U_{i, k} \cdot \Lambda_{i, k}\\K_{i \cdot} \cdot U &= U_{i \cdot} \cdot \Lambda\\K \cdot U & = U \cdot \Lambda \\\Lambda_{ii} & \approx \lambda_{i} \cdot q\end{gather*}\end{cases}
$$

至此，我们可以认为 $K$ 矩阵代表有限维度的核函数，向量组合 $U$ 代表特征映射向量。

$$
\begin{cases}U & \rightarrow [\phi_1, \phi_2, \dots, \phi_q]^T \cdot  [x_1, x_2, \dots, x_q] \\U_k & \rightarrow [\phi_1(x_k), \phi_2(x_k), \dots, \phi_q(x_k)]^T \\U_{i, k} & \rightarrow \phi_i(x_k) \\K_{i, j} & \rightarrow K(x_i, x_j)  \\\Lambda_{ii} & \rightarrow \lambda_{i} \cdot q\end{cases}
$$

下面考虑一般输入向量的特征映射$\phi_i(x_j)$ 

$$
\begin{cases}\begin{gather*}\lambda_i \phi_i(x_j) & \approx \frac{1}{q} \sum_{k=1}^{q} K(x_j, x_k) \phi_i(x_k) \\\phi_i(x_j) & \approx \frac{\sqrt{q}}{\Lambda_{ii}} \sum_{k=1}^{q} K(x_j, x_k) U_{i, k} \\ \phi_i(x_j) & \approx \frac{\sqrt{q}}{\Lambda_{ii}} \cdot K_{j \cdot} \cdot U_i \\ \end{gather*}\end{cases}
$$

其中，$j$ 代表第 $*j^{th}*$ 个输入向量，$i$ 代表第 $i^{th}$ 个特征。

---

## Nystrom 方法

![Untitled](Nystrom%20%E6%96%B9%E6%B3%95%20ca87a4c7d09e4a16bba7873fa46cb3c9/Untitled.png)

Nystrom 方法采用核函数的低秩近似,将高维核函数分解成低秩部分与剩余部分。 具体来说,将核函数矩阵进行特征分解,选取前 $m$ 个特征向量与特征值进行重构,作为低秩近似项。 剩余部分作为高秩与低秩之差,称为剩余项。 因此 ,Nystrom 方法可以被表示为:

$$
K \approx U_m \Lambda_m U_m^T + K_{res}
$$

其中 $U_m$ 代表前 $m$ 个特征向量组成的矩阵；$\Lambda_m$ 代表 $m \times m$ 对角矩阵,包含前 $m$ 个特征值;$K_{res}$ 代表剩余项。 由于 $U_m$ 与 $\Lambda_m$ 可以通过核函数矩阵的 SVD 分解直接获得,因此 Nystrom 方法的核心在于剩余项的估计。

通常,我们可以采用下式对剩余项进行估计:

$$
K_{res} \approx K - U_m \Lambda_m U_m^T
$$

上式中,核函数矩阵 $K$ 可以通过输入向量的采样获得。 然而,这样的估计方法存在明显的缺陷,即忽略了特征向量与特征值之外的信息,造成了信息损失。 因此,在实际应用中,我们可以通过下式获得更精确的剩余项估计:

$$
K_{res} \approx K - U_m (\Lambda_m + \Delta \Lambda_m) U_m^T
$$

其中，$\Delta \Lambda_m$ 代表特征值的修正项,通常可以通过最小二乘法等方法进行估计。 具体来说,我们可以构造剩余项的线性方程组,再求解 $\Delta \Lambda_m$ 以使方程组残差最小。 这样一来,我们不仅利用了前 $m$ 个特征向量与特征值,同时还充分利用了核函数矩阵的信息,从而获得更加精确的剩余项估计。