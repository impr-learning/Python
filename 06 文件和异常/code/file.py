# 读python.txt，打印
def read_file():
    #   r模式。只读
    f = open('writing.txt', 'r', encoding='utf-8')
    #   r+模式。文件指针将会放在文件的开头
    # f = open('writing.txt', 'r+', encoding='utf-8')
    #   w+模式。对于存在的文件会将原来内容删除
    # f = open('writing.txt', 'w+', encoding='utf-8')
    #   a+模式。文档说可读，这里测试可以打开，但无法读取内容，不会报错
    # f = open('writing.txt', 'a+', encoding='utf-8')
    print(f.read())
    f.close()


def writing_file():
    #   x模式。只写，对于已存在的文件会报错
    f = open('writing.txt', 'x', encoding='utf-8')
    # f.write('hello world!')
    #   r+模式。文件指针将会放在文件的开头。  会等字符长度覆盖，不是插入。
    # f = open('writing.txt', 'r+', encoding='utf-8')
    # f.write('mode: r+')
    #   w模式。对于不存在的文件创建，存在的删除原来的再写入。
    # f = open('writing.txt', 'w', encoding='utf-8')
    # f.write('mode: w')
    #   w+模式。对于不存在的文件创建，存在的删除原来的再写入。
    # f = open('writing.txt', 'w+', encoding='utf-8')
    # f.write('mode: w+')
    #   a模式。对于不存在的文件会创建，对于存在的文件会从文件结尾开始加内容
    # f = open('writing.txt', 'a', encoding='utf-8')
    # f.write('mode: a')
    #   a+模式。对于不存在的文件会创建，对于存在的文件会从文件结尾开始加内容
    # f = open('writing.txt', 'a+', encoding='utf-8')
    # f.write('''mode: a+''')
    # 此处读不到
    # print(f.read())
    f.close()


def copy_img():
    with open('../file_zh.png', 'rb') as fs1:
        data = fs1.read()
        print(type(data))  # <class 'bytes'>
    with open('file_copy.png', 'wb') as fs2:
        fs2.write(data)


if __name__ == '__main__':
    read_file()
    # writing_file()
    # read_file()
    # copy_img()
