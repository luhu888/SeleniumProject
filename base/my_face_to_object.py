# coding=utf-8
# author:luhu
"""
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
    例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
    和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。

    Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调
    用基类中的同名方法。

    对象可以包含任意数量和类型的数据。
"""


# ----------------------------------------------------------------------------------------------------------------------
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

# 很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为__init__()的特殊方法（构造方法）
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

    def prt1(runoob):
        print(runoob)
        print(runoob.__class__)
# ----------------------------------------------------------------------------------------------------------------------

# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的
"""
    类的方法
    在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
"""


# ----------------------------------------------------------------------------------------------------------------------
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁, 体重是%dkg。" % (self.name, self.age, self.__weight))
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
    继承
    Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
        class DerivedClassName(BaseClassName1):
            <statement-1>
            .
            .
            .
            <statement-N>
    需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
    从左到右查找基类中是否包含方法。
    
    BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
"""


class People:    # 类定义
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
    多继承
    Python同样有限的支持多继承形式。多继承的类定义形如下例:
        class DerivedClassName(Base1, Base2, Base3):
            <statement-1>
            .
            .
            .
            <statement-N>
    需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
    从左到右查找父类中是否包含方法。
"""


class People:      # 类定义
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
    方法重写
    如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
"""


class Parent:  # 定义父类
    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def my_method(self):
        print('调用子类方法')
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
    类属性与方法
    类的私有属性
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
    类的方法
    在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
    self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
    类的私有方法
    __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


class Site:      # 类的私有方法实例
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    @staticmethod
    def __foo():  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
"""
    类的专有方法：
        __init__ : 构造函数，在生成对象时调用
        __del__ : 析构函数，释放对象时使用
        __repr__ : 打印，转换
        __setitem__ : 按照索引赋值
        __getitem__: 按照索引获取值
        __len__: 获得长度
        __cmp__: 比较运算
        __call__: 函数调用
        __add__: 加运算
        __sub__: 减运算
        __mul__: 乘运算
        __div__: 除运算
        __mod__: 求余运算
        __pow__: 乘方
"""
# 运算符重载
# Python同样支持运算符重载，我们可以对类的专有方法进行重载


class Vector:        # vector   矢量
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # 实例化类
    # x = MyClass()
    # # 访问类的属性和方法
    # print("MyClass 类的属性 i 为：", x.i)
    # print("MyClass 类的方法 f 输出为：", x.f())

    # t = Test()
    # t.prt()

    # x = Complex(3.0, -4.5)
    # print(x.r, x.i)  # 输出结果：3.0 -4.5

    # 实例化类
    # p = people('runoob', 10, 30)
    # p.speak()

    # s = Student('ken', 10, 60, 3)
    # s.speak()

    # test = Sample("Tim", 25, 80, 4, "Python")
    # test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

    # c = Child()  # 子类实例
    # c.my_method()  # 子类调用重写方法

    # counter = JustCounter()
    # counter.count()
    # counter.count()
    # print(counter.publicCount)
    # try:
    #     print(counter.__secretCount)  # 报错，实例不能访问私有变量
    # except AttributeError:
    #     print('实例类不能访问私有变量__secretCount')

    # x = Site('菜鸟教程', 'www.runoob.com')
    # x.who()        # 正常输出
    # x.foo()        # 正常输出
    # try:
    #     x.__foo()      # 报错
    # except AttributeError:
    #     print('外部不能调用私有方法__foo')

    # v1 = Vector(2, 10)
    # v2 = Vector(5, -2)
    # print(v1 + v2)

    a = People('孙悟空', 999)    # 重载__str__方法
    print(a)






