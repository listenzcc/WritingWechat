## 三维模型解析及渲染

解析`GLTF`文件的代码。

---

- [三维模型解析及渲染](#三维模型解析及渲染)
- [三维模型解析及渲染](#三维模型解析及渲染-1)
- [Parse GLTF and GLB Files](#parse-gltf-and-glb-files)
- [File Name Setup](#file-name-setup)
- [Excellent Functions](#excellent-functions)
- [Check What We Got](#check-what-we-got)
  - [Parse from Buffer](#parse-from-buffer)
  - [Check the Data Details](#check-the-data-details)
  - [Plot if Things Go Right](#plot-if-things-go-right)
  - [Save the Results](#save-the-results)

## 三维模型解析及渲染

三维模型和平面图像一样，
都是计算机图形学的重要研究内容。

本着不重复造轮子的原则，
我尝试用现成的工具完成它们的解析和渲染。
其中，

- 解析：代表针对`GLTF`格式为代表的文件进行解码，
  从中解析出三维顶点和三角微元数据；
- 渲染：代表使用前端工具，如`REGL`等，
  进行在网页端进行前面渲染。

当然，三维模型可以用诸如`Blender`和`画图 3D`等工具，
进行“拿来主义”，
如下图所示

![3D Models](./3DModels.png)

3维渲染的计算效率也是可以满足实时交互要求的。

【这是一段棒到不行的视频】

本文只是一份代码文档，
它是基于`Python`对二进制`Buffer`进行解析。
后面有机会，
也许会说一些技术细节。

## Parse GLTF and GLB Files

Parse the 3D model of .gltf and .glb files into

- vertex: The vertex of the 3D models;
- mesh: The 3-vertex mesh element of the 3D models.


```python
import os
import base64
import struct

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from gltflib import GLTF
```

## File Name Setup


```python
fname = r'3dModel/deer-printable.glb'
fname = r'3dModel/fullDeer.glb'
```

## Excellent Functions


```python
def parse_gltf(fname):
    '''
    Parse the GLTF or GLB file,

    '''

    gltf = GLTF.load(fname)
    gltf.convert_to_base64_resource(gltf.resources[0])
    gltf.export_gltf(fname + '.gltf')

    resources = gltf.resources
    bufferViews = gltf.model.bufferViews
    accessors = gltf.model.accessors

    return resources, bufferViews, accessors

def parse_buffer(resources, idx):
    '''
    Parse buffer from the resources of idx.
    '''

    buffer = resources[idx]

    bins = buffer.uri.split(',', 1)[1]

    # ! Make sure you are using the correct decoder
    packed = base64.b64decode(bins)

    describe = dict(
        fname=fname,
        buffer=buffer,
        mime_type=buffer.mime_type,
        uri_header=buffer.uri[:80],
        uri_length=len(buffer.uri),
        bins_header=bins[:80],
        bins_length=len(bins),
    )

    return describe, bins, packed

def parse_accessor(ac, resources, bufferViews):
    '''
    Parse the data of the accessor [ac]
    '''

    bv = bufferViews[ac.bufferView]

    describe, bins, packed = parse_buffer(resources, bv.buffer)
    packed_bytes = packed[bv.byteOffset: bv.byteOffset + bv.byteLength]

    ctype = ac.componentType

    d = struct.unpack(componentTypes[ctype][2].format(ac.count * types[ac.type]), packed_bytes)
    d = np.array(d).reshape((-1, types[ac.type]))

    return d
```


```python
componentTypes = {
    5126: ['FLOAT', 4, '<{}f'],
    5123: ['UNSIGNED_SHORT', 2, '<{}H'], # ? Not so sure about this.
}

types = {
    'VEC4': 4,
    'VEC3': 3,
    'VEC2': 2,
    'SCALAR': 1,
}
```

## Check What We Got

The accessors with valid max and min attributes are the vertex accessors.


```python
resources, bufferViews, accessors = parse_gltf(fname)

display(resources)

display(bufferViews)

display(accessors)
```


    [Base64Resource(15992380 bytes)]



    [BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=0, byteLength=98784, byteStride=None, target=34963),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=98784, byteLength=114372, byteStride=None, target=34962),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=213156, byteLength=114372, byteStride=None, target=34962),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=327528, byteLength=76248, byteStride=None, target=34962),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=403776, byteLength=6148885, byteStride=None, target=None),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=6552661, byteLength=1117135, byteStride=None, target=None),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=7669796, byteLength=6203620, byteStride=None, target=None),
     BufferView(extensions=None, extras=None, name=None, buffer=0, byteOffset=13873416, byteLength=2118963, byteStride=None, target=None)]



    [Accessor(extensions=None, extras=None, name=None, bufferView=0, byteOffset=None, componentType=5123, normalized=None, count=49392, type='SCALAR', max=None, min=None, sparse=None),
     Accessor(extensions=None, extras=None, name=None, bufferView=1, byteOffset=None, componentType=5126, normalized=None, count=9531, type='VEC3', max=[2.438467025756836, 6.775949001312256, 3.775106906890869], min=[-1.54141104221344, -0.01114455983042717, -1.244312047958374], sparse=None),
     Accessor(extensions=None, extras=None, name=None, bufferView=2, byteOffset=None, componentType=5126, normalized=None, count=9531, type='VEC3', max=None, min=None, sparse=None),
     Accessor(extensions=None, extras=None, name=None, bufferView=3, byteOffset=None, componentType=5126, normalized=None, count=9531, type='VEC2', max=None, min=None, sparse=None)]


### Parse from Buffer

And Automatically select the idx_vertex and idx_meshes,
I do not if the method works forever.


```python
ds = []
idx_vertex = -1
idx_meshes = -1

for j in range(len(accessors)):
    accessor = accessors[j]

    if accessor.min:
        idx_vertex = j

    d = parse_accessor(accessor, resources, bufferViews)
    ds.append(d)

    if d.shape[1] == 1:
        idx_meshes = j

display(idx_vertex, idx_meshes, [e.shape for e in ds])
```


    1



    0



    [(49392, 1), (9531, 3), (9531, 3), (9531, 2)]


### Check the Data Details


```python
ds[0], ds[1], ds[2], ds[3]
```




    (array([[ 0],
            [ 1],
            [ 2],
            ...,
            [58],
            [56],
            [57]]),
     array([[0.206407  , 4.90350294, 2.95625091],
            [0.195921  , 4.87971783, 2.963691  ],
            [0.19394843, 4.88100863, 2.99142122],
            ...,
            [0.29448101, 5.17738295, 2.49478698],
            [0.306748  , 5.20883894, 2.5882709 ],
            [0.48311001, 5.26201487, 2.5467689 ]]),
     array([[-0.91591316,  0.30660406, -0.25903106],
            [-0.97743601,  0.064569  , -0.201121  ],
            [-0.98845887,  0.05413099,  0.14148799],
            ...,
            [-0.63948184, -0.75505179, -0.14477497],
            [-0.77751702, -0.089656  ,  0.62243801],
            [ 0.88460547,  0.42173076,  0.19903888]]),
     array([[0.32930681, 0.92279738],
            [0.33733615, 0.93756545],
            [0.35515046, 0.93445587],
            ...,
            [0.7043426 , 0.91362393],
            [0.69977868, 0.90015256],
            [0.68084556, 0.96216458]]))



### Plot if Things Go Right


```python
d2plot = ds[idx_vertex]

x = d2plot[:, 0]
y = d2plot[:, 1]
z = d2plot[:, 2]

trace = go.Scatter3d(
   x = x, y = y, z = z,mode = 'markers', marker = dict(
      size = 1,
      color = z, # set color to an array/list of desired values
      colorscale = 'Viridis'
      )
   )
layout = go.Layout(title = '3D Scatter plot')
fig = go.Figure(data = [trace], layout = layout)
fig
```

### Save the Results

You may have to change the

- vertex: The vertex;
- meshes: The 3-vertex meshes.

to save the correct results.


```python
vertex = ds[idx_vertex]
meshes = ds[idx_meshes]
```


```python
df_vertex = pd.DataFrame(vertex, columns=['x', 'y', 'z'])
df_vertex.to_csv(fname + '-vertex.csv')
df_vertex
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.206407</td>
      <td>4.903503</td>
      <td>2.956251</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.195921</td>
      <td>4.879718</td>
      <td>2.963691</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.193948</td>
      <td>4.881009</td>
      <td>2.991421</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.200583</td>
      <td>4.908579</td>
      <td>2.986342</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.207705</td>
      <td>4.903961</td>
      <td>3.014799</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9526</th>
      <td>0.335468</td>
      <td>5.175738</td>
      <td>2.421746</td>
    </tr>
    <tr>
      <th>9527</th>
      <td>0.316176</td>
      <td>5.173036</td>
      <td>2.451739</td>
    </tr>
    <tr>
      <th>9528</th>
      <td>0.294481</td>
      <td>5.177383</td>
      <td>2.494787</td>
    </tr>
    <tr>
      <th>9529</th>
      <td>0.306748</td>
      <td>5.208839</td>
      <td>2.588271</td>
    </tr>
    <tr>
      <th>9530</th>
      <td>0.483110</td>
      <td>5.262015</td>
      <td>2.546769</td>
    </tr>
  </tbody>
</table>
<p>9531 rows × 3 columns</p>
</div>




```python
df_meshes = pd.DataFrame(meshes, columns=['id'])
df_meshes.to_csv(fname + '-meshes.csv')
df_meshes
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>49387</th>
      <td>649</td>
    </tr>
    <tr>
      <th>49388</th>
      <td>652</td>
    </tr>
    <tr>
      <th>49389</th>
      <td>58</td>
    </tr>
    <tr>
      <th>49390</th>
      <td>56</td>
    </tr>
    <tr>
      <th>49391</th>
      <td>57</td>
    </tr>
  </tbody>
</table>
<p>49392 rows × 1 columns</p>
</div>



