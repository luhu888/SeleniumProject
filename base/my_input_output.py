# -*- coding: utf-8 -*-
# __author__=luhu
import math

s = 'Hello Python3.5!'


def my_input():
    print(str(s))      # 函数返回一个用户易读的表达形式
    print(repr(s))     # 产生一个解释器易读的表达形式


def my_ljust():     # 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
    for i in range(1, 11):
        print(repr(i).ljust(2), repr(i**2).ljust(3), repr(i**3))


def my_format():    # 与上述方法效果相同
    for i in range(1, 11):   # 大括号中的0,2,1表示格式化的位置
        print('{0:2d} {2:4d} {1:3d}'.format(i, i**2, i**3))


def my_keyword_format():     # 带关键字参数的格式化
    print('名字:{name} 年龄:{age}'.format(name='luhu', age=55))


def my_format_function():
    print('常量 PI 的值近似为:{!s}。'.format(math.pi))    # '!s' (使用 str())
    print('常量 PI 的值近似为:{!r}。'.format(math.pi))    # '!r' (使用 repr())
    print('常量 PI 的值近似为:{!a}。'.format(math.pi))    # '!a' (使用 ascii())
    print('常量 PI 的值近似为:{0:.3f}。'.format(math.pi))  # 可选项 ':' 和格式标识符可以跟着字段名,保留3位小数
    print('常量 PI 的值近似为:{0:5d}这就是pi的近似值。'.format(12))   # 在 ':' 后传入一个整数（或者整数后加d）, 可以保证该域至少有这么多的宽度


def my_zfill():     # zfill(), 它会在数字的左边填充 0
    for i in range(1, 11):
        print(repr(i).zfill(4), repr(i**2).zfill(4), repr(i**3).zfill(4))


def my_format_dictionary():
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    # print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
    print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))


if __name__ == '__main__':
    # my_input()
    # print(my_ljust())
    # my_format()
    # my_zfill()
    # my_keyword_format()
    # my_format_function()
    my_format_dictionary()








































