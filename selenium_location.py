# -*- coding: utf-8 -*-
# __author__=luhu
"""
    selenium的webdriver提供了八种元素定位方法：
        id
        name
        class name
        link text    超链接文字定位（链接对应在前端界面的文字）
        partial link text   是对link定位的一个补充，有些文本链接会比较长，这个时候就可以去文本链接的部分文字
        定位，只要这一部分信息可以唯一标识这个链接即可。
        xpath
        css selector
    在Python语言中对应的定位方法如下：
        find_element_by_id()
        find_element_by_name()
        find_element_by_class_name()
        find_element_by_tag_name()
        find_element_by_link_text('地图')
        find_element_by_partial_link_text('一个很长的')       '文本链接：一个很长的文本链接'
        find_element_by_xpath()
        find_element_by_css_selector()
"""
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    print '设置浏览器宽高为480,800'
    # driver.maximize_window()
    driver.set_window_size(480, 800)  # 默认全屏执行可以使用maximize_window()方法，或使用set_window_size()方法不传值
    driver.find_element_by_id('kw').send_keys("selenium")
    driver.find_element_by_id('su').click()
# except ElementNotVisibleException:
#     print '抛出异常！！！'
finally:
    sleep(4)
    driver.close()












