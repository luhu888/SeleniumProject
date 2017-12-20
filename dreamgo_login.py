# -*- coding: utf-8 -*-
# __author__=luhu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://192.168.1.102/test_dreamgo/app/#/homepage')
driver.implicitly_wait(10)
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("15856691310")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("luhu199515lbh", Keys.ENTER)
# ERROR: Caught exception [Error: Dom locators are not implemented yet!]
print driver.find_element_by_css_selector("#homePage > div.topmenu > div.topmenu-badge > ul > li.pull-left.user_name").text