# coding=utf-8
# author:luhu
# 构建庞大复杂的项目得结合函数，类和方法的使用


def my_add(a, b):
    # print a+b    # 更多的情况下，add（）函数不会直接打印结果，
    return a+b     # 而是将结果通过return关键字返回


def my_add2(a=3, b=4):       # 如果调用函数不传参数，可以设置参数默认值
    return a+b


print(my_add2())
print(my_add2(2, 4))


class Calculate:
    def __init__(self):
        pass

    @staticmethod
    def my_add(a, b):      # 创建一个Calculate类，在类下面创建一个my_add（）方法，方法的创建同样
        return a+b         # 使用关键字def，唯一不同的是方法必须有一个且必须是第一个默认参数self，但是这个参数不用传值


count = Calculate()
print(count.my_add(2, 5))


class MyCalculate(Calculate):    # My_Calculate继承Calculate类，所以可以使用Calculate里的方法
    @staticmethod
    def my_sub(a, b):
        return a-b


count2 = MyCalculate()
print(count2.my_sub(7, 9))
print(count2.my_add(7, 6))








