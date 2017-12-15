# -*- coding: utf-8 -*-
# __author__=luhu
"""
        有时候需要在不同的窗口切换，从而操作不同窗口中的元素，webDriver
    提供了switch_to.window()(switch_to_window()已过时)：
        current_window_handle         获得当前窗口句柄
        window_handles                返回所有窗口的句柄到当前会话
        switch_to.window()            用于切换到相应的窗口
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(5)   # 注册界面不会立即打开，不设置等待会抛异常
search_windows = driver.current_window_handle    # 获得当前窗口句柄
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
all_handles = driver .window_handles   # 获取当前所有打开的窗口句柄，实际就两个
for handle in all_handles:
    if handle != search_windows:  # 如果当前界面不是百度首页
        driver.switch_to.window(handle)  # 就跳转到另一个界面，就是注册界面
        print '现在在注册界面！！！'
        driver.find_element_by_name('userName').send_keys(u'自动输入用户名')  # 对中文进行Unicode编码
        driver.find_element_by_name('phone').send_keys('15856691310')
        driver.switch_to.window(search_windows)
        print '回到百度首页！！！'
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        driver.find_element_by_id('kw').send_keys('my_selenium')
        driver.find_element_by_id('su').click()
        sleep(3)
driver.quit()





















