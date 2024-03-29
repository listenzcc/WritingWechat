# File = Content + Coding

In Computer System, the files are the real-world content in coding.

The **Subject** will explain the process.

The folder contains following md files:

---
## Edge 浏览器的历史记录本地数据库

本文是一些代码，用于从你自己的电脑上提取你自己的浏览记录，也可以用来分析浏览习惯等动作，但是不用担心，它完全是本地数据，外人不会知道。至于如何利用这些信息则是之后的事情了。

## 三维模型解析及渲染

解析`GLTF`文件的代码。

## 三维模型的同胚变换

对于特定的三维模型，
我们总是希望它与单位球体具有连续的变换关系。

用数学语言来说，
这叫做“同胚”。

这种变换关系可以用于多个三维模型之间的配准等等。

本文给出了一个简单的实例，
以便对这种变换进行直观说明。

## 手写汉字对齐的可计算方法

本人从小就困扰于一个问题，那就是写字不好看。家长对我的评价是写字大小不一，不够整齐。但我一直不服，主要是不解“什么叫整齐” 。本文尝试对这个问题进行计算，顺便解决 OpenCV 如何使用本地 TTF 字体的技术问题。

开源代码如下

[https://github.com/listenzcc/opencv-play-with-ttf](https://github.com/listenzcc/opencv-play-with-ttf)

## 文件 = 内容 + 编码 （之一）

在目前主流的电脑系统中，所有的数据都可以看作一组二进制数所构成的具体的流。
如果你拿一个示波器去看，你是能够在主板的合适位置上观测到这一列数字的。
另一方面，这组数据的内容往往对应现实世界中的一张图像、或者是一段文字。
这就构成了一种两端的结构，一端是计算机要处理的物理世界，另一端是计算机的具体硬件，而把这两个具体端联系起来的，我们可以理解成是抽象的编码过程。
本文将解析这一过程。

## 文件 = 内容 + 编码 （之三）

本部分接上文《文件 = 内容 + 编码 （之二）》。

> 我们重新审视编码纠正的工作，会发现 PS 操作过程中，至少暗含着两个未经考察的问题，这两个问题都是针对字节解码的问题，它们分别对应着在纠正代码中所使用的`utf-16`和`latin1`编码协议。
> ……如果我们轻易放过这两个编码问题，我们将错过 W 系统进行中文编码的重要细节，给之后的代码工作留下后患。
> 因此，在接下来的一篇文章，我将对此进行分析。

本文将跳出图像矩阵编码的范畴，讨论在计算机系统中较为一般的符号编码问题。
但是由于该问题过于繁杂，本文将集中讨论 Python 语言环境下的二进制编码问题，以及中文符号加入后，给原先的拉丁字母表达系统造成的麻烦。
另外，由于本部分内容可能包含过多的细节，为了避免失于细碎，我们不妨先将其中容易出现理解偏差的关键节点列写出来，再逐一作出解析。

## 文件 = 内容 + 编码 （之二）

本部分接上文《文件 = 内容 + 编码 （之一）》。

> 至此，我们已经可以将矩阵图像等价成一列数字，之后的工作将专注于对这一列数字进行编码。……这一工作将等同于对矩阵图像本身进行编码。

本文将介绍基本的矩阵图像编码方法，并且给出一个 PS 进行网络请求图像的例子，来具体说明图像矩阵与二进制序列之间互相转换的关系。

## 文件 = 内容 + 编码 （之四）

在《文件 = 内容 + 编码 （之三）》中，我们提到

> 目前，最主流的兼容包括中文在内的多种语言字符的解决方案，是称为 Unicode 的字符集。
> ……为了比 utf-8 更加完整地覆盖 Unicode 字符集（Unicode 的范围为`0x0~0x10FFFF`，可以用来表示大量的特异性字符），计算机系统必须做出广度和效率之间的妥协。

​ 本部分是《文件 = 内容 + 编码》的最后部分，其目的是对之前的遗留问题进行说明，可以当作附录来使用。
但本部分内容也有其自然的逻辑，即同样的内容在计算机系统中，可以具有不同的表达或存储方式。

