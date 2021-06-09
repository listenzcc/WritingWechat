## 用 PowerShell 寻找你找不到的文件

继续说 PowerShell （PS）的事情，通过本文档，希望你能够获得一个在 Windows （W）系统中高效找到你想要的文件的方法。能够开始使用 W 系统中提供的 PS 终端，并且习惯用键盘打字的方式而不是鼠标乱点的方式操作你的电脑。
当然，本文档的目的还是深入理解 PS 的抽象类模式，并提供一个非常工程化的视角来阐述这一特性。

---

## 找文件

当用户使用电脑时，很常见的一个情况就是要找到某个文件，却忘了它在哪。
在 L 系统中，可以使用如下语句来找寻想要的文件。

```sh
#!/bin/sh
find -name [fname]
```

理想很丰满，但现实很骨感，要是用户记得文件名，还需要费那么大劲找吗？
另一更现实的问题是，在输入过程中，神奇的自动补全 TAB 键完全派不上用场。

> 这里啰嗦一下神奇的 TAB 键的用法，它其实就是一个自动补全的呼出方式，假设要查看一个文件叫做 abcdefg.docx，其实不必输入文件全名
>
> ```sh
> #!/bin/sh
> cat abcdefg.docx
> ```
>
> 而是可以转而使用 TAB 键进行补全
>
> ```sh
> #!/bin/sh
> cat abcd<TAB>
> ```
>
> 系统会自动把文件的全名补全出来。
> 这样来说，假设要找一个 `WORD` 文件，由于 `TAB` 键补全功能的缺失，就不得不把正则表达式 `xxxx.docx` 完整地打在到屏幕上。
> 你知道的，优秀程序员往往是按敲击键盘次数计价的，所以这么做就赔大发了。

## 把 TAB 补全用上

如果能够将 TAB 补全用到找寻文件上，操作将会简化很多，也比较不容易出错。
事实上，更常见的情况是，用户并不完全清晰地记得自己要找的文件后缀，最好系统能够把能够找的选项列出来，并且适当地允许用户使用 TAB 键进行补全。
或者更进一步地，最好系统能够快速、全面地生成一份报告，告诉用户有哪些文件是可选的。

### 目前的情况

这样的工作很难吗？不见得。现在有这样的工具吗？并没有。

- 至少 L 系统的 Terminal 实现起来比较麻烦，普通用户一般不会弄出来，（当然也没有普通用户会没事就用这个环境）；
- W 系统的资源管理器在这个方面是个废物，搜索功能在右上角，但每次点进去找文件时我的血压都会有点高，我总能看到一堆莫名其妙的文件，当我点开其中一个但发现不是想要的，而需要返回的时候，它会再费时费力地搜索一遍，留我在屏幕前思考人生（搜索时间越长，思考得就越深刻）；
- MacOS 的 Finder 直接一脸劝退的态度，它很漂亮，还允许你进入目录、浏览或选择文件，其他真的就没有了；
- 其他类似的工具，如 Everything 等，虽然补足了各个操作系统的搜索 GUI 的不足，但使用起来也没有办法将 TAB 补全加入操作流程。

### 功能抽象

那么这个不难，还实用，却没有的功能是什么呢？我们不妨抽象一下。
就拿扩展名为例，我想我们需要这样一个工具，它能够快速并自动对当前目录及子目录的文件扩展名进行识别和统计，并在用户输入过程中，可以使用在 TAB 键进行智能补全。这样做有几个好处

- 用户可以通过自动补全功能减少输入量，比如输入`.d<TAB>`，系统会自动在 `.docx, .doc, .data`等等可选扩展名中切换，等待用户确认；
- 允许用户浏览当前目录下的所有可选文件扩展名，用户往往需要看看当前目录下到底有哪些种类的文件；
- 能够根据用户输入的扩展名，列出所有待选文件。
  在列出所有待选文件后，用户可以比较容易地找到目标文件（如果存在这个文件的话）。

### 功能实现

下面，我们将使用简单的 PS 代码实现这一功能。首先是基础功能。

