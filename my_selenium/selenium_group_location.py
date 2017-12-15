# -*- coding: utf-8 -*-
# __author__=luhu
"""
        实际情况中除了定位单个元素外，可能还有定位一组元素，webdriver也提供了定位一组
    元素的方法,就是element的后面加上s：
        find_elements_by_id()
        find_elements_by_name()
        find_elements_by_class_name()
        find_elements_by_tag_name()
        find_elements_by_link_text()
        find_elements_by_partial_link_text()
        find_elements_by_xpath()
        find_elements_by_css_selector()
        定位一组对象一般用于以下场景:
            批量操作对象，比如将页面上所有的复选框都被勾选；
            先获取一组对象，再在这组对象中过滤出具体定位的一些对象，比如定位出页面上所有的
            CheckBox，然后选择最后一个。
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://192.168.1.102/test_dreamgo/app/#/homepage')
driver.find_element_by_name('user').send_keys('15856691310')
driver.find_element_by_name('password').send_keys('luhu199515lbh', Keys.ENTER)
sleep(2)
driver.find_element_by_xpath('//*[@id="homePage"]/div[1]/div[2]/div[4]/div').click()
inputs = driver.find_elements_by_xpath('//div')
driver.find_elements_by_xpath('//div').pop().click()   # pop()函数用于获取列表中的一个元素
print len(inputs)                                      # (默认为最后一个元素)，pop(2)默认获取一组中的第三个
for i in inputs:
    i.click()
    print len(i)
sleep(6)
driver.close()