# -*- coding: utf-8 -*-
# __author__=luhu
"""
        继承 object 类的是新式类，不继承 object 类的是经典类，在 Python 2.7 里面新式类和经典
    类在多继承方面会有差异,B、C 是 A 的子类，D 多继承了 B、C 两个类，其中 C 重写了 A 中的
    foo() 方法。如果 A 是经典类（如下代码），当调用 D 的实例的 foo() 方法时，Python 会按照深
    度优先的方法去搜索 foo() ，路径是 B-A-C ，执行的是 A 中的 foo() ；如果 A 是新式类，当调用
    D 的实例的 foo() 方法时，Python 会按照广度优先的方法去搜索 foo() ，路径是 B-C-A ，执行的
    是 C 中的 foo() 。因为 D 是直接继承 C 的，从逻辑上说，执行 C 中的 foo() 更加合理，因此新
    式类对多继承的处理更为合乎逻辑。在 Python 3.x 中的新式类貌似已经兼容了经典类，无论 A 是否
    继承 object 类， D 实例中的 foo() 都会执行 C 中的 foo() 。但是在 Python 2.7 中这种差异仍然
    存在，因此还是推荐使用新式类，要继承 object 类。

"""


class A:
    def foo(self):
        print('called A.foo()')


class B(A):
    pass


class C(A):
    def foo(self):
        print('called C.foo()')


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    d.foo()
    a = A()
    a.foo()
