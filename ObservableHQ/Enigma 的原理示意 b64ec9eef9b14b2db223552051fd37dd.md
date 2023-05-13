# Enigma 的原理示意

Enigma（译为恩尼格码）密码机是一种使用配对设备进行同步加密和解码的机械式密码机，本文是在前人代码的基础上，通过添加着色的方法使其原理更加便于理解。本文的开源代码可见我的 ObservableHQ 笔记本

[Enigma machine demo](https://observablehq.com/@listenzcc/enigma-machine-demo)

---
- [Enigma 的原理示意](#enigma-的原理示意)
  - [原理说明](#原理说明)
  - [示意图](#示意图)


## 原理说明

由于 Enigma 机过于著名，因此在网络上可以方便地找到它的原理，本文主要参考 Brilliant 的介绍。

[Enigma Machine | Brilliant Math & Science Wiki](https://brilliant.org/wiki/enigma-machine/)

从机械的角度上讲，它是由一系列棘轮层层连接所组成的信号通路，每层棘轮都承载着一组 $26 \rightarrow 26$ 的对应关系。

![Untitled](Enigma%20%E7%9A%84%E5%8E%9F%E7%90%86%E7%A4%BA%E6%84%8F%20b64ec9eef9b14b2db223552051fd37dd/Untitled.png)

![Untitled](Enigma%20%E7%9A%84%E5%8E%9F%E7%90%86%E7%A4%BA%E6%84%8F%20b64ec9eef9b14b2db223552051fd37dd/Untitled%201.png)

以上图的三棘轮系统为例，它的三层分别有 $5, 4, 3$ 种选择，另外每个棘轮有 $26$ 种初始相位可供选择，对应 $26$ 个字母，因此总的排列组合数量为

$$
\begin{cases}
5 \times 4 \times 3 = 60\\
26^3 = 17576
\end{cases}
$$

接下来的分析过于冗长，因此我把原文抄写如下

> Since there are $26$ letters in the alphabet, there are $26!$ ways to arrange the letters, but the plugboard can only make $10$ pairs, so there are $20$ letters involved with the pairings, and 66 leftover that must be divided out. Furthermore, there are $10$ pairs of letters, and it does not matter what order the pairs are in, so divide also by $10!$, and the order of the letters in the pair does not matter, so divide also by $2^{10}$. The resulting number of combinations yielded by the plugboard is as follows:
> 
> 
> $$
> \frac{26!}{6!×10!×210}=150,738,274,937,250
> $$
> 
> All of the components put together yields total number of ways to set a military-grade Enigma machine
> 
> $$
> 60×17576×150,738,274,937,250=158,962,555,217,826,360,000
> $$
> 

## 示意图

接下来我在 ObservableHQ 上找到另一个挺好的例程，它用层次化的结构呈现几个棘轮的交互关系。我在其基础上，适当加入的着色功能，这样不同颜色的线条就能够更好地代表字母的输入与输出之间的对应关系。

![Untitled](Enigma%20%E7%9A%84%E5%8E%9F%E7%90%86%E7%A4%BA%E6%84%8F%20b64ec9eef9b14b2db223552051fd37dd/Untitled%202.png)

[Enigma machine demo](https://observablehq.com/@listenzcc/enigma-machine-demo)

[Enigma machine](https://observablehq.com/@tmcw/enigma-machine)