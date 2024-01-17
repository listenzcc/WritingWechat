# The Daily Writing NoteBook

Visit
[Writing](https://listenzcc.github.io/WritingWechat/ "Writing")
to see all the contents.

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
# Dataset

The useful datasets and their codes.

The folder contains following md files:

---
## 细粒度的中国地理数据分析（一）

如果有人让你解释什么是中国，你总不能告诉它这里是 960 万平方公里陆地面积的一只雄鸡，这太敷衍了，因为这么一大片土地上有着无数的细节。相信你也和我一样，想要了解这些细节。

本系列的数据来自 2018 年公开的细粒度的地理图像数据，它将中国的土地厘定成有意义的标签，包括住宅、商业、工业、交通和公共服务等。本系列将对其进行分析，尝试用定量的手段解释中国人文地理。

这是一个系列，随着写随着展开。也许我能发现什么有意思的东西。

## 细粒度的中国地理数据分析（三）

本文不再向前推进，而是承接上文将之前的聚类结果进行进一步展示，并尝试以此为契机说明目前我比较推荐的绘图或可视化思路，即在后端进行数据分析后，由开源前端对数据进行呈现和发放，并且参与呈现的数据规模不宜过大。本文代码可见我的前端笔记本

[Chinese geometry dataset analysis with fine land types / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/chinese-geometry-dataset-analysis-with-fine-land-types)

## 细粒度的中国地理数据分析（二）

本文对数据进行进一步分析，通过引入另一个地理包，能够提升地图数据的观感。

另外，本文还将涉及 Pandas 和 GeoPandas 的一些细节。

本系列的开源代码可见我的 Github 仓库

[https://github.com/listenzcc/China-geometry-landmark](https://github.com/listenzcc/China-geometry-landmark)

## 细粒度的中国地理数据分析（五）

本文将之前所述的地块分类数据映射在 Mapbox 地图上，它能够以更加清晰的方式展示城市的地块分布。另外本文的经验还说明，我们在考虑数据分析和可视化问题的时候，应该充分考虑如何将它们与现有的 API 和数据分发手段结合起来，既要注意闭门造车，也要注意出门合辙。

本文的映射结果可见我的前端笔记本。

[Mapbox with land types](https://observablehq.com/@listenzcc/mapbox-with-land-types)

## 细粒度的中国地理数据分析（四）

本文利用 Delaunay 算法进行地块的邻居识别，并将计算统计的结果进行展示。开源代码可见我的前端笔记本

[Neighborhood of land types](https://observablehq.com/@listenzcc/neighborhood-of-land-types)

## 随机图中的测地线实时寻路方法（插曲）

本文可以作为本系列的一个小插曲，为后续分析打下一个算法的基础。尝试引入 Delaunay算法，使用算法从大量的地块中心中提炼出它们之间的拓扑关系。这些信息可以用于进行“测地线”距离的计算，而测地线用于在较复杂的连通图中进行自动寻路。随机场景下自动寻路的开源代码可见我的前端笔记本

[Path finder in random graph](https://observablehq.com/@listenzcc/path-finder-in-random-graph)

# Diffusion Model

Learn more about the Diffusion Model.

The folder contains following md files:

---
## 扩散模型入门（一）

扩散模型是近年来比较热门的神经网络模型，我认为所谓扩散模型就是对扩散过程进行数学建模，并且能够逆转扩散过程的数学方法。本文将开始从一个初学者的视角尝试理解它的思想和应用。

本文使用的 Toy demo 可见我的在线笔记本

[Diffusion of the curve](https://observablehq.com/@listenzcc/diffusion-of-the-curve)

## 扩散模型入门（七）

本文将对前文内容进行总结，最终列出扩散模型的损失函数。

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

# Economist

The articles in economist, and my translation.

The folder contains following md files:

---
## A global house-price slump is coming

**It won’t blow up the financial system, but it will be scary**

癞蛤蟆爬脚面，不咬人但膈应人。

October 20, 2022 5:12 PMShare

## A new macroeconomic era is emerging. What will it look like?

A great rebalancing between governments and central banks is under way

政府与央行之间关系的重新平衡迫在眉睫

Oct 6th 2022

## A reckoning has begun for corporate debt monsters

As rates rise, how messy will the squeeze on business get?

利率高企造成的混乱形势会对商业造成怎样的压迫性影响？

## America’s economy is too strong for its own good

Despite market turmoil, the Fed is set on relentless rate rises

尽管市场动荡，联邦仍然一意孤行地加息。

FILE -- Visitors in Times Square in New York, Aug. 30, 2022. The number of tourists visiting New York City in 2022 is expected to rebound to 85% of the level in 2019, a year in which a record 66.6 million travelers came to the city. (Christopher Lee/The New York Times)Credit: New York Times / Redux / eyevineFor further information please contact eyevinetel: +44 (0) 20 8709 8709e-mail: [info@eyevine.comwww.eyevine.com](mailto:info@eyevine.comwww.eyevine.com)
Oct 2nd 2022 | WASHINGTON, DC

## Bibi is back, and Israel faces a dilemma over democracy

[Leaders](https://www.economist.com/leaders/ "Leaders") | When doves cry

**Though Binyamin Netanyahu is riding high, he cannot forget the Palestinians**

Binyamin Netanyhu （内塔尼亚胡）正在上位，（但）他不能忘记 Palestinians 人。（暂时不明白是褒是贬，看完后发现是阿拉伯国家害怕他受到宗教狂热分子的影响（？）而不给阿拉伯人活路）

November 5, 2022 1:29 AMShare

## China and the West are in a race to foster innovation

**Which will have more success?**

谁更胜一筹？

October 13, 2022 6:10 PM | WASHINGTON, DC

## 左右逢源的当今美国

Conservative Americans are building a parallel economy

[United States](https://www.economist.com/united-states/) | The red and the black

有些东西它不是东方或者西方独有的，只是人在其中有时会看不清楚。但有了 ChatGPT 的帮忙，这些晦涩的语言变得更加容易理解。

本文是某杂志的一篇文章，它讲述了美国社会，甚至美国的商业秩序正在被政治的左和右撕裂，而将它们绑在一块的，竟然是消费（主义）。

June 1, 2023 8:58 PM | WASHINGTON, DC

## Elon Musk buys Twitter at last

马云想吃外卖，所以买了肯德基；马斯克想吐槽，所以买了推特。
这告诉我们一个道理，管住嘴就能省很多钱。

![Untitled](Elon%20Musk%20buys%20Twitter%20at%20last%2084277637efdb4ddca8f1c8eeadcd2e34/Untitled.png)

## Elon Musk’s challenge to management thinking

**If the billionaire succeeds at Twitter, the MBA will need an update**

如果马斯克在推特成功了，那你们的 MBA 就白学了。

译者PS：突然想干件事情，就是弄清楚马老板解雇的那些人，他们是程序员还是中层管理人员？

November 8, 2022 12:44 AMShare

## Financial markets are in trouble. Where will the cracks appear?

The first big test of a new-look financial system

经济新常态下的第一次大考

Oct 4th 2022 | NEW YORK

## OPEC defies Joe Biden with a big output cut

Will it backfire?

你能怎样？
2DJW59X Silhouette Cranes Against Sky During Sunset
Oct 5th 2022

## Should you send your children to private school?

[International](https://www.economist.com/international/) | Studying for success

**As shortcuts to elite universities, American schools work better than British ones**

June 8, 2023 9:48 PMShare

## The hunt for the weakest link in global finance

Credit Suisse won’t be the last firm to fall under the spotlight

Credit Suisse 不会是浮在台面上的最后一个倒霉蛋。

This photograph taken on May 6, 2022 shows a sign of Switzerland's second largest bank Credit Suisse on a branch's building next to a Swiss flag in downtown Geneva. (Photo by Fabrice COFFRINI / AFP) (Photo by FABRICE COFFRINI/AFP via Getty Images)
Oct 3rd 2022

## 今天的历史【2022-11-19】

我希望这能够是一个足够长期的记录，
坚持到退休，能够把 21 世纪给串起来。

The world in brief 【2022-11-19】

Catch up quickly on the global stories that matter

## 今天的历史 【2022-11-26】

Catch up quickly on the global stories that matter

## The world in brief 【2022-12-03】

Catch up quickly on the global stories that matter

## The world in brief 【2022-12-10】

Catch up quickly on the global stories that matter

## The world in brief 【2022-12-24】

Catch up quickly on the global stories that matter
_Updated 4 hours ago (21:02 GMT / 05:02 Hong Kong)_

## The world in brief 【2022-12-31】

Catch up quickly on the global stories that matter
_Updated 9 hours ago (17:11 GMT London)_

## The world in brief 【2023-01-07】

汉堡起义（德语：Hamburger Aufstand），是1923年10月23—25日由德国共产党人领导的汉堡工人武装起义。主要领导者有恩斯特·台尔曼和拉狄克等人。

而今年是 2023 年。

## The world in brief 【2023-01-14】

资本主义时代已然落幕，现在是债务主义。

只要百姓在工作和消费，经济就不会衰退。

国家强大在不于体量而在于潜力。

助产士不会带着孩子回家。

## The world in brief 【2023-02-04】

本周话题还是能源、战争和 AI。

## The world in brief【2022-12-17】

Catch up quickly on the global stories that matter

# Every document

The development process of every-document.

The folder contains following md files:

---
## Every document

本工程的最终目的是提供一个易用的本地文件搜索和管理器，它不仅能实现全部本地文件的按名称管理，就像 Everything 对于文件名的管理那样，也能以同样方便的方法实现全部本地文件的按内容管理。工程在施工中，开源代码可见我的 Github 页面

[https://github.com/listenzcc/every-document](https://github.com/listenzcc/every-document)

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

# Invariance

There are several invariance by math.
Knowing them means knowing everything.

---
## Nystrom 方法 II

本文尝试说明核函数与特征映射之间的关系，并借此介绍 Nystrom 的核函数加速方法。

本文比前文增加的地方是改进了矩阵特征分解的方法描述，现在它更简洁易懂；增补了低秩表示方法的描述，现在它在逻辑上与 Nystrom 方法的衔接更加自然。

## Nystrom 方法

本文尝试说明核函数与特征映射之间的关系，并借此介绍 Nystrom 的核函数加速方法。

## 一些不变性（之一）

函数的本质是映射。
而“不变性”是规范映射变量之间关系的重要渠道。
本文试图从不变性的角度，
探索描述惯性系之间坐标变换的“洛仑兹变换”。

## 一些不变性（之二）

之前提到双曲余弦函数，
它在复数空间内的性质十分有趣。

## 三年以下五年以上

开大会，
重要的议题是立法。
所以本文就尝试对《刑法》的刑期进行可视化。

当然，本文的目的不是要试图说明一个什么事情，
而是举一个反例，
说明数据可以被怎样误用。

## 乘法总比除法好

这是基于欧几里得辗转相除法的扩展，是一个生成互质的随机数对的快速方法。

在这之前我从没想过，互质的整数还能用乘法算出来。

在这里碎碎念一下，如果我们将一系列小矩阵看作是卷积网络的很多层，把最大公约数看作是迭代开始的种子点，那么这就是一个

> 生成拥有指定最大公约数的整数对的 GAN 网络

## 事件地图

这个统计是基于一个外国小哥分享的地图数据制作的。
从这个统计地图上看，
事件几乎是瞬间发生，
并且一直保持在那里了。

本工程的代码可以见[我的在线代码](https://observablehq.com/@listenzcc/russia-ukraine-war-incidents-over-time "我的在线代码")。

## 交叉熵的校正

交叉熵是个好东西，只要它不崩溃。

## 从一张交互式图表看现代互联网的前端与后端

不知道从什么时候起，一提到互联网就会生出“前端”和“后端”来，最初好像一面镜子，总有前也总有后；最近又好像成了一颗玻璃球，既没有前也没有后。
那么，在两方程序员打得如火如荼的时候，以 ChatGPT 为代表的新晋 AI 能做些什么呢？我觉得 **AI 能把桌子掀了**。

本文是自己作为一个 WEB 门外汉的肤浅想法，不仅不具有普遍性，专业性也可能欠佳。但门外汉有门外汉的优势，那就是我从门外看到的东西，可能比较适合给其他门外的人提供一些感性的经验，比较容易哄骗几个好奇的到门内去，希望门内的人不要见怪。

## 信息论中熵的一些证明（一）

本文提供一些信息熵的有用证明，供日后查阅。

## 信息论中的各种熵

信息论中有各种熵的定义，本文用一组例子说明熵的计算方式。以及通过熵对信号进行排序，我们可能会得到怎样的结果。

## 勘误

本文是对“信息论中的各种熵”一文的勘误，并且提供了一个更加易用的脚本。

## 卷积及傅立叶变换的矩阵计算

傅氏变换与卷积都可以用矩阵乘法的形式进行表达。
图神经网络的优化正是以这种矩阵形式为基础的，
从信号连续空间到图拓扑空间的拓展。

本文是其中的第一步，
用矩阵的形式表达信号的傅氏变换与卷积。

本文只涉及必要的原理解释，
具体实现代码可见我的[GitHub 仓库](https://github.com/listenzcc/JupyterScripts.git "GitHub 仓库")。

## 合适的统计检验方法

统计检验是个非常复杂的话题。

它在形式上通常非常简单，
对于任何统计检验方法，
你都能喂给它任意两组数，
然后它反馈给你一个$p$值。

因此，如何选择合适的统计检验方法，
让$p$值能够具有明确的统计意义，
就成了问题的关键。

本文将以转换检验的例子出发，
尝试引出一些有意思的检验方法。

## 咬文嚼字

我唯一知道的是我什么都不知道。

哲学从本体论退化到认识论，
再退化到现在的语言哲学，
导致这种情况的根本原因是

> 在语言不恰当的情况下，
> 我们其实什么也说不清楚。

## 四维时空

对于同一个“事件”，
不同的参考系会给出不同的“描述”。
而在光速不变原理的约束下，
空间和时间都是相对的，
它们之间甚至没有差别。

## 卷积定理的矩阵巧合

从矩阵的角度来看“卷积定理”，
仿佛它只是数字角频率完备正交基下的一个特例。

## 抛物线是圆角的三角形

有点羊，所以本文有点短。

本文试图证明抛物线的弓面积与内接三角形面积之间的关系。

## 抛物线是圆角的三角形 2

有点羊，所以本文有点短。

本文试图证明抛物线的弓面积与内接三角形面积之间的关系。

## 数列

数列的存在是为了解决如何表达不那么自然的实数的问题。

## 方差分析（一）

本系列将逐步涉及方差分析的一些概念。
但在此之前，需要厘清一个更基本的问题，
为什么需要对数据进行方差分析。

## 方差分析（三）

本文对随机数据的方差与分割之间的关系进行简要的可视化。
通过可视化的结果可以看到，
建立线性模型的过程，可以形象地看作是一种规划过程；
而方差分析，是对这种规划过程的合理性进行判定。

## 方差分析（二）

上文描述了二阶统计量的稳定性，
本文将基于二阶统计量的计算方式，
对它的变动来源进行分析。

## 方差分析（五）

除了之前介绍的情况之外，
样本变量之间的协方差也是影响方差分析的难点之一。
本文继续进行实验。

## 方差分析（四）

本篇将考察方差分析何时会给出错误的判断，
这种问题很有用，却鲜有人提及。

## 旋转构成不可交换群

辛辛苦苦做了一个多轴联动的系统，
但发现它不能归零。

郁闷半天，发现多轴旋转竟然是不可交换的。

好在我可以用度量张量来证明这件事情。

## 旋转的坐标系

三维空间中，点的运动有平移和旋转两种方式。
因此，需要为点建立自身的笛卡尔坐标系，
从而描述它的旋转过程。

## 有图必有谱

谱聚类是针对“图”的节点分割算法。
理想的谱聚类需要解决 NP-Hard 问题：
分割导致解空间不连续；
而节点搜索导致计算规模随着数据规模而扩大。
因此，谱聚类算法是寻找一个可行的近似解。

## 有限循环群

偶然发现，似乎在所有有限的循环群中，
幺元是群内生的禀赋，
而不需要额外的假设。

这说明，
如果宇宙中先有某种法则的话，
只要我们观测到了自然数，
就无法否定在某个地方，
它能够把原本极大的，映射为极小的，
从而把终点变成起点。

## 样本均衡

在分类研究中，如果待分类的样本数量不均衡，
会给分类准确性度量造成极大的影响。
本文将使用可视化方法对这种影响进行量化。

## 样本点影响范围的定量估计

对于连续时间信号，我们总可以用离散时间的样本点来近似地逼近它。

由于离散时间采样和噪声的影响，需要采用复杂的计算方法，才能从样本点出发，对连续时间信号的原始分布进行估计。

由于我们假设信号是连续的，因此就不能把观测到的样本点孤立地看待，而是要认为这些样本点之间彼此具有某种关联。要分析这种关联，就需要对这些样本点的影响范围和强度进行估计。

本文是一个 DEMO，尝试通过 B 样条的方法对孤立样本点在连续时间轴上的影响范围和强度进行定量估计。

## 椭圆周长

椭圆与圆有本质的区别，
它的周长没有初等表达式的闭式解，
这是一个很神奇的现象。

## 江山不改

我就知道普大帝不会让人失望，
在我
[之前的文章](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485087&idx=1&sn=1d3e649125bf9d24a7d979a74a0dbd14&chksm=c1634d9af614c48c68e4406b27088e8bb49c1abebce8bdd0524d0e88c0b7ccb14c9912c9d18f&token=856934625&lang=en_US#rd "之前的文章")
就觉得他一定要在乌克兰搞事情。

![Putin 1](./putin-1.png)

因为江山不改，本性不移。
他不搞事情，整个俄罗斯的文化脉络也会推着他搞。

但从个人角度讲，
请德先生先靠边，
我要是俄罗斯人，
这个总统我也想让他当到天荒地老。

## 没头没尾的事

一个方程组摆在面前，
你猜我想让你干点啥？

## 精度消失

本文尝试说明一个案例，该案例通过适当的数学约束，解决在概率密度函数计算过程中遇到的浮点数计算精度消失的问题。

## 群

群是个神奇的概念。

## 群的例子（之一）

本文将给出一个简单的例子，
试图说明如何从变换的角度理解群。

## 自学习的生成模型小例

自学习和生成式模型是机器学习领域的新兴方法。

这种方法的特点是不依赖样本标注，仅通过一些简单的规则就能够生成期望的结构。

本文试图训练这样一个极简模型，它通过自学习的方法，学会从平面生成类似球面的结构。

## 质能方程

所谓伟大分为两种，
一曰为天下之大不韪；
一曰开启天下之先。

上个世纪由爱因斯坦博士提出的相对论就是后者的典型代表。
它否定时空不变性，时间和空间是什么？

-   是描述速度的参考系；
-   是度量物理量的载体；
-   换句话说，只是观念里的一把尺子。

一则，它提出时空的尺度受速度影响；
二则，它暗示质量和能量也并非物体的禀赋，而只是用来度量空间弯曲程度的变量。

本文是对“质能方程”的一些思考，
描述它与速度之间的关系。

奇怪的是，
在速度之外，
质能方程还有一个副产品，
就是**预言**了物体的质量和能量能够相互转化。

## 车枪球-四冲程

天下大事，无非车枪球三样而已，今天先说车。

众所周知，汽缸越多车越稳，
而好车通常采用直列八缸发动机，
本文将解释这是因为什么，以及如何使用群进行分析。

## 这个世界比我预想的更讲道理

我承认这是个标题党，因为本文既不是讨论逻辑问题，也不是讨论世界观问题，这里的道理是万物有道，万物有理之意。本文通过高斯过程在图像中的一个应用，说明仅使用图像的散碎局部信息，就可以用它们来还原整张图像。本文的开源代码可见我的 Github 页面

[https://github.com/listenzcc/Gaussian-Process-Image-Reconstruct](https://github.com/listenzcc/Gaussian-Process-Image-Reconstruct)

## 这可能是一种 BIAS

今天与同学讨论，聊到这么一篇文章

Putative rhythms in attentional switching can be explained by aperiodic temporal structure

[Putative rhythms in attentional switching can be explained by aperiodic temporal structure - Nature Human Behaviour](https://www.nature.com/articles/s41562-022-01364-0)

很多研究发现，在注意力转移过程中，采集到的大脑信号具有“节律性”变化。

而这篇文章试图说明，这种现象可能是由于所采用的置换检验的统计方法破坏了原始信号的时间非周期的连续性而产生的。换句话说，它可能是时间置换检验方法带来的 BIAS，而不是信号本身所具有的属性。

我无意讨论后面的问题，只是单纯地好奇

> 从纯数据的角度出发，这个 BIAS 是如此严重的吗？

## 逻辑游戏1

一天，鬼谷子随意从2-99中选取了两个数。他把这两个数的和告诉了庞涓， 把这两个数的乘积告诉了孙膑。但孙膑和庞涓彼此不知道对方得到的数。第二天， 庞涓很有自信的对孙膑说：虽然我不知道这两个数是什么，但我知道你一定也不知道。随后，孙膑说：那我知道了。庞涓说：那我也知道了。这两个数是什么？

本文的开源代码可见我的前端笔记本

[Logistic Game I](https://observablehq.com/@listenzcc/logistic-game-i)

## 群的边界

从《群》的第一篇不难看出，
群是一个包罗万象的概念。
但越是面对这样的东西，
就越需要谨慎。

本文将通过一个例子说明哪些元素不在群里，
从而厘定群的边界。

## 采样率越高越好

如果你的目的是寻找频率特征，那么对信号的采样率是越高越好。

这种好并不是无脑的好，而是有数字依据的好。

本文就通过计算模拟的方式，说明一个问题，那就是

> 即使在奈氏频率高于感兴趣频带最高频率的情况下，采样率过低也会导致信号失真。

因此，我认为，采样频率的追求越高越好，没有上限。

## 知识、经验和随机性

本文试图说明为什么以及如何使用线性模型对随机变量进行解构。

## 高斯过程 + Nystrom 方法

由于高斯过程可以用于建模连续无限维空间中的函数,而 Nystrom 方法可以用于在有限维度空间中近似计算高斯过程, 因此将两者结合可以有效地解决大规模机器学习中的核方法问题。
高斯过程的求解关键在于核函数，而 Nystrom 方法则说明了这样一个事实，那就是在观测空间的随机采样对核函数估计的准确性影响有限。于是本文对这个原理提供一个可交互的可视化平台。

[Gaussian Process with ChartJS Interactive](https://observablehq.com/@listenzcc/gaussian-process-with-chartjs-interactive)

## 高斯过程与方差“齐次性”

在这里有一个假设，那就是多元高斯分布的协方差矩阵的先验可以通过样本的核函数来确定。在这个假设条件下，高斯过程其实并不涉及任何优化，只是简单地求解多元高斯分布的条件概率密度。在这里面有一些贝叶斯方法的影子。

