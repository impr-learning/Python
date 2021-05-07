# 正则
import re


class Test:
    def __init__(self, str):
        self.str = str

    def main(self):
        # 虽然re.compile()好处很多，但是在cpython中其实你用不用都无所谓
        pattern = re.compile(r'(\d{3})-(\d{3,8})')
        res = re.match(pattern, self.str)
        res1 = re.match(r'(\d{3})-(\d{3,8})', self.str)
        print(res)
        print(res1)

    def search(self):
        res = re.search(r'(\d{3})-(\d{3,8})', self.str)
        print(res)

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
        print(res)

    def finditer(self):
        res = re.finditer(r'\d{3}', self.str)
        test_list = []
        for res_obj in res:
            # 正则表达式中，group（）用来提出分组截获的字符串，（）用来分组
            test_list.append(res_obj.group())
        print(test_list)


if __name__ == '__main__':
    s = '010-123045ns22-1232-32-3213124'
    t1 = Test(s)
    t1.main()
    t1.search()
    t1.split()
    t1.sub()
    t1.full_match()
    t1.find_all()
    t1.finditer()
