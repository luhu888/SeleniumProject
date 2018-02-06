# -*- coding: utf-8 -*-
# __author__=luhu
"""
        数据驱动化难免要读取文件，如.txt .xlsx  .csv  .xml 等等，下面先学习下如何
    读取txt文件。
        read()          读取整个文件
        readline()      读取一行数据
        readlines()     读取所有行的数据
"""
import csv
import xml.dom.minidom
from time import sleep

import xlrd
from selenium import webdriver

file_info = open('base_files/luhu.txt', 'r')
values = file_info.readlines()
file_info.close()


def my_search():
    for search in values:
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(search)
        driver.find_element_by_id('su').click()
        sleep(4)
        driver.quit()


"""
        实现一行读取用户名和密码：使用split()方法进行拆分，以逗号作为分割点，拆分为
    两半，用[0]获取左半边的字符串，[1]获取右半边的字符串。
"""


def login_txt():
    for info in values:
        driver = webdriver.Chrome()
        driver.get('http://www.jstjjg.com/manage/')
        username = info.split(',')[0]    # 如果登录页可以响应回车键登录，这不用定位登录按钮
        password = info.split(',')[1]    # 因为txt换行会有个回车符
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('btn_login').click()
        sleep(4)
        driver.quit()
        # txt = info.split(',')
        # print txt
        # print txt[1]
        # print txt[2]
        # print txt[0]


"""
        如果现在需要读取一组信息，这一组数据包括，用户名，密码，邮箱，年龄，性别等，
    这个时候虽然也可以使用split()方法拆分，但文件的可读性太差，这是我们可以读取excel表。
"""


def read_csv():
    my_file = 'base_files/test_csv.csv'
    date = csv.reader(open(my_file, 'rb'))
    for user in date:    # 读取到的每一行是一个数组，循环遍历每一行的数组
        print(user[0])
        print(user[1])
        for element in user:   # 循环遍历每一行数组中的元素
            print(element)


"""
        读取xlsx的方法相似
"""


def read_xlsx():
    data = xlrd.open_workbook('base_files/test_info.xlsx')
    table = data.sheets()[0]   # 该表的第1个页签
    nrows = table.nrows   # 获取表的行数
    # print nrows
    for i in range(2, nrows):
        # print table.cell_value(0, 0)   # 第1行，第一列
        username = table.cell_value(i, 0)
        age = table.cell_value(i, 1)
        email = table.cell_value(i, 2)
        tel = table.cell_value(i, 3)
        print(username, int(age), email, int(tel))  # 没有强转成int类型，获得的数据会是小数


"""
        当我们所需要读取的文件并没有固定的行和列，而是一些不规则的配置信息，例如我们
    需要一个配置文件来配置当前自动化测试脚本的url，浏览器，登录用户名/密码等，这个时候
    我们可以选择xml来配置这些信息。
        xml即可扩展标记语言，他可以用来标记数据，定义数据类型，是一种允许用户对自己的
    标记语言进行定义的源语言。
        xml有如下特征：
            他是标签对组成的：<aa></aa>
            标签可以有属性：<aa id= '123'></aa>
            标签可以嵌入数据：<aa>abc</aa>
            标签可以嵌入子标签（具有层级关系）：
                <aa>
                    <bb></bb>
                </aa>
        getElementByTagName()可以通过标签名获取某个标签，他所获取的对象是以数组形式存放。
    如‘caption’和‘item’标签在test_info.xml文件中有多个，那么可以指定数组的下标获取
    某个指定标签：
            tagname[0]表示一组标签的第1个
            tagname[2]表示一组标签的第2个
        getAttribute()方法可以获取元素的属性所对应的值;
        firstChild.data,firstChild属性返回被选节点的第一个子节点，data表示获取该节点的数据。
"""


def read_xml():
    dom = xml.dom.minidom.parse('base_files/test_info.xml')    # 打开xml文档
    root = dom.documentElement
    tagname = root.getElementsByTagName('maxid')    # 获取名称为'maxid'标签组
    print(tagname[0].tagName)  # 获取该标签组的第一个标签名称
    items = root.getElementsByTagName('item')    # 获取标签组名称
    id_value = items[0].getAttribute("id")           # 获取该标签组中第一个标签id属性对应的值
    print(id_value)
    captions = root.getElementsByTagName('caption')    # 获取名称为captions的标签组
    print(captions[0].firstChild.data)  # 获取该标签组中第一个节点对应的数据
    print(captions[2].firstChild.data)  # 获取该标签组中第三个节点对应的数据


if __name__ == '__main__':
    # my_search()
    # login_txt()
    # read_csv()
    # read_xlsx()
    read_xml()






