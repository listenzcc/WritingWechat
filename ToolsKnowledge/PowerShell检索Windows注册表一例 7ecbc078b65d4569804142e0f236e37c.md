# PowerShell检索Windows注册表一例

Windows注册表是系统和应用程序配置的关键存储库。它由键（key）、子键（subkey）和值（value）组成。键代表顶层结构，子键进一步组织信息，值存储配置数据。PowerShell可以用于检索注册表，包括查找、枚举、搜索和筛选注册表中的键和值。

[https://github.com/listenzcc/dig-regedit-with-powershell](https://github.com/listenzcc/dig-regedit-with-powershell)

---
[toc]

## Windows注册表的树型结构

在Windows注册表中，术语"项"（key）、"键"（subkey）和"值"（value）用于描述注册表的组织结构和内容。它们的含义如下：

1. **项（Key）**：
    - 在注册表中，项是顶级元素，类似于文件系统中的文件夹。每个项可以包含多个子项和/或值。注册表路径以根键开始，比如`HKEY_LOCAL_MACHINE`或`HKEY_CURRENT_USER`，然后依次向下划分为多个项，形成树状结构。
    
    ```powershell
    "REGISTRY::HKEY_CLASSES_ROOT" = "HKEY_CLASSES_ROOT" = "HKCR:"
    "REGISTRY::HKEY_CURRENT_CONFIG" = "HKEY_CURRENT_CONFIG" = "HKCC:"
    "REGISTRY::HKEY_USERS" = "HKEY_USERS" = "HKU:"
    "REGISTRY::HKEY_CURRENT_USER" = "HKEY_CURRENT_USER" = "HKCU:"
    "REGISTRY::HKEY_LOCAL_MACHINE" = "HKEY_LOCAL_MACHINE" = "HKLM:"
    ```
    
2. **键（Subkey）**：
    - 键是项下的子元素，类似于文件系统中文件夹的子文件夹。它们用于进一步组织和分类注册表中的信息。
    - 键可以包含其他键或值，从而形成更深层次的层次结构。
3. **值（Value）**：
    - 注册表项中的值存储了具体的数据或配置信息。值可以是字符串、整数、二进制数据等不同类型的数据。
    - 每个键可以包含多个值，这些值通常用于存储与该键相关联的配置数据或参数。

总的来说，项表示注册表的顶层组织结构，键是项的子元素用于进一步组织信息，而值则存储实际的配置数据。通过组合使用这些元素，Windows注册表可以灵活地存储和管理系统和应用程序的配置信息。

**注意，要操作这些内容，有时需要system权限，而非admin权限。在此推荐PSTools工具进行操作，详见附件。**

## PS检索的基本方式

这段PowerShell脚本展示了如何使用PowerShell操作Windows注册表，从而可以执行一系列操作，包括查找、枚举、搜索以及筛选注册表中的键和值。下面的例子用于检索全部USB存储设备。

![Untitled](PowerShell%E6%A3%80%E7%B4%A2Windows%E6%B3%A8%E5%86%8C%E8%A1%A8%E4%B8%80%E4%BE%8B%207ecbc078b65d4569804142e0f236e37c/Untitled.png)

```powershell
# -------------------------------------------------------------
# Setup
$setName = "ControlSet001"
$setName = "CurrentControlSet"

$errorAction="SilentlyContinue"

# -------------------------------------------------------------
# Header
echo "
----------------------------------------------------------------------------
Guessing the registry keys of your USB storage devices
The CurrentControlSet can also be ControlSet001, ControlSet002 ...
"

# -------------------------------------------------------------
# List children
echo "
----------------------------------------------------------------------------
USBSTOR session
"
$path = "HKLM:\SYSTEM\"+$setName+"\Enum\USBSTOR\"
ls -Path:$path

# -------------------------------------------------------------
# Search recursively
echo "
----------------------------------------------------------------------------
USB session
"
$path = "HKLM:\SYSTEM\"+$setName+"\Enum\USB\"
ls -Path:$path -Recurse -ErrorAction:$errorAction |Where-Object {$_.GetValue('Service') -eq 'USBSTOR'}

# -------------------------------------------------------------
# Search recursively
echo "
----------------------------------------------------------------------------
My best guess
"
$path = "HKLM:\SYSTEM\"+$setName+"\Control\DeviceClasses\"
ls -Path:$path -Recurse -ErrorAction:$errorAction | Where-Object {$_.getValue('DeviceInstance') -like 'USBSTOR*'}
```

## 附录：GUID

GUID（Globally Unique Identifier，全球唯一标识符）是一种128位的标识符，用于在计算机系统中唯一标识对象或资源。GUID通常以一种形式被表示为字符串，例如 "{57edcd85-0281-4893-a224-6719f892b1a4}"。在Windows的注册表中，GUID经常被用作键或值的名称，以唯一标识特定的组件、设置或资源。

## 附录：注册表的提权操作方式

PSTools是Sysinternals Suite的一部分，它提供了一组强大的命令行实用工具，可用于执行各种系统管理任务，包括对注册表的操作。要以系统权限操作注册表，你可以使用PSTools中的PsExec工具，以下是基本步骤：

1. **下载并解压PSTools**：
首先，从Sysinternals Suite的官方网站下载PSTools工具[https://download.sysinternals.com/files/PSTools.zip](https://download.sysinternals.com/files/PSTools.zip)

    ![Untitled](PowerShell%E6%A3%80%E7%B4%A2Windows%E6%B3%A8%E5%86%8C%E8%A1%A8%E4%B8%80%E4%BE%8B%207ecbc078b65d4569804142e0f236e37c/Untitled%201.png)
    
2. **以系统权限运行命令行**：
打开命令提示符（cmd.exe），右键单击并选择“以管理员身份运行”，以确保以管理员权限打开命令提示符。
3. **使用PsExec执行命令**：
在以管理员身份打开的命令提示符中，导航到PSTools所在的目录，并使用以下命令执行你的注册表操作：
    
    ```powershell
    # Run the regedit in the System account, it interacts with the desktop.
    PsExec.exe -s -i regedit
    # or, in x64 system use PsExec64.exe instead
    PsExec64.exe -s -i regedit
    ```
    
    这将以系统权限运行注册表编辑器，允许你进行必要的注册表更改。 `-s`参数指定以系统权限运行，`-i`参数允许交互式会话。
    
4. **进行注册表更改**：
在注册表编辑器中，你可以像在普通情况下一样对注册表进行操作，但这次你以系统权限运行，因此可以执行需要特权的操作。

请注意，对注册表的更改可能会对系统产生重大影响，因此在进行更改之前，请确保了解所做更改的后果，并备份注册表以防止意外情况的发生。