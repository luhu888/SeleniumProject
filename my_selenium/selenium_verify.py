# -*- coding: utf-8 -*-
# __author__=luhu
"""
        验证码的处理也是一个头疼的问题，webdriver并没有提供相应的方法来处理验证码，这里有几种
    常用处理验证码的方法：
            1.测试版本去掉验证码（风险较大）；
            2.设置万能码，与开发沟通设置一个万能码，只要输入这个验证码就能通过验证；
            3.验证码识别技术，正确率并不是百分百，较为复杂，以后说；
            4.记录cookie，通过向浏览器中添加cookie可以绕过登录的验证码，当你访问网站时，如果有
        记住密码的功能就是这个原理，他将用户的账号密码报保存在cookie中或者将验证登录状态的token
        之类的令牌保存在本地cookie中，再次访问服务器会直接读取浏览器cookie登录。
"""
import os
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("http://www.jstjjg.com/manage/")
# driver.find_element_by_name('username').send_keys('portal')
# driver.find_element_by_name('password').send_keys('portal123')
# driver.find_element_by_id('btn_login').click()
# login_cookie = driver.get_cookies()
# fp = open('login_cookie.txt', 'w')
# fp.write(login_cookie)
# fp.close()

profile_dir = "C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
chrome_options = webdriver.ChromeOptions()    # 使用带cookie的浏览器，可跳过登录界面
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.jstjjg.com/manage/')    # 注意要关闭Google浏览器才行，要不然会打开一个标签页，会有冲突

# '''对应火狐的写法'''
# fp = webdriver.FirefoxProfile(r'C:\Users\yan\AppData\Roaming\Mozilla\Firefox\Profiles\btnc8mzb.default')
# browser = webdriver.Firefox(fp)
# browser.get("http://www.baidu.com")
driver.close()