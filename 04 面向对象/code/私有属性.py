class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')
# 需要有两空行


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)

    # test = Test('hello')
    # test._Test__bar()
    # print(test._Test__foo)


if __name__ == "__main__":
    main()
