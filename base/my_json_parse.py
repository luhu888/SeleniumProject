# -*- coding: utf-8 -*-
# __author__=luhu
"""
    JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
    Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
    在json的编解码过程中，python 的原始类型与json类型会相互转换，具体的转化对照如下：

    Python 编码为 JSON 类型转换对应表：
    Python	                                    JSON
    dict	                                    object
    list, tuple	                                array
    str	                                        string
    int, float, int- & float-derived Enums	    number
    True	                                    true
    False	                                    false
    None	                                    null

    JSON 解码为 Python 类型转换对应表：
    JSON	                Python
    object	                dict
    array	                list
    string	                str
    number (int)	        int
    number (real)	        float
    true	                True
    false	                False
    null	                None
"""
import json  # Python 字典类型转换为 JSON 对象

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoobww.com'
}


def my_dic_to_json():
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoobww.com'
    }
    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)
# 通过输出的结果可以看出，简单类型通过编码后跟其原始的repr()输出结果非常相似


def my_json_to_data():
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoobww.com'
    }

    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])


# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
# 写入数据
def my_write_json():
    with open('base_files/data3.json', 'w') as f:
        json.dump(data, f)


# 读取数据
def my_read_json():
    try:
        with open('base_files/data4.json', 'r') as f:
            data = json.load(f)
        print(data)
    except FileNotFoundError:
        print('该文件不存在！！！')


if __name__ == '__main__':
    # my_dic_to_json()
    # my_json_to_data()
    # my_write_json()
    my_read_json()
