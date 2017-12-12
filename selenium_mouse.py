# -*- coding: utf-8 -*-
# __author__=luhu
"""
    在webdriver中这些关于鼠标操作的方法由ActionChains类提供；
    ActionChains类提供的鼠标操作的常用方法：
        perform()                                  执行所有ActionChain中存储的行为
        context_click(element)                     右击，element为定位到的元素
        double_click(element)                      双击
        drag_and_drop(element)                     拖动
        move_to_element(element)                   鼠标悬停
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://pan.baidu.com/')    # 登录百度云盘
driver.find_element_by_class_name('account-title').click()
driver.find_element_by_name('userName').send_keys('15856691310')
driver.find_element_by_name('password').send_keys('luhu199515lbh')
driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
sleep(2)
driver.find_element_by_class_name('tip-button').click()

# 定位到要右击的元素
right_click = driver.find_element_by_partial_link_text('装机软件')

# 对定位到的元素进行右击操作
ActionChains(driver).context_click(right_click).perform()
driver.find_element_by_link_text('装机必备').click()

# 鼠标悬停事件,其他方法通用
element = driver.find_element_by_class_name('DIcOFyb')
ActionChains(driver).move_to_element(element).perform()  # 注意鼠标悬浮后该组件的classname会变

# 鼠标拖放操作，drag_and_drop(source,target)在源元素上按下鼠标左键，然后移动到目标元素上释放
target = driver.find_element_by_class_name('dfdsa')
ActionChains(driver).drag_and_drop(element, target).perform()
sleep(3)
driver.close()






