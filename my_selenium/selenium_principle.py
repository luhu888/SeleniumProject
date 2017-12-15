# -*- coding: utf-8 -*-
# __author__=luhu
"""
        WebDriver是按照server-client的经典设计模式设计的。
        server端就是remote server，可以是任意的浏览器。当我们的脚本启动浏览器后，该浏览器就是remote
    server，他的职责就是等待client发送请求并作出相应响应。
        client端简单说就是我们的测试代码，我们测试代码中的一些行为，比如打开浏览器，跳转到特定的
    url等操作是以http请求的方式发送给被测试服务器，也就是remote server：remote server接受请求，并执行
    相应操作，并在response中返回执行状态、返回值等信息。
        WebDriver的工作流程：
            1.WebDriver启动目标浏览器，并绑定到指定端口，该启动的浏览器实例作为WebDriver的remote server；
            2.Client端通过CommandExcuter发送HTTPRequest给remote server的监听端口（通信协议：the webdriver wire protocol）；
            3.Remote server需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe），来转化浏览器的native调用。
        在python提供了logging模块，logging模块给运行中的应用提供了一个标准的信息输出接口。他提供了basicConfig（）
        方法用于基本信息的定义。将debug模块开启，就可以捕捉到客户端与服务端的交互信息了。
"""
import logging

from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('my_selenium')
driver.find_element_by_id('su').click()
driver.close()















