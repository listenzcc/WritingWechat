## GIT-bug

GIT 是常用的版本管理软件，它偶尔也会出问题。

---
- [GIT-bug](#git-bug)
- [问题描述](#问题描述)
- [解决方案](#解决方案)

## 问题描述

今天安装了最新版本的 GIT 软件

但是它好像在我这里有些水土不服，具体表现为它和 OneDrive 打架

![Untitled](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Untitled.png)

![Snipaste_2022-07-05_20-21-13.png](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Snipaste_2022-07-05_20-21-13.png)

情况很简单，就是凡是 OneDrive 同步过后的目录，只要里面含有 GIT 的 REPO，那么 GIT 就不会再认为这是自己的 REPO 了。

![Untitled](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Untitled%201.png)

就很神奇（糟心）。再简单分析一下，发现是 GIT 在获取 .git 目录中文件的 stat 的时候出了某些问题，无法获取这些文件的状态。隐约觉得与 OneDrive 的同步锁有关，但无法证实。

## 解决方案

幸好 Cygwin 和 MobaXterm 的 GIT 都是可以用的，只需要简单移植一下就可以解决问题。

![Untitled](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Untitled%202.png)

![Untitled](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Untitled%203.png)

要谈移植，先要找到它们与 WIN 版本的 GIT 有何不同，它们最主要的不同点是对输出目录的处理，

- Windows 的目录风格是盘符加文件夹的结构；
- 而类 UNIX 系统的目录网络是树的路径结构；

```powershell
# Windows
C:/Users/user1/Documents/...

# Unix-like (cygwin)
/cygdrive/c/Users/user1/Documents/..
```

因此，移植的主要工作就是将 Unix-like 的目录转化为 Windows 网络的目录。这个工作可以使用 Cygwin 提供的工具 cygpath 来完成

```powershell
# convert will be set to: "C:/Users/user1/Documents/..."
$convert = cygpath -w /cygdrive/c/Users/user1/Documents/..
```

具体来说，我们要做的就是提供一个接口程序，在系统每次调用 git 程序的时候，我们就把接口程序塞给它。接口程序会调用 git 程序，并将返回的路径经过转换后返回给系统。

系统可能会以特别诡异的方式来调用我们的接口，以下是几个例子，

```powershell
# Simple version
# Base dir detection, it has only one output
git rev-parse --show-toplevel

# Complex version
# Base dir detection with options, it has only one output
git -c core.quotepath=true rev-parse --show-toplevel

# Crazy version
# For-loop with mutiple options and countless outputs
git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) refs/heads/main refs/remotes/main
```

我一开始的想法是用 Python 或 PHP 来应付这些调用方式，最差也是想用 PowerShell。但无奈许多程序只能调用远古的 .bat 和封装好的 .exe。可执行程序（.exe）显然太过麻烦了，无奈只能选择 .bat 来做这个事情。

这里为了避免日后再走弯路，就将测试程序，而不是最终版本放在这里。

```powershell
@ECHO on

@ECHO -------------
SET PATH=C:\cygwin64\bin;%PATH%

@ECHO -------------
@ECHO %PATH%
@ECHO -------------
@ECHO %*
@ECHO %1

@ECHO -------------
set Replaced=%%*:rev-parse=%%
If NOT "%%*"=="%Replaced%" (
     echo contains
) else (
     echo does not contain
)

@ECHO -------------
SET c=git %*
@ECHO %c%
@ECHO ('git %*')

@ECHO -------------

FOR /F "usebackq" %%1 IN (`"%c%"`) DO cygpath -w %%1
```

这里还需要另外说一下的就是 .bat 的一个莫名其妙的 BUG。它就是在 FOR 语句中，如果按照最直观的方法调用 c 语句的话，传入参数中的“=”会莫名其妙消失掉。

```powershell
# Input %c% is like "git -c core.quotepath=true ..."
# However, in operation, the %c% is exceuted as "git -c core.quotepath true ..."
# The git will fail since it does not know the command "true"
FOR /F %%1 IN ('%c%') DO cygpath -w %%1
```

我在想，也许 GIT 的失效或许会与这个 BUG 有关。

![Untitled](GIT-bug%209e6cc17fb9274fd38bc0f13a01cc61f7/Untitled%204.png)