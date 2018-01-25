# -*- coding: utf-8 -*-
# __author__=luhu
"""
    控制浏览器的前进后退
    back()
    forward()
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# 访问百度首页
first_url = 'https://www.baidu.com'
print('现在在 %s' % first_url)
driver.get(first_url)
sleep(5)

# 访问新闻页面
second_url = 'https://news.baidu.com'
print('现在在 %s' % second_url)
driver.get(second_url)
sleep(5)

# 返回（后退）到百度首页
print('后退到 %s' % first_url)
driver.back()
sleep(5)

# 前进到新闻页
print('前进到 %s' % second_url)
driver.forward()
sleep(5)
driver.quit()

