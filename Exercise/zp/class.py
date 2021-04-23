class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    aa = 'sss'
    def __init__(a, name, age):
        a.name = name
        a.age = age

    def study(b, course_name):
        # print('%s正在学习%s.' % (b.name, course_name))
        # print(b)
        return '%s正在学习%s.' % (b.name, course_name)

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

# p = Student('张三', [1,2,3])
# print(p.name)
# print(p.age)


# p1 = Student('李四', 25)
# # p1.name = '王五'
# # print(p1.name)
# print(p1.age)
# print(p1.study('ss'))

# 只能打印类开头，方法上面的第一段信息
# print(Student.__doc__)




















