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


# 默认参数说明
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


print(variable_param(1, 2, 3, 4, 5, 6))
print(variable_param())
shuzu = [1, 2, 3, 4, 5, 6, 7]  # tuple 元组
print(variable_param(*shuzu))
