# -*- coding: utf-8 -*-
# __author__=luhu
import cmath


def my_square_root():
    num = float(input('请输入一个数字： '))
    num_sqrt = num ** (1/2)
    print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))


"""
    通过用户输入一个数字，并使用指数运算符 ** 来计算改数的平方根。
    该程序只适用于正数。负数和复数可以使用以下的方式
"""


def my_square_root2():
    num = int(input("请输入一个数字: "))
    num_sqrt = cmath.sqrt(num)
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))


def my_square_triangle():      # 求三角形面积
    a = float(input('输入三角形第一边长：'))
    b = float(input('输入三角形第二边长：'))
    c = float(input('输入三角形第三边长：'))
    while a + b <= c or a + c <= b or b + c <= a:
        print('输入的边构不成三角形，请重新输入！')
        a = float(input('输入三角形第一边长：'))
        b = float(input('输入三角形第二边长：'))
        c = float(input('输入三角形第三边长：'))

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('三角形面积为：%0.2f' % area)


def my_judge_leap_year():
    year = int(input("请输入一个年份："))
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))


def my_judge_prime_number():
    num = int(input("请输入一个数字: "))
    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "不是质数")
                print(i, "乘于", num // i, "是", num)
                break
        else:
            print(num, "是质数")

    # 如果输入的数字小于或等于 1，不是质数
    else:
        print(num, "不是质数")


if __name__ == '__main__':
    # my_square_root()
    # my_square_root2()
    # my_square_triangle()
    # my_judge_leap_year()
    my_judge_prime_number()

























