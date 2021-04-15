"""
# 寻找水仙花数
for i in range(100, 1000):
    low = i % 10
    mid = i % 100 // 10
    high = i // 100
    num = low ** 3 + mid ** 3 + high ** 3
    if num == i:
        print(i)


# 百鸡百钱 都不为空
for big in range(1, 20):
    for mid in range(1, 31):
        small = 100-big*5-mid*3
        if small > 0:
            print('%d %d %d' % (big, mid, small))


# 摇骰子
import random

touzi = random.randint(1, 6) + random.randint(1, 6)
print('第一次摇出的点数是:', touzi)
if touzi == 7 or touzi == 11:
    print('玩家胜利')
elif touzi == 2 or touzi == 3 or touzi == 12:
    print('庄家胜利')
else:
    count = 2
    while count < 10:
        second = random.randint(1, 6) + random.randint(1, 6)
        print('第', count, '次摇出的点数是:', second)
        if second == 7:
            print('庄家胜利')
            break
        elif second == touzi:
            print('玩家胜利')
            break
        else:
            count += 1
    if count == 10:
        print('未分出胜负')



# 斐波那契数列
first = 1
second = 1
count = 2
print(first)
print(second)

while count < 20:
    three = first + second
    print(three)
    first = second
    second = three
    count += 1



# 完美数  出本身外，所有的约数之和等于其本身
for i in range(2, 10001):
    num = 1
    string = '1'
    for j in range(1, i-1):
        # string = '1'
        if i % j == 0 and j != 1:
            string = string + ' + ' + str(j)
            num += j
    if num == i:
        print(string, '=', i)

"""

# 素数
# for i in range(2, 101):
#     num = 1
#     while num < i:
#         if i % num == 0 and num != 1:

