# -*- coding: utf-8 -*-
# __author__=luhu
# 在 python 中，类型属于对象，变量是没有类型的：
"""
    函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
    函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。
    但你也可以自己创建函数，这被叫做用户自定义函数。

    定义一个函数

    你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""
a = [1, 2, 3]
a = "Runoob"
"""
    以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个
    对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 
    被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，
    只是其内部的一部分值被修改了。
    python 函数的参数传递：
    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在
    fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响;
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


def change_obj(my_list):      # 传可变对象的实例
    my_list.append([1, 2, 3, 4])
    print("函数内取值: ", my_list)


def print_out_change_obj():
    # 调用change_obj函数
    my_list = [10, 20, 30]
    change_obj(my_list)
    print("函数外取值: ", my_list)


"""
以下是调用函数时可使用的正式参数类型：
必需参数    必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

关键字参数  关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

默认参数    调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
注意默认参数放在最后

不定长参数    你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名

"""


def print_info1(name, age=35):   # 默认参数实例
    print("名字: ", name)
    print("年龄: ", age)


def print_info2(arg1, *vartuple):    # 不定长参数实例
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)


"""
    python 使用 lambda 来创建匿名函数。
    所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    lambda 只是一个表达式，函数体比 def 简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""

sum = lambda arg1, arg2: arg1 + arg2     # 匿名函数实例


"""
return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值
"""


def my_sum(arg1, arg2):
    total = arg1 + arg2
    print("函数内 : ", total)
    return total    # 调用my_sum方法后返回total值，使用了return让my_sum方法有返回值，外部调用才有值


"""
    变量作用域
    Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
    变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
    L （Local） 局部作用域
    E （Enclosing） 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域
    以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


if True:
    msg = 'I am from Runoob'      # 实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
print(msg)                       # 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问


def test():
    if True:
        msg = 'I am from Runoob'


try:
    print(msg)
except NameError:
    print('msg 定义在函数中，它就是局部变量，外部不能访问')


total = 0    # 这是一个全局变量


def my_sum2(arg1, arg2):
    total = arg1 + arg2    # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
my_sum2(10, 20)
print("函数外是全局变量 : ", total)







if __name__ == '__main__':
    # print_out_change_obj()
    # 调用print_info1函数
    # print_info1(age=50, name="runoob")
    # print_info1(name="runoob")
    # # 调用print_info2 函数
    # print_info2(10)
    # print_info2(70, 60, 50)
    # # 调用sum匿名函数
    # print("sum匿名函数相加后的值为 : ", sum(10, 20))
    # print("sum匿名函数相加后的值为 : ", sum(20, 20))
    # 调用sum函数
    # total = my_sum(10, 20)
    # print("函数外 : ", total)
    my_sum2(10, 20)
    print("函数外是全局变量 : ", total)


































































