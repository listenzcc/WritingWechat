# Nystrom 方法 II

本文尝试说明核函数与特征映射之间的关系，并借此介绍 Nystrom 的核函数加速方法。

本文比前文增加的地方是改进了矩阵特征分解的方法描述，现在它更简洁易懂；增补了低秩表示方法的描述，现在它在逻辑上与 Nystrom 方法的衔接更加自然。

---
- [Nystrom 方法 II](#nystrom-方法-ii)
  - [核函数与特征映射](#核函数与特征映射)
  - [概率密度的经验近似](#概率密度的经验近似)
  - [矩阵的特征分解](#矩阵的特征分解)
  - [低秩表示](#低秩表示)
  - [Nystrom 方法](#nystrom-方法)


## 核函数与特征映射

输入向量经过 feature map 的映射成为特征 $\phi_i(x)$，而特征之间的内积称为核函数

$$
\kappa(x, y) = \sum_{i=1}^{N} \lambda_i \phi_i(x) \phi_i(y)
$$

其中，$N \le \infty$，这说明特征维度可以无限多； $\lambda_i \in R$，称为特征值；$\phi_i(\cdot) \in R$，代表一种特征映射，它将输入映射成一个值。 不同的特征映射彼此具有耦合关系，作为特征映射的约束，一种典型的约束称为 p-正交（p-orthogonal）

$$
\int \phi_i(x) \phi_j(x) p(x) dx = \delta_{ij}
$$

其中，$p(x)$代表输入向量出现的概率函数，我们要求特征之间依概率正交。 正交条件虽然严格，但由于概率密度函数的存在，我们不再需要“过度”关注那些小概率事件。 另外，由以上两式，我们可以立即得到下式

$$
\int \kappa(y, x) \phi_i(x) p(x) dx = \lambda_i \phi_i(y)
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
\frac{1}{q} \sum_{k=1}^{q} \kappa(y, x_k) \phi_i(x_k) \approx \lambda_i \phi_i(y)
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
U \rightarrow [x_1, x_2, \dots, x_q]^T \cdot [\phi_1, \phi_2, \dots, \phi_q]
$$

之后是该矩阵的每一列 $U_k$ 都代表一个特征

$$
U_k \rightarrow [\phi_k(x_1), \phi_k(x_2), \dots, \phi_k(x_q)]^T
$$

这样，我们就构建了矩阵的特征分解与核函数特征映射之间的关系。 为了将映射关系进行量化，我们首先计算映射函数，即特征向量。 计算过程主要利用到特征向量之间的正交关系， 以及矩阵 $U$ 的单位正交性质。

$$
\begin{cases}\begin{gather*}\frac{1}{q} \sum_{k=1}^{q} \phi_i(x_k) \phi_j(x_k) &\approx \delta_{ij} \\U_i^T \cdot U_j &= \delta_{ij} \\\phi_i(x) &\approx \sqrt{q} \cdot U_{i} \\\phi_i(x_j) &\approx \sqrt{q} \cdot U_{j, i}\end{gather*}\end{cases}
$$

之后计算特征值。 先将核函数扩展成矩阵

$$
\begin{cases}
\kappa(x_i, x_j) &= \sum_{k=1}^{N} \lambda_k \phi_k(x_i) \phi_k(x_j) \\
\frac{\kappa(x_i, x_j)}{q} &\approx \sum_{k=1}^{N} \lambda_k U_{i, k} U_{j, k} \\
\frac{1}{q} K &\approx U \cdot \lambda \cdot U^T \\
\lambda &= \begin{bmatrix}
\lambda_1 & & & \\
& \lambda_2 & & \\
& & \dots & \\
& & & \lambda_N \\
\end{bmatrix}
\end{cases}
$$

将其代入矩阵分解式，有

$$
\begin{cases}
K \cdot U &= U \cdot \Lambda \\
\Lambda &= U^T \cdot K \cdot U \\
\Lambda &\approx q \cdot U^T \cdot (U\lambda U^T) \cdot U \\
\Lambda &\approx q \cdot \lambda \\
\Lambda_{ii} & \approx q \cdot \lambda_{i} 
\end{cases}
$$

至此，我们可以认为 $K$ 矩阵代表有限维度的核函数，向量组合 $U$ 代表特征映射向量

$$
\begin{cases}U & \rightarrow [x_1, x_2, \dots, x_q]^T \cdot [\phi_1, \phi_2, \dots, \phi_q] \\U_k & \rightarrow [\phi_k(x_1), \phi_k(x_2), \dots, \phi_k(x_q)]^T \\U_{i, k} & \rightarrow \phi_k(x_i) \\K_{i, j} & \rightarrow \kappa(x_i, x_j)  \\\Lambda_{ii} & \rightarrow \lambda_{i} \cdot q\end{cases}
$$

下面考虑一般输入向量的特征映射$\phi_i(x_j)$ 

$$
\begin{cases}
\lambda_i \phi_i(x_j) & \approx \frac{1}{q} \sum_{k=1}^{q} \kappa(x_j, x_k) \phi_i(x_k) \\\phi_i(x_j) & \approx \frac{\sqrt{q}}{\Lambda_{ii}} \sum_{k=1}^{q} \kappa(x_j, x_k) U_{k, i} \\ \phi_i(x_j) & \approx \frac{\sqrt{q}}{\Lambda_{ii}} \cdot K_{i, j} \cdot U_{i} \\ 
\end{cases}
$$

其中，$j$ 代表第 $*j^{th}*$ 个输入向量，$i$ 代表第 $i^{th}$ 个特征。

## 低秩表示

接下来我们对 Nystrom 方法的核心，即低秩表示的原理进行解释。有了矩阵分解式打底，我们可以将核函数矩阵表示为简单形式

$$
K = U \cdot \Lambda \cdot U^T
$$

从上式可知，此矩阵的秩完全由对角矩阵$\Lambda$控制。所谓低秩表示，即是认为该矩阵对角线上的元素从大到小进行排列，这个有序数列呈现快速收敛到 $0$ 的特性。因此，我们总可以使用前若干个特征值对它进行降维表示而不影响核函数的精度。

$$
\tilde{K} = \tilde{U} \tilde{\Lambda} \tilde{U^T}
$$

其中，$\tilde{\cdot}$代表选择其中的低秩成分

$$
K_{nm} = U_{nm} \Lambda_{mm}U_{nm}^T
$$

其中，$n$和$m$分别代表样本数量和低秩成分的数量，而 $X_{ab}$代表选择该矩阵的前$a$行和前$b$列。接下来考虑下式

$$
K_{nm} K_{mm}^{-1} K_{mn}
$$

将它进行分解可得

$$
U_{nm} \Lambda_{mm} U_{nm}^T \cdot
U_{mm} \Lambda_{mm}^{-1} U_{nm}^T \cdot
U_{nm} \Lambda_{mm} U_{nm}^T
$$

由特征矩阵$U$的标准正交特征可知总有下式成立

$$
\tilde{K} = K_{nm} K_{mm}^{-1} K_{mn}
$$

而它与原始核函数矩阵之间的差异可以表示为

$$
K - \tilde{K} = U_{res} \Lambda_{res} U_{res}^T
$$

其中，$X_{res}$是指低秩部分对应的特征值和特征向量。

---

## Nystrom 方法

![Untitled](Nystrom%20%E6%96%B9%E6%B3%95%20II%20ca87a4c7d09e4a16bba7873fa46cb3c9/Untitled.png)

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