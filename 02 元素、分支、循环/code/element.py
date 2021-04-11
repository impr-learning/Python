# 整数
print(0b100)
print('0o100')
# 浮点数
print(1.23456e2)
# 字符串
print('1:hello world!')
print('''2:hello world!
    3:hello world!!''')
word = 'hello'
print(word)
print("word")
# I'm a big fans of Python.   单引号与双引号
print('I\'m a big fans of Python.')
print("I'm a big fans of Python.")
# 布尔型
print(True)
print(3 == 5)


# 这里是单行注释
"""
这里是多行注释
这里还是多行注释
"""





a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

print(str(type(a))[8:-2])    # int
print(str(type(b))[8:-2])    # float
print(str(type(c))[8:-2])    # complex
print(str(type(d))[8:-2])    # str
print(str(type(e))[8:-2])    # bool