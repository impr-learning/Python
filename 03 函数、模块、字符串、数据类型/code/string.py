s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

print('a\nb')
print('a\tb')
print('a\'b')
print(r'a\nb')
print(R'a\nb')

string = 'ab'* 3 + 'cd'
print(string)
print(str.upper(string))
print(str.title(string))
print(str.replace(string, 'cd', 'ef'))

a = []
for i in range(1, 10):
    a.append(i)

print(a)
print(a[5])
print(a[:5])
print(a[5:])
print(a[2:5])

print(a[-1])
print(a[:-3])
print(a[-3:])
print(a[-3:-1])

print(a.index(min(a)))  # 最小元素的位置
print(a.index(max(a)))

a.append('张三')
print(a)

a.insert(0, '李四')
print(a)

b = ['王五']
a.extend(b)
print(a)

a.remove('王五')
print(a)

print(a.pop())
a.pop(0)
print(a)

del a[8]
print(a)

# del a
# print(a)
a.reverse()
print(a)

print(sorted(a))
a.sort(reverse=True)
print(a)

a.sort()
print(a)

print('元组')
d = ()  # 空元组
e = ('a')
f = ('a', ) # 元组中只包含一个元素时，需要在元素后面添加逗号
print(type(e))
print(type(f))

print('字典')
dict = {'name' : '张三'}
dict['age'] = 28
print(dict)
del dict['age']
print(dict)









