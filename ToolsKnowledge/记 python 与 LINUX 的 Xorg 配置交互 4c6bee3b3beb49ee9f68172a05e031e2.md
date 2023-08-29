# 记 python 与 LINUX 的 Xorg 配置交互

本文的目的是使用 python 与 linux 的 lspci 命令进行交互，将交互结果交给 Xorg，用来搭建可用的 display。本文的开源代码可见我的 Github 仓库

[https://github.com/listenzcc/python-with-linux-xorg](https://github.com/listenzcc/python-with-linux-xorg)

---
- [记 python 与 LINUX 的 Xorg 配置交互](#记-python-与-linux-的-xorg-配置交互)
  - [实用的多屏输出拓扑图和 Xorg 设置图解](#实用的多屏输出拓扑图和-xorg-设置图解)
  - [获取 lspci 的规范化输出](#获取-lspci-的规范化输出)
  - [Python 与 lspci 的交互](#python-与-lspci-的交互)


## 实用的多屏输出拓扑图和 Xorg 设置图解

下图展示了如何理解 Xorg 的多屏输出拓扑图，以及 Xorg 的多屏输出设置如何与硬件匹配。

![example.png](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/example.png)

## 获取 lspci 的规范化输出

LINUX 系统是开源系统，它会把计算机的全部信息毫无保留地展示给管理员。而计算机的软件和硬件是相辅相成的，举例来说， lspci 这种脚本能够将计算机硬件的细节全部展示在软件中。

如下图所示，通过合适的参数设置，我们既可以按照物理连接显示硬件之间的关系（-t），又可以将这些信息表格化，方便机器读取（-mm）。

```bash
$ lspci -tvnn
$ lspci -mmvnn
```

![Untitled](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled.png)

```less
$ lspci --help

lspci: invalid option -- '-'
Usage: lspci [<switches>]

Basic display modes:
-mm             Produce machine-readable output (single -m for an obsolete format)
-t              Show bus tree

Display options:
-v              Be verbose (-vv or -vvv for higher verbosity)
-k              Show kernel drivers handling each device
-x              Show hex-dump of the standard part of the config space
-xxx            Show hex-dump of the whole config space (dangerous; root only)
-xxxx           Show hex-dump of the 4096-byte extended config space (root only)
-b              Bus-centric view (addresses and IRQ's as seen by the bus)
-D              Always show domain numbers
-P              Display bridge path in addition to bus and device number
-PP             Display bus path in addition to bus and device number

Resolving of device ID's to names:
-n              Show numeric ID's
-nn             Show both textual and numeric ID's (names & numbers)
-q              Query the PCI ID database for unknown ID's via DNS
-qq             As above, but re-query locally cached entries
-Q              Query the PCI ID database for all ID's via DNS
```

![Untitled](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled%201.png)

## Python 与 lspci 的交互

1. 执行脚本并将结果转换为 Pandas 数据库；
2. 按 Vendor 和 Class 对数据库进行分组；
3. 选择其中感兴趣的内容；
4. 将这些内容中的 Slot 信息转换为 BusID；
5. 将 BusID 写入文件，并开启 Xorg。

![原始输出与数据库构建](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled%202.png)

原始输出与数据库构建

![分组统计](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled%203.png)

分组统计

![增加 BusID](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled%204.png)

增加 BusID

![虚拟化编号（顺序仅供参考）](%E8%AE%B0%20python%20%E4%B8%8E%20LINUX%20%E7%9A%84%20Xorg%20%E9%85%8D%E7%BD%AE%E4%BA%A4%E4%BA%92%204c6bee3b3beb49ee9f68172a05e031e2/Untitled%205.png)

虚拟化编号（顺序仅供参考）