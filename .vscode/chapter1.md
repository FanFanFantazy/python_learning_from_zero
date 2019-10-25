## 1.	Windows + Python 3 + VS Code 环境搭建
### 1.1.	Python 3 环境搭建
Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。Python 由 Guido van Rossum 于 1989 年底发明，第一个公开发行版发行于 1991 年。像 Perl 语言一样, Python 源代码同样遵循 GPL(GNU General Public License) 协议。官方宣布，2020 年 1 月 1 日， 停止 Python 2 的更新。Python 2.7 被确定为最后一个 Python 2.x 版本。因此此教程只会讲述Python 3.0+ 的相关应用。

首先登陆[Python官网](https://www.python.org/)， 导航栏下Download 模块中显示最新发布的python稳定的版本，本文使用的时Python 3.8.0

<img src="../mdSrc/download_Python3.png" width="300"></img>

点击超链接进入版本详情界面，可以看到版本的简介，和上一版本比较，新功能，对windows 和macOs用户的安装环境的要求，和下载文件列表。

<img src="../mdSrc/python_download_Packages.png" width="800"></img>
 
Python可应用于多平台包括 Linux 和 Mac OS X。官网提供了不同操作系统下多种安装包，可以通过安装器installer安装，也可以直接下载压缩包安装。Unix & Linux 平台安装和其他[安装细节](https://www.runoob.com/python/python-install.html)可参考菜鸟。
### 1.2.	Windows环境变量的配置
程序和可执行文件可以在许多目录，而这些路径很可能不在操作系统提供可执行文件的搜索路径中。path(路径)存储在环境变量中，这是由操作系统维护的一个命名的字符串。这些变量包含可用的命令行解释器和其他程序的信息。可以简单的理解为使用一个变量来保存python执行文件的路径，在任何地方使用命令行解析器（CMD）都可以调用python的命令。
#### 1.2.1.	 命令行添加
打开“命令提示符”，搜索“cmd”即可看到。 

<img src="../mdSrc/search_cmd_in_Windows.png" width="300"></img>

输入
```
path=%path%;C:\XXX\XXX\Python
```
此路径为Python在本地的安装路径
#### 1.2.2.	控制面板添加
在windows 中搜索“**编辑系统环境变量**”，进入控制面板。

<img src="../mdSrc/search_edit_env_var_in_Windows.png" width="300"></img>

点击“环境变量”按钮，进入环境变量编辑页。

 <img src="../mdSrc/system_prop_in_Windows.png" width="300"></img>

可以在定义环境变量问用户变量或者系统变量中的Path变量，区别在于用户变量指对计算机当前用户有效，系统变量可以被任何本机用户适用。

  <img src="../mdSrc/edit_sys_var_Windows.png" width="500"></img>

如果没有Path，可以点击“**新建**”添加一个。
双击Path或选中后点击“**编辑**”，即可打开“**编辑环境变量**”。在新的一行添加Python的文件路径，系统环境变量都在一行编辑，需要用英文分号与其他路径隔开。

  <img src="../mdSrc/edit_sys_var.png" width="500"></img>

添加后可以打开CMD验证，在任意文件位置输入 ```python``` 回车，即可显示Python的版本号和基本提示。如果显示类似信息可以认为我们已经成功安装了Python 3。Congratulations!

  <img src="../mdSrc/cmd_test_py_installiation.png" width="800"></img>

我们可以在Cmd 中执行简单的Python脚本，但是强大的编辑器会是我们轻松的进行复杂编辑，使用一些框架，进行调试等等。因此我选用了Visual Studio Code 这一较轻量级的编辑器来进行代码编辑。最主要的优点就是VS code有良好的开发团队，不断的在增加对不同语言的支持,尤其是较新的语言。同时插件非常丰富，编译速度也很快。
## 1.3 Visual Studio Code
[VS Code官网](https://code.visualstudio.com/)下载稳定版编辑器

<table width="500">
  <tr>
    <td>
      <img src="../mdSrc/download_vscode.png"></img>
    </td>
    <td>
      <img src="../mdSrc/click_extensions_button.png"></img>
    </td>
  </tr>
</table>

安装完成后，打开VS code， 点击左侧导航栏图标，或使用快捷键 ```Ctrl + Shift + X``` 打开插件（Extensions）管理插件。
在搜索框中输入Python，选择Python 插件，安装并启用。

  <img src="../mdSrc/vscode_extension_python.png" width="800"></img>

其他建议安装插件：
+ **Beautify**
+ **Bracket Pair Colorizer**
+ **Git History**
+ **Visual Studio IntelliCode**

首先，创建一个空文件夹，然后使用VS Code打开它。通过VS Code打开文件夹，该文件夹就变成了你的”工作区“。VS Code在```.vscode/settings.json```中存储该工作去的特殊配置，与用户的全局设定相分开。因此要单独给VS Code配置Python的环境变量，以便在VS Code自带的terminal中输入环境变量快速启动Python程序。

在文件夹中创建一个新文件，例如：main.py作为程序主文件。使用 ```Ctrl + Shift + P``` 打开顶部命令板， 输入 ```Python: Select Interpreter``` 并回车或选择，接下来所有的Python解析器会展示在列表中，我选择了最原始的**Python 3.7.2 64-bit**

<img src="../mdSrc/vscode_python_complier.png" width="800"></img>

也可以在，打开 **文件->首选项->设置**， 搜索```python.pythonPath```，输入Python的地址到Python Path下的输入框，既可以指定编译器使用你已经下载的Python 3.x
 
<img src="../mdSrc/vscode_preference_menu.png" width="500"></img>

<img src="../mdSrc/vscode_settings_ui.png" width="800"></img>

 
也可以通过打开文件夹.vscode中的**setting.json**直接配置，注这种方式地址中需要对```\```进行转义，暨```\\```即可。
 
 <img src="../mdSrc/vscode_settings.json.png" width="800"></img>

配置结束，打开终端中，新的终端。终端便于我们直接执行命令行，查看代码编译问题，查看debug的控制台，直接看到输出结果等。对于配置细节可参考[VS Code 官网](https://code.visualstudio.com/docs/python/environments) 
 
 <img src="../mdSrc/vsocde_newTerminal_menu.png" width="800"></img>

切换到终端Terminal， 输入```python``` 回车， 即可看到和CMD 中相同的效果，暨VS code的环境变量配置成功，Congratulations!

 <img src="../mdSrc/vscode_terminal_test_python.png" width="800"></img>

在一次编辑中，暨打开一VS code工程，terminal 可以反复利用。
+ **New Terminal** - 快速打开多个terminal，方便启功多个脚本
+ **Kill terminal** - 垃圾桶图标 关闭当前terminal
+ **选择器** - 对terminal的切换
+ **Split terminal** – 同一窗口打开多个terminal
+ **Maximize/Restore Peniel Size** - 全屏或小窗口terminal

好了，我们已经成功的搭建了开发环境，接下来我们来看看Python语言究竟怎样使用

---
[主页](../README.md) ----- [下一章](./chapter2.md)
