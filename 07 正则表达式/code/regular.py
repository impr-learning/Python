# 正则
import re


class Test:
    def __init__(self, str):
        self.str = str

    def main(self):
        # re.compile()只是规范，放在循环体里面正则匹配的时候不会多次编译     34
        pattern = re.compile(r'(\d{3})-(\d{3,8})')
        res = re.match(pattern, self.str)
        res1 = re.match(r'(\d{3})-(\d{3,8})', self.str)
        print(res)
        print(res1.group())
        print(res.span())
        print(res.end())

    @staticmethod
    def search(str):
        res = re.search(r'(\d{3})-(\d{3,8})', str)
        print(res)
        print(res.group())
        print(res.start())

    def split(self):
        res = re.split('0', self.str, 0)
        print(res)

    def sub(self):
        res = re.sub(r'\d', '我', self.str, 3)
        print(res)

    def full_match(self):
        res = re.fullmatch(r'(\d{3})-(\d{3,8})', self.str)
        print(res)

    def find_all(self):
        res = re.findall(r'(\d{3})-(\d{2})', self.str)
        for result in res:
            print(result)
            print(result[0], result[1])

    def finditer(self):
        res = re.finditer(r'(\d{3})', self.str)
        print(res)
        test_list = []
        for res_obj in res:
            # 正则表达式中，group（）用来提出分组截获的字符串，（）用来分组
            test_list.append(res_obj.group())
        print(test_list)


if __name__ == '__main__':
    s = '010-123045ns22-1232-32-3213124'
    t1 = Test(s)
    # t1.main()
    Test.search('ss001-1234562')
    # t1.split()
    # t1.sub()
    # t1.full_match()
    t1.find_all()
    t1.finditer()
