# coding=utf-8
# author:luhu

"""
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，
    或索引，第一个索引是0，第二个索引是1，依此类推。
    Python有6个序列的内置类型，但最常见的是列表和元组。
    序列都可以进行的操作包括索引，切片，加，乘，检查成员。
    此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
    列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
    列表的数据项不需要具有相同的类型
"""
def list_update_and_del():
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    print("list1[0]: ", list1[0])
    print("list2[1:5]: ", list2[1:5])
    list1[2] = 2005
    print("更新后的第三个元素为 : ", list1[2])    # 更新列表
    del list1[2]
    print("删除第三个元素 : ", list1)    # 删除列表元素


"""
列表脚本操作符
Python表达式	                         结果                  	                描述
len([1, 2, 3])	                         3	                                    长度
[1, 2, 3] + [4, 5, 6]	                 [1, 2, 3, 4, 5, 6]	                    组合
['Hi!'] * 4             	             ['Hi!', 'Hi!', 'Hi!', 'Hi!']	        重复
3 in [1, 2, 3]	                         True	                                元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	 1 2 3	                                迭代
"""

"""
列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
Python表达式	  结果	                    描述
L[2]	          'Taobao'	                读取第三个元素
L[-2]	          'Runoob'	                从右侧开始读取倒数第二个元素: count from the right
L[1:]	          ['Runoob', 'Taobao']	    输出从第二个元素开始后的所有元素
"""


def list_nested():
    squares = [1, 4, 9, 16, 25]
    print(squares + [36, 49, 64, 81, 100])
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]       # 列表支持嵌套操作，将列表嵌套在列表中
    print(x)


"""
    len() 方法返回列表元素个数。
    语法
    len(list)
    参数
    list -- 要计算元素个数的列表。
    返回值
    返回列表元素个数。
"""


def list_len():
    list1 = ['Google', 'Runoob', 'Taobao']
    print(len(list1))
    list2 = list(range(5))    # 创建一个 0-4 的列表
    print(len(list2))


"""
    max() 方法返回列表元素中的最大值。   
    语法  
    max(list)
    参数
    list -- 要返回最大值的列表。
    返回值
    返回列表元素中的最大值。
"""


def list_max():
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1 最大元素值 : ", max(list1))
    print("list2 最大元素值 : ", max(list2))


"""
    min() 方法返回列表元素中的最小值。
    语法
    min(list)
    参数
    list -- 要返回最小值的列表。
    返回值
    返回列表元素中的最小值。
"""


def list_min():
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1 最小元素值 : ", min(list1))
    print("list2 最小元素值 : ", min(list2))


"""
    list() 方法用于将元组转换为列表。
    注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
    语法
    list( seq )
    参数
    list -- 要转换为列表的元组。
    返回值
    返回列表。
"""


def list_list():
    tuple = (123, 'Google', 'Runoob', 'Taobao')
    list1 = list(tuple)
    print("列表元素 : ", list1)

    str = "Hello World"
    list2 = list(str)
    print("列表元素 : ", list2)


"""
    append() 方法用于在列表末尾添加新的对象。
    语法
    list.append(obj)
    参数
    obj -- 添加到列表末尾的对象。
    返回值
    该方法无返回值，但是会修改原来的列表。
"""

list3 = ['Google', 'Runoob', 'Taobao']


def list_append():
    list3.append('Baidu')
    print("更新后的列表 : ", list3)


"""
    count() 方法用于统计某个元素在列表中出现的次数。
    语法
    list.count(obj)
    参数
    obj -- 列表中统计的对象。
    返回值
    返回元素在列表中出现的次数。
"""


def list_count():
    list4 = [123, 'Google', 'Runoob', 'Taobao', 123]
    print("123 元素个数 : ", list4.count(123))
    print("Runoob 元素个数 : ", list4.count('Runoob'))


"""
    extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。  
    语法
    list.extend(seq)
    参数
    seq -- 元素列表。
    返回值
    该方法没有返回值，但会在已存在的列表中添加新的列表内容。
"""


