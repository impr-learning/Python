# 补充
### 1、class Student(object):
    (object) 可以写也可以不写
    区别：class Student 和 class Student(object)
    python2.x: 不继承object对象，只拥有了__doc__ , __module__ 和 自己定义的name变量, 也就是说这个类的命名空间只有三个对象可以操作. 继承了object对象，拥有了好多可操作对象，这些都是类中的高级特性。最典型的student.__class__来定位类的名称
    python3.x: 默认就帮你加载了object了（即便你没有写上object）
### 2、初始化方法__init__(self):
    1. self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
    2. 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。但是self不是python的关键字，所以把self换成其他词也可以正常执行。
    3. 创建实例的时候,self不需要传，Python解释器自己会把实例变量传进去：
### 3、

