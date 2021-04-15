# for循环
sum = 0
# 0到100
for x in range(101):
    sum += x
print(sum)
# 99到100
sum = 0
for x in range(99,101):
    sum += x
print(sum)
# 1到100 偶数和
sum = 0
for x in range(1,101,2):
    sum += x
print(sum)
# while循环
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("Good bye!")




