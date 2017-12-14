# -*- coding: utf-8 -*-
# __author__=luhu
"""
        自动化脚本是交给工具去执行，有时候打印的错误信息并不十分明确，如果在脚本执行出错的时候
    将当前窗口截图保存，那么通过图片信息会更直观帮助我们找到出错原因，webdriver提供了截图函数
    get_screenshot_as_file()来截取当前窗口。
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
try:
    driver.find_element_by_id('kw_error').send_keys('selenium')
    driver.find_element_by_id('su').click()
except:
    driver.get_screenshot_as_file('picture/error.jpg')   # 报存到该脚本同级目录对应的picture文件夹中
    driver.close()    # close()方法用于关闭一个窗口，quit()用于关闭所有窗口