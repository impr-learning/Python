# test
"""
测试

a = 100
b = '100'
c = 12.33
d = 1 + 5j
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(int(b))

a = 3
print(a)
b = 2
print(b)
print('%d + %d = %d' % (a, b, a + b))
"""
"""
for tran in range(1, 10):
    for long in range(1, tran+1):
        print('%d * %d = %d' % (tran, long, tran * long), end='\t')
    print()
"""

a = 10
b = 3
a += b        # 相当于：a = a + b
print('%d * %d = %d' % (a, a+2, a*(a+2)))
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么
print('%d / %d / %d = %d' % (a, b, b, a/b/b))

flag1 = 1 == 2
flag2 = 1 != 2
print(flag1)
print(flag2)
print(flag1 and flag2)
print(flag1 or flag2)


# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# f = float(input('请输入圆的半径: '))
# print(type(f))
# print(type(2*3.14*f))
# per = 2*3.14*f
# area = 3.14*f*f
# print('圆的周长是：%.2f' % per)
# print('圆的面积是：%.2f' % area)

# year = int(input('请输入年份：'))
# for year in range(1994, 2021):
#     leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#     if leap_year:
#         print('%d' % year, ' 是闰年')
#     else:
#         print('%d' % year, ' 不是闰年')

# grade = float(input('请输入成绩：'))
# if grade > 90 or grade == 90:
#     print('A')
# elif grade >80 or grade == 80:
#     print('B')
# elif grade >70 or grade == 70:
#     print('C')
# elif grade >60 or grade == 60:
#     print('D')
# else:
#     print('E')

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     print('周长: %f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print('面积: %f' % (area))
# else:
#     print('不能构成三角形')


num = int(input('请输入整数：'))
str1 = str(num)
if str1 == str1[::-1]:
    print('%d ' % num, '是回文数')
else:
    print('%d ' % num, '不是回文数')




















