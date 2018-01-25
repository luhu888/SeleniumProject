# -*- coding: utf-8 -*-
# __author__=luhu
"""
        web应用中经常会遇到frame嵌套页面的，webDriver每次只能在一个页面上识别元素，对于frame嵌套内的页面元素，
    直接定位是定位不到的，这个时候就要使用switch_to.frame()方法(switch_to_frame()已过时)将当前定位的主体切换
    到frame里。
        switch_to.frame(id(name)='')默认可以直接取表单的id或name属性进行切换,如果没有id或name属性，可以通过xpath
    先定位frame框架，如下面的例子，switch_to.frame()中传入的是frame框架的定位。
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
iframe = driver.find_element_by_xpath('//*[@class="iframe-box ng-scope"]')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@id="searchDiv"]/div[2]/button').click()
# inputs = driver.find_elements_by_css_selector('//*/div/div/div')
# print(len(inputs))                 # 完成在当前表单的操作后，通过该方法返回到上一层表单，该方法不用指定某个表单
driver.switch_to.default_content()  # 的返回，默认对应与他最近的switch_to_frame()方法







































