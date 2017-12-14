# coding=utf-8
# author:luhu
"""
        WebDriver除了不能操作本地Windows控件，对于浏览器上的控件也不是都可以操控的。比如
    浏览器上的滚动条，虽然WebDriver提供操作浏览器的前进和后退按钮，但对于滚动条并没有提供
    相应的办法。那么在这种情况下就可以借助JavaScript方法来控制浏览器滚动条。WebDriver提供
    了execute_script()方法来执行Javascript代码，一般用到操作滚动条的两个场景：
            注册时的法律条文的阅读，判断用户是否阅读完成的标准是：滚动条是否拉到最下方；
            要操作的页面元素不在视觉范围内，无法进行操作，需要拖动滚动条。
        当然，JavaScript的作用不止于此，他同样可操作页面上的元素，让这个元素隐藏，学习
    JavaScript可以让这些web页面元素操作变得游刃有余。
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(4)    # 睡4秒，等拖动条出现后再下拉到底部
js = 'var q=document.documentElement.scrollTop=10000'     # 距顶端的值为10000个像素，即为下拉操作
driver.execute_script(js)
sleep(3)
js2 = 'var q=document.documentElement.scrollTop=0'    # 距顶端距离为0个像素，即拖动到顶部
driver.execute_script(js2)
sleep(3)
driver.close()
