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

---

- [像上网一样使用FSL](#像上网一样使用fsl)
  - [一般要求](#一般要求)
  - [数据解析](#数据解析)
- [Workshop](#workshop)
- [Developing Diary](#developing-diary)
  - [Code Improvement 1](#code-improvement-1)

### 一般要求

为了满足“像上网一样的使用需求”，
首要条件是实现“数据自由”，
即本工程需要满足一些基本的特性和条件。

1. 数据结构具有扩展性，即使用兼容形式的数据结构记录脑皮层数据；
   本部分可见[代码仓库1](https://github.com/listenzcc/extractFreeSurfer "代码仓库1")

2. 计算协同具有扩展性，即需要兼容多种脑成像数据的分析处理软件；
   本部分可见[代码仓库2](https://github.com/listenzcc/freesurferAnalysisScripts "代码仓库2")

3. 使用场景具有扩展性，即需要使用兼容性强的前端技术，将可视化和简单计算工作放在前端呈现，如有必要，还需要加入云计算的环境支持。
   本部分可见[在线笔记本](https://observablehq.com/@listenzcc/fsaverage-in-freesurfer "在线笔记本")

目前已经有了一个性能还说得过去的，
具有一定功能的可视化前面构架

- 皮层厚度呈现
  ![Cortex Thickness](./cortexThickness.png)

- 激活叠加呈现
  ![Cortex Activities](./cortexActivities.png)

- 多种选项的可交互呈现
  【这是一段棒到不行的视频】

### 数据解析

其中，数据解析是重要的一环，
现将目前的进度直接列写如下。

```md
# Extract FreeSurfer Cortex

The project extracts FreeSurfer cortex into OBJ format.

The OBJ format is general 3D format which is portable to other softwares,
like WebGL, Blender, Unity, ...

## Data Transformation

The visualization of the FreeSurfer Cortex is based on extraction the surface files.
To display the cortex in the surface manner,
there are at least **3** things we need

1. The 3D mesh of the cortex;
2. The feature value for the surface structure, like thickness, curvature, ...;
3. The functional activities across the cortex, which is basically from the other softwares, like `FSL`, `SPM`, ....

The `1st` and `2nd` features can be accessed through the `subjects` folder of the FreeSurfer.
Take the example of `fsaverage`,

1. The 3D mesh file is like `fsaverage/surf/lh.inflated`.
   It is a classic 3D OBJ file, but encoded by the FreeSurfer's private tools.
   It can be decoded as

   ```sh
   # The command converts the left hemisphere cortex into its ascii coded file
   fileName=$FREESURFER_HOME/fsaverage/surf/lh.inflated
   mris_convert $fileName $fileName.asc
   ```

   There are **vertex/positions** and **surface/cells** features in the file.
   The header of the file is like
   ```txt
   # Line1: Description of where the file is converted from
   # Line2: xxxx, yyyy
   #        xxxx refers the count of the vertex
   #        yyyy refers the count of the surface
   ```

2. The feature value specific to every vertex are restored in the files like `fsaverage/surf/lh.thickness`.
   To decode the file, the commands should work

   ```sh
   # The command converts the left hemisphere cortex's thickness values into ascii coded file
   # It requires template file to locate the vertex,
   # and the -C option refers the following file is scalar file.
   fileName=$FREESURFER_HOME/fsaverage/surf/lh.thickness
   tempName=$FREESURFER_HOME/fsaverage/surf/lh.white
   mris_convert -C $fileName $tempName $fileName.asc
   ```

   The values are listed in the file with the format of
   ```txt
   # Line1: 0000 xxxx yyyy zzzz value
   #        0000: The index of the vertex;
   #        xxxx | yyyy | zzzz: The x-, y-, z- position in the template file
   #        value: The value of the vertex.
   ```

3. Basically, the activities features are from different softwares.
   Currently, I only provide my another project to translate `FSL`'s `Zstat.nii.gz` files to the surface space.
   Please see my [GITHUB Page Reference](https://github.com/listenzcc/freesurferAnalysisScripts "GITHUB Page Reference") for details.

## Workshop

I have updated [Online Script](https://observablehq.com/@listenzcc/fsaverage-in-freesurfer "Online Scrip") to bed the projection.

## Developing Diary

### Code Improvement 1
The scripts have been **deprecated**,
not because they are bad.
But I have found better solution.

```md
## Scripts

-   The ./freesurfer2obj.sh script converts the cortex into OBJ format;
-   The ./srf2obj script provides the core functional of the converting;
-   The ./obj2csv.py script converts the OBJ format into vertex and surface files.

## Workshop

I have initialized [visualization project](https://observablehq.com/@listenzcc/free-surfer-cortex "visualization project") to the OBJ files.
```md
```