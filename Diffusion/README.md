# Diffusion Model

Learn more about the Diffusion Model.

The folder contains following md files:

---
## 扩散模型入门（一）

扩散模型是近年来比较热门的神经网络模型，我认为所谓扩散模型就是对扩散过程进行数学建模，并且能够逆转扩散过程的数学方法。本文将开始从一个初学者的视角尝试理解它的思想和应用。

本文使用的 Toy demo 可见我的在线笔记本

[Diffusion of the curve](https://observablehq.com/@listenzcc/diffusion-of-the-curve)

## 扩散模型入门（三）

我在前文抛出一个概念，那就是随机性先于一切而存在，而我们观测到的信号只是对某个高维的随机变量进行了一次采样。本文尝试从协方差矩阵的角度来说明有意义的信号处于更低秩的状态，说明其背后的逻辑更加简单。从这个观点来看，噪声比信号更加复杂，那么我们用复杂的噪声去表达简单的信号，这个思路应该是可行的。

本系列相关代码整合在 Github 仓库

[https://github.com/listenzcc/diffusion-model-learning](https://github.com/listenzcc/diffusion-model-learning)

## 扩散模型入门（二）

前文说到扩散模型是尝试逆转扩散过程的数学方法，那么立即产生的问题就是如何对“扩散”进行可计算的描述。本文尝试从两个角度解读我们日常观测到的信号，相信它们不仅有助于理解随机变量，也有助于后续引入扩散的计算方法。在扩散模型中，我更加倾向于将红线理解成对均值为零的随机变量进行的一次采样，它背后的逻辑是“随机性先于一切而存在，而我们观测到的信号只是对某个高维的随机变量进行了一次采样”。

本系列相关代码整合在 Github 仓库

[https://github.com/listenzcc/diffusion-model-learning](https://github.com/listenzcc/diffusion-model-learning)

## 扩散模型入门（五）

本文在前文的基础上开始实践扩散模型，扩散模型的学习目标是一条给定的连续曲线，它指代一个 50 维的连续信号。从最实用的角度上讲，**扩散模型的学习目标是通过模型预测扩散终点，即噪声**。

[https://github.com/listenzcc/diffusion-model-learning](https://github.com/listenzcc/diffusion-model-learning)

## 扩散模型入门（六）

本文比较无聊，是对扩散逆过程的公式推导。

## 扩散模型入门（四）

从如前文所述的例子观点来看，随机信号是方差的游戏。在实际场景中，我们很难事先知道协方差矩阵的精确值，事实上我们往往需要用对角矩阵来模拟它。而扩散模型则有希望完成两者之间的跨越。

我们将扩散过程看作是在一系列均值为零的高维空间中不断采样，这些采样的累积效应将信号扩散到标准正态空间中。最终将扩散过程理解成这样一个动态过程，它不断地、蚂蚁搬家式地将先验信号$X_0$的协方差矩阵“替换”为标准正态分布的协方差矩阵。

我想在这里吐个槽，初学数理统计时喜欢算均值，觉得方差是碍事的东西，但越学越反过来，开始觉得**数理统计是研究方差的学问，均值是妨碍我理解它的绊脚石**。
