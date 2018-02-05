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


def my_exchange1():      # 使用临时变量进行变量交换
    x = input('输入x的值：')
    y = input('输入y的值：')
    temp = x
    x = y
    y = temp
    print(x, y)


def my_exchange2():       # 不使用临时变量直接进行变量交换
    x = input('输入x的值：')
    y = input('输入y的值：')
    x, y = y, x
    print(x, y)


"""
    如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
    1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


def my_check_armstrong():
    # Python 检测用户输入的数字是否为阿姆斯特朗数

    # 获取用户输入的数字
    num = int(input("请输入一个数字: "))

    # 初始化变量 sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    # 输出结果
    if num == sum:
        print(num, "是阿姆斯特朗数")
    else:
        print(num, "不是阿姆斯特朗数")


def my_sys_convert():
    dec = int(input("输入数字："))

    print("十进制数为：", dec)
    print("转换为二进制为：", bin(dec))
    print("转换为八进制为：", oct(dec))
    print("转换为十六进制为：", hex(dec))


def my_asc2_character():
    # 用户输入字符
    c = input("请输入一个字符: ")
    # 用户输入ASCII码，并将输入的数字转为整型
    a = int(input("请输入一个ASCII码: "))
    print(c + " 的ASCII 码为", ord(c))
    print(a, " 对应的字符为", chr(a))


"""
    欧几里得算法：
    两个数的最大公约数可以使用 欧几里得算法实现。即两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。
"""


def my_gcd():        # greatest common divisor    最大公约数
    n1 = int(input('请输入一个正整数：'))
    n2 = int(input('请输入另一个正整数：'))
    if n1 == 0:
        n1, n2 = n2, n1
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


def my_lcm():
    n1 = int(input('请输入一个正整数：'))
    n2 = int(input('请输入另一个正整数：'))
    temp1 = n1
    temp2 = n2
    if n1 == 0:
        n1, n2 = n2, n1
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return int(temp1 * temp2 / n1)


def my_calendar():
    # 引入日历模块
    import calendar

    # 输入指定年月
    yy = int(input("输入年份: "))
    mm = int(input("输入月份: "))

    # 显示日历
    print(calendar.month(yy, mm))


if __name__ == '__main__':
    # my_square_root()
    # my_square_root2()
    # my_square_triangle()
    # my_judge_leap_year()
    # my_judge_prime_number()
    # my_exchange2()
    # my_exchange1()
    # my_asc2_character()
    # print(my_gcd())
    # print(my_lcm())
    my_calendar()





















