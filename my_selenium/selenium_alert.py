# -*- coding: utf-8 -*-
# __author__=luhu
"""
        在webdriver中有时也要处理JavaScript所生成的alert、confirm以及prompt，就是使用
    switch_to_alert()方法定位到alert/confirm/prompt,然后使用text/accept/dismiss/send_keys
    按需求进行操作：
        text        返回alert/confirm/prompt中的文字信息；
        accept      点击确认按钮
        dismiss     点击取消按钮，如果有的话
        send_keys   输入值，这个alert\confirm没有对话框就不能用了，不然会报错
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://baidu.com')
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_class_name('setpref').click()
sleep(3)
driver.find_element_by_class_name('prefpanelgo').click()
driver.switch_to_alert().accept()
driver.close()
























