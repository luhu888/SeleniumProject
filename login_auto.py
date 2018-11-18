# -*- coding: utf-8 -*-
# __author__=luhu
"""
        模块化实例
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

"""
        创建表Account类，对用户名密码进行初始化设置，紧接着创建login_as()函数用于实现用户的
    登录操作，他需要一个user_info参数用于接收用户的登录信息，取user_name中的username输入到用户名
    输入框中，取user_info中的password输入密码输入框。
        紧接着通过调用Account实例化用户admin，进行个性化的参数设置，最后调用login_as()函数来
    实现用户的登录。  
        创建Account类，继承object类，2.x 里 object 是一个较新基类，在3.x里object已经做为所有
    东西的基类。
        继承 object 类的是新式类，不继承 object 类的是经典类，在 Python 2.7 里面新式类和经典类
    在多继承方面会有差异，新式类对多继承的处理更为合乎逻辑。
        调用这个方法的时候不必为这个参数self赋值，还将这个参数显示出来的原因：
        self在Python里不是关键字。self代表当前对象的地址。self能避免非限定调用造成的全局变量。
    恶忌阴，善忌阳。故恶之显者祸浅，而隐者祸深；善之显者功小，而隐者功大，是善事，隐胜于明；
    是恶事，显胜于隐。就是显示出来方便沟通。
"""


class Account(object):      # 在Python3.x中可以不继承object类，在3.x里object已经做为所有东西的基类
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password


def login_as(user_info):
    driver.find_element_by_name('username').send_keys(user_info.username)
    driver.find_element_by_name('password').send_keys(user_info.password)
    driver.find_element_by_id('btn_login').click()


def logout():
    element = driver.find_element_by_class_name('layui-circle')
    ActionChains(driver).move_to_element(element).perform()
    driver.find_element_by_link_text('退出').click()
    sleep(3)

    driver.close()


admin = Account(username='3334', password='123456')
login_as(admin)
sleep(3)
logout()