```powershell
function Get-FilesByExtension {
    # Binding Parameters
    [CmdletBinding()]
    param(
        [Parameter(
            Position = 0
        )]
        [string] $Extension
        , $Depth = 2
        , $Exclude = ""
    )

    # Echo the Current Job
    Write-Output "Selecting Extension of $Extension"

    # If Extension is Empty, all the Available Extension are listed
    if ($Extension -eq "") {
        Get-ChildItem -Recurse -Depth $Depth -File | Where-Object { $_.FullName -NotLike '*\.*' } | Group-Object Extension | Sort-Object Count
        return
    }

    # If Extension is Inputed, all the Files with the Extension are listed
    $all = Get-ChildItem -Recurse -Depth $Depth -File | Where-Object { $_.FullName -NotLike '*\.*' } | Select-Object FullName, Name, LastWriteTime, Extension | Group-Object Extension

    $select = $all | Where-Object { $_.Name -like $Extension } | Select-Object Group

    $select.Group | Select-Object Name, LastWriteTime, fullname, extension | Sort-Object LastWriteTime
}
```

由于首次涉及 PS 函数脚本，我想这里有必要对其功能进行解释。

1. 此部分是规定该脚本有哪些输入参数，其中默认参数是`$Extension`，也就是说，该函数的默认输入参数就是`$Extension`参数。另外，用户还可以指定`$Depth`和`$Exclude`两个参数，它们的意义似乎并不是很重要，在此不多着墨；
2. 此部分是反馈给用户目前是在查找`$Extension`这个扩展名的文件；
3. 下面有两个分支，第一个分支是当`$Extension`参数是空值时，该函数将列出所有可选的扩展名，如图 1 所示；
4. 第二个分支是列出所有`$Extension`扩展名文件的绝对目录，如图 2 所示。

图 1、扩展名列表示意图

图 2、文件列表示意图

5. 到此，该函数的全部功能介绍完毕。

函数功能介绍完毕后，我们回到 PS 的抽象类特性，以 #3 为例进行介绍，

- Write-Output 获取所有子文件，并将它们存储为抽象的文件类；
- Where-Object 是管道的第一站，它将忽略所有以点开始的文件或目录；
- Group-Object 是按文件类的扩展名进行分组，也就是说把相同扩展名的文件排到在一起；
- Sort-Object 是对扩展名计数进行排列，结果可见图 1 的第一列。

可见，在抽象类的基础上，PS 可以将处理的对象进行流动，并且在流动的每一站，以处理类的方式对成员进行加工。
有加工，就可以自然地联想到工厂模式，我们可以通过工厂模式来为该函数添加 TAB 补全功能。所需的代码如下

```powershell
$getExtensions = {
    param($commandName, $parameterName, $wordToComplete, $commandAst, $fakeBoundParameters)
    Get-ChildItem -Recurse -Depth 1 -File | Where-Object { $_.FullName -NotLike '*\.*' } | Select-Object Extension | Sort-Object Extension | get-unique -AsString | Where-Object { $_.Extension -like "$wordToComplete*" } | ForEach-Object { $_.Extension }
}
Register-ArgumentCompleter -CommandName Get-FilesByExtension -ParameterName 'Extension' -ScriptBlock $getExtensions
```

不难看出，`Register-ArgumentCompleter`是一个注册补全功能的方法，它将目标函数的 `$Extension` 参数注册到一个补全脚本上，补全脚本是在 `$getExtensions` 上定义的。
补全脚本所做的事情则比较简单，即在用户按下 TAB 键要求补全时，它会查找所有可行的扩展名，并且过滤出以当前输入字符串开头的扩展名，并将这些扩展名以列表的形式返回。
这样，列表元素可以通过 PS 的内置补全机制一个一个地出现在用户的手边。
至此，功能实现完毕。

## 总 结

可以看到，PS 的抽象类理念允许用户以对象的方式对功能实体进行管道式的处理，并且可以通过面向对象的工厂设计模式进行功能开发，从而大大简化实现较为复杂功能时的代码量。
但是，同样由于其抽象类特性，PS 在执行较为简单命令的时候却显得较为复杂和臃肿。可见，PS 的设计理念在代码量方面，大大降低了复杂功能的代码量上限，却同时提高了简单功能的代码量下限。
但有一点，在面向对象的特性方面，PS 的代码可读性较高，几乎每个操作是合理的抽象语言。

如果你足够细心，可以发现所有的 PS 命令都是“动宾短语”这样的结构，这恰恰是功能抽象的体现。
