# coding=utf-8
# author:luhu
"""
    Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
    注意：
    1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    3、在Python中没有switch – case语句。
"""
from pip._vendor.distlib.compat import raw_input


def if_get_evaluate(result):
    if result >= 90:    # 分支和循环，分支就用if，循环就用for
        print('优秀')
    elif 80 <= result < 90:
        print('良好')
    elif 60 <= result < 80:
        print('一般')
    elif result < 60:
        print('不及格')


def if_in_sequence():        # Sequence    序列
    strings = 'hello python'
    for i in strings:
        print(i, end=',')

    for i in range(1, 10, 2):    # range(start，end，scan)表示一连串数，start表示起始数，end表示结束位置，scan表示步长
        print(i, end=',')


def dog_age():
    print("=======欢迎进入狗狗年龄对比系统========")
    while True:
        try:
            age = raw_input("请输入您家狗的年龄:")
            print("系统在奋力计算中。。。。。。")
            age = float(age)
            if age <= 0:
                print("您在逗我？")
            elif age == 1:
                print("相当于人类14岁")
                break
            elif age == 2:
                print("相当于人类22岁")
                break
            else:
                human = 22 + (age - 2)*5
                print("相当于人类：", human)
                break
        except ValueError:
            print("输入不合法，请输入有效年龄")
    # 退出提示
    input("点击 enter 键退出")


def while_loop():
    n = 100
    sum = 0
    counter = 1
    while counter <= n:
        sum = sum + counter
        counter += 1
    print("1 到 %d 之和为: %d" % (n, sum))


def while_endless():      # 我们可以通过设置条件表达式永远不为 false 来实现无限循环,无限循环在服务器上客户端的实时请求非常有用。
    var = 1
    while var == 1:  # 表达式永远为 true
        num = int(input("输入一个数字  :"))
        print("你输入的数字是: ", num)

    print("Good bye!")


def while_else(count):
    while count < 5:
        print(count, "小于5")
        count = count + 1
    else:
        print(count, "大于等于5")


def while_simple():    # 简单语句组,类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
        flag = 1
        while flag: print('欢迎访问菜鸟教程!')
        print("Good bye!")


# for循环可以遍历任何序列的项目，如一个列表或者一个字符串
def for_loop():
    languages = ["C", "C++", "Perl", "Python"]
    for x in languages:
        print(x)


def for_break():
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        if site == "Runoob":
            print("找到菜鸟教程!")
            break                    # break 语句用于跳出当前循环体
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")


# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
def for_continue():
    for letter in 'Runoob':     # 第一个实例
        if letter == 'o':        # 字母为 o 时跳过输出
            continue
        print('当前字母 :', letter)


def prime_number():
    for n in range(2, 9000):
        for x in range(2, n):
            if n % x == 0:
                # print(n, '等于', x, '*', n//x)
                break
        else:
            # 循环中没有找到元素
            print(n, ' 是质数')


# pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
def for_pass():
    for letter in 'Runoob':
        if letter == 'o':
            pass
            print('执行 pass 块')
        print('当前字母 :', letter)

    print("Good bye!")


def for_enumerate():
    sequence = [12, 34, 34, 23, 45, 76, 89]

    for i, j in enumerate(sequence):
        dict1 = {i: j}
        print(dict1)
        print(type(dict1))


def print_isosceles_triangle(n):
    for i in range(1, n):
        print('-'*(n-i-1)+'*'*((i-1)*2+1)+'-'*(n-i-1))


if __name__ == '__main__':
    # if_get_evaluate(88)
    # if_in_sequence()
    # dog_age()
    # while_loop()
    # while_endless()
    # for_continue()
    # prime_number()
    # for_enumerate()
    print_isosceles_triangle(10)


















