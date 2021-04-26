# range 用法 range(start, stop[, step])
# format 用法 print('{}{}'.format('hello', ' world') 连接字符串
for yy in range(1, 10):
    for jj in range(1, yy + 1):
        print('{} * {} = {}'.format(jj, yy, jj * yy), end='')
    print()
