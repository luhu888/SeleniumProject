# -*- coding: utf-8 -*-
# __author__=luhu
"""
        前面说的是web端元素的定位，定位只是第一步，定位之后还需要对这个元素进行操作，
    点击，输入，提交等等；所以在webdriver中，大多简单的页面交互都是通过webdriver
    接口提供的，最常用的是以下几个：
        clear()                 清除文本，如果是一个文件输入框
        send_keys(*value)       在元素上模拟按键输入
        click()                 单击元素
        submit()                用于提交表单，特别用于没有提交按钮的情况，如回车操作
        size                    返回元素的尺寸
        text                    返回元素的文本
        get_attribute（name）   获得属性值
        is_displayed()          设置该元素是否用户可见
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()

# 获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print size

# 返回百度首页的备案信息
text = driver.find_element_by_id('cp').text
print text

# 返回元素的属性对应的值，可以是id，name，type或元素拥有的其他任意属性
my_attribute = driver.find_element_by_id('kw').get_attribute('name')
print my_attribute

# 返回元素的结果是否可见
result = driver.find_element_by_id('kw').is_displayed()
print result

sleep(5)

driver.quit()














