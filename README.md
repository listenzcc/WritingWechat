- [The Daily Writing NoteBook](#the-daily-writing-notebook)
  - [The Structure of the Project](#the-structure-of-the-project)
- [File = Content + Coding](#file--content--coding)
  - [文件 = 内容 + 编码 （之一）](#文件--内容--编码-之一)
  - [文件 = 内容 + 编码 （之三）](#文件--内容--编码-之三)
  - [文件 = 内容 + 编码 （之二）](#文件--内容--编码-之二)
  - [文件 = 内容 + 编码 （之四）](#文件--内容--编码-之四)
- [Power Shell](#power-shell)
  - [PowerShell 与 LinuxShell 之不同](#powershell-与-linuxshell-之不同)
  - [用 PowerShell 寻找你找不到的文件](#用-powershell-寻找你找不到的文件)
- [Random Analysis](#random-analysis)
  - [概然而非必然的世界（之一）](#概然而非必然的世界之一)
  - [概然而非必然的世界（之二）](#概然而非必然的世界之二)

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
## 概然而非必然的世界（之一）

阿甘正传里有个寓言，说是人生就像一盒巧克力，你永远不知道下一块是什么。
很浪漫地说明了这个世界是概然的而不是必然的，随机和有序是这个世界的基本特征。
因此，随机变量及其统计分析，是解释世界的基本工具之一。

## 概然而非必然的世界（之二）

本文之标题有“世界”二字，但笔力其实撑不起来。
为了避免过于高开低走，本文将进行一个简单的实验，并且尝试以可视化的方式，展示一个非常简单的动力学模型。
通过该模型，我们似乎可以涉足一个可爱的问题，即我们是否可能通过提高生产力的路径，达到均贫富的目标？

