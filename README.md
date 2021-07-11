- [The Daily Writing NoteBook](#the-daily-writing-notebook)
  - [The Structure of the Project](#the-structure-of-the-project)

# The Daily Writing NoteBook

Everyday, I would like to write something down in this **PROJECT**.

To convert the materials to WeChat Publication Area,
the website of [mdnice](https://mdnice.com/ "mdnice") will be used.

The 2nd level titles refer the topics.
I hope you readers like them.

## The Structure of the Project

In the project, the folders are the separated **Topics**.

The `readme.md` files in the folders will be used as the summary of the **Topic**.
They are listed as following.

---
# File = Content + Coding

In Computer System, the files are the real-world content in coding.

The **Subject** will explain the process.

The folder contains following md files:

---
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

# Power Shell

Powershell is a **Object Oriented Programming** programming environment.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

---
## PowerShell 与 LinuxShell 之不同

[PowerShell](https://www.powershellgallery.com/ "PowerShell") 是微软自带的交互软件，与类 Linux 系统的 Shell 具有一定的平行替代关系。
但使用起来，二者却给人以完全不同的感觉。

当然，PowerShell （PS）令人智熄的蓝色界面有一定影响，这却不是主要原因。
其根源在于 Windows 系统（W）与类 Linux 系统（L）的不同构建哲学。
一句话来说，L 是以文件为基础而构建的系统，W 是以抽象为基础而构建的系统。
在 L 系统中，用户所看见和所操作的都是具体的文件，所谓“一切皆文件”；
而在 W 系统中，用户始终处于抽象构建的类结构中，所见的都是一望无际的抽象概念。
孰优孰劣我们不去评价，具体和抽象的区别却是在实际使用中产生直观的感受。

## 用 PowerShell 寻找你找不到的文件

继续说 PowerShell （PS）的事情，通过本文档，希望你能够获得一个在 Windows （W）系统中高效找到你想要的文件的方法。能够开始使用 W 系统中提供的 PS 终端，并且习惯用键盘打字的方式而不是鼠标乱点的方式操作你的电脑。
当然，本文档的目的还是深入理解 PS 的抽象类模式，并提供一个非常工程化的视角来阐述这一特性。

# Random Analysis

Learn the way to obtain the world, using the **Random View**.

The **Topic** is the handbook for the random analysis methods.

The folder contains following md files:

---
## 从检验到瞎编

本文将正式介绍统计检验的基本方法，并简要说明它的适用范围，以及它是怎么被玩坏的。

## 屈打成招

本文将用一个简单的例子说明前文《从检验到瞎编》与《通往显著之路》中介绍的校正方法之必要性。


## 我们与真相的距离

俗话说“众口难调”，要摸底某个群体的真实情况往往是十分困难和意义重大的事情。
那么，我们需要调研多少个样本，才能在较高的置信度下，确定该群体的真实情况呢？
本文将通过概率分析方法，尝试分析并解决这一问题。
那么，这个调研样本的数量要求，就是“我们与真相的距离”。

## 概然而非必然的世界（之一）

阿甘正传里有个寓言，说是人生就像一盒巧克力，你永远不知道下一块是什么。
很浪漫地说明了这个世界是概然的而不是必然的，随机和有序是这个世界的基本特征。
因此，随机变量及其统计分析，是解释世界的基本工具之一。

## 概然而非必然的世界（之误差的估计与估计的误差）

本文可以总结成一句绕口令，

> 误差的估计与估计的误差

将从马尔可夫不等式开始，尝试涉及参数估计的重要思想。
并且，通过本文您将看到，估计出的参数，天然地具有误差，而这些误差范围也需要合理的估计。

## 概然而非必然的世界（之二）

本文之标题有“世界”二字，但笔力其实撑不起来。
为了避免过于高开低走，本文将进行一个简单的实验，并且尝试以可视化的方式，展示一个非常简单的动力学模型。
通过该模型，我们似乎可以涉足一个可爱的问题，即我们是否可能通过提高生产力的路径，达到均贫富的目标？

## 概然而非必然的世界（之五）

本文将续前文《[概然而非必然的世界（之四）](http://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247483914&idx=1&sn=72609edc3197161a25d727a0f56f65f1&chksm=c163490ff614c019abf7f49717edcb3cdf60a1e7b27d3ff2e32b43ab6a483b0972327fb2306d&token=135658256&lang=zh_CN#rd "概然而非必然的世界（之四）")》。
继续介绍“卡方分布”与“T分布”。

## 概然而非必然的世界（之六）

本文将解决上篇文章所遗留的待证明问题。

## 概然而非必然的世界（之善战者无赫赫之功）

“欧洲杯”开始了，本文暂时应个景，尝试用概率分析方法解决一个长久以来的思考，即

> 冠军比亚军强多少？

通过分析我们可以看到，在“联赛”体系下，其实二者差不多；但在“杯赛”体系下，亚军则有大概有$25\%$的概率“德不配位”。
现在的很多商业理论，如“弯道超车”、“差异化经营”等，都是在这样的概率体系下，才得以成立。
许多竞技或商业的“奇迹”，不过是这种概率行为的具体表现而已。

## 概然而非必然的世界（之四）

本文将以“二项分布”为起点，分别引申出“泊松分布”、“正态分布”、“卡方分布”与“T分布”。
虽然名目众多，但通过本文的分析可以看到，这些分布完全是一脉相承的关系，并不难理解。
这些分布在实际应用中，可以解决$90\%$以上的统计分析问题。

## 概然而非必然的世界（之杠精总动员）

本文将从概率角度试图解释一个令人十分糟心的现象。

> 为什么互联网会放大个人的极端观点，而持有极端观点的人往往并不自知。

有人说，这是因为互联网提供了一个远程沟通的渠道，使参与者不必在乎对方的反馈。
但我认为事实远不止如此简单。

通过本文的分析，您将看到。
互联网提供了一个“百家争鸣”的密集型话语环境。
正是这样的环境，使得每个参与者，无论其观点有多极端，都能够找到属于自己的一个“小圈子”，使自己处于圈子的中心。
个人处于这样安逸的位置上，当然不会承认，自己的观点之“极端”。

## 概然而非必然的世界（之三）

本文是针对“概然而非必然的世界（之二）”的数学原理解释和说明。

> 我将从“二项分布”和“正态分布”的角度，来对以上实验结果进行解释，……并顺理成章地，引出参数估计与统计检验的基本概念。

相信通过本文的论述，我们可能对随机变量的“均值”、“方差”及“均值的方差”这些拗口的概念，具有直观的理解。

## 通往显著之路

上文《从检验到瞎编》介绍了统计检验的基本方法。
并引出了多重比较校正的概念和经典的FWE校正方法，本文将介绍另一种多重比较校正方法。

# Talk with Picture

The Topic will try to create **Pictures** for **Key Ideas**.

The folder contains following md files:

---
## 图解FDR

鉴于写字没人看，于是决定改成图。
这个系列争取一张图讲明一个故事。
本图是对`FDR`校验过程及原理进行图解。

后面的简要说明，您可以选择看或不看，因为它是为了凑足300字的最低字数要求，完全不影响疗效。

## 图解HSV空间

以颜色空间的“舌形图”为蓝本，我们可以在RGB空间之外，得到更加符合人眼观感的HSV空间。
本文对其进行图解。

## 图解图论分析

本文是标题党，因为一文和一图无法解释清楚图论的概念。
但是，结合《图解词向量》的相关分析，并且使用相同的语料，我们可以进行简要分析，并帮助我们从图的角度理解文章内容。

## 图解审美（一）

本系列将试图通过可视化方法，解释图画审美的问题。

本文将图画打散并嵌入到颜色空间中，用来剖析一个问题

> 什么样的图，是好看的图？

祝我好运吧。


## 图解审美（二）

本文接上文《图解审美（一）》。
本文试图说明，可以通过在`HSV`颜色空间中的变换，对图像进行风格化变换。

## 图解审美（三）

本文将对《图解审美（二）》中的线性变换问题进行图解说明。
并且还将提供一种基于非线性映射的改进方法，用于提升颜色分布变换的效果。

## 图解词向量

本文将对`NLP`的重要概念“词向量”进行图解。
并且以“重要讲话”为语料，通过简单的可视化分析，对其内容进行“数据驱动”的解析。

## 图解词向量与图论的代码

本文是列出以上两篇文章《图解词向量》与《图解图论分析》的相关代码。

## 图解贝斯公式

本文对贝叶斯公式进行图解。
并且说明，在先验知识存在的情况下，观测样本只能在一定范围内对后验概率进行修正。
而不是直接进行数据驱动地估计。
这即是贝叶斯公式背后的精湛哲学。

## 图解颜色空间

不知道你是否和我一样，对颜色空间的形状有些好奇。
它之所谓是个“舌头”的形状，是与眼睛感光的机制有关。
本文将进行适当图解。

## 配色方法

如果你经常纠结于怎么为自己的PPT或其他什么东西配色的话。
本文将介绍一种基于`HSV`空间的配色方法，也许能解决你的问题。

# Tools Knowledge

The Topic is about how to use software tools better.

The folder contains following md files:

---
## 简洁带来的麻烦

`Python`是十分简洁的计算机语言，但是简洁会不避免地带来歧义。
这些歧义则会导致一些麻烦。

# Traffic Analysis

The Topic is about Analysis the Traffic Situations.

The folder contains following md files:

---
## 图的谱聚类

本文将继续介绍图的谱聚类方法，不纠结方法，只尝试说明它的用途。

## 图的距离度量

本文将在上文《最小连通图》的基础上，介绍图距离度量理念及方法。

## 所谓路径依赖

继续图论。
本文将借用之前“过于简单粗暴”的图示来说明所谓“路径依赖”的问题。
往大了说，它代表一种全局和局部的矛盾关系。

## 改出路径依赖

上文我们介绍了“路径依赖”现象，本文将继续介绍通过添加捷径的方法，改出路径依赖的肤浅思路。
并给出一个例子，尝试利用数值化分析方法对该思路其进行说明。

另外，添加捷径的方法综合利用了前文中谱娶类和最小连通图的方法，
并且引入了图论中“超节点”和“超边”的概念。

由于本文说理性较强，相关代码也有不少需要说明的内容。
因此，相关代码和具体算法的体量将在下一篇文章继续完成。

## 最小连通图

本文将介绍最小连通图原则，及其在图构建过程的应用。

## 贪婪算法及其困境.md

本文将详述形成最小连通图的贪婪算法。
在此基础上，我们才能说明捷径加入之后，原始算法是如何失效的。

