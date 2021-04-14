a = -30.3
print(abs(a))


# 自定义绝对值函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-20))


# 必备参数说明
def necessary_param(string):
    """打印任何传入的字符串"""
    # print(string)
    return string


# 调用necessary函数
print(necessary_param('abc'))


# 默认参数说明  必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）https://blog.csdn.net/troubleshooter/article/details/41649805
def default_param(name, age=25):
    return '名字：' + str(name) + ' 年龄：' + str(age)


print(default_param('张三'))
print(default_param('李四', 28))
print(default_param(28, '王五'))
print(default_param(age=28, name='和六'))


# 可变参数说明
def variable_param(*number):
    sum = 0
    for i in number:
        sum += i
    return '总和是：' + str(sum)


print(variable_param(1, 2))
print(variable_param())
shuzu = (1, 2, 3, 4, 5, 6, 7)  # tuple 元组
print(variable_param(*shuzu))
# *shuzu表示把shuzu这个list的所有元素作为可变参数传进去
# print(variable_param('Bob', 35, city='Beijing')) 因为是元组所以传入的参数不能是键值对


# 关键字参数说明  （必选参数 + 关键字参数）
def keyword_param(name, age, **args):
    print('name:', name, ' age:', str(age), ' other:', args)
    return


keyword_param('Bob', 35)
keyword_param('Bob', 35, city='Beijing')
keyword_param('Bob', 35, city='Beijing', area="chaoyang")
extra = {'city': 'Beijing', 'area': 'chaoyang', 'street': 'jintailu'}
keyword_param('Bob', 35, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**args参数


# 参数组合 必备参数 + 默认参数 + 可变参数 + 关键字参数
def compose(a, b, c=0, *number, **args):
    print('a =', a, 'b =', b, 'c =', c, 'number =', number, 'args =', args)
    return


number = (4, 5, 6)
eg     = ('十三', '十四', '十五')
args   = {'name': '张三', 'age': '28', 'sex': 'woman'}
compose(1, 2)
compose(1, 2, 3)
compose(1, 2, 3, *number)
compose(1, 2, *number)   # 当默认参数和可变函数一起使用，不传入默认参数且传入可变参数的时候，可变参数的元组前几个参数会填充到默认参数位置上
# compose(1, 2, *eg)
compose(1, 2, **args)
compose(1, 2, 3, *number, **args)

print ('模块')
# 没有类
import math
print(math.ceil(3.45))

from math import ceil
print(ceil(3.45))

from math import *
print(ceil(3.45))

# 有类
import random
print(random.Random().randint(1, 6))
print(random.randint(1, 6))

from random import *
print(randint(1, 6))
print(Random().randint(1, 6))

print('-----')
import module3
print(module3)







