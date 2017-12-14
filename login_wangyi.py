# -*- coding: utf-8 -*-
# __author__=luhu
"""
        模块化实例
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.jstjjg.com/manage/')
driver.implicitly_wait(10)


def login():
    driver.find_element_by_name('username').send_keys('portal')
    driver.find_element_by_name('password').send_keys('portal123')
    driver.find_element_by_id('btn_login').click()


def logout():
    element = driver.find_element_by_class_name('layui-circle')
    ActionChains(driver).move_to_element(element).perform()
    driver.find_element_by_link_text('退出').click()
    sleep(3)

    driver.close()


login()
sleep(3)
logout()