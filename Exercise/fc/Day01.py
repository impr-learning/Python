# 1. 安装Python，输入下面的代码并查看结果，尝试理解结果的意思
import this

# 2. 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%dx%d=%d" % (j,i,i*j), end="  ")
    print()
