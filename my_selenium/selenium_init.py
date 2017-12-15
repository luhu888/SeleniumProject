# coding=utf-8
# author:luhu
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()     # 载入google驱动，使用google浏览器打开
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium2')
driver.find_element_by_id('su').click()
sleep(5)
driver.quit()