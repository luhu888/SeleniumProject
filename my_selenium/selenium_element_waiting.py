# coding=utf-8
# author:luhu
"""
        如今大多数的web应用程序使用ajax技术，当浏览器在加载页面时，页面的元素可能并不是同时被加载完全的，
    这给元素定位添加了困难，如果因为在加载某个元素时延时而造成ElementNotVisisibleException的情况出现，那
    么就会降低自动化脚本的稳定性。
       WebDriver提供了两种类型的等待：显式等待和隐式等待。
       显式等待是WebDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常(TimeoutException)
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://wwww.baidu.com')
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
element.send_keys('my_selenium')
sleep(2)
driver.close()