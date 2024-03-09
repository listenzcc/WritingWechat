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

## 你还是挣得太多：Your pay is still going up too fast

央行是干什么用的？在2023年，它是抗通胀用的。从2022年以来，（发达国家）央行将通胀率从10.7%降低到了5.4%，但他们设定的目标是2%，行百里路半九十，最后一点最难降。2024年的最后一块拼图是降低劳动力报酬，因为之前它们太高了。

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

# Observable HQ

JAVASCRIPT gives HTML amazing Abilities to present Things.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

---
## 2023 年北京中考成绩的按区分布

东城、海淀和朝阳三个区的加权平均成绩高于 600 分。

虽然东城区的加权平均值最高，但主要得益于参考人数较少。初中阶段教育质量最高的属海淀区，从分布上看属于遥遥领先。另外，朝阳区和西城区处于二者之间。

至于其他的区，洗洗睡吧。

本文很无聊，代码可见我的 ObservableHQ 笔记本

[Beijing high school entrance exam](https://observablehq.com/@listenzcc/beijing-high-school-entrance-exam)

## Bunny Render

本文尝试通过 WebGL 渲染 Bunny 兔子模型，它的颜色受到一个简单的神经网络的控制。

从结果上来看，虽然实验用的神经网络极其简单，但它可以用来高亮模型表面的任何区域。

本文代码可见我的前端笔记本

[Demo of Neural Network](https://observablehq.com/@listenzcc/demo-of-neural-network "Demo of Neural Network")

## Delaunay 算法的边界风险和规避

在边界处发生未连接的Delaunay邻居存在一些特定的风险，它是由于算法“误认为”两个点之间的有邻居关系，但它们的连接点又位于边界之外。本文对这种现象进行解释，并尝试进行规避。

本文开源代码可见我的 ObservableHQ 笔记本

[Delaunay neighbours / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/delaunay-neighbours)

## Delaunay算法与应用一例

本文尝试使用Delauney算法进行快速次近邻检索。该方法在d3.js库的帮助下，能够在数十毫秒内解决10000个点的次近邻问题求解。本文的开源代码可见我的在线开源笔记本

[Find the closest Two points using the delaunay](https://observablehq.com/@listenzcc/find-the-closest-two-points-using-the-delaunay)

## EEG 和 LFP 相互关系的动态展示

本文对 LFP（局部场电位）和EEG（脑电图）的理解进行简单的可视化，要表达的信息是 LFP 是大脑内部 $Na^+, Ca^{2+}$等离子有序迁移引起的局部电位变化，而 EEG 是在头皮表面，以无创的方法采集到的电场强度变化。

本文通过一段代码直观地展示了这一过程，你可以在这里找到它

[LFP & EEG](https://observablehq.com/@listenzcc/lfp-eeg)

## Enigma 的原理示意

Enigma（译为恩尼格码）密码机是一种使用配对设备进行同步加密和解码的机械式密码机，本文是在前人代码的基础上，通过添加着色的方法使其原理更加便于理解。本文的开源代码可见我的 ObservableHQ 笔记本

[Enigma machine demo](https://observablehq.com/@listenzcc/enigma-machine-demo)

## Gabor 函数的参数空间-1

Gabor 函数是常用的数学函数，可以用来对多种物理现象进行表达。

> 函数在参数空间沿最短线移动时，与目标的距离先上升后下降，这导致梯度方法无法用于寻找到这条路径。

换句话说，Gabor 函数在参数空间中是非凸的。

开源代码可见我的前端笔记本

[Parameter Space of Gabor](https://observablehq.com/@listenzcc/parameter-space-of-gabor "Parameter Space of Gabor")

## Gabor 函数的参数空间-2

本文是接续前文的拓展，探讨在估计最优参数时，梯度下降方法是否能够得到最优解。

梯度下降可能有三种结果

1. 能够得到几乎正确的结果，但过程曲折；
2. 能够得到几乎正确的结果，过程也与理想轨迹大致吻合；
3. 梯度下降轨迹与理想轨迹南辕北辙。

本文代码可见我的前端笔记本

[Parameter Space of Gabor (Gradient)](https://observablehq.com/d/e5f15050d1568991 "Parameter Space of Gabor (Gradient)")

## NBA 赛季投篮数据可视化

我使用开源工程下载典型的投篮数据库，记录的信息非常丰富，从表中可以查到这样的信息

> 在某一节的某一分钟，某名球员在某场比赛中，在球场上的某个位置进行投篮。投篮的结果是投中 | 未中。

我据此绘制了投篮出手的球场位置分布图和时间分布图，开源代码可见我的 ObservableHQ 笔记本

[NBA Player Shot Statistic (2022-23 Regular Season)](https://observablehq.com/@listenzcc/nba-player-shot-statistic-2022-23-regular-season)

## NBA 赛季投篮数据可视化（二）

本文对 NBA 2022-23 赛季常规赛部分球员的投篮数据进行细化统计，开源代码可见我的 ObservableHQ 笔记本。

[NBA Player Shot Statistic (2022-23 Regular Season)](https://observablehq.com/@listenzcc/nba-player-shot-statistic-2022-23-regular-season)

## Perlin 噪声与随机地形

在许多情况下，需要生成随机的地形或者空间连续的随机变量。

这里 Perlin 噪声往往是很好的选择。

比如我在前端页面做的一个小demo [Perlin Noise Contours with GeoProjection](https://observablehq.com/@listenzcc/perlin-noise-contours-with-geoprojection "Perlin Noise Contours with GeoProjection")

## THREEJS 的三阶魔方

春去江花红胜火，春来江水绿如蓝，能不忆江南。这个周末气温回暖，草木发芽，于是在家有前端做了个虚拟化的三阶魔方。本文的开源代码可见我的前端笔记本

[Rolling magic cube with THREE.js](https://observablehq.com/@listenzcc/rolling-magic-cube-with-three-js)

## WebGL渲染 与 D3.plot 绘图的结合

WebGL 是一种基于 GPU 并行计算的高速渲染方法。而 D3.plot 绘图是基于 d3.js 的绘图库，它的优势在于规范化的图表制图。本文提供的工具是对另一款开源工具的修改，现在它将两类制图工具的数据通道打通，从而实现两层的渲染。

[Observable Plot + regl (Animation I)](https://observablehq.com/@listenzcc/observable-plot-regl-animation-i)

## WebGL的实时渲染

本文提供一个前端样例，用于实时捕捉流数据并进行计算和渲染。

开源代码可见我的前端笔记本

[Image Cookbook](https://observablehq.com/@listenzcc/image-cookbook "Image Cookbook")

## WebGL绘图（之一）

`WebGL`是重要的前端技术之一，
是高性能的像素级渲染工具。

## WebGL绘图（之三）

我在之前的基础上添加了一点点细节。
现在能够呈现一个动态的复数空间。

## WebGL绘图（之二）

不得不说`WebGL`是个坑，坑在哪呢？
一是计算机语言，二是高等数学。

## 一个简单的动力学模型

借助JAVASCRIPT的实时计算工具，HTML（也就是网页）具有强大的​呈现能力。
而以D3为代表的工具进一步简化了这一过程。
本文借助该平台，建立了一个简单的动力系统。
该系统可以在一定程度上显示出“混沌”现象。

## 一种莫名其妙的自组织结构

我的初衷是在某个图形之内构造一组致密点云，我最初的设想是这个点云应该会**像水波一样，从一个中心向外不断扩张。**但事与愿违，这些点似乎有他们自己的想法，**他们开始自组织起来，以一种匪夷所思的像下围棋一样的方式向外扩张**。这是出乎我意料的，因此记录下来。本文的开源代码如下

[Plot population](https://observablehq.com/@listenzcc/plot-population)

## 万有引力与第一只手

万有引力定律是个伟大的定律，它从数学原理上描述了这个“有序的”宇宙。

然而这个定律并没有保证这个宇宙一定是有序的，甚至不需要要“三体”，最简单的地-日系统都可能直接把地球弹出去流浪。

于是我尝试用模拟的方法解释日-地式的双星系统可以不稳定到什么程度。欢迎访问我的前端笔记本

[Play ground: Law of universal gravitation](https://observablehq.com/@listenzcc/play-ground-law-of-universal-gravitation "Play ground: Law of universal gravitation")

## 不圆的轮子：Reuleaux 三角

人总要摆脱经验造成的路径依赖，比如能够稳定转动的东西不一定就是轮子。本文介绍一种不是圆形的轮子 Reuleaux 三角，它是一种“等宽闭曲线”，能够像圆轮子一样平稳转动。

本文尝试以数据驱动的方式解决解析几何问题，让人可以不依赖几何知识就可以验证以上结果。由于我得到的 Reuleaux 三角是纯数值的，不依赖于几何公式推导，因此，我可以用工程学的方法来模拟它在等宽范围内的转动。结果发现，即使这种曲线能够在水平方向上进行平稳转动，但其转速却并不平稳。另外，曲线不同位置的线速度和轨迹也不尽相同。

这说明这种三角轮子的转动稳定性并不理想。路径依赖虽然有保守的风险，但至少可以规避一些创新风险。本文的开源代码可见我的 ObservableHQ 开源代码库

[Reuleaux triangle](https://observablehq.com/@listenzcc/reuleaux-triangle)

## 乌合之众

系统中多个成员的复杂关系一般可以用网络进行描述，
在该网络中的信息传递效率是值得关注的关键点。

通过本文的模拟可以看到，
一个无中心的，
单纯依靠节点之间的互信进行信息传递的网络，
其网络容量令人难以置信的低。

本文是之前“行路难”系列的延伸，
与之不同的是，本文提供了一个实时模拟和显示代码，
让读者可以“看到”网络中消息“流动”和“迟滞”的动态过程。

## 二维场及其可视化

这是一个进行二维场生成和可视化的前端工具，
但还是初版。

## 云图

最近科研圈出了个大事，就是一度非常火热的老年痴呆与一种知名蛋白沉淀之间的关联指控是数据造假的结果。

简单来说，它等价于这样一种行为，就是我可以通过各种 CG 方法生成一张图，然后把这张图给地球披上，然后指着它说，看吧，这就是之后 30 年的地球气候的云图。

虽然这张图实际上没有一点儿意义。

## 云雾效果

本文是在之前“等高线图”的基础上，
开发了一个类似“云雾效果”或“封冻效果”的渲染生成方法。

## 人口曲线再挖掘⛏️

有的数据不公布了，这不是什么好事儿。虽然上面总有自己的考量，但这提醒我要学学如何从已知的数据进行猜测性分析。本文开始尝试从人口普查的年龄分布数据开始进行分析，初步代码可见我的 ObservableHQ 笔记本

[How many females will have no child](https://observablehq.com/@listenzcc/how-many-females-will-have-no-child)

## 人口曲线再挖掘⛏️【2】

书接上回，继续从人口分布数据中估计未来丁克的女性数量。结论是，未来十数年内，我国不选择生育的女性数量约为 2500 万人。这是相当保守的估计，因为我目前的假设是所有新生儿都是一人一胎，杜绝多胞胎和一人多胎的情况。因此，未来 5 千万到 1 亿不生育的年轻人将是我国必将面临的新常态。开源代码还是在这里

[How many females will have no child](https://observablehq.com/@listenzcc/how-many-females-will-have-no-child)

## 人口红利

姜文电影有一句名言

> 我就是为了这碟醋，才包的这顿饺子。

我让 ChatGPT 给我编了一段解释兰彻斯特方程的代码，于是我给它加了一个可视化的壳，现在已经说不清谁是饺子谁是醋了。代码可见我的前端笔记本

[The Lanchester function explaining by ChatGPT](https://observablehq.com/@listenzcc/the-lanchester-function-explaining-by-chatgpt "The Lanchester function explaining by ChatGPT")

## 今天的风儿有些喧嚣

今天刮大风，刮的建筑像要被吹跑似的。
所以趁着机会做一个简单的粒子运动模拟。

## 从地理交互看 Walmart 的时间线

本文是结合地理数据与 Walmart 经营数据的可视化尝试，尝试使用可交互的手段提升对数据的理解。从静态图中可以明显看出 Walmart 发迹于美国中东部，而后逐渐向东、西两个海岸发展。虽然这个趋势非常明显，但会忽略它发展轨迹中的一些细节，这些细节可以从可交互的可视化分析中得到生动的补充。

[An animation demo of Walmart in America / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/an-animation-demo-of-walmart-in-america)

## 使用二维拓扑表示三维魔方

二维拓扑是指在平面上表示物体的形状和关系，而三维魔方是一个由小立方体组成的立体结构。虽然二维拓扑无法直接表示三维魔方的立体性质，但我们可以使用映射的方法通过二维拓扑表示魔方的交换群特性。

本文的可交互代码可见我的 ObservableHQ 在线笔记本

[Magic cube in 2D space](https://observablehq.com/@listenzcc/magic-cube-in-2d-space)

## 便携的深度网络

最近 ChatGPT 从实验室走到了千家万户，这说明虽然深度网络是极其依赖于计算资源的服务方式，但只要通过合适的技术途径，是可以实现轻计算终端接入的。在神经网络计算功能日益强大的今天，这是复杂计算落地的必由之路。因此，本文提供一个 DEMO，将预训练好的轻量图像计算网络直接放在前端进行图像识别计算。

本文开源代码可见我的前端代码库

[The TensorFlow in Javascript](https://observablehq.com/@listenzcc/the-tensorflow-in-javascript "The TensorFlow in Javascript")

## 保守场的最短路径估计

本文将“最速降线的蒙特卡洛逼近”一文的方法推广到任意的保守场。

开源代码可见我的前端笔记本

[Estimate the Brachistochrone using Monte Carlo Simulation V2](https://observablehq.com/@listenzcc/brachistochrone-using-monte-carlo-simulation-v2 "Estimate the Brachistochrone using Monte Carlo Simulation V2")

## 信息茧房

都说互联网是个信息茧房，所以我们就来试试。

其实什么也没试出来。

## 俯冲轰炸过程图解

俯冲轰炸是一种军事战术，通常用于航空战中，特别是在飞机和目标之间的攻击阶段。本文仅仅是出于好奇，对这个过程进行模拟，模拟了炸弹下落和飞机逃逸的轨迹。由于受到重力影响，无动力的炸弹落点会在飞行员视线之后，距离约为 100 英尺。当飞机的俯冲航线角度与理想角度有偏差时，即使偏差角度较大（约25度），误差也能够控制在 200 英尺以内。

开源代码可见我的 ObservableHQ 笔记本。

[Dive bombing](https://observablehq.com/@listenzcc/dive-bombing)

## 像上网一样使用FSL

`FSL`是个好软件，
它强在皮层水平的各种统计计算。
但缺点同样明显，
它太难用了，
如此功能强大的软件却将数据格式过度封装，
导致除了它给定的几种算法之外，
想要做出一点扩展都艰难异常。
让人非常费解。

本工程做出一些尝试，
希望让它的分析和呈现能够变得像“上网”一样简单。
目前，离这个目标还相当之遥远。

## 光场渲染的 MRI 点云

Nerf 是用深度神经网络表达某个物体，虽然我没有这个本事构造深度神经网络，但好在我并不需要这么做，因为我只要能根据已知的点云，把 MRI 数据渲染出来就达到目的了。本文开源代码可见我的在线代码笔记本

[3D MRI volume rendering in slices with WebGL](https://observablehq.com/@listenzcc/3d-mri-volume-rendering-in-slices-with-webgl)

## 全国铁路站点

本文尝试使用 mapbox，force graph 和 sankey diagram 对全国铁路车站进行可视化。

本文绘图代码可见我的前端库

[Railway stations](https://observablehq.com/@listenzcc/railway-stations "Railway stations")

本文数据预处理的代码可见我的 Github 库

[China-rail-way-stations-data](https://github.com/listenzcc/China-rail-way-stations-data "China-rail-way-stations-data")

效果看着还行，所以最后还有一点碎碎念。

## 函数映射

本文在 Observable 提供了一个好用的函数可视化工具。

[Mathmatic notebook III](https://observablehq.com/@listenzcc/mathmatic-notebook-iii "Mathmatic notebook III")

## 刹车对车流造成的持续性影响

由于汽车的加速能力远不及刹停能力，因此在密集车流中，前车的刹车会对后车造成持续性影响。本文动态仿真了这一过程。本文构造了一个循环的车流系统，不许超车。在系统中，多辆小车沿圆形轨道自主行进，所有小车均**在恰好不与前车相撞的最佳车距的最佳时刻选择制动**。

开源形码可见我的 ObservableHQ 笔记本

[How can a break slow down the running cars](https://observablehq.com/@listenzcc/how-can-a-break-slow-down-the-running-cars)

## 前端是个好东西，但需要数据支撑

前端是个好东西，但需要数据支撑。所谓产业赋能就是强大的后台+好用（好看）的前端。本文以地铁为例做一次眼高手低的尝试。

## 前端的GPU渲染库

GPU是强大的计算单元，擅长进行较大规模的并行计算。

本文通过一款优秀的前端GPU渲染库，提供几个GPU渲染的前端样例。

[Learning GPU-IO](https://observablehq.com/@listenzcc/learning-gpu-io "Learning GPU-IO")

## 前端输入微调交互样例

Figma 是一个十分漂亮和高效的原型设计辅助软件，在使用它的过程中，遇到了很多提升用户交互效率的小 Trick。

本文复现了 Figma 上的一个十分用户友善的应用，它在前端输入时，允许用户采用鼠标拖动的方式对数值型输入进行微调。

## 北京中考成绩的统计分析，我仿佛看到了城乡差异

本文对 2023 年中考成绩分布，我仿佛看到了城乡差异。从成绩上看，北京的高中似乎只对东城、海淀、朝阳和西城区的初中生开放。其中，前 4 区的学生成绩明显优于其他区。另外，东城区没有海淀区名气这么大，但东城区的 CDF 曲线与另外三区之间有一定的间隔，说明这个区的学生成绩更高。

另外，在 625 分以上的学生中，他们“均匀”来自 18 个区的假设不能成立。这说明成绩好的区在高成绩方面有近乎垄断的优势。

本文涉及的理论内容见附件，本文的代码可见我 ObservableHQ 笔记本

[Beijing high school entrance exam](https://observablehq.com/@listenzcc/beijing-high-school-entrance-exam)

## 北京西北水系与万里长城

前两天跟老同学聊天儿，聊起北京洪灾。我说那边的地势比较容易受山洪影响，还给他画了张图。他看地图不错，于是想在上面看看长城。但我惊讶地发现，现在的地图工具没有提供这个功能，于是我就画了一个，在我的 ObservableHQ 笔记本上。

[Great wall display](https://observablehq.com/@listenzcc/great-wall-display)

## 历代君王

刷B站看到一条弹幕，
它说雍正和华盛顿是一个时代的人。
于是我就统计了一下，
还真是。

## 变异 Covid-19

人年纪大了就会不自觉地思考最后的归宿，死 Covid-19 可乎？

不停地变异是病毒的特点之一，感染数量和范围可以看作是变异的直观反应。

本文从 **pango_lineage** 分类学数据库出发，试图对 Covid-19 如何变异提供一个可视化视角。

代码可见我的前端程序库

[The pango-lineage of Covid-19](https://observablehq.com/@listenzcc/the-pango-lineage-of-covid-19 "The pango-lineage of Covid-19")

## 后验概率的暴力计算

本文提供一种后验概率的暴力计算思路，但很遗憾，暴力计算解的精度低于解析解，这也许就是数据驱动的机器学习和数据分析之间的差距。

本文的开源代码可见我前端代码库

[Simulation of Maximized Posterior Probabilities](https://observablehq.com/@listenzcc/simulation-of-maximized-posterior-probabilities "Simulation of Maximized Posterior Probabilities")

## 吹气球

`FreeSurfer`是将功能磁成像数据映射到大脑皮层空间的软件。
它的计算原理就像吹气球。

## 困在时间胶囊💊里

定性的讨论光速和相对论，只需要直觉和初中几何，甚至不需要列公式。

要解释这个问题，我们需要动起来，站在运动物体的角度重新分析这个坐标系统。结论先行，在匀速直线运动的坐标系（称为新坐标系）的眼中，原坐标系产生了时空扭曲，扭曲的结果是一族双曲线。新坐标系的运动速度越快，那么这些双曲线就越收敛到它们在无穷远处的渐近线。最终，当新坐标系的速度无限接近光速时，运动轨迹与时间轴重合。

我们注意到，在这些双曲线收敛于无穷远时，所有时间点的“直线”都收敛在一起。也就是说当速度达到光速时，它能够在空间维度任意移动，但时间维度的消失了。就像困在时间“胶囊💊”里（冰冻），也像是能够在不同的时刻任意穿梭（虫洞），但到底是冰冻还是虫洞，这个没有有人知道。

本文的开源代码可见我的 ObservableHQ 笔记本

[Easy understanding of why Light speed is a limit](https://observablehq.com/@listenzcc/easy-understanding-of-why-light-speed-is-a-limit)

## 图神经网络的计算和收敛

图神经网络是考察节点关系的模式识别方法。
多用于解决复杂系统中，
针对节点之间的关系进行运算的模式识别问题。

本文是对它的运算过程进行模拟，
并且尝试通过简单的例子，
说明这类网络的收敛性。

本样例的代码可见[我的开源代码](https://observablehq.com/@listenzcc/graph-network "我的开源代码")

## 圆反演及其分形

圆反演分形是通过应用圆反演（Circle inversion）变换来生成的一类特殊分形。它会从已有的圆开始进行迭代，不断解决满足 Apollonius' Problem 的解（见附录）的圆周上的点，将这些点渲染出来即可得到复杂的分型图样。本文是用 CPU 进行暴力计算，效率并不是很高。

[Circle inversion fractals step-by-step](https://observablehq.com/@listenzcc/circle-inversion-fractals-step-by-step)

## 圆反演的不变性与相切关系的传递

经过反演前后的圆的圆心和半径均相同，因此对于单位圆来说，与单位圆垂直的圆与其反演的圆相互重合。另外，只要圆有相切关系，那么它们经过映射后还是相切的。另外，当圆彼此相交时，反演映射关系会因之变得非常复杂，从而渲染出奇怪的纹理。这是圆反演分形图样的理论基础。

[Circle inverse with joint circles using force simulation](https://observablehq.com/@listenzcc/circle-inverse-with-joint-circles-using-force-simulation)

## 圆反演的基本性质

前文涉及一个有趣的数学问题，那就是为什么随机映射的点“总是”能收敛，形成互相相切的圆形图样？本文先解决一个圆的反演问题，之后再对多个圆的情况进行扩展

[Inverse geometry I](https://observablehq.com/@listenzcc/inverse-geometry-i)

## 在太阳内部航行

真空中的光速为每秒30万公里，
但太阳最内部发出的光则需要10万年才能到达太阳表面，
这是由于那里的光子需要不停的与其他光子发生碰撞。

## 在线实验的信号边缘频率失真

所谓在线实验就是将连续信号不断切断，并且在断口处进行实时分析的苦逼过程。然而信号的有些频率成分会在断口处出现较大的失真，这是离线算法不能直接移植到在线实验场景的重要原因之一。

本文直观地显示了这一点，开源代码可见我的ObservableHQ 笔记本

[EEG filters](https://observablehq.com/@listenzcc/eeg-filters)

## 地图工具 V0.1

地图是一个让人能够更加理解地缘的好东西。

于是我决定一点一点地做一套自己的地图工具。

## 地铁密度对比

在某个神奇的国度，不是每个人都有把握方向盘的权力，因此，地铁就是出行的主力。

本文试图通过蜂窝状的网格进行计数，用来对各个地区的地铁方便程度进行量化。

本文代码可见我的前端笔记本 

[Subway stations in hex grids](https://observablehq.com/@listenzcc/mapbox-with-hex-grids-version-3 "Subway stations in hex grids")

## 均贫富

本文是使用 Atomic Agents 分析另一个有意思的问题。

> 在平等交易的前提下，贫穷和富裕是如何诞生的？

本文的分析结果偏向于认为贫穷和富裕是在自由交易的市场中自发形成的，动态平衡的经济学现象。

## 基于Delaunay算法的自组织纹理

本文将“人以群分”的原则应用在随机分布的点集中，其中Delaunay算法用于确定每个点的邻居及其阶数。如果某个点类别不是其邻居点集的简单多数时，他就选择搬家。无数个这样的个体会导致整体上呈现某种纹理，实验结果说明多样性越低，邻居的外延性越强，越容易生成较大的连片”集合“。

[Crazy neighbours by delaunay](https://observablehq.com/@listenzcc/crazy-neighbours-by-delaunay)

## 基于GPU的快速Julia集计算

本文记录一个利用GPU计算的前端程序，它用来在PC上快速计算和实时渲染大量迭代的 Julia 集。由于 GPU 算的实在是太快了，因此我决定让它成为一个实时计算和渲染程序。开源代码可见我的前端笔记本
[The Fractal (Julia Set) on GPU](https://observablehq.com/@listenzcc/the-fractal-julia-set-on-gpu "The Fractal (Julia Set) on GPU")

或GITHUB页面
[JuliaSet-GPUIO](https://listenzcc.github.io/JuliaSet-GPUIO/ "JuliaSet-GPUIO")

## 基于人口普查数据的性别比例分析

出于偶然，本文尝试对第七次人口普查的公开数据进行分析，尝试将表 1-5 和 1-6 中的性别差异进行可视化。**本工程的特点是形成的数据更加像是数据库，因此更加便于进行可视化分析。**得到初步结论如下

- 天津户籍人口，他参加高中入学考虑并考上高中的概率约为 $66 \% \sim 77 \%$；
- 按照地区和年龄进行区分可知，我国男性青年多于女性，大约多 $10 \%$；老年女性多于男性，且二者差异随年龄不断扩大；
- 如果中国有“重男轻女”的观点的话，那么它造成的恶果是小学升初中阶段失学女童数量多。而是之后的教育阶段中，除了攻读博士研究生女性较少之外，女性均强于男性。

开源代码可见

[https://github.com/listenzcc/population-by-gender-1](https://github.com/listenzcc/population-by-gender-1)

[Population by gender - 1](https://observablehq.com/@listenzcc/population-by-gender-1)

## 增长方程的两个不变性

本文将在前文的基础上，对增长方程的性质进行简要分析，即从矩阵的行和列观点来看，分析它的两个不变性。分析和演示代码可见我的前端代码库

[Generating the Optimized Production Matrix II](https://observablehq.com/@listenzcc/generating-the-optimized-production-matrix-ii)

## 增长的最优系数

在前文中，我们论述了在指定生产矩阵的条件下，如何确定初始化资源比例，以及在这种比例下增长会如何发生。

本文将这个过程反过来，尝试解决在给定初始条件和期望增长的前提下，如何选择生产方程的问题。

## 大事记

最近有同志去世，比较好奇他在任期间有哪些大事，于是找到了官方的权威文档，但这个文档看起来有点麻烦，于是我尝试把它们整合在一个页面里。

[中华人民共和国大事记（1949 年 10 月－2009 年 9 月）*历史概况*中国政府网](http://www.gov.cn/guoqing/2009-10/09/content_2582666.htm "中华人民共和国大事记（1949年10月－2009年9月）_历史概况_中国政府网")

[Story of China](https://observablehq.com/@listenzcc/story-of-china "Story of China")

## 大新闻

号外号外，真有文化人说别人是犬子了。

## 大风扯乎

最近在知乎上看到一篇奇文，
算是“地摊文学”的上乘之作，
隐隐然有种《细菌、病毒与钢铁》的扯淡气魄。

于是找了点材料，
看上去还真是这么回事。
本文的分析代码可见
[我的代码本](https://observablehq.com/d/4037ab90a91424a7 "我的代码本")

## 天津中考成绩的数值分析

本文尝试对2023年度天津中考成绩进行分析，讨论学生和郊区学生在不同分数范围下的表现以及估计他们进入高中和大学的情况。

市区学生在高分范围（>750）表现更好，而郊区学生在中等分数范围（~700）表现更好。高中录取方面，市区学生的录取要求分数约为580，而郊区学生为560。

进入大学的情况根据高中入学考试成绩进行估算，其中郊区学生在985211工程大学录取中略处于劣势，而在总计录取中表现出优势。综合而言，学生的地区背景可能会对录取结果产生一定影响，

本文的数据图可见我的 ObservableHQ 笔记本

[High school entrance exam in TianJin](https://observablehq.com/@listenzcc/high-school-entrance-exam-in-tianjin)

## 好界面是拖出来的

本文提供一个大道至简的界面编辑框架，解决的痛点是普通人如何把“我要把这个框框画在那个位置”这个朴素的审美需求转化成程序员能看懂并用程序实现的设计需求。本工程的代码可见我的 ObservableHQ 笔记本

[Layout player](https://observablehq.com/@listenzcc/layout-player)

## 字体比较工具

这是一个字体比较工具，它的优势是快捷和风格可调。

目前确有这样的在线工具，但它们可能 ​ 没办法像我这样实时调整背景。

## 宇宙为何空空荡荡

这是标题党，但又不全是标题党，因为我有实验。

## 将FSL统计结果映射到FreesSurfer皮层上

这是一个工作过程记录。
总的目的是将`FSL`的预处理及统计分析结果，
映射到`FreeSurfer`的皮层空间上。

工作流可见我的[GITHUB工程](https://github.com/listenzcc/freesurferAnalysisScripts "GITHUB工程")，
可视化代码可见我的[ObservableHQ工程](https://observablehq.com/@listenzcc/free-surfer-cortex-v2 "ObservableHQ工程")。

## 局部最优如何随机地填满整个空间

本文继续用 Delaunay 算法构造一个二维连通图，一些点按照局部最优的规则进行随机游走，我记录了整个连通图中各个节点数量密度的动态变化，并且记录了这些点从源到漏的可能路径。我原本的假设是这些有一定自主性的点会自发地形成较短或较稳定的通路，但事实并不是这样。相反，这些局部最优的点会随机地填满整个空间，并且整个分布模式随时间变化。

本文的开源代码可见的 ObservableHQ 笔记本

[Random walkers](https://observablehq.com/@listenzcc/random-walkers)

## 布朗桥噪声的三种可视化方法

布朗桥噪声具有回归性质，该特性使得布朗桥噪声在金融建模和信号处理等领域中有广泛的应用。本文通过可视化的方法说明，随着时间的变化，一系列布朗桥的时序变化是统一的，都呈现了先扩散、再收敛的趋势。

另外，我使用 Plotly 工具将全部点绘制在三维图上，用来表示其在三维空间中可以更加全面地展示整体分布。本文的开源代码可见的 ObservableHQ 笔记本

[Simulate diffusion using Brownian Bridge](https://observablehq.com/@listenzcc/simulate-diffusion-using-brownian-bridge)

## 布朗桥（Brownian Bridges）

在建立某个随机动力过程时，我们虽然希望其随机性尽可能大，但又要防止它的范围过分扩张。通过使用合适的约束手段，我们可以达到这一目的，Brownian bridge 是其中之一。

本文的开源代码可见我的 ObservableHQ 笔记本

[Brownian Bridges](https://observablehq.com/@listenzcc/brownian-bridges)

## 弯道超车

滑冰也好，赛车也好，
都是速度的游戏。
而弯道既是速度的瓶颈，
更是超越的机遇，
所以是比赛的关键。

本文是使用**动态规划**的方法，
对通过弯道的**最快方案**进行估计。
该方法简单和粗糙的不可理喻，
但它的结果似乎又有点靠谱。
气不气人。

经过一通分析告诉我们一个道理，
玩赛车或者滑冰等竞速游戏，
遇到弯道要记得

> 早刹车、切内弯，然后油门焊死，你就赢了。

所以，在冬奥会看滑冰，
他们那帮人才会在入弯时拼了命地使小动作，
毕竟谁占内弯，谁就赢。

## 形式逻辑的陷阱

最近 ChatGTP 火出圈了，但和小伙伴交流发现，大家都认为这种语言模型可能会让人误会他说的是有道理的，即使它们只符合形式逻辑。因此，不能简单地拿它当作搜索引擎用，并且只有明确地知道它返回结果的意义，才能更好地让它为人服务。

本文以容易理解的二维场作例子，试图说明在采用不同的计算方法时，场的叠加可能会得到截然不同的结果，即使这些结果看上去都还行，但是否能够反映实际情况，则有待分析。本文的例子可见我的前端笔记本

[The gravity field of two stars III](https://observablehq.com/@listenzcc/the-gravity-field-of-two-stars-iii "The gravity field of two stars III")

## 扩散模型-1

最近扩散模型比较火，所以本文尝试用前向计算尝试对它进行解释。

本文的代码可见我的前端笔记本

[Diffusion Model Demo (Forward)](https://observablehq.com/@listenzcc/diffusion-model-demo-forward "Diffusion Model Demo (Forward)")

## 扩散模型-2

本文尝试将扩散过程反过来，即从随机噪声“生成”有意义的图像或者数据。

## 色块拼图

计算机里的图像一般是方方正正的，
由像素组成的矩形集合。

而人描述一个场景或图像时，
所使用的往往不是这样规矩的矩形，
而是这样的话语

> 这里有山有云，在夕阳下，
> 山和云都显出很好看的红色。

因此，我们或许可以尝试使用“色块”对场景进行描述。

【这是一段棒到不行的视频】

本样例的代码可见我的[在线笔记本](https://observablehq.com/@listenzcc/quadtree-art "在线笔记本")。

## 数据截断及估计

继上文“滤波及失真”之后，我们还需要考察的问题是，是否能够使用被截断的信号来估计出原始信号。当然，这里的反推并不是完全的还原，因为对于随机信号来讲，我们往往更关注它的统计特性，而非具体取值。这就要在频谱上做文章。

## 文件结构树

现代计算机操作系统往往会用目录树的结构来维护用户的文件。

但用户面对这个树形的结构往往需要四处翻找，才能找到他想要的文件。

因此，本文尝试用交互式圆饼图展示文件结构，力图用最简洁的方式来帮助用户找到他需要的文件。

## 新冠地图

本文是简单的染色地图，
染色的数据是新冠疫情爆发以来，
世界各国的感染人数、死亡人数和死亡率。

## 无限上升的卡农

交变电场产生磁场，
而为了产生稳定的磁场，
就需要建立时刻变化的电场，
就像《GEB》书中写到的所谓“无限上升的卡农”。

## 日地月-2

本文是上文《日地月》的补足。
我用`THREE.js`建立了一个三维模型，还是太阳-地球-月亮互相转动的故事。

## 日地月

我用`ObservableHQ`平台搭建了一个好玩的`DEMO`。
它形象地展示了为啥一个月有大约`30`天，
以及为什么月相会呈现一种奇妙的周期性。

## 时空坐标中 Grid 的变换

本文对前文的分析进行补全，在时空坐标中，进一步绘制网格（Grid）在另一个坐标系中的变换图样。总体上看，静止坐标系中的矩形 grid 经过变换后形成类似菱形 grid 的新时空结构，这有点儿像一组平行四边形的架子，新坐标系运动的速度越快，架子扭曲就越强烈，时间和空间轴也就贴得越紧密。

开源代码可见 ObservableHQ 笔记本

[Easy understanding of why Light speed is a limit (grid version)](https://observablehq.com/@listenzcc/easy-understanding-of-why-light-speed-is-a-limit-grid-versio)

## 时间的漩涡

在时间的河流中，日子容易过得头昏脑涨。我觉得时间像个齿轮令人眩晕，人在眩晕中顾不上看年华老去。本工程希望通过螺旋的时间线来传达我的感受。怎么说呢，反正看上去可能有点晕。

开源代码如下

[How do the time pass?](https://observablehq.com/@listenzcc/how-do-the-time-pass)

## 最速降线的蒙特卡洛逼近

本文进行了一次尝试，尝试通过简单粗暴的蒙特卡洛方法逼近一条“最速降线”。

本文代码详见我的前端仓库

[Estimate the Brachistochrone using Monte Carlo Simulation](https://observablehq.com/@listenzcc/estimate-the-brachistochrone-using-monte-carlo-simulatio "Estimate the Brachistochrone using Monte Carlo Simulation")

## 机械臂运动控制的位置和角度关系及其可视化

本文是记录一个交互式可视化工程，
它对二维二轴机械臂的平面运动过程中，
控制角度与机械臂端点位置的相互关系进行可视化，
并且允许用户通过鼠标模拟二者之间的对应关系。

## 三轴机械臂运动的逆解

在`THREE.js`的支持下，我们可以做出一些有意思的应用。
比如模拟一个三轴机械臂的运动。
于是有了这个缝合怪。

## 树形数据结构的表形管理

这篇东西仍然比较无聊，它描述了如何用表对一种树形数据结构进行表达。

树形数据结构支持深度和广度遍历，优点是使用灵活，缺点是内容偶合度过高，导致难以单独存储；

而表形数据结构则更贴近数据库，优点是条目清晰，易于存储。

本文尝试在牺牲一定存储空间的条件下，用数据库的形式对树结构进行一定程度的表达。

## 每日一图

不得不说`BING`的每日一图是真的好看。
不妨以为契机，记录一下前端绘图的一些经验和坑点。

## 气温地图

接着上回的温度数据，再做一点工作。

具体来说，我关注一个温度指标，它就是

> 今年 7 月的温度比去年同期高多少？

能看得出来，我国西南今年是真的热，

> 有多热？比去年高 9 度的那种热。

## 水球效果

这是一个在真空中的水球效果的模拟。
不是物理模拟，
而是看上去相似的一个动画。

## 涂鸦玩具

窗外在下雨，这种天气特别适合在家写程序。正好学一下 pixi.js，并与 perfect-freehand.js 结合，写了一个特别跟手的涂鸦绘板 demo。源程序可见我的 ObservableHQ 页面

[Hand writing with Pixi.js & perfect-freehand](https://observablehq.com/@listenzcc/hand-writing-with-pixi-js-perfect-freehand)

## 混淆矩阵的统计量绘制工具

本文提供了一个简单易用的二分类混淆矩阵的统计量结果绘制工具，能够比较全面地绘制出分类模型在各种性能条件下的统计量分布。本工具对分类器所有可能的三个维度均设为可调的，这形成了可拖动的软件界面，方便使用者调整到自己想要的条件。另外，本软件还支持多种统计量的全局展示，

软件工具的开源地址如下：

[Confusion matrix computer (binary)](https://observablehq.com/@listenzcc/confusion-matrix-computer-binary)

## 滤波及失真

针对信号进行滤波是信号处理的基本操作之一，它可以用来提取信号中我们感兴趣的特定成分。

但操作必然会导致信息量的损失，失真就是这种损失的直观表现。

这个话题很大，我就遇到哪写到哪。

## 漂移变道

最近常做梦，梦到买了辆车，车牌号很吉利，叫做 BJHJYD。

买了车咱就开，那么问题就来了，为啥超车变道的时候需要后车刹车呢？

为了回答这个问题，我写了个前端程序

[Over taking](https://observablehq.com/@listenzcc/over-taking "Over taking")

## 激活函数的功率谱密度

本文从量化的角度解释双曲正切激活函数对信号的 FFT 造成的影响。
本文开源代码可见我的前端笔记本
[FFT for Activation](https://observablehq.com/@listenzcc/fft-for-activation)

## 点集的着色及其生成顺序分析

我们之前在给定图形之内构造了一组致密点云，本文进一步解决如何对这些点进行分类着色的问题，并分析点集的类别与生成顺序之间的关系。如果我们稍微放飞一下自我，也许它可以作为一个 demo，用于解释机器学习中的“涌现”现象。

开源代码位置仍为

[Plot population](https://observablehq.com/@listenzcc/plot-population)

## 物以类聚

都说物以类聚，人以群分。但又都说要兼容并包，兼收并蓄。

后一个说教其实大家都不怎么喜欢听，因为它天然的假定物以类聚这个现象，是因为个体微观的不够包容而造成宏观现象。

也就是说错在个人，社会是个人意愿的加和。

而群体行为的研究却有证据认为，群体行为往往不是个体行为的简单累积，而是具有混沌属性，往往与参与者的主观意愿相悖。

落实在本问题上，即使每个人都很大程度的包容自己的邻居，在群体层面也会呈现出极其严重的分类和隔离。

## 特斯拉阀水管的粗糙模拟

特斯拉阀（又称 fluid diode）是一种单向阀门，也被称为流体二极管。

出于好奇，我用之前的粒子模拟程序做了一个简单的 demo，实验结果表明顺向流动的出口流速大于逆向流动，在一定程度上模拟了 fluid diode 的特性。

开源代码可见我的 ObservableHQ 笔记本

[LiquidFun Tesla Fluid Diode explain](https://observablehq.com/@listenzcc/liquidfun-tesla-fluid-diode-explain)

## 生产与增长

最近看到一个东西，叫做“增长方程”。它可以在一定程度上解决两个问题，一是在生产开始之前预知增长能否持续，二是预知生产的最优初始条件。它附带地解决了另一个问题，那就是为什么总有人说增长一旦停滞，就意味着 some thing is going very wrong.

[Growth equation](https://observablehq.com/@listenzcc/growth-equation)

## 瞎画的艺术

数据科学往往能在不经意间诞生艺术创作。

但这个过程可能有点过于不走心了，所以称为瞎画的艺术。

## 程序员的格子

我用 Mapbox 做了一个地图玩具，可以对地图进行精准定位，并且方便比较。

工程可见我的代码笔记本

[map-grid-by-mapbox](https://observablehq.com/@listenzcc/map-grid-by-mapbox "map-grid-by-mapbox")

## 等高线图

等高线图，又称为等势线图，
是对样本点的场的势面进行可视化的制图方法。

数学上，等高线图需要根据边界条件，
对连续函数进行求解。
但由于实际上并不可行，
因此本文提供一个的生成式的离散逼近方法。

## 素描

花鸟鱼虫皆入笔下，魑魅魍魉信手拈来。绘画素描应该是个挺有意思的事情，但可惜我并不会。

但不妨碍我看到一张图，就看看它用素描的方法画出来，是个啥样子。纯属好奇。

## 统计检验工具-F分布的可视化和速查工具

本文构造了一个方便的前端工具，能够以可交互的方式展示 F 检验中 F 值与 p 值之间的关系。这种工作本身没有意思，因为它除了根据已有的知识构造一个工具之外别无科学价值。

但本文在代码方面能够解决两个问题，首先它提供了 javascript 标准库引用的方法，其次它以更直观的方式展示了 F 分布在实数域的全貌。

本文开源代码与可交互页面如下：

[Stats of F Distribution](https://observablehq.com/@listenzcc/stats-of-f-distribution)

## 三维场景的受力模拟

本文还是基于`THREE.js`的三维场景呈现。
但缝合了`D3`的力模拟功能。

## 脑皮层的褶皱渲染

大脑皮层是高度卷曲的褶皱状结构。本
[前端工具](https://observablehq.com/@listenzcc/vertices-render "前端工具")
试图展示这一点。

## 腿部运动轨迹重建

这一个基于`THREE`的可视化工程尝试。
基于`IMU`角度信号对行走过程中的腿部运动轨迹进行重建。

## 致最可爱的天津地铁

虽然规模不大，但换乘可是一点都不方便。

与北京和上海相比，它会给你带来物超所值的通勤体验。

本文开源代码可见

[Subway stations v2](https://observablehq.com/@listenzcc/subway-stations-v2 "Subway stations v2")

## 艺术细菌

用了三种方法对图片进行艺术化渲染，分别是低分辨率化、马赛克化和动态化。
工科狗的艺术细菌就长到这了。。

## 蓝队加油

INTEL新近发布了第`12`代CPU，
在长时间挤牙膏之后，终于爆发了一次。
虽然没有了当前“默秒全”的统治力，
但新产品确实是让人大呼NB。

本文是十分应景的一文，
正好有一个良好的实验，
来说明“睿频”这个功能为计算资源的释放提供了怎样颠覆性的贡献。

## 贷款与存款

这是在不考虑通胀的条件下，按揭、月供和储蓄之间相爱相杀的故事。
首先，它回答了贷款一定金额时，其本息相当于在银行存了多少钱；
之后，它回答了“等额本息”月供的计算方式，以及当确定首月还款特定数量的本金时，多少个月后能够结清贷款。

[Saving & Loan Curve](https://observablehq.com/@listenzcc/saving-loan-curve)

## 赛博种树

话说十年树木，百年树人。我没有自己的土地种一棵树，但我有一台电脑，可以通过分形算法随机生成许多树，可以称之为赛博种树。种的什么树？种的是基于分形的随机树。这些树既没有用到 Github，也没有用到非法信道，又无法产生任何经济价值，所以应该不会被没收……吧？

[Fractal Tree Animation](https://observablehq.com/@listenzcc/fractal-tree-animation)

## 跳舞火柴人

本文以 Openpose 的骨架识别能力为基础，从视频中解析出人体关节的实时位置，并进行绘制。

解析代码可见我的 GitHub 仓库

[https://github.com/listenzcc/dancing-body](https://github.com/listenzcc/dancing-body "https://github.com/listenzcc/dancing-body")

绘制代码可见我的前端笔记本

[Dancing Body](https://observablehq.com/@listenzcc/dancing-body "Dancing Body")

## 辛普森悖论

在统计学中有一个挺神奇的悖论，称为辛普森悖论（Simple’s Paradox）。

简单来说，就是“在分组比较中都占优势的一方，在总评的时候有时反而是失势的一方。”

本文试图通过交互式的可视化方法，对它进行解释。

并且试图说明这种矛盾的情况并不是很偏僻的角落，甚至在合适的构造方法下，这种矛盾总能发生。

## 那些弃籍的美国人

根据一些奇奇怪怪的美国法律，
它的国务院会公开一些奇奇怪怪的信息，
其中就有放弃了美国国籍的人的名单。

本文对这些“不穷”的美国人用脚投票的结果进行可视化。

## 那抹五彩斑斓的黑

感谢 Apple，让我们见识到了传说中五彩斑斓的黑。

## 钢笔大厂的产品特点一览

我下载了一份关于钢笔的统计文档，里面收录了不同品牌钢笔的长度及重量信息，稍作统计如下。为了增强分析的可视性，我将派克笔厂现在仍然在产的较为经典的 Duofold International 系列作为参考，用红色十字线来表示，并且对大笔厂产品的重量分布也稍做统计，本文的可交互分析图可见我的前端笔记本

[Fountain pen database / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/fountain-pen-database)

## 长津湖

这篇很俗，但值得一写。

## 阿波罗尼奥斯问题

WebGL 的强项是进行大量并行的迭代计算，因此为了继续深入掌握它的使用技巧，我需要找一些有意思的迭代问题。Apollonius’ Problem 是一个很有意思的切入点，它可以用于形成十分美观的分形纹理。本文解决其中最基础的代数计算问题，开源代码见我的 ObservableHQ 笔记本

[Apollonius’ Problem for Multiple Circles](https://observablehq.com/@listenzcc/apollonius-problem-for-multiple-circles)

## 随机弹跳产生的混沌现象

本文是偶然看到一个模拟案例，在复现过程中意外发现一种混沌现象。在考虑了重力和反弹、不考虑摩擦和能量损失的情况下，小球在两个斜面之间弹跳可以导致混沌现象。本文的开源代码可见我的 ObservableHQ 笔记本。

[Random jump](https://observablehq.com/@listenzcc/random-jump)

## 随机游走片段的距离度量

本文尝试对随机游走过程得到的随机时间序列进行度量分析，通过分析这些时间序列之间的欧氏距离建立度量空间，并对该空间进行呈现。本文的开源代码可见我的 ObservableHQ 笔记本

[Distance between the brownian bridges](https://observablehq.com/@listenzcc/distance-between-the-brownian-bridges)

## 雨滴打在窗户上

本文使用 Canvas 模拟了雨滴打在窗户上的视觉效果。

实现这个玩意需要在前端实现三个功能，分别是图像的径向模糊、Canvas 绘图的遮罩方式和动态帧动画。

实现过程可见我的前端笔记本

[Rain drop simulation](https://observablehq.com/@listenzcc/rain-drop-simulation "Rain drop simulation")

## 颜色空间映射

本文试图解释一个可视化现象，那就是在单独改变某一个颜色通道的条件下，得到的颜色序列在颜色空间中如何分布。

## 风雨

风雨送人来，风雨留人住。草草杯盘话别离，风雨催人去。

泪眼不曾晴，眉黛愁还聚。明日相思莫上楼，楼上多风雨。

## 黄金分割探测器

所谓闭门造车，出门合辙。如果你遇到一个构图问题，比如摄影或者做 PPT 什么的，那么黄金分割律就是你要合的辙。本文提供了一个可交互的前端工具，用来从好看的图中找到其中的黄金分割律

[Golden Ratio in Image](https://observablehq.com/@listenzcc/golden-ratio-in-image)

# oh-my-image

The oh-my-image project.

The folder contains following md files:

---
## image

## tensorflow-1to2

# OpenGL

OpenGL Details on developing.

---
## B 样条

一般来说，立体渲染需要首先获取物体的三维模型。

而在有限信息的情况下，完全的三维模型往往难以取得，这就需要进行估计。

本系列将一步一步来，先从 B 样条开始。

B 样条是一种经典的物体表面估计方法。

## 三个火枪手

立体渲染是一个充斥着工程师卓越智慧的领域。它的科学问题不多，但工程上的困难几乎无处不在。因此，这也是一个大坑。

## 复矩阵的特征值点云

本文将之前的转移矩阵更进一步，不再局限于右随机矩阵，尝试扩展到复矩阵，并且对复矩阵的特征值分布进行可视化。本文通过渲染点云的方式展示特征值分布，由于要绘制的内容较多，且与特征值的科学计算深度耦合，因此本文采用 pyOpenGL 实现点云渲染。这就又绕回到 OpenGL 来了。

[https://github.com/listenzcc/stochastic-matrix.git](https://github.com/listenzcc/stochastic-matrix.git)

## 张量的缩并

张量，Tensor，是个数学概念。在计算机应用中，它可以用来极大地对计算进行提速。

本实验的结论表明，在样本规划大于 1 万的时候，张量计算快；在样本规模小于 1 万的时候，张量计算又装 X 又快。

## 搬砖小能手

常见的三维数据有两种，
一种是高度结构化的点集和面元数据，易于使用`3D`渲染工具，如`OpenGL`绘制；
另一种是单纯的体素数据，就让人很头疼。
本文提出的解决方法是像砖墙一样，将体素垒起来。

## 浅析 Ref-NeRF

NeRF 是目前比较流行的三维渲染网络，本文以新的 RefNeRF 为契机，
尝试说明三维表面中的法线与渲染之间的紧密联系。

## 超级加倍-反直觉的计算机视觉

计算机视觉算法实现过程中，
会遇到一系列相当“反直觉”的问题。
当然，这里的“直觉”指的是过于“想当然”的直觉，
而不是基于纯几何分析的理性推断。

事实上，这些问题的解决方式，通常是以几何分析为突破口的。
本文将描述如何正确处理计算机视觉三维呈现过程中，
如何生成一个正确的“表面”的问题。

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
## Sterling 公式

Sterling 公式将阶乘和幂函数统一起来，
它在 Gamma 函数的分析和使用过程中十分有用，
因此有必要将它的简要证明过程列写如下。

## 中值与均值的方差差异

本文尝试计算标准正态分布的中值的方差，并尝试分析它与均值方差之间的差异。

## 从条件概率理解 Sigmoid 损失函数

经过分析可知，它是线性方程或者二次方程的条件概率。线性方程的要求非常宽松，在两个类别的协方差矩阵相同时，只要求它们在特征$x$的空间中测度为$0$即可。在这种情况下，优化sigmoid损失函数等价于求解线性方程，寻找最合适的线性方程系数。

## 从检验到瞎编

本文将正式介绍统计检验的基本方法，并简要说明它的适用范围，以及它是怎么被玩坏的。

## 协方差矩阵的“半正定性”

前文不小心提到了一个错误的结论，那就是“协方差矩阵的特征值不小于0” 。我后来越想越不对，最后甚至发现这个题设是不成立的。计算实例可见我的 ObservableHQ 笔记本。

[Covariance matrix's semi definite](https://observablehq.com/@listenzcc/covariance-matrixs-semi-definite)

## 对称矩阵不必然是协方差矩阵

本文继续分析协方差矩阵。好消息是理论推导没有问题，之前实验与理论有出入是因为生成随机协方差矩阵的方法过于“简单粗暴”，导致将“不是协方差矩阵的矩阵”纳入了分析之中。

## 屈打成招

本文将用一个简单的例子说明前文《从检验到瞎编》与《通往显著之路》中介绍的校正方法之必要性。


## 平均分布的范围估计原理

我一直觉得这顶多是个排列组合问题，但谁能想到，这样一个简单的计数问题能追溯到高斯超几何函数上去（Gauss’ hypergeometric function）。

## 我们与真相的距离

俗话说“众口难调”，要摸底某个群体的真实情况往往是十分困难和意义重大的事情。
那么，我们需要调研多少个样本，才能在较高的置信度下，确定该群体的真实情况呢？
本文将通过概率分析方法，尝试分析并解决这一问题。
那么，这个调研样本的数量要求，就是“我们与真相的距离”。

## 概然而非必然的世界

这是之前写过的一个系列，但之前写的过于散碎，因此重新编辑一下。
我想通过这个大系列，慢慢地将全部概率统计知识囊括进来。

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

## 粽子一样的结构：协方差的分布特点

前文说明了协方差矩阵是对称矩阵的子集，本文通过蒙特卡洛模拟的方法进一步绘制了协方差矩阵非对角线上的值的联合分布特性，实验表明，低维特征协方差的联合分布不仅不会占满整个空间，甚至呈现出一种粽子皮一样的四棱椎形结构。

## 通往显著之路

上文《从检验到瞎编》介绍了统计检验的基本方法。
并引出了多重比较校正的概念和经典的FWE校正方法，本文将介绍另一种多重比较校正方法。

## 隐空间的可区分性

前文涉及了多元高斯分布以及它的协方差矩阵的逆，列出了隐变量的二次方程，还从后验概率的角度阐述了它与sigmoid损失函数之间的关系。本文继续在这个隐空间中，阐述隐变量的可分性，尝试从最肤浅的角度回答一个基本问题，那就是“sigmoid损失函数是如何区分不同类别的”，暨二次方程的一次和二次项在何时生效的问题。分析表明，我们更希望隐变量的一次项起主导作用，这也是深度神经网络最后一层通常使用全连接层的原因。

# Sun at Four

Have you saw the Beautiful Sun at 4:00?

The folder contains following md files:

---
## 你见过早上四点钟的太阳吗？

我没见过，因为教育部不太允许我四点起床。
我们这疙瘩在四点钟也不是很经常能看见太阳。

不过我现在每天只需要写`1`个小时的作业了，补课也不用去了。

## 卷起来

中国人太过聪明。
似乎一切既定的规则，只要有中国人的参与，就都将成为内卷的源动力。
人更像是手段，而不是目的。
甚至，连出生年份都能卷。

## 搭建 GIT 服务器

如果你拥有一台服务器的使用权限，就可以将它作为你的 GIT 服务器，像使用 GITHUB 一样来使用它。

要达到这个目的并不难，但中文互联网技术（IT）的经验分享，可能会让这个过程变得有些艰难。

## 诗人和远方

网传麦克阿瑟在西点的演讲被收入了语文教材的爱国篇。这让我有点想吐，难道中国文人这两千多年来什么都没干，竟然沦落到要一个美国人教中国孩子怎么爱国吗？你这与XX做XX的XX。

当然，单纯的抱怨没有任何用处，就写写相关的东西吧。

中国文人重游历，足迹遍及海内。充耳不闻天下事，一心只读圣贤书？你寒碜谁呐？

# Tableau

The workshop in public.tableau.com

The folder contains following md files:

---
## 人在美国，刚刚破产

这两天天气热，因为无心写程序所以有此文。我当然去不了美国，但昨天不知道哪只耳朵听到了他们这两天破产的事情比较热闹，于是我就来凑凑热闹。本文的数据分析可见我的 Tableau 笔记本

[](https://public.tableau.com/app/profile/chuncheng1883/viz/bankruptcy-in-us/Story1)

## 春来江水绿如蓝

本文介绍一个道听途说的科学方法，它能够对春天到来的准确时间进行定位。通过将春天到来的日期与平均气温进行比较，可以发现它们之间的巧妙关联。这个关联如同废话一般：气温越高则春天来得越早。原始数据和交互式数据表可见我的 Tableau 工作薄

[](https://public.tableau.com/app/profile/chuncheng1883/viz/Temperature-vs-sprintComming/Dashboard1#1)

## 汉堡指数

他们发布了近20年来的汉堡指数原始数据，于是我通过 Tableau 工具对原始数据进行进一步拆解，以世界各国货币购买力为对象，分别在人民币和美元的度量下，分析它们的平价购买力变化趋势。

# Talk with Picture

The Topic will try to create **Pictures** for **Key Ideas**.

The folder contains following md files:

---
## 21 世纪的我们一无所有

21 世纪的我们可能拥有一切，却始终一无所有。

## COCO图像类别空间的简单可视化

本文将分别使用`PCA`、`TSNE`和`SOM`三种方法对`COCO`数据图像的类别信息进行映射。
从而以较低的维度对数据进行呈现。

## Coco数据集

Coco数据集是通用较强的数据集，
它的全称为“Common Objects in Context”，
里面包含了各种日常物品，可以细分为`80`类。
对这些图像中的物品进行统计，
也许可以帮助我们了解一般的图像的统计特性。


## EEG，LFP 和路径积分

上篇文章中，我成功模拟了有限源数量下的头皮 EEG 处的电场强度。但如果您做过 EEG 实验的话，可能会觉得我是在胡扯，因为采集到的 EEG 信号是标量而非矢量。因此您心中会有疑惑：那些黑色矢量是干什么用的？

本文将回答这个问题，在本文的代码中，**黑色矢量是局部电场梯度，而我使用路径积分的方式将电场梯度转化为 EEG 设备采集到的电压值。**

本文代码开源，可见我的 ObservableHQ 笔记本

[LFP & EEG and Path Integral](https://observablehq.com/@listenzcc/lfp-eeg-and-path-integral)

## GDP与财政收入的年度变化

有人说《繁花》说上海的富和《山海情》说西北的穷在时间上是同步的。我不信，于是找到了一些数据，非常有趣。80年代到90年代这段时间内，除了广东省的GDP一飞冲天之外，其他四个地区的排序和比例基本不变。上海市的GDP四倍于甘肃一个省。从财政收入占全国GDP的比例变化看，似乎可以反映祖国经济周期的变化，自1994年分税制改革开始，三条曲线的变化非常平稳，这也是祖国发展最快的时期之一，其中似乎有无为而治的精神内核在。第三产业所占的比例也在2016年超过50%，这印证了祖国大步迈进工业化，服务业也开始繁荣的说法。但从整个国民经济的比重来看，农业的发展是否过慢，这个我不太懂。

## Genie，为何更贴近世界模型

Genie模型标志性地通过分析视频中的连续动态变化来学习物体如何随时间变形和移动，与仅处理文本数据的语言模型如Sora不同。它的这一能力使得Genie能够理解从一个状态到另一个状态之间的整个过程，类似于人类观察世界的认知过程。这种对中间过程的理解对于执行复杂交互任务至关重要，有助于提高人工智能系统在自动驾驶、机器人技术等领域的性能和适应性，使其行为更加自然和人性化。

## Linux User Cookbook

<aside>
💡 To whom wants to, but never got a chance to try Linux Server.

</aside>

## Quick Start

- [ ]  🌐Download & Install MobaXterm
- [ ]  🙂Ask admin to make you account (Login IP, Username, Password)
- [ ]  🤖Establish the remote session of MobaXterm to log in the server with SSH
- [ ]  ⌨️(Optional) Establish the remote development environment with VSCode or Pycharm or something like
- [ ]  🆗(Optional) Set up your Key Authorization of SSH login without password

## Movie in Machine Learning

如果你实在是没有时间看电影，不妨让算法把相似的信息提取出来。

当然，目前的算法很粗糙，提取的信息也很朴实。

## Who are they

为纪念两会胜利召开，本文提供一个前端工具，分析代表们的性别、年龄、民族和地域分布。当然，这些都是 baidu 上搜来的公开信息。

[Who are they](https://observablehq.com/@listenzcc/who-are-they)

## World trade data

The analysis script and data are provided in

[World-trade-data-I](https://github.com/listenzcc/World-trade-data-I "World-trade-data-I")

Two opinions raise by the analysis

-   Every country trade with limited other countries. And there are not any country expanding to every other country.
-   The world has only little countries that dominate the international trading.

## 一种线性反馈的多输出零点控制方式

本文将试图说明一种面向线性反馈系统的，
基于共模差模控制的，
双输入、双输出反馈控制方式。
这只是第一个版本，
只给出定性分析，并不列出系统方程。

## 丙子双十二

1936年12月12日，西安事变。
我们被揍得鼻青脸肿，
国家元首还被自己人给绑了。

如今75年过去了，
我们却在购物。

## 从词向量的角度理解COCO

上一篇从类别标签的角度介绍了`COCO`数据集的基本情况，
本文将从“词向量”的角度理解这组数据。


## 从财报看股票

本文从下载的 AP7 的财报出发，首先使用 Power BI 解析 PDF 文件，之后利用 Power BI 进行可视化分析。

Page: [jiangxiangkeji](https://listenzcc.github.io/jiangxiangkeji-powerBI-parse-pdf "jiangxiangkeji")

从分析中可以看出，对于 AP7 来说，宝岛的投资价值无论从数量和质量来说，都是高于大陆的，可能很多西方国家也都这么想吧。

## 价格从哪里来

最近麦当劳涨价了，因此本文的观点有点解释不通。为了想清楚哪里不对，我先要把这些东西组织一下，正好写出来。矛盾的点集中在需求曲线上。现今的经济环境会导致需求曲线向下掉，即在相同价格下，消费更少的商品。在低价大量的消费品区间，企业为了生存下去，他只能选择降价提量的策略。
此次麦当劳的涨价不太符合现在经济环境的大众认知。这也是我矛盾的起源。

## 仿生人眼中的电子羊

我手里有两个模型，一个是 stable-diffusion 的 txt2img，一个是最近开源的 minigpt-4，它能够做到 img2txt，我让他们开始左右互搏。AI 的飞速发展给我们带来了一个契机，让我们有机会“看到” AI 心中的鱼，有机会“计算” AI 心中的鱼是悲还是乐。本文采取的做法是让一个 AI 模型去解读图像，之后让另一个 AI 模型根据他的解读来复现原始图像。这个过程能够解决这样一个问题：**两位仿生人眼中的电子羊是不是一只羊？**

## 全面开往小康社会

过年嘛，既然日子也就那么回事，
所以就畅想些美好的未来。

今年据说是全面建成小康社会的一年。
它标志着我们也许可以开始畅想着买小汽车的事情了。

## 公务员，如何高收入？

本文综合了从遥远的科普卢星区得到的信息，制作了2023年的公务员工资制度一览表，并结合了最新（2024年1月）发布的国民经济统计报告，进行了一些可视化展示。

直观地解决两个问题，首先，如果你选择成为一名公务员，那么按照目前的标准，你如何获得高收入？其次是给大家提供一个视角，管中窥豹地、片面地、不负责任地推理，站在上层官员的视角，他们如何看待你的收入。

[公务员工资制度一览表(2023)](https://observablehq.com/@listenzcc/2023)

## 初五迎财神

一晃已经初五，
假期余额严重不足。

正好今天的习俗是祭灶，
就索性写写发财的事。

> 从概率统计的角度来分析，
> 麻将怎么打才能赢？

本文可以带来三条建议

- 牌局进行到大概`14`轮时，就要警惕赢家的出现了；
- 如果你会赢的话，尽量基于起始的牌，不要大换血；
- 尽量留中间的牌，这样赢的概率更大。

## 北京冰冷的腊月与 El Niño

起源于太平洋赤道附近水域的El Niño现象导致Hadley circulation增加，由于Hadley circulation规模巨大，因此它的改变会大规模地引起全球气候短期变化。比如，导致中国北方冬天寒冷的西伯利亚高压（Siberian high）就受到它的影响而变得更强，这导致冬天更冷了。极端气候也会因此增多，所以今年冬天要注意防护。

## 商业精神

《潜伏》里的谢若林同学曾说过一句名言，
嘴里都是主义，眼里全是生意。
如今流行的WEB3.0自然也是商业逻辑催生的产物。

## 喜迎世界杯，尝试可视化

可视化是数据的表达方式，而数据是可视化的基础。

比如，一场足球比赛下来，足球、球员和裁判员的位置会形成一组庞大的数据。

我一直希望有机会看看这些数据是什么样子的，而如火如荼进行的卡塔尔世界杯正好给了这样一个契机，可以边看球边写代码的契机。

[football-event-visualization-1](https://github.com/listenzcc/football-event-visualization-1 "football-event-visualization-1")

## 降维打击-四元数

欧拉四元数简直是神迹，
用四维的形式解决三维的问题。

在四元数规范下，
我们将看到内积和外积对应同一个方程的实部和虚部，
也因此，三维世界的解析几何经典公式在四维世界中成对出现。

这也是目前主要的计算机视觉工具在处理三维空间几何计算问题时，
使用四元数对空间坐标进行表示的原因。

## 图像的颜色风格化

神经网络的非线性映射方法能够方便地进行各种有效的计算机视觉设想。
本文尝试使用SOM与KMEANS相结合的方式，对图像进行有效的颜色风格化。

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

## 地图映射

同志你好，请问基辅怎么走？

克里米亚属于山区，而旁边的基辅是个大平原。
怎么说呢，它们就相当于中原腹地与燕云十六州之间的关系。
因此，我不觉得普大帝在装腔作势，毕竟换谁能忍得住？

所以问题来了，
为什么俄罗斯在地图上显得这么大？

## 声音的谱

本文对英文中易混淆发音的单词进行谱分析，
从谱分析结果中，
可以看出一些不容易听出来的东西。

## 她是活的人，而不是尸体

长太息以掩涕兮，哀民生之多艰。

## 如果数据对得上

这是一件值得高兴的事情，因为这个数据它吻合得很好。

说是英国 2022 的新生儿名字排名第一名是 Muhammad，即伊斯兰教的教名“穆罕默德”。经过数据分析可知，这主要是因为穆斯林的命名习惯，而不是因为他们人多或者生育意愿更高。

本工程的开源代码可见我的github仓库

[https://github.com/listenzcc/baby-names-in-england](https://github.com/listenzcc/baby-names-in-england)

## 如果时间是条河

尽管空间旅行的速度越来越快，但人类目前的技术还无法跨越时间。如果时间是条河，那么人们只能随波逐流，因此，你的起点就决定了你的终点。

## 宝马司机醉驾撞人拖行案，有行为，但没有后果

这件事情让我感到愤怒，我知道应该慎言，我也不会讲脏话，但人至少要有良心。

肖做了两个行为，却只有第一个涉及交通肇事的行为受到了法律的制裁，第二个涉及故意伤害的行为没有任何代价。退一万步讲，即使认定“特别残忍手段”较为困难，那么至少应该有故意伤害致人重伤的行为吧？也就是说，肖至少欠了人民 3 年 9 个月。

老爷们，难道将人活活地拖行 2100 米致重伤不算是“特别残忍手段”的“故意伤害”吗？

## 恒大而不倒

所谓“大而不能倒”不是个笑话，而是当你的资产足够多之后，你会在地球 Online 上自动得到的特权。这对“计算随笔”来说并非文不对题，因为写这个东西的目的是通过一切计算的和事实的记录，增进我对这个世界运行规律的理解。

数学的、物理的和计算机的知识是规律，而社会的、经济的和法律的事实也是规律。

本文顺便介绍了恒大这次的电动车业务资产重组的动议，所谓“资产重组”就是这样不断剥离“好”资产，不断得到钱还债的过程。当“好”资产卖完时，剩下的东西就申请破产清算。只不过这个破公司暴雷日久，但我们似乎还并不知道最后剩下的“渣滓”会是什么，以及这些渣滓会由谁来买单。

## 按需分配

那个啥的核心奥义是实现按需分配，
所以请拥抱`HTML`吧，
这里啥都有。

当然，有时候你需要一些`JS`提供的帮助。

## 收益率诱导的均富或分化

我们将世界抽象成为一个金融机器，简单来说，就是一些人有一些钱。我们让每个人的财富开始增长，这里开始体现阶层之间的差异。我假设钱多的人把钱都拿出来进行投资，而钱少的人则把钱都花在了自我消费上，导致越有钱的人他的收益率就越高，越穷的人他的收益率就越低。接下来就是求解带约束的二次规划问题。

我们不能理想化地假设 $r_m \gt r_g$，事实上也没有人能够一定跑得过超高的社会总财富增长率，因此我们在实验中将它设定为可变的（max_interest_ratio = 0.05, 0.1, 0.15），用来模拟社会财富的分配情况。实验结果表明，最终的财富分配情况对该值十分敏感，它几乎决定了社会走向共同富裕、两极分化或者拥有庞大的中产阶级。

本文开源代码可见我的 Github 仓库

[https://github.com/listenzcc/economy-experiment-1](https://github.com/listenzcc/economy-experiment-1)

## 文化自信

自信就是相信自己，进而相信自己的邻居和同胞能够成就伟大的生活和事业。

但是国人近期对谷爱凌的关注，反映出了国人目前普遍崇拜美国归来的游子。

所谓中国是世界上最大的美分，这句话似乎没有原则上的错误。

## 旅居中国的生活成本

本分析探讨了外籍人士在中国生活的成本。数据显示，外籍人士的月生活成本介于2698元至7100元之间，这与中国中等收入群体的生活水平相似。生活成本中，住房支出占比最大，反映出在中国，“消费通缩、住房通胀”的现象。在不同城市类别中，随着城市经济水平的下降，生活成本占收入的比例也呈下降趋势。然而，三线城市的房租成本相对较高，可能由于受到周边大城市影响，导致地产价格与收入不成正比，形成价格畸高现象。

[如果外国人来我国生活，他的生活成本](https://observablehq.com/@listenzcc/if-you-are-living-in-china-for-expats)

## 日本排放核废水给大洋做了 PET

最近糟心的新闻比较多，不敢骂想骂的，就阴阳怪气儿一下八竿子打不着的。

日本前两天宣布向太平洋排放核废水，我想如果用分析大洋垃圾的方法来分析这些废物是可行的数据驱动方法。具体来说，如果将大洋当作病人，那么日本这次的行为相当于给他注射了放射性示踪剂，剂量极大且半衰期极长，追踪如此大量放射性同位素的轨迹可以帮助人类进一步弄清楚洋流的动力学特性。（运气好的话，这项工作有希望在 10 年后发 Nature，甚至获得诺贝尔核平奖）。

## 星链

马斯克搞的这个星链就很有意思，它既依靠大量小卫星覆盖全球，又让这些卫星的使用和发射成本足够小，像蜂群一样为地球服务。

## 来自 2018 的美国就业数据

本文是对美国 2018 年就业数据的搬运和简单可视化分析，该数据不仅是包括各行业门类，也包括这些门类中对不同教育水平人才的需求量和期望薪资，这些材料对青年的教育及就业选择极其重要。所谓“男怕入错行，三分钟带你选好专业”是也。本文使用的分析工具是 Tableau，开源地址如下

[tableau](https://public.tableau.com/app/profile/chuncheng1883/viz/Jobs-in-2018/sheet0?publish=yes)

## 汪淼的纳米丝：LK99，新型潜在室温超导材料的快问快答

如果 LK99 具有常温超导能力的话，凡是用到电的领域，生产力将继续翻倍。至于翻几倍，则取决于人类的想象力。也说明刘慈欣的《三体》中对未来世界的想象是合理的，**原始突破性创新很可能诞生于应用物理。**

如果不能的话，就当是科幻吧。

## 泡沫

习惯了经济学价值叙事的我发现，价值叙事解释不了时下很多的经济学现象。
其中一个重要的缺失是它解释不了经济泡沫的成因。

本文借用《再售期权理论（Resale Option Theory）》中的一个例子，
试图说明经济泡沫也许可以解释成异质信念条件下的资产交易属性。

## 甜品卡的 AI 甜品速度

我使用适当的模型对高清图像进行计算，以考察图像的处理速度。实验结果显示，普通电脑每秒能够处理 1 到 2 张图像。这个速度数据在家用机处理类似任务的情况下很重要，表明处理速度大约为每秒 1 张图像。

这也暗示两个情况：
- 系统无法处理流畅的视频信号，因为每秒只有 1 帧图像；
- 对于时间分辨率小于 1 秒的信号，普通电脑已足够。

## 硅谷银行暴了一颗“低风险”的雷

最近美国 Silicon Valley Bank 爆雷，我从 FDIC 上下载了近 30 年美国银行的暴雷统计，总觉得这次和往年的有点不太一样，因为这次的存款比重太大了。

如果对暴雷过程感兴趣的话，请阅读附录：SVB 的死亡倒计时。

[FDIC: Bank Failures in Brief](https://www.fdic.gov/bank/historical/bank/bfb2023.html)

## 科里奥利力

本体论追求并提炼万物的本源，
在遇到抽象现象时往往会遇到阻碍。

比如“科里奥利力”，这个找不到施力物的，
甚至受力物体都感受不到的，无形的力。

认识论就简单很多，
只要认识它就可以了。

## 素描

这是一段将图片转换为铅笔素描版本的小程序。

## 紧锣密鼓

这两天看知乎，似乎有一种ZZZQ，那就是新 20 条时群众应该已经开始备药了，所以后来新 10 条出台后，没有药是自己的问题。

好的，那么我们看看普通人怎么才能在 20 条和 10 条之间买到药。然而，经过简单分析可知，群众根本没有时间窗口买到充足的药品。

## 纹理与着色

如果你喜欢某一张图的配色，想把颜色方案应用到另一张图上。本文提供的方法和代码可以帮你一把。

## 蚌埠出差，读子养电

最近来蚌埠出差，机缘巧合看到了粟裕将军曾写的“子养电”，实在佩服。电文从今天看来，更像是一篇毫无私心的建议书，又像是对后来事情发展趋势的精准寓言，高屋建瓴。

本文记录的是我被电文纠正的几条成见。

> 淮海战役，是共产党方面的命名。在国民党方面，这场战事称之为“徐蚌会战”。淮海战役最先提案者是粟裕将军，但后来以徐州为中心的大决战，已非彼“淮海”，后来发生的“淮海战役”，实际上已经名不符实。

## 被收购的一年：动视暴雪的股价过山车

简单来说，动视暴雪的股价被自己的 CEO 作（zuo 一声）没了（A），微软看到了机会开始溢价收购（B），英国监管机构 CMA 反复横跳导致股价波动（C、D），美国监管机构 FTC 彻底败诉代表收购尘埃落定（E）。 从这个线条可以看到，当今世界的金融事件始终离不开英、美的 CMA 和 FTC 两家机构。金融世界的老大还是这些监管机构，他们的几条消息、几个上诉就可以操纵股价上天下地。

[Stocks (2021-2023) of Activision Blizzard, Inc. (ATVI)](https://observablehq.com/@listenzcc/stocks-2021-2023-of-activision-blizzard-inc-atvi)

## 记一个实用的数据浏览、收集和绘图流程

本文的重点不在数据分析，而在记录一个实用的数据浏览、收集和绘图的流程。这个流程的优势体现在充分使用互联网资源，使用TableCapture获取数据，使用GoogleSheet管理数据，使用Tableau展示数据。不消说数据展示会随数据积累和处理而实时变化，甚至除了浏览器之外，我的PC甚至都不需要安装硬盘。

[tableau](https://public.tableau.com/app/profile/chuncheng.zhang5140/viz/cost-of-living/scatterGraph#2 "tableau")

## 记一个神奇的BUG

今天遇到一个神奇的BUG，
解决方式虽然非常简单。
但它暴露出来一个问题，
即，我已经被弱类型语言给惯坏了。

## 运动反解算法

本文将综合之前的“四元数”计算、“机械臂”运动和“THREE”可视化的代码，
构建了一个仿“人体骨骼”的运动反解工程。

## 配色方法

如果你经常纠结于怎么为自己的PPT或其他什么东西配色的话。
本文将介绍一种基于`HSV`空间的配色方法，也许能解决你的问题。

## 酸葡萄

这一篇酸臭味道很冲的文章。

## 雾里看花：从MLP看验证集的作用

机器学习难，难在观测到的数据稀疏，从稀疏数据中估计总体分布如隔岸观火，如隔靴搔痒，如雾里看花。因此，交叉验证方法能利用有限的数据对估计出的分类器进行辅助评价和验证。

本文开源代码可见我的 GITHUB 仓库

[MLP-notebook/experiment-6 at main · listenzcc/MLP-notebook](https://github.com/listenzcc/MLP-notebook/tree/main/experiment-6)

## 高台跳水还是平稳着陆？

这个世界上什么都有，但就是没有意外。

有人诟病中国在 2000 年后发生了新生儿数量断崖式下跌的情况。虽然从国家的宏观层面上来看确实如此，但从个人的视角来看，其实这个过程相当平稳。
本文尝试说明，如今所谓“跳水式下跌”并不是某个特殊原因引起的，也不是某个特殊因素集中爆发的，而是生育水平在长达 30 年的时间内保持低位的必然结果。世上本无事，只是看上去比较吓人罢了。

本文数据及分析代码可见我的 Github 页面
[Github: population-vs-birth](https://github.com/listenzcc/population-vs-birth)

## 鱼眼看世界

很好奇鱼眼镜头里的“扭曲”是如何生成的，于是就有了这个模拟计算。

## 鱼眼看世界-V2

很好奇鱼眼镜头里的“扭曲”是如何生成的，于是就有了这个模拟计算。

本文对之前的内容进行了两个方面的扩展，一是考虑了空间角的影响；二是通过变换还原真实的视野内容。

# Tools Knowledge

The Topic is about how to use software tools better.

The folder contains following md files:

---
## AI 识图的易错场景

AI 是人工智能的简称，由于 ChatGPT 等强力产品的问世，已经有很长时间没人诟病 AI 是“人工智障”了。但事实上，AI 还是极易受到攻击。本文尝试进行一个简单的实验，说明 AI 识图还不是特别可靠。

首先，AI 模型对清晰的、未叠加的图像具有良好的识别能力。其次，叠加图的实验表明 AI 尚没有叠加的概念，叠加图的纹理会产生对抗攻击，导致 AI 得出错误结果。

本文的代码可见我的 GitHub 仓库

[https://github.com/listenzcc/hugging-face-image-player](https://github.com/listenzcc/hugging-face-image-player)

## Canvas 和 SVG 的设计理念

Canvas 的设计思路是“绘制图像”，它绘制出的图像中除了像素什么也没有。当你打开一个网页，如果里面有可以直接存储的图片，那么它们就是 canvas 的设计理念，这个理念特别适合复杂视觉内容输出。

SVG 是对内容的定义。而将它们渲染成图像的工作是与定义独立的，因此 SVG 的内容在用户界面中通常得到了保留，易于单独操作。当你打开一个网页，如果里面的图形内容可以用鼠标圈住，那么它们就是 SVG 的设计理念，这个理念特别适合富文本信息和图形信息的界面分发。

## Chrome 插件

浏览器插件可以增强 Web 浏览体验。

## DNS可视化实践

偶然看到一个可视化工具，它做了两件事：一是使用google的api迭代地搜寻某个网址的DNS信息；二是使用viz-js工具对迭代结构进行呈现。

[DNS graph](https://observablehq.com/@listenzcc/dns-graph)

## Django后端与JS前端

本文将以一个图像工程为线索，记录Django后端与JS前端的合作过程。虽然这些工作必将被 AI 取代，但现在还得有人干不是？这可能是一个较长期的记录，所以下次还会看到我，但是肯定会有些不一样。

## Docx 和 pptx 文档的再压缩

本文使用 P 颜色模式对图像进行压缩，并提供一个 gradio 工具实现 docx 和 pptx 文档的高度压缩。

[https://github.com/listenzcc/image-compress](https://github.com/listenzcc/image-compress)

## GIT-bug

GIT 是常用的版本管理软件，它偶尔也会出问题。

## how covid-19 is becoming

如果 a 比 b 快，
那么 b 就永远都追不上 a。
这是小学生都知道的事情。

那么如果病毒感染的速度比人类生育的速度快呢？

## MLP的相位估计

MLP可以用来估计信号的相位。通过训练带有相位估计目标的MLP,可以学习输入信号和相位之间的复杂非线性关系,从而产生相位估计。

上一句话是 AI 写的，但我有点怀疑 MLP 的能力，于是有此实验。而实验结果说明用 MLP 做相位估计具有较大的潜在风险。 

## MLP需要适当的规模

由于上次 MLP 回归失败，因此我决定对它进行改进。在增加了网络层数之后，我发现回归精度和收敛速度均有所提高。

[https://github.com/listenzcc/MLP-notebook](https://github.com/listenzcc/MLP-notebook "https://github.com/listenzcc/MLP-notebook")

## MRI 体积点云的旋转与渲染

体积数据的规模是表面面片数据的数十倍，导致框架设计困难，且渲染开销较大。本文使用坐标表示的方法实现 MRI 数据旋转截面的实时渲染，后端负责将点云数据及其坐标编辑成数据表的形式，而前端在一次性获取该数据表后独立完成旋转和渲染计算。

本工程的渲染开销相当于用前端孱弱计算的能力来实时解算 4K 视频，性能表现大约为每秒 3 帧，这对于 CPU 来说已经不错了吧？又不是不能用。

本文的开源代码可见我的 Github 仓库

[https://github.com/listenzcc/3D-brain-viewer](https://github.com/listenzcc/3D-brain-viewer)

## Mapbox 与 GeoJson

与 Canvas 相比，Mapbox 的原生 Layer 显然是更加优雅的解决方案，但它需要 GeoJson 的支持。

本文的代码可见我的开源前端库

[Mapbox with hex grids](https://observablehq.com/@listenzcc/mapbox-with-hex-grids)

## ONNX 下的 Transformer.js

你的浏览器远比你想象的强大。比方说，它可以在 ONNX runtime 下直接跑通 transformer.js 进行 NLP。

本文代码可见我的前端笔记本

[Transformer.js in browser](https://observablehq.com/@listenzcc/transformer-js-in-browser)

## Pubmed 搜索扩展的浏览器插件

我一直觉得搜索结果应该尽可能地方便用户使用，而不是单纯了吸引人点进去的入口。

于是我尝试制作了一个用于 Chrome 或 Edge 浏览器的插件，该插件用于查文献时常用的 Pubmed 搜索引擎，能够自动为它的搜索结果增加一些易用性功能。

简单来说，你不需要再点击进入任何一篇文章，而是可以直接在搜索界面上完成想要的操作。

[PubMed](https://pubmed.ncbi.nlm.nih.gov/ "PubMed")

## Python 进程与线程的使用指南

我们的目标是让 Python 多快好省地完成计算任务，本文实现了进程间的共享内存方法，在分布式计算的同时实现进程间的数据交互。另外，本文还使用代数计算的样例对进程、线程的并行计算性能进行测试和分析，讨论如何选择更合理的计算方式，才能通过并行计算提升整体计算效能。

本文代码可见我的 Github 仓库

[https://github.com/listenzcc/python-parallel](https://github.com/listenzcc/python-parallel)

## Python 进程与线程的使用指南

我们的目标是让 Python 多快好省地完成计算任务，本文实现了进程间的共享内存方法，在分布式计算的同时实现进程间的数据交互。另外，本文还使用代数计算的样例对进程、线程的并行计算性能进行测试和分析，讨论如何选择更合理的计算方式，才能通过并行计算提升整体计算效能。

## RDM与图像关系分析

本文记录近期开发的一套前后端工具，它利用 RDM 矩阵进行图像关系分析，而 RDM 矩阵的来源为 fMRI 和 MEG 采集的神经影像数据。文中附录部分为 AI 补写的 RDM 矩阵的细节，虽然有点啰嗦但十分靠谱。

## Socket之网络拥堵

一直很好奇在网络拥堵时 Socket 通信质量会劣化成什么样子。

于是今天做了个实验。

## Tensor flow 踩坑记

Tensor flow 删除了 contrib 模块，这是万恶之源。

## Terminal 伴侣

我发现了 windows terminal 的一个盲点，那就是我不能从中复制出制表符 \t，这限制了它的内容在表格应用中的转换，所以我开发了一个在线的转换工具，它的功能是将复制内容中的空格重新转换为制表符 \t，由于它的存在，其他类表格 APP 才能正常识别这些表格化内容。

[Suppose to be table](https://listenzcc.github.io/Suppose-to-be-table/)

## LLM 中 Token 的通俗解释

本文使用 python 的 transformers 包提供的预训练模型进行 token 解析，并尝试通过解析结果来回答 token 是什么的问题。通过几个例子看到，在不同的语境下，相同的 token 经过语言模型计算之后，可以得到不同的特征向量。这说明 LLM 在 token 的特征向量这一层级已经开始对语义信息进行处理，处理的基础是 token 对应的特征向量。

本文开源代码可见我的 Github 仓库

[https://github.com/listenzcc/learn-tokenizer](https://github.com/listenzcc/learn-tokenizer)

## Vedo 的体积点云计算

Vedo 是很好用的 3D 点云操作工具，本文使用该工具进行体积点云的初步计算。

## 三维大脑展示页面

本文是介绍大脑标准模板的一站式展示工具。

不用装任何软件，打开网页即可。

我很奇怪，都2022年了，竟然还没有人做这个事情。

[Brain Atlas Gallery](https://observablehq.com/@listenzcc/brain-atlas-gallery)

## Vscode更新不当人啦

Linux很稳定，但稳定是有代价的。Vscode很好用，但好用也是有代价的。今天Vscode升级了，导致好用的V不再支持过老的L。好在我会一点IT，经过一番折腾，老机器还能暂时绕开它。

## We are So Strong

As a whole.

## WebSocket 实用记录

手头的项目需要用到 WebSocket。

你敢相信吗，这个破玩意的通信功能已经集合了 HTTP，WebSocket 和 Parallel Ports，诚可谓五毒俱全。

本文将记录使用 WebSocket 的一些实用方案，比如如何建立和测试连接，如何判断失联并实现重联等。

## Websocket 通信的方法取舍

本文设想了两种 websocket 使用场景，一种是面向低延时的单路串行场景；另一种是面向大吞吐量的多路并行场景。针对两种场景分别设计了 websocket 服务和客户端对，并进行通信实验。

实验结果表明多路并行方法吞吐量更大，但延时稍不可控；而单路串行方法准时性强，但数据阻塞现象严重。两种方法各有所长，使用时应根据具体要求，因地制宜地进行选择。

开源代码可见我的 github 仓库

[https://github.com/listenzcc/websocket-speed-test](https://github.com/listenzcc/websocket-speed-test)

## Websocket 的极简后端

在对连接不敏感的情况下，Websocket 能够给 Web 后端开发带来极其轻便的开发体验。

## 今天你过得如何

今天可是个大日子。
因为现在地球上大概有7,975,447,402，这么多人。
其中，今年出生的有55,713,877，这么多人。
很值得庆祝，不是吗？

所以你，
70多亿分之一，
今天过得怎么样？

## js实现自省的简易语法

本文继续解释 js 的递归启动器，将前文未言尽的部分补齐。

[https://observablehq.com/@listenzcc/recursive-i](https://observablehq.com/@listenzcc/recursive-i)

## notion和飞书

## 一切皆文件：强化学习的 Xorg 虚拟环境

对于任意一个文件，在权限范围内的任何人都可以读取和分享它，这是代码开源的基础。

LINUX 系统的过人之处在于它将全部系统行为都和可分享的文件绑定，操作文件即等同于操作系统功能。

为强化学习搭建 Xorg 虚拟环境的过程，深化了我对这一哲学设计的理解。

## 一次清除挖矿脚本的工作

恶意脚本和 Rootkits 的设计目标是隐匿其存在，因此检测和清除它们通常需要综合的方法。在实践中，与网络活动结合使用其他检测和防御工具是至关重要的。

## 一种实用的chatgpt主从框架

该系统框架通过主从架构解决了小型团队在使用ChatGPT类工具时的难题。服务端主机负责用户鉴权、提供界面和消息分发，而从属机通过长连接处理消息，格式化并向互联网服务商发送请求，保障统一身份和数据安全。该异步通信机制支持负载均衡，同时隔离了主机和梯子，提高了系统可维护性，有效解决了团队内部信息共享和安全问题。

## 一种面向脑电信号包的无损压缩思路

脑电信号一般具有较高的采样率，因此在实时系统中，如何对它进行快速传输是比较棘手的问题。

本文提供了一个高效的、轻量化的压缩思路，能够在信号源头减少传输开销。

## 三维场的体渲染样例

将大脑的MRI-T1像视为标量场，并使用`yt`进行3D体积渲染，提供了一种将这些医学影像数据转化为连续变化场的方法。这种处理方式不仅允许从多个角度和深度全面理解大脑结构，而且通过半透明的可视化手段，有助于呈现大脑内部复杂的褶皱和结构。

## 不仅仅是播放器

大家都熟悉播放器，它可以把视频播放出来。

但抖音模式的播放没有任何价值，因为它只是放了一遍，却没有任何东西留下来。

我想要是功能更多一点的播放器，比如看到好玩的东西可以把它们留下来，然后自动生成一份报告，方便以后查看。

但这个功能市面上好像是没有，于是我就自己做了一个。


所以它并不是一个简单的播放器，
而是一个电影写作器，
它可以你在看电影的同时，
自动生成一份摘要。
这个摘要是图文并茂的，
之后你无须再看电影，
就可以回顾起当时的感觉。
当然也方便分享。

## 不同源的 MRI 数据点阵匹配

假设我们已经通过技术手段完成了 MRI 数据到标准模板的头动校正，但这并不能保证新数据与标准模板是同源的。为了解决该问题本文介绍快速配准的算法原理，该方法能够对不同源的 MRI 数据点阵进行匹配。

## 两个bug合体成一个feature

这个事情非常有趣。想象你是我，你改变了解码器的某个功能，但重启程序后发现这个新功能并没有实装。这时你开始怀疑一切，直到某个偶然的机会，你发现了一条看上去无关的进程占用了本应该释放的那个端口，你恍然大悟，原来解码服务一直驻留在系统中，已经守候了超过几个月的时间。

## 中日颜色风格

这两网站是配色苦手的福音。

## 习惯数据库之MongoDB

本文记录了使用 MongoDB 实现日常信息汇总的程序样例，和我对数据库的一些碎碎念。

## 从 canvas 的角度理解图形程序

本文开始涉及具体问题，从 canvas 的角度理解如下三个问题

1. 高速准实时信号采集过程中（如 EEG 信号），如何完成信号的实时显示、处理和反馈？
2. 为什么“过高”的显示器刷新率可能导致系统准时性变差？
3. 在有图形的界面中，如何使“图形”与用户进行交互？

## 从南桥的角度理解 Vision Pro 的 R1 芯片

我们日常使用的计算机，它不仅有更漂亮的屏幕和更轻薄的机身，它的结构也一直在进化，只不过是在普通人不太关注的领域。比如，Vision Pro 的 R1 芯片就可以理解成一种高级南桥。

同时这个设备也表明，经典的计算机结构需要进行一定程度的异化，才能适应新一代智能硬件的需求。

## 从易用性的角度理解Python的装饰器

最近使用fastapi写小项目，它的易用性非常棒，很多功能非常具有启发性。本文做一简要记录。

## 从最优传输的角度理解信号耦合

通过将观测到的信号与对应的边缘分布相匹配，我们可以解释为何两个信号之间存在着复杂的相互作用。每一种概率密度函数的形式代表一种可能的耦合方式，而最优传输问题的求解则提供了一种方法来探索这些可能性之间的变化。简而言之，最优传输框架允许我们通过寻找使得边缘分布相匹配的概率密度函数，来探索和理解信号之间复杂的相互作用和耦合机制。

## 信号加窗方法：不同的窗参数对PSD的影响

在处理实际信号时，除了加窗以减少频谱泄露外，对信号进行切分（segmentation）并对切分后的各段信号求取平均的PSD也是一种重要的技术，以进一步提高PSD估计的准确性和可靠性。计算结果表明，信号切分后的平均PSD不仅受到不同窗形状的影响，即使在相同窗函数下，也受到不同参数的影响。从分析结果中，我们可以观察到不同窗函数和不同窗参数对PSD的影响。特别是，通过比较hann窗和hamming窗以及不同重叠度（overlap）的hann窗，我们可以看到窗函数的选择和参数设置对PSD的计算结果有显著影响。

## 信号加窗方法：各种窗函数及其功率谱

窗函数在信号处理中用于减少频谱泄露。矩形窗提供最高的频率分辨率但泄露最大。汉宁窗和汉明窗通过平滑边缘减少泄露，后者旁瓣衰减更佳。Barthann窗结合了Bartlett和Hann窗的优点，提供平滑过渡和快速旁瓣衰减。Cosine窗以简单的余弦形状减少泄露，旁瓣低但主瓣略宽。选择窗函数需平衡频率分辨率与旁瓣抑制需求。

本文展示了几种经典窗函数的形状和功率谱，这也是一个实用工具，可以选择多种窗函数进行展示。

[Windowed Function as The Preprocessing of Discrete Fourier Transform](https://observablehq.com/@listenzcc/windowed-function-as-the-preprocessing-of-discrete-fourie)

## 借助深度估计的点云场景重建

所谓身怀利器，X心自起。

当你手上有 GPU 服务器的时候，总会想用它来弄点东西。

这次的东西就是借助深度估计网络的点云生成的尝试。

## 冷

一场秋雨一场凉，一到十月特别冷。
于是我开发了一个 `IPython` 笔记本，
它能够实时获取一个气象数据网站上的历史气温数据，
并以合适的方式把它们绘制出来。

看历史温度图，我们或许就能够解释为啥九、十月份时，体感会这么冷。
其实很简单，

> 在时间进入九、十月的这一段时间，
> 气温在经历了`8`个月的上升之后，
> 首次开始下降。

另一个问题，今年比往年“热”或“冷”吗？

> 数据告诉我们每年的气温基本上都差不多，
> 那些说往年并不如此的言论，
> 就是十足的“活在当下”而已。

## 功能连接分析

功能连接（Functional Connectivity Analysis）分析是认知神经科学重要的分析方法。

> 它是研究各个体素、各个体素之间”共变“关系的重要计算工具。

何为共变关系以及如何对它进行度量，就是功能连接分析的重要课题。

更进一步地，共变关系可以解决什么问题，以及如何利用这些共变特性，就是另外的故事了。

## 功能连接可视化

本文介绍另一个大脑功能可视化工具，还是不用装任何软件，打开网页即可。

要说明的是目前的版本是一个半成品，更完整一点的工具应该是与之前的工具产生联动的一个玩意。

[https://observablehq.com/@listenzcc/functional-connectivity-explorer](https://observablehq.com/@listenzcc/functional-connectivity-explorer)

## 双目视觉

双目视觉是立体感知的重要途径。
然而，从双目视觉的原理来看，
也许，我们所认为自己所“看到”的图像或场景，
其实都是脑补出来的。
当然，本文也可以看作是自动景深算法的一个粗糙实现。

## 和光同尘

人眼观测到的是现象，而背后的逻辑可能比看上去要简单许多。
比如，光沿直线传播。

## 图像分割

这是一个最近做的东西的副产品。
能够实现按照图像的自动分割。

## 图像加窗对二维FFT带来的改进

图像加窗能够对二维FFT带来改进。通过对图像施加合理的窗函数，可以提高图像频谱的信噪比，减小二维FFT结果中的噪声影响。具体表现为窗函数的应用有助于减小图像边缘跳变引起的噪声，增强特征频率成分，并扩大二维FFT结果的动态范围。对于自然图像，窗函数也有助于减小噪声影响，增强高频信息。

## 图像缩放工具

本例提供了一个批量图像缩放工具，用于指定目录下的图像统一缩放。
源码可见[GITHUB](https://github.com/listenzcc/resizeImages "GITHUB")

## 天气热不热，取决于记性好不好

人往往囿于眼前的苦难，却淡忘过往的悲伤。

就好像每年都在说“今年天气热，胜过往年”。

## 如何安装一个机械臂

这是一篇极其无聊的工作记录。
它涉及如何固定一个机械臂，让它在固定的平台上安全地自由运动。

## 封装的方法不一定更优

本文比较无聊，是针对 javascript 语言中的 flatMap 和自定义的 for-loop 方法进行速度比较，比较结果表明，其封装的 flatMap 方法在速度上略差于自定义的 for-loop。这说明虽然 javascript 脚本执行效率已经很高，但仍具有较大的优化空间。

本文代码可见我的前端笔记本

[Compare speed between .flatMap and for-loop in javascript](https://observablehq.com/@listenzcc/compare-speed-between-flatmap-and-for-loop-in-javascript)

## 小作坊实验室的简易 GPU 集群

这是一些我觉得使用计算机的研究生应该知道，但从日常交流看来，我又不知道大家知道不知道的事情。

## 小程序开发记录

微信小程序是基于微信的独特交互方式，

> **小程序简介**
>
> 小程序是一种全新的连接用户与服务的方式，它可以在微信内被便捷地获取和传播，同时具有出色的使用体验。

鉴于微信生态在中国的巨大体量，可以这样说，它是任何工作走向大众、走向互联网的不可或缺的一环。

本文是这样一个记录，是我这样一个互联网门外汉，试图了解其开发方式所做的一些尝试和分享。恰恰是因为我对这个领域什么不都懂，所以可能会闹一些笑话，写出一些不太专业的描述，不是用各种专业名词，而是用自己的语言和逻辑对其中涉及的概念进行一定程度的抽象和归并。

当然，我还是希望最终呈现出来的逻辑是简明和自洽的，并且希望对读者您是有些用的。

## 干点正事

了解一个领域最快捷的方式就是读文献。

本文借助`Scopus`和`VOSViewer`两个工具联合来帮你捋清文献的脉络。

## 异步程序设计中的“同步”机制

在现代的软件设计中，异步编程模型变得越来越重要，特别是在处理网络通信、并发操作和用户界面响应等方面。异步操作可以提高程序的性能、可扩展性和用户体验。

然而，与人交互的程序就需要有一些同步的特点。这就要求程序能够“等待”某些操作完成之后才能进行下一个步骤。在异步场景中，有两种常见的临时同步策略，分别是**通过异步等待实现同步和通过可控启停实现同步。**

## 快速序列视觉呈现

快速序列视觉呈现是很折磨人的脑-机接口实验范式。
它拖着一串问题，是视频编码算法的天敌。

## 房贷那点事

如果你背上了房贷，那么是否应该提前还呢？这是个问题，但没有答案。

不过分析这个事情是挺有意思的，因为我得出了一个挺有意思的事实，那就是你越有钱，你使用钱的自由越大（比如不着急用它归还银行贷款），在一段长时间之后，你的财富就越多。相反，如果你被贷款追着跑，那么就要背负庞大的债务。所谓富的越来越富，穷的越来越穷是也。

## 数据库MySQL

本文将记录一些 MySQL 数据库的使用方式。

## 最优传输在图像颜色映射的应用

最优传输（Optimal Transport，OT）理论在图像颜色映射或颜色转移方面有着广泛的应用。最优传输问题的目标是在最小化某种成本（例如，移动颜色分布中每个颜色到目标颜色分布的“距离”）的情况下，找到一个从一个颜色分布映射到另一个颜色分布的最优方案。这在图像处理领域尤其有用，因为它可以用于在不同图像之间转移颜色风格，使得源图像在保持其原始结构的同时，采用目标图像的颜色风格。

[https://github.com/listenzcc/optimal-transport](https://github.com/listenzcc/optimal-transport)

## 有一种见微知著的美

众所周知，统计分析是挖掘数据特性的科学方法。面对他们明明清楚地知道，但就是不想告诉你的信息，统计分析就成了满足好奇心的完美手段。比如，有人通过遗嘱登记的增加量分析出了某场大规模现代战争一方的阵亡士兵和他们大致来源。统计结果做得非常漂亮，值得学习和记录下来。

## 机场的密度分布

能一飞冲天的东西，我们叫做飞机。
本位文对世界范围内的机场分布的密度图进行估计和可视化。
结果表明，我国配不上所谓的“基建狂魔”的称号，
甚至可以说，扩大内需没有尽头，大国工匠大有可为。

## FSL 的核磁数据配准方法

本文对 FSL 软件的配准方式进行说明，并提供一个实用脚本，用于将数据转换到标准空间

## 永远干不完的工作

之前做了一个​面向视频的整理工具，
[不仅仅是播放器](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485688&idx=1&sn=d7b4ff708ab4587910bf7e0089066798&chksm=c16343fdf614caebda9e81c5777f31c609509ab6b517f235724e9e66afd40d9ac0c6e600bfbf&token=1683679924&lang=zh_CN#rd "不仅仅是播放器")。

但转念想想，
这个思路用来整理琐碎的调研工作似乎更合适。

## 深度网络与大脑区域的 RDM 度量

本文使用的 RDM 方法用于度量神经网络不同层次与大脑不同脑区之间的相似性。对简单图像的分析表明，在图像出现时的脑响应与神经网络最为相似，之后随时间递减。但对复杂图像的分析表明，它随时间变化呈现先低后高，单调上升的趋势。这是与简单图像相反的。

## 狭义相对论的简单图解

偶然看到一个狭义相对论的简单图解，很有意思

## 用激活函数“纠正”脑电数据

这是使脑电数据“看上去”正常的一个方法，但它的安全性我还没有考察。

本文的目的是开一个头，要追究的问题是“神经网络是如何看待和处理脑电数据的”，于是首当其冲的就是激活函数对信号的变换原理。本文只阐述现象，原理等我弄明白再补充。

## 神经网络的表达能力

人工神经网络是近年来火热的模式识别算法，
在计算机视觉领域应用广泛。

本文是一个例子，
表明如何使用一个结构异常简单的神经网络，
在随机参数的情况下，
对一只兔子进行剖析。

可以看到，
如此简单的神经网络，
即使未经训练，也具有表达兔子各个部位的能力。

至于如何对它进行训练和优化，则是另一个问题。

## 科学还贷

本文是对提前还贷是否合算的科学计算。

我首先假设了绝对公平的比较方法，比较了提前还贷与否，在 25 年后造成的盈亏。如果你选择按月还款，你需要向银行支付 88 或 76 万元；如果你选择提前还款，你需要向银行支付 33 或 29 万元。

之后，对有些不尽人情的假设进行修正，因为没有人会为了不存在的月供利息压力，而把钱按月放在银行里存着。这样算下来，如果按当期来说，提前还款只能省下 5 到 6 万元，因为明天的钱没有今天值钱。

## 立体渲染

要渲染一个立体结构，除了将它解析成表面之外，还可以通过体渲染的方式来解决问题。

## 简易文档

文档是良好组织的富文本信息，能够携带大量有意义的信息。

现代科技让文档的排版和传播变得异常简单。

## 简洁带来的麻烦

`Python`是十分简洁的计算机语言，但是简洁会不避免地带来歧义。
这些歧义则会导致一些麻烦。

## 粗看ERD和ERS

ERD和ERS是信号随机叠加的两种不同的现象，
它们的差异更多地是体现在叠加的波形上，
而在它们的幅度上，不容易看到较大的差异。

## 纹理增强

由于上述图像过于“模糊糊”，因此尝试使用“空间滤波”的方式进行纹理增强。

人生如树花同发，随风而堕。自有拂帘幌坠于茵席之上，自有关篱墙落于粪溷之中。坠茵席者，殿下是也。落粪溷者，下官是也。贵贱虽复殊途，因果竟在何处？

## 线性模型的实例之一

线性模型是解析观测变量的有效手段。
但它实在是太庞大了，所以只能蚂蚁式的、慢慢地啃下来。

## 股价预测

本文是使用**机器学习**方法对股票价格进行预测的实用方法。

但如果想用它来赚钱，
猜猜你会赔多少？

## 脑成像数据的标准空间

脑成像设备和数据都需要进行一定程度的标准化才能进行后续分析。
本文是对其基本概念的一些介绍。

## 脑电地形图绘制

我对电极位置进行$\mathbb R^3 \rightarrow \mathbb R^2$的映射。在新的二维平面坐标系中，电极之间的距离与三维空间中的距离“相似”。这也是我们常见的脑地形图电极位置的由来。所谓连续地形图是将脑电电极在离散空间位置采集到的电动势数值，以空间连续的方式呈现出来的方法。本文使用plot@observable绘图工具进行连续地形图的绘制。

## 脑电溯源方法简述（I）

信号溯源是一种通过记录头皮表面的电信号或磁场，反推回大脑活动源头的方法。首先，需在被试者头部安置电极或磁力传感器以采集信号。接着，建立头部模型描述头部几何形状和组织特性。逆问题求解方法用于将头皮信号反推回源头，确定大脑中活动的具体位置。最后，通过在三维脑模型上显示结果，展示活动源的位置。信号溯源提供了有关大脑活动的空间定位信息，有助于研究特定神经活动发生的脑区。联合信号溯源和头皮脑电等技术可以为神经科学研究提供全面的信息。这一方法对于理解认知、感知、运动控制等大脑功能具有重要意义。

本文通过 jupyter 笔记本用最简单的方法实现了脑电溯源，详见我的 github repo。

[eeg-source-analysis](https://listenzcc.github.io/eeg-source-analysis/ "eeg-source-analysis")

## 脑电点电荷假设的前向模型

前文展示了脑电电极位置，以及它们与大脑标准模板中神经元之间的位置关系。本文假定这些神经元是点电荷的情况下，当它们的值随机连续变化时，脑电电极会采集到怎样的电位信息。本文代码可见我的Github仓库

[https://github.com/listenzcc/where-are-the-eeg-sensors](https://github.com/listenzcc/where-are-the-eeg-sensors)

## 脑磁图的探头位置坐标说明

本文对脑磁图的探头位置坐标及其提取和干预方式进行简单说明。

## 英文苦手

作为英文苦手，
语法几乎是遥不可及的玩意，
从来就没有弄明白过。
但也许可视化的方法可以帮助解决这个问题。

## 莫须有的两种 RDM

这是我要求 AI 撰写 RDM 时它给我的两个答案，而我之前并不知道 Relative Dissimilar Matrix 是个什么东西，我想 AI 也不知道。所以说，使用 AI 的时候还要十分小心。当然，Reprensentational Dissimilarity Matrix 还是靠谱的。

## 蒙特卡洛方法

蒙特卡洛（Monte Carlo）方法是一种无奈，
却高效的遍历方法。
本文是该方法的一个样例。

## 视角渲染

不同的视角下看到同一个东西通常会得到不同的图像。我就搭建了这样一个场景，即模拟高空俯瞰一小片陆地的场景。

这算是一个框架上的尝试，它是在渲染过程中，尝试对同一个三维场景进行多次渲染。

## 计时精度

都说`LINUX`比`WINDOWS`操作系统更适合做工程开发，
这也许是谣言，
但绝非空穴来风，
本文就是一例。

设想一个典型场景，
你需要让计算机每隔一段时间做一件事情，
比如显示一张图片什么的，
那么就要用到计时器。

当这段时间短到毫秒级的时候，
问题就来了。

## 计算机图形编程的设计理念：Canvas 和 SVG 的理念（1）

最近继续出差，可以写些内容。编程工具也并不趁手，所以就干写写吧。

## 让 Python 更好用，OmegaConf

问：写一套好用的程序分几部？

答：分三步！第一步是功能抽象，第二步是为功能配置参数，第三步是让这些参数跑起来。

感谢 OmegaConf 提供的配置项解决方案，它能够让第二步走得更加容易。

本文的详细说明可见我的 Github 文档库

[https://github.com/listenzcc/better-config.git](https://github.com/listenzcc/better-config.git)

## 让 python 更快一点

本文要解决的问题是如何在 Python 环境下，在 100 毫秒之内稳定处理随机的大量 4k （$3840 \times2160$）图像线性运算。由于图像信息具有特殊性，我们通过并行计算和GPU加速的方式进行优化。本文对这两种加速方法都进行尝试，实验结果表明，Python加速的有效手段并非并行计算，而是装到GPU中进行计算，加速效果可以达到 $2$ 倍。

接下来，我决定再进一步，将数据全部放入 GPU 中进行计算，省去临时装载和读取的开销，实验结果如下图中 cuda 所示。这样做的加速效果可以达到 $200 \sim 1200$ 倍不等，但计算负荷越高则加速效果越差。

本文开源代码可见我的 Github 仓库
[python-speed-validation](https://github.com/listenzcc/python-speed-validation)

## 记 python 与 LINUX 的 Xorg 配置交互

本文的目的是使用 python 与 linux 的 lspci 命令进行交互，将交互结果交给 Xorg，用来搭建可用的 display。本文的开源代码可见我的 Github 仓库

[https://github.com/listenzcc/python-with-linux-xorg](https://github.com/listenzcc/python-with-linux-xorg)

## 记MLP的一次回归失败

多层感知机（MLP）是常用的神经网络结构，在数学上证明它可以用来表达几乎全部连续函数。

但由于函数的复杂性和训练算法设计的不足，它有时候并不能很好地完成给定的任务。

本文是记录一次用 MLP 进行回归的失败尝试，代码可见我的 GITHUB 仓库

[https://github.com/listenzcc/MLP-notebook](https://github.com/listenzcc/MLP-notebook "https://github.com/listenzcc/MLP-notebook")

## 语法分析（Online）

本文是前文《[英文苦手](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485066&idx=1&sn=486594ad89329b0a2f7e4de408a3c7f2&chksm=c1634d8ff614c499a753ee3c6423c6cc541a3eb8709a242bda55ac1d44602fed0b31a54675fc&token=537192075&lang=zh_CN#rd "英文苦手")》的前端实现方案。
主要解决两个问题，分别是
- 前端词性快速解析；
- 基于词性标签的文档可视化。

## 转移矩阵-1

这两天没有稳定的网络可用，也没有完整的编程环境，所以只能看看无聊的小东西。比如“**一个人扔六面的骰子，数值1到6，扔到几就向前走几格，可以无限扔，问他恰好走到第2023格的概率是多少?**”

## 转移矩阵-2

接着前文定义的转移矩阵，经过简单的计算可知它是满秩矩阵，且最大的特征值的模为 1，其他特征值的模均小于 1。因此，它是马尔可夫过程的转移矩阵。虽然收敛值可以计算得到，但似乎可以通过观察得到一种快速计算收敛值的等式，但我还是没想好如何证明它。

[Matrix production](https://observablehq.com/@listenzcc/matrix-production)

## 转移矩阵-3

由于这两天的东西比较水，所以写两个事情。

首先，前文中猜想的那个命题根本没有道理，这类矩阵也没有那么复杂，它就是典型的“右随机矩阵”。这类矩阵具有良好的性质，它最大特征值为实数 1，且对应的特征向量为全 1 向量，另外，其他特征值的模总小于 1，这导致它的连乘总收敛于全 1 向量。这种良好的性质是我之前产生误会的根源。这部分的随机值样例可见开源代码

[Right Stochastic Matrix](https://observablehq.com/@listenzcc/right-stochastic-matrix)

其次是除了说明这种现象之外，本文还尝试使用 vscode 中的 sourcery 插件进行代码分析，它可以自动理解代码、生成高质量的文档和测试用例。本文附录部分的全部内容都是由它自动生成的。我只是调整了一下格式。

[Sourcery | Automatically Improve Code Quality](https://sourcery.ai/)

也因为这个原因，本文的内容以英文为主，因为在 vim 模式中切换输入法实在是很不方便。本文的详细代码可见我的 github 仓库

[https://github.com/listenzcc/stochastic-matrix](https://github.com/listenzcc/stochastic-matrix)

## 运动轨迹分析

这是一个纯工程的方法，
尝试解决多轴连动的运动参数与终点轨迹之间的关系。

## 递归启动器

递归的逻辑很简单，不是左脚踩右脚的虚无飘渺，而是不使用相同方法的不断挖掘。因此，只要规定了启动方向和边界条件，递归就能顺利进行。

[https://observablehq.com/@listenzcc/recursive-i](https://observablehq.com/@listenzcc/recursive-i)

## 马斯克口中的第一原则-first principle

端午安康，等等……，康，康德的康？

今天放假，我看了几个鸡血视频。承蒙大数据的关照，这些视频以 Elon Musk 的采访为主。他反复强调 first principle 这概念。

我想我能用康德提到的分析和综合判断对它进行解释，即**第一原则既是分析判断的结果，也是综合判断的起点。**也能用休谟的观点进行解释，**它是我们对过去经验的总结和概括，用来指导我们对新的情境和问题的理解和解决。**二者并不冲突，也许这种方法论就叫唯物主义。

## 魑魅魍魉

互联网世界中的奇奇怪怪的符号通常是用 Unicode 符号表达的，因此，我做了一个 Unicode 符号的速查表，来看看奇怪字符的奇怪表达。

欢迎访问我的
[Github 主页](https://listenzcc.github.io/home-page-2/unicodes/ "Github 主页")

## 鸡同鸭讲的 BUG

Python-opencv 遇到了一个中文支持的 BUG，它不能读取目录中带有中文的图像文件。

这背后的原因是编码和解码过程不一致所导致的乱码现象。

# Traffic Analysis

The Topic is about Analysis the Traffic Situations.

The folder contains following md files:

---
## MBS的负凸性

数学是一门严谨的学问，它里面有公理、有定理和推论。同样和数字有关的还有经济，也就是钱，但钱不怎么讲道理，即使负凸性是个描述函数趋势的概念，当它和经济上的 MBS 结合起来时，后者表现出来的负凸性却不是因为它服从数学定理，而是理性经济人的可预测行为的统计结果。

## 以空间换时间

为了解决《私人订制》一文中遇到的，由于计算规模扩大所导致的，
寻路计算负担问题。
我们将从寻路算法的原理出发，对动态规划算法进行改进。

## 学而不思则罔

这是解决寻路问题代码的最后一篇，尝试让算法再快一点。
天知道我在贪婪算法上已经水了多少天。
水日常到此为止。

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

## 私人订制

为解决上文《贪婪算法及其困境》中遇到的困难。
我们在本文中对算法进行改进，从而使其能够用来解决一般性的“寻路”问题。

## 行路难

过分追求全局最优会降低局部效率。
那么这种情况有多严重呢？本文是基于图分析对该问题进行量化。
通过分析，我们可以看到以下现象，

1. 全局最优解往往会陷于路径依赖困境；
2. 可以通过极少的“捷径”开销，提升总体效率；
3. 但全局最优往往已然促成“天然垄断”；
4. 总体效率的提升会造成“垄断”权益的稀释，从而受到阻碍。

虽然修建捷径是利国利民的好事，但会损害天然垄断的利益。
不难想见，垄断权益受到损害的体量，就是修建捷径的成本。
其值甚至与社会总收益相当，甚至可能产生“投鼠忌器”级别的阻力。
所谓“行路难”是也。

## 贪婪算法及其困境

本文将详述形成最小连通图的贪婪算法。
在此基础上，我们才能说明捷径加入之后，原始算法是如何失效的。
从而解决《改出路径依赖》一文所提出的问题。

# Transformer

The workshop in learning transformer

The folder contains following md files:

---## SORA的盲人摸象

从目前的消息来看，SORA是一个先进的视频生成模型，它通过变分自编码器（VAE）将视频编码为隐空间中的时空patches，然后利用基于Transformer的扩散模型对这些patches进行操作，以生成高质量的长视频内容。

[Video generation models as world simulators](https://openai.com/research/video-generation-models-as-world-simulators)

## 如何教会transformer生成文本

什么是大模型？我想，至少在在2024年初，我可以简单地说：使用transformer的模型就是大模型。

本文尝试开一个新坑，简述我对transformer网络结构的理解，并且尝试说明它是如何进行文本和图像处理的。

[https://github.com/listenzcc/learn-ViT](https://github.com/listenzcc/learn-ViT)

# WebApp

记录一个基于 Python 的 Webapp 的开发过程。

---## Fastapi + tailwindcss = 各司其职

最近要写个功能稍微复杂的 APP，所以需要搭微型网络服务。出于好奇，我选择了时下流行的 fastapi 作为后台；选择了 tailwindcss 让我的 APP 免得过于难看。本系统将逐步记录开发过程。

本文的主旨在于澄清一个误会。由于以上两个框架都较为流行，因此不免存在大量的网络文档试图将它们结合在一块来讲。但我觉得似乎并无必要：因为它们干的是不同的事情，让它们各司其职就好，二者不应该有太多的交互。

本系列对应的开源代码位于我的 Github 仓库

[https://github.com/listenzcc/eeg-for-everyone](https://github.com/listenzcc/eeg-for-everyone)

## 曼德尔球的渲染及简要原理

曼德尔球（Mandelbulb）是一个神奇的分型数学结构，我可以使用 Three.js 方便地渲染它。由于 ObservableHQ 不支持必要的插件，因此我将源码挂在了 github 的 page 上。

[https://github.com/listenzcc/mandelbulb-in-three](https://github.com/listenzcc/mandelbulb-in-three)

## 脑电电极在哪里

本文将三个东西画在一起，它们分别是果冻形式的大脑、脑内功能区的代表性节点和标准配列的脑电电极。它展示了脑电电极如何将大脑包裹起来。代码托管在了 Github 的代码仓库。

[https://github.com/listenzcc/where-are-the-eeg-sensors](https://github.com/listenzcc/where-are-the-eeg-sensors)

# Learning WebGL

Learn WebGL in Baby's steps.

---
## Hessian 与梯度结合

本文讲述了利用 Hessian 提供的二阶信息确定梯度下降最优步长的方法，这种梯度下降法只进行了 10 次迭代即可找到极小值，这说明该方法大大提高了寻优效率，并且有机会跳出局部最优值，受起始点影响更小。

本文代码还是在我的 ObservableHQ 笔记本上。

[Searching maximum by Hessian (Improve)](https://observablehq.com/@listenzcc/searching-maximum-by-hessian-improve)

## Hessian 粗解

Newton 法是一种迭代优化算法，用于求解非线性优化问题。它利用目标函数的二阶导数信息（Hessian 矩阵）来进行迭代，以更快地收敛到局部最小值。尽管 Newton 法在很多情况下具有快速收敛的特性，但也存在一些问题，其中之一是它的稳定性可能较差，也更容易陷入鞍点。

本文将其与梯度方法进行平行对比，开源代码可见我的 ObservableHQ 笔记本

[Searching maximum by Hessian](https://observablehq.com/@listenzcc/searching-maximum-by-hessian)

## REGL 简化了 WebGL 的什么？

WebGL 这类工具的学习曲线较为陡峭，因为它虽然工作在 javascript 上，但渲染过程中却会直接用到 C 代码。这样做的原因是由于它在渲染的实现过程中，需要用户自己定义每个 shader 的渲染行为。WebGL 的渲染过程是严格规范化的过程，因此 REGL 对它进行了包装。用户只需要调用这样的函数即可实现渲染。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## REGL提供的上下文机制

阅读regl源码的时候看到一个非常有趣的机制。在regl.frame中，可以通过上下文迭代的机制实现varying变量的复用，从代码中可以看到，这个变量是透过函数调用传递下去的。这好像是一种闭包机制，非常好用。它可以保证vert中变量的一致性，有效减少开发成本。

[Game of Life](https://observablehq.com/@listenzcc/game-of-life)

## SDF中有趣的几何问题

最近在看SDF（****Sign Distance Function****），但没看懂，不过发现了一些有意思的边角东西。我在学习SDF的过程中遇到它GeoGebra，更准确地讲，我是在学习如何绘制正五边形的SDF时遇到它的。再进一步讲，在绘制正五边形的SDF时，为了避免SHADER过于复杂，需要将任意位置的点映射到正五边形中的某个三角形中。在前人的经验中，这种映射“总是”能通过有限次的“翻转”来做到，而对于正五边形来说，翻转的次数不超过四次。

## SDF在WebGL中的实现：以三角为例

本文以三角为例，在WebGL中实现SDF计算和实时渲染。

[SDF in WebGL](https://observablehq.com/@listenzcc/sdf-in-webgl)

## WebGL 中 buffer 的进一步理解

借用出差的间隙想了 4 天，我似乎把 buffer 这个东西想明白了一些。但由于出差过程中实在摸不着电脑，所以基本上属于闭门造车。 但是万幸的是，从效果上看，我的理解似乎没什么大问题。

感兴趣的话可以留意我的开源代码

[Image histogram using the buffer in WebGL (II)](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl-ii)

## WebGL 初涉 buffer：像素的颜色直方图

本文利用 WebGL 的 buffer 机制实现了图像的像素级颜色直方图绘制，虽然能实现功能，但我仍然没有弄透这个东西。

[Image histogram using the buffer in WebGL](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl)

## WebGL 实现线积分卷积（1）：framebuffer 基础

在现代图形编程中，Framebuffer 更常指代图形硬件或 API 中的一个对象，用于存储图像的像素数据。Framebuffer 可以包含颜色缓冲区、深度缓冲区、模板缓冲区等。在渲染流水线中，图形数据首先渲染到帧缓冲区，然后再传递到屏幕。通过反复渲染到不同的帧缓冲对象，可以实现图像像素的累积效果，达到一种积分计算的效果。这种技术在一些图形效果和计算中经常被使用，例如模糊效果、光照效果等。

代码可见我的 ObservableHQ 笔记本。

[Accumulate in the framebuffer](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer)

## WebGL 实现线积分卷积（2）

本文使用 WebGL 实现了线积分的基本前序功能。在迭代中，我使用局部梯度 $dFdx, dFdy$ 更新点的位置，让它沿梯度方向向下运动。并且采取了采用了双 framebuffer 耦合的方法，避免点的痕迹造成的影响。

本文的开源代码可见我的 ObservableHQ 笔记本

[Accumulate in the framebuffer (II)](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer-ii)

## WebGL 实现线积分卷积（3）：改变像素形态

前文实现了像素点沿梯度方向的移动，并且能够实时绘制它们。这距离实现线积分卷积的绘制还有一步之遥，那就是如何画线。具体来说是”如何改变像素形态，实现将像素绘制成成小线段“的功能。

功能代码可见我的 ObservableHQ 笔记本

[WebGL pixel shape](https://observablehq.com/@listenzcc/webgl-pixel-shape)

## WebGL 实现线积分卷积（4）：组合

终于把之前的东西组合起来，形成了完整的线积分渲染程序。开源代码可见我的 ObservableHQ 笔记本

[Accumulate in the framebuffer (III)](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer-iii)

## WebGL 的 texture 入门

缓冲器是 WebGL 的重要组成部分，它用来缓冲一张图像，本文说明它的基本使用逻辑。为了让本文不会过于无聊，本文实现了图像颜色空间的随机化，它保证了在原始图像上连续的颜色在新的颜色空间上还是连续的。又由于随机过程中含有时间变量，因此新的颜色空间是实时变化的。这就形成了一种奇怪的动态效果。得益于 WebGL 的优秀性能，这个过程是实时的，帧率可以达到显示器的刷新率。

[WebGL Texture Usage](https://observablehq.com/@listenzcc/webgl-texture-usage)

## WebGL 的简要入门

优秀的 WebGL 工程代码是开源的，但除了好看之外几乎利用不上。这些没有注释、难以理解其复杂计算过程的代码满天乱飞，乍看起来它们已经足够酷炫和好用，导致继续花时间开发相似的功能就只有成本，但没有意义。而事实是，一旦落实到实际需求上，除了被抄一遍之外，它们无一例外地没有进一步修改的余地。因此，为了让我自己能够在将来的某一天，看得懂、改得动这些代码，我决定开始这个话题。

## WebGL 页面中有用的 IDE 工具

虽然集成开发环境（IDE）这个概念有点大，但在 WebGL 开发和调试过程中，需要用到 C 和 JS 混合编程的技巧，因此顺手的开发工具有助于提升开发效率。
除此之外， 本文提供的样例渲染过程看上去是透过三角碎片观察一个完整的 HSV 调色板。为了强化这个过程，我在图上渲染了一个圆环，它的半径是 $0.3$。这种渲染思路可以解决一些科学绘图问题，这些问题满足如下条件

> 要绘制某个区域内的全部点，而这些点的颜色有解析的表达式，可以表示为 $color = f(x, y)$ 的形式。
> 

[WebGL's Simple Animation & Stats & Code-Prettify](https://observablehq.com/@listenzcc/webgls-template)

## WebGL的framebuffer渲染会受到depthStencil的影响

简单来说，当使用framebuffer交互渲染时，应该关闭dephStencil选项。否则，会导致framebuffer无法按要求更新。这个经验是在绘制多个点的SDF时得到的。

## WebGL绘制球协函数

由于表面与球面对应关系的存在，我们总能用球面建模和绘制的方式进行物体建模和绘制。这是物体表面建模及绘图的基本原理之一。球协函数是三维函数，它可以用极坐标表示。为了说明它与球的对应关系，我对将它与一个球绘制在一起，用球的颜色表示它表面的各个点，用HSL颜色空间表示，其中，Hue表示$\varphi \in (0, 2\pi)$，Lightness表示$\varphi \in (0, \pi)$。绘图的代码可见我的ObservableHQ笔记本。

[Spherical Harmonic](https://observablehq.com/@listenzcc/spherical-harmonic)

## WebGL 面与点的绘制方式对比

绘制一个场景有两种方式，分别是按照面和按照点进行绘制。在 webgl 中，两种模式具有相似的形式。本文解释了两种绘图方式的差异。

[WebGL Template](https://observablehq.com/@listenzcc/webgl-template)

## 三维视角的vert变换

本文用极简的语言说明如何在opengl的语境中实现vert的三维视角变换。再简单一点说，它可以表示为矩阵连乘的计算结果。

## 三角 shader 的重心坐标系

前文遗留了一个问题，那就是如何使用 WebGL 渲染平移不变的三角 shader。本文尝试使用重心坐标系解决这个问题。为了体现重心坐标的意义和作用，我还增加了 wireframe 的线绘制方法。另外，前文的三角形端点移动方法并不令人满意，因此本文更换成 simplex-noise 方法，它使端点的运动看上去更加自然、柔和。

[Barycentric coordinate in WebGL](https://observablehq.com/@listenzcc/barycentric-coordinate-in-webgl)

## 任意三角形的SDF组合与阴影投射

将之前的内容组合起来就得到了这样一个“利用SDF进行实时投影计算”的样例程序。
在我的ObservableHQ开源笔记本可以找到它，

[SDF and Ray Tracing (Dev. III)](https://observablehq.com/@listenzcc/sdf-and-ray-tracing-dev-iii)

## 使用WebGL实现简单的三维交互

本文是纯粹工程实现的用例，它呈现的是低阶球协函数（Spherical Harmonic, SH）的随机叠加，并且这个三维构型可以与观察者进行实时交互。工程的难点有二，一是如何将观察者的MPV（Module, Projection, View）映射（详见前文）与用户在canvas上的鼠标操作联系起来；二是如何将大量的球协函数计算用最高效的方法计算出来，从而实现实时叠加。

## 在 WebGL 上画线：Wireframe

所谓曲线就是两个等值面互相吻合的边缘的点的集合。而 glsl-solid-wireframe 就是通过 WebGL 的微分库实现了这个点集的探测功能。本文试图从连续噪声图中找到等值线，并渲染它们。为了说明点集是如何被探测出来的，我还写了一些有用的数学推导。

开源代码可见我的 ObservableHQ 笔记本

[Contour demo of WebGL & glslify](https://observablehq.com/@listenzcc/contour-demo-of-webgl-glslify)

## 在SDF的基础上绘制光源投影

本文介绍了基于 Signed Distance Field (SDF) 的光源追踪方法。通过动态确定迭代步长，使用 SDF 可以有效地判断光线是否经过物体，并避免了传统方法的采样问题和大量物体信息的输入。另外，还在迭代过程中记录最小 SDF 值用于绘制光线颜色，并展示了样例场景的光线强度图和彩色结果。末尾还附上了追踪的核心代码。

[SDF and Ray Tracing (Dev. II)](https://observablehq.com/@listenzcc/sdf-and-ray-tracing-dev-ii)

## 将任意三角形规范化：简化计算SDF的尝试

由于计算任意三角形SDF的代码显得过于臃肿，所以我想将它简化一下。仅通过一次映射将任意三角形转换为规范的三角形，在这个规范的二维空间中进行近似计算，似乎可以提升代码的简洁性。

[Regular triangle](https://observablehq.com/@listenzcc/regular-triangle)

## 平面在三维中旋转：REGL解决实际问题之一

这是一个平面在三维空间中旋转并通过仿射变换反映在二维空间的问题。通过对平面进行维度扩展和仿射变换的数学建模，介绍了如何处理三维空间中的旋转问题，并尝试从二维空间的信息中反推三维空间的信息。然而，由于信息的不完整性，这个问题成为了一个欠定问题，特别是当只能从二维空间中提取到部分信息时。

为了解决这个问题，采用了REGL进行模拟实验，设计了一个二维矩形在三维空间中的旋转模拟，并记录下角点的位置变化。通过对这些数据进行回归分析，我尝试了解是否可以仅通过仿射变换后的三个角点的二维坐标来推断出第四个角点的二维坐标。实验结果显示，虽然无法准确推测出第四个角点的第三维$z$成分，但如果只关注二维平面内的位置，通过三个角点的信息反推第四个角点的二维坐标是可行的。

实验代码可见：

[Geometry Dim 2 to 3](https://observablehq.com/@listenzcc/geometry-dim-2-to-3)

分析代码可见：

[https://github.com/listenzcc/geometry-dim-2-to-3](https://github.com/listenzcc/geometry-dim-2-to-3)

## 开源，就是随取随用

程序员的生产工具和工作对象是二进制代码，但这是个很扭曲的群体，他们是最不喜欢敲代码的一群人，是能复制粘贴的就绝不多写一个字的一群人。这是把人从工具中解放出来的懒惰，这种极度的懒惰就是开源。

WebGL 的 shader 渲染过程需要“编写” c 代码，由于实现了开源代码的随取随用，我们可以使用 promise 机制临时下载它们。

[Glslify](https://observablehq.com/@listenzcc/glslify)

## 梯度粗解

梯度就是局部效用最大的变化方向。对于给定的标量场，我们总能让某个点沿着它的梯度进行“移动”。移动的过程中，该点的值会不断增加。因此这个过程称为梯度上升。如果将这个场倒过来，那么不断增大的过程会转换成不断减小的过程，这个过程就是“梯度下降”。

开源代码可见我的 ObservableHQ 笔记本

[Searching maximum by gradient ascending](https://observablehq.com/@listenzcc/searching-maximum-by-gradient-ascending)

## 流浪像素：逐像素的微分偏移

本文以前文这基础，在 WebGL 上实现了逐像素的微分偏移，使图像看上去像是在“流动”。

[Image histogram using the buffer in WebGL (III)](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl-iii)

## 离散、连续和插值：WebGL 的 vertex 与 fragment

本篇是对上篇的进一步解释和说明，尝试说明在 WebGL 的渲染过程中，程序是如何处理端点（vertex）和光栅片（fragment）之间的关系。这是一种离散、连续和插值之间的微妙关系，它们的背后是令人叹为观止的优秀工程实现。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## 继续SDF：简单压倒一切

本文尝试一种计算简单，且适用于任意凸多边形SDF计算的快速算法。在这个算法中，对于每条边只需要计算二次内积即可，因此这是一种复杂度为$N$的算法。

[Easy to compute the SDF of triangle](https://observablehq.com/@listenzcc/easy-to-compute-the-sdf-of-triangle)

## 随机三角形的SDF

SDF（Signed Distance Field）是多边形空间中任意点到最近边缘的最短距离标量。通过重心坐标系，类似于三角形Shader的技巧，可实现三维模型的SDF。利用重心坐标化，可在片元着色器中计算距离场，用于绘制三角形边缘，实现视觉效果。

# 时间序列分析

分析时间序列的一些方法和有趣的事情。

---
## 实时序列及其频谱密度

渐出的信号对频谱造成的影响主要体现在它让频谱密度在复空间内旋转起来，旋转的轨迹近似于椭圆。当信号在时间上发生左右横移时，会导致频谱在复空间上发生相应的变化，形成椭圆状的轨迹。这种现象可以通过傅里叶变换的性质来理解。

[FFT Conj. of Running Signals](https://observablehq.com/@listenzcc/fft-conj-of-running-signals)

