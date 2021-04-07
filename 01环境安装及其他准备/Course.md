### Python简介

#### Python的历史

1. 1989年圣诞节：**Guido von Rossum**为了打发无聊的圣诞节而编写的一个编程语言。
2. 1991年2月：第一个Python编译器（同时也是解释器）诞生，它是用C语言实现的（后面），可以调用C语言的库函数。在最早的版本中，Python已经提供了对“类”，“函数”，“异常处理”等构造块的支持，还有对列表、字典等核心数据类型，同时支持以模块为基础来构造应用程序。
3. 1994年1月：Python 1.0正式发布。
4. 2000年10月16日：Python 2.0发布，增加了完整的[垃圾回收](https://zh.wikipedia.org/wiki/%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8)，提供了对[Unicode](https://zh.wikipedia.org/wiki/Unicode)的支持。与此同时，Python的整个开发过程更加透明，社区对开发进度的影响逐渐扩大，生态圈开始慢慢形成。
5. 2008年12月3日：Python 3.0发布，它并不完全兼容之前的Python代码，不过因为目前还有不少公司在项目和运维中使用Python 2.x版本，所以Python 3.x的很多新特性后来也被移植到Python 2.6/2.7版本中。
6. 之后得益于机器学习和数学统计应用的兴起，通过[Tiobe](https://www.tiobe.com/tiobe-index/)我们可以看到Python在今天的崛起。

现在最新的版本已经到了Python 3.9.x，Python的版本号分为三段，形如A.B.C。其中A表示大版本号，一般当整体重写，或出现不向后兼容的改变时，增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。如果对Python的历史感兴趣，可以阅读名为[《Python简史》](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)的网络文章。

#### Python的应用领域

目前Python在日常需要的小工具（脚本）、Web应用后端开发（许多大型网站就是用Python开发的，例如YouTube、Instagram，还有国内的豆瓣）、网络数据采集、自动化测试、数据分析、机器学习等领域都有着广泛的应用。

---
### 安装Python
Python是跨平台的，它可以运行在Windows、Mac和各种Linux/Unix系统上。 

安装完之后你会得到Python解释器（就是负责运行Python程序的），一个命令行交互环境，还有一个简单的集成开发环境。

>当我们从Python官方网站下载并安装好Python 3.x后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。
Python的解释器很多，比如Java语言实现的Jython、C#语言实现的IronPython以及PyPy、Brython、Pyston等但使用最广泛的还是CPython。

#### 在Mac上安装Python
Mac系统自带的Python版本是2.7，直接在Terminal运行python就可以看到。要安装新版Python，在 Mac 下同样有多种安装方式，如 Homebrew、安装包安装、Anaconda 安装：

##### 1. Homebrew 安装

Homebrew 是 Mac 平台下强大的包管理工具，首先安装 Homebrew，官方网站是 [https://brew.sh/](https://brew.sh/)。

执行如下命令，即可安装 Homebrew：

```
ruby -e"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

安装完成后，便可以使用 brew 命令安装 Python 3 和 pip 3 了。

```
brew install python3
```

命令执行完成之后，我们发现 Python3 和 pip 3 均已经成功安装。

##### 2. 安装包安装

可以到官方网站下载 Python 3 安装包。链接为 https://www.python.org/downloads/

在 Mac 平台下，可以选择下载 Mac OS X 64-bit/32-bit installer，下载完成后，打开安装包按照提示安装即可。

##### 3. Anaconda 安装

Anaconda 同样支持 Mac，其官方下载链接为：https://www.continuum.io/downloads，选择 Python 3 版本的安装包下载即可

安装完毕后可以通过在终端进行验证：

```Shell
python3 --version
```
或者
```Python
import sys

print(sys.version_info)
print(sys.version)
```

### Python开发工具

#### IDLE - 自带的集成开发工具

IDLE是安装Python环境时自带的集成开发工具,但是由于IDLE的用户体验并不是那么好所以很少在实际开发中被采用。

#### IPython - 更好的交互式编程工具

IPython是一种基于Python的交互式解释器。相较于原生的Python交互式环境，IPython提供了更为强大的编辑和交互功能。可以通过Python的包管理工具pip安装IPython

```Shell
pip install ipython
```

或

```Shell
pip3 install ipython
```

安装成功后，可以通过下面的ipython命令启动IPython

#### Sublime Text
这个大家都比较熟悉了，老牌编辑器
#### Visual Studio Code
[Visual Studio Code](<https://code.visualstudio.com/>)是比较好的选择，它不用花钱并提供了更为完整和强大的功能，有兴趣的读者可以自行研究。

#### PyCharm - Python开发神器
[下载地址](https://www.jetbrains.com/pycharm/download/#section=mac) 可以选择社区版，功能没有专业版多但是够用，也是免费的。 

PyCharm的安装、配置和使用在[《玩转PyCharm》](./玩转PyCharm.md)进行了介绍，感兴趣可以读一下。

---

### Jupyter Notebook

#### Jupyter Notebook是什么
按照 Jupyter 创始人 Fernando Pérez 的说法，他最初的梦想是做一个综合 Ju （Julia）、Py （Python）和 R 三种科学运算语言的计算工具平台，所以将其命名为 Ju-Py-te-R。发展到现在，Jupyter 已经成为一个几乎支持所有语言，能够把软件代码、计算输出、解释文档、多媒体资源整合在一起的多功能科学运算平台。
>一句话就说是一种 Web 应用，能让用户将说明文本、数学方程、代码和可视化内容全部组合到一个易于共享的文档中。

#### 特点
整合所有的资源、交互性编程体验和零成本重现结果。

#### 安装
#####一、使用pip命令安装
1. 把pip升级到最新版本

```
pip3 install --upgrade pip
```
2. 安装Jupyter Notebook

```
pip3 install jupyter
```
#####二、使用Anaconda安装
>[参考地址](https://github.com/selfteaching/the-craft-of-selfteaching/blob/master/T-appendix.jupyter-installation-and-setup.ipynb)

Anaconda已经自动为你安装了Jupter Notebook及其他工具，还有python中超过180个科学包及其依赖项。

可以通过进入Anaconda的[官方下载页](https://www.anaconda.com/products/individual#macos)自行选择下载

####使用
1. 帮助
```
jupyter notebook -h
```

2. 启动
```
jupyter notebook
```

#### Google Colab 环境
[介绍](https://colab.research.google.com/notebooks/welcome.ipynb)

---

### 练习

1.安装Python，输入下面的代码并查看结果，尝试理解结果的意思

```Python
import this
```

> **说明**：输入上面的代码，在Python的交互式环境中可以看到Tim Peter撰写的[“Python之禅”](Python之禅.md)，里面讲述的道理不仅仅适用于Python，也适用于其他编程语言。

2.在colab或者jupyter notebook打印一个九九乘法表，并将代码和结果通过自己fork的仓库pull到impr-learning下的[Python仓库](https://github.com/impr-learning/Python)（以自己的名字首字母命名的文件夹下）



