# coding=utf-8
# author:luhu
"""
    字典是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
"""
import copy

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}


def dictionary_visit():     # 访问字典里的值,如果用字典里没有的键访问数据，会输出KeyError错误
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])


def dictionary_alter():
    dict['Age'] = 8    # 更新 Age
    dict['School'] = "菜鸟教程"  # 添加信息
    print("dict['Age']: ", dict['Age'])
    print("dict['School']: ", dict['School'])


def dictionary_delete():
    del dict['Name']      # 删除键 'Name'
    # dict.clear()          # 清空字典
    # del dict              # 删除字典
    print("dict['Age']: ", dict['Age'])
    try:
        print("dict['Name']: ", dict['Name'])
    except KeyError:
        print("Name元素已被删除")


"""
    字典键的特性
    字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
    两个重要的点需要记住：
    1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""


def dictionary_speciality1():
    dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
    print("dict['Name']: ", dict['Name'])


def dictionary_speciality2():
    try:
        dict = {['Name']: 'Runoob', 'Age': 7}
        print("dict['Name']: ", dict['Name'])
    except TypeError:
        print("字典的键必须不可变")


def dictionary_len():    # 计算字典元素个数，即键的总数。
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(len(dict))


def dictionary_str():     # 输出字典，以可打印的字符串表示。
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(str(dict))


def dictionary_type():       # 返回输入的变量类型，如果变量是字典就返回字典类型。
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(type(dict))


def dictionary_clear():      # clear() 函数用于删除字典内所有元素。
    dict = {'Name': 'Zara', 'Age': 7}
    print("字典长度 : %d" % len(dict))
    dict.clear()
    print("字典删除后长度 : %d" % len(dict))


def dictionary_copy():      # copy() 函数返回一个字典的浅拷贝
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    dict2 = dict1.copy()
    print("新复制的字典为 : ", dict2)


"""
    直接赋值：其实就是对象的引用（别名）。
    浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
    深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
"""


def compare_identically_equal_with_copy():
    a = [1, 2, 3, 4, ['a', 'b']]     # 原始对象
    b = a                       # 赋值，传对象的引用
    c = copy.copy(a)            # 对象拷贝，浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）
    d = copy.deepcopy(a)        # 对象拷贝，深拷贝,a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的
    a.append(5)                 # 修改对象a
    a[4].append('c')            # 修改对象a中的['a', 'b']数组对象
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)


def dictionary_fromkeys():      # fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
    seq = ('name', 'age', 'sex')
    dict = dict.fromkeys(seq)
    print("新的字典为 : %s" % str(dict))
    dict = dict.fromkeys(seq, 10)
    print("新的字典为 : %s" % str(dict))


"""
    get()函数返回指定键的值，如果值不在字典中返回默认值。
    语法
    dict.get(key, default=None)
    参数
    key -- 字典中要查找的键。
    default -- 如果指定键的值不存在时，返回该默认值值。
    返回值
    返回指定键的值，如果值不在字典中返回默认值 None。
"""


def dictionary_get():
    dict = {'Name': 'Runoob', 'Age': 27}
    print("Age 值为 : %s" % dict.get('Age'))
    print("Sex 值为 : %s" % dict.get('Sex', "NA"))


"""
    Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
    语法
    key in dict
    参数
    key -- 要在字典中查找的键。
    返回值
    如果键在字典里返回true，否则返回false。
"""


def dictionary_in_dict():
    dict = {'Name': 'Runoob', 'Age': 7}
    # 检测键 Age 是否存在
    if 'Age' in dict:
        print("键 Age 存在")
    else:
        print("键 Age 不存在")
    # 检测键 Sex 是否存在
    if 'Sex' in dict:
        print("键 Sex 存在")
    else:
        print("键 Sex 不存在")


"""
    items() 方法以列表返回可遍历的(键, 值) 元组数组。
    语法
    dict.items()
    参数
    NA。
    返回值
    返回可遍历的(键, 值) 元组数组。
"""


def dictionary_items():
    dict = {'Name': 'Runoob', 'Age': 7}
    for i, j in dict.items():
        print(i, ":\t", j)


"""
    keys() 方法以列表返回一个字典所有的键。
    语法
    dict.keys()
    参数
    NA。
    返回值
    返回一个字典所有的键。
"""


def dictionary_keys():
    dict = {'Name': 'Runoob', 'Age': 7}
    print("字典所有的键为 : %s" % dict.keys())


"""
    Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。  
    语法
    dict.setdefault(key, default=None)
    参数
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。
    返回值
    如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，
    default 默认值为 None。
"""


def dictionary_setdefault():
    dict = {'Name': 'Runoob', 'Age': 7}
    print("Age 键的值为 : %s" % dict.setdefault('Age', None))
    print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
    print("新字典为：", dict)


"""
    update() 函数把字典dict2的键/值对更新到dict里。
    语法
    dict.update(dict2)
    参数
    dict2 -- 添加到指定字典dict里的字典。
    返回值
    该方法没有任何返回值。
"""


def dictionary_update():
    dict = {'Name': 'Runoob', 'Age': 7}
    dict2 = {'Sex': 'female'}
    dict.update(dict2)
    print("更新字典 dict : ", dict)


"""
    values() 方法以列表返回字典中的所有值。
    语法
    dict.values()
    参数
    NA。
    返回值
    返回字典中的所有值
"""


def dictionary_value():
    dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
    print("字典所有值为 : ", list(dict.values()))


"""
    Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    语法
    pop(key[,default])
    参数
    key: 要删除的键值
    default: 如果没有 key，返回 default 值
    返回值
    返回被删除的值。
"""


def dictionary_pop():
    site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj = site.pop('name1', '要删除的元素不存在')
    print(pop_obj)


"""
    Python 字典 popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。
    如果字典已经为空，却调用了此方法，就报出KeyError异常。
    语法
    popitem()
    参数
    无
    返回值
    返回一个键值对(key,value)形式。
"""


def dictionary_popitems():
    site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj = site.popitem()
    print(pop_obj)
    print(site)


if __name__ == '__main__':
    # dictionary_visit()
    # dictionary_alter()
    # dictionary_delete()
    # dictionary_speciality1()
    # dictionary_speciality2()
    # dictionary_items()
    dictionary_popitems()


































































