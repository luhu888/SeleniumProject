# -*- coding: utf-8 -*-
# __author__=luhu
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('seleniumm')

sleep(2)
# 删除多输入的m
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
"""
    send_keys(Keys.BACKSPACE)                       删除键
    send_keys(KEYS,SPACE)                           空格键    
    send_keys(KEYS,TAB)                             制表键
    send_keys(KEYS,ESCAPE)                          回退键      
    send_keys(KEYS,ENTER)                           回车键
    send_keys(KEYS.CONTROL,'a')                     全选
    send_keys(KEYS.CONTROL,'c')                     复制
    send_keys(KEYS.CONTROL,'v')                     粘贴
    send_keys(KEYS.CONTROL,'x')                     剪切
    send_keys(KEYS.F1)                              F1键
    ...                                             ...
    send_keys(KEYS.F12)                             F12键
    
"""
# 按下Ctrl+A,Ctrl+V,其他同理
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
sleep(2)
driver.close()










