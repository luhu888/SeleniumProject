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


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为__init__()的特殊方法（构造方法）


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5

# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的


class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()






