def list_extend():
    list1 = ['Google', 'Runoob', 'Taobao']
    list2 = list(range(5))     # 创建 0-4 的列表
    list1.extend(list2)  # 扩展列表
    print("扩展后的列表：", list1)


"""
    index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
    语法
    list.index(obj)
    参数
    obj -- 查找的对象。
    返回值
    该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
"""


def list_index():
    list1 = ['Google', 'Runoob', 'Taobao']
    print('Runoob索引值为', list1.index('Runoob'))
    print('Taobao索引值为', list1.index('Taobao'))


"""
    insert() 函数用于将指定对象插入列表的指定位置。
    语法
    list.insert(index, obj)
    参数
    index -- 对象obj需要插入的索引位置。
    obj -- 要插入列表中的对象。
    返回值
    该方法没有返回值，但会在列表指定位置插入对象。
"""


def list_insert():
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.insert(1, 'Baidu')
    print('列表插入元素后为 : ', list1)


"""
    pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    语法
    list.pop(obj=list[-1])
    参数
    obj -- 可选参数，要移除列表元素的对象。
    返回值
    该方法返回从列表中移除的元素对象。
"""


def list_pop():
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.pop()
    print("列表现在为 : ", list1)
    list1.pop(1)
    print("列表现在为 : ", list1)


"""
    remove() 函数用于移除列表中某个值的第一个匹配项。
    语法
    list.remove(obj)
    参数
    obj -- 列表中要移除的对象。
    返回值
    该方法没有返回值但是会移除两种中的某个值的第一个匹配项。
"""


def list_remove():
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu', 'Taobao']
    list1.remove('Taobao')
    print("列表现在为 : ", list1)
    list1.remove('Baidu')
    print("列表现在为 : ", list1)


"""
    reverse() 函数用于反向列表中元素。
    语法
    list.reverse()
    参数
    NA。
    返回值
    该方法没有返回值，但是会对列表的元素进行反向排序。
"""


def list_reverse():
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.reverse()
    print("列表反转后: ", list1)


"""
    sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    语法
    list.sort([func])
    参数
    func -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
    返回值
    该方法没有返回值，但是会对列表的对象进行排序。
"""


def list_sort():
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.sort()
    print("列表排序后 : ", list1)


"""
    clear() 函数用于清空列表，类似于 del a[:]。
    语法
    list.clear()
    参数
    无。
    返回值
    该方法没有返回值
"""


def list_clear():
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.clear()
    print("列表清空后 :", list1)


"""
    copy() 函数用于复制列表，类似于 a[:]。
    语法
    list.copy()
    参数
    无。
    返回值
    返回复制后的新列表。
"""


def list_copy():
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list2 = list1.copy()
    print("list2 列表: ", list2)


'''
copy()和直接=赋值的区别
下例可以看出，使用=直接赋值，是引用赋值，更改一个，另一个同样会变, 例子中的a,b改变两次都影响到了对方
copy() 则顾名思义，复制一个副本，原值和新复制的变量互不影响
'''


def compare_identical_with_copy():
    a = [0, 1, 2, 3, 4, 5]
    b = a
    c = a.copy()
    del a[1]
    print('del a[1]后的值:   ', 'a=', a, 'b=', b, 'c=', c)
    b.remove(4)
    print('b.remove(4)后的值:', 'a=', a, 'b=', b, 'c=', c)
    c.append(9)
    print('c.append(9)后的值:', 'a=', a, 'b=', b, 'c=', c)
    print(id(a))
    print(id(c))


vec = [2, 4, 6]
a = [3*x for x in vec]      # 列表推导式
print(a)
# if __name__ == '__main__':
    # compare_identical_with_copy()
    # list_update_and_del()
    # list_nested()
    # list_len()
    # list_max()
    # list_min()
    # list_list()
    # list_append()
    # list_count()
    # list_extend()
    # list_index()
    # list_insert()
    # list_pop()
    # list_remove()
    # list_reverse()
    # list_sort()
    # list_clear()
    # list_copy()













































