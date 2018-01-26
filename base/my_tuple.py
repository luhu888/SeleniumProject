# -*- coding: utf-8 -*-
# __author__=luhu
"""
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
"""


def tuple_create():
    tup1 = ()      # 创建空的元组tuple
    print(type(tup1))
    # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
    tup2 = (50,)
    print(type(tup2))


def tuple_visit():      # 元组可以使用下标索引来访问元组中的值
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7)
    print("tup1[0]: ", tup1[0])
    print("tup2[1:5]: ", tup2[1:5])


def tuple_alter():     # 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')
    # 以下修改元组元素操作是非法的。
    # tup1[0] = 100
    # 创建一个新的元组
    tup3 = tup1 + tup2
    print(tup3)


def tuple_delete():      # 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
    tup = ('Google', 'Runoob', 1997, 2000)
    print(tup)
    del tup
    try:
        print("删除后的元组 tup : ", tup)
    except UnboundLocalError:
        print("删除后的元组 tup : ", '元组已被删除')


"""
    元组运算符
    Python表达式	                结果	                         描述
    len((1, 2, 3))	                3	                             计算元素个数
    (1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	             连接
    ('Hi!',) * 4	                ('Hi!', 'Hi!', 'Hi!', 'Hi!')	 复制
    3 in (1, 2, 3)	                True	                         元素是否存在
    for x in (1, 2, 3): print x,	1 2 3	                         迭代
"""

"""
    元组索引，截取
    L = ('Google', 'Taobao', 'Runoob')
    Python表达式	  结果	                    描述
    L[2]	          'Runoob'	                读取第三个元素
    L[-2]	          'Taobao'	                反向读取；读取倒数第二个元素
    L[1:]	          ('Taobao', 'Runoob')	    截取元素，从第二个开始后的所有元素。
"""


def tuple_len():     # 计算元组元素个数
    tuple1 = ('Google', 'Runoob', 'Taobao')
    len(tuple1)


def tuple_max():     # 返回元组中元素最大值。
    tuple2 = ('5', '4', '8')
    max(tuple2)


def tuple_min():       # 返回元组中元素最小值。
    tuple2 = ('5', '4', '8', 'x')
    min(tuple2)


def tuple_tuple():      # 将列表转换为元组。
    list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
    tuple1 = tuple(list1)
    print(tuple1)


"""
    tuple元素不可变有一种特殊情况，当元素是可变对象时。对象内部属性是可以修改的！
    tuple的不可变限制只是在一个纬度上：元素的类型。实现理解，tuple的元素所保存的内容（数值或内存地址）
    是不允许修改的，但地址映射的对象自身是可以修改的。
"""


def tuple_alter2():
    a = (1, [3, 2])
    a[1][0] = 1
    print(a)
    a[1].append(3)
    print(a)
    del a[1][2]
    print(a)
    try:
        del a[1]
        print(a)
    except TypeError:
        print("元组不支持删除操作")

    del a[1][1]
    del a[1][0]
    print(a)


if __name__ == '__main__':
    # tuple_delete()
    # tuple_alter()
    # tuple_create()
    # tuple_visit()
    # tuple_len()
    # tuple_max()
    # tuple_min()
    # tuple_tuple()
    tuple_alter2()



























































































