import sys


def exception1():
    f = None
    try:
        f = open('writing2.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def exception2():
    a = 2
    b = 5
    c = 1
    try:
        c = b / a
        print(a, b, c)
    # except ZeroDivisionError:
    #     print('分母不能为0!')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # 抛出异常
        # raise
    # else:
    #     print('no exception')
    #     print(a, b, c)
    finally:
        print(a, b, c)


if __name__ == '__main__':
    # exception1()
    exception2()
