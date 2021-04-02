# mac 上 python 的安装
mac 自带的 python 版本一般都是最低的版本 2.7，可以在命令行输入 python 查看版本。如果想要升级，可以从官网下载最新的版本，按照步骤一步一步安装。最终安装完成的目录为
```bash
/Library/Frameworks/Python.framework/Versions/
```
安装完成之后，为了使用方便，需要修改默认的版本
在终端执行以下命令打开 .bash_profile 文件
```bash
open ~/.bash_profile
```
在 .bash_profile 文件中输入新版本的地址
```bash
alias python="/Library/Frameworks/Python.framework/Versions/3.x/bing/python3.x"
```
保存之后，重新打开终端，输入
```bash
source ~/.bash_profile
```
在终端输入 python 再次检查版本，此时应该是安装的新版本。

一般情况下，mac 系统自带 python 路径为
```bash
/System/Library/Frameworks/Python.framework/Versions
```
自己另行安装的 python 路径为
```bash
/Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/site-packages
```
