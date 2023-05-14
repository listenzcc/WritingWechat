# Dataset

The useful datasets and their codes.

The folder contains following md files:

---
## Dataset

The useful datasets and their codes.

The folder contains following md files:

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

