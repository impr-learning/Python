def one():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()


def two():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print('{}x{}={}\t'.format(j, i, i * j), end='')
            j += 1
        i += 1
        print()


def three():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        j = 1
        while j <= i:
            # %-3d 是控制输出结果占据3位，且从左面开始对齐
            print('%d*%d=%-3d' % (i, j, i * j), end='\t')
            j += 1
        print()


def four():
    print('\n'.join([' '.join([f"{j}x{i}={i * j}" for j in range(1, i + 1)]) for i in range(1, 10)]))


def main():
    # four
    print([i ** 2 for i in range(1, 10)])


if __name__ == '__main__':
    main()
