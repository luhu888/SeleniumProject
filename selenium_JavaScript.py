# coding=utf-8
# author:luhu
"""
        WebDriver除了不能操作本地Windows控件，对于浏览器上的控件也不是都可以操控的。比如
    浏览器上的滚动条，虽然WebDriver提供操作浏览器的前进和后退按钮，但对于滚动条并没有提供
    相应的办法。那么在这种情况下就可以借助JavaScript方法来控制浏览器滚动条。WebDriver提供
    了execute_script()方法来执行Javascript代码，一般用到操作滚动条的两个场景：
        注册时的法律条文的阅读，判断用户是否阅读完成的标准是：滚动条是否拉到最下方；
        要操作的页面元素不在视觉范围内，无法进行操作，需要拖动滚动条。
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
sleep(3)
js2 = 'var q=document.documentElement.scrollTop=0'
driver.execute_script(js2)
sleep(3)
driver.close()