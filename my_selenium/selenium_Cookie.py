# coding=utf-8
# author:luhu
"""
        有时我们需要验证浏览器中是否存在某个cookie，因为基于真实的cookie的测试是
    无法通过白盒和集成测试完成的。webdriver提供了操作cookie的相关方法可以读取、添
    加和删除cookie信息。
        WebDriver操作cookie的方法有：
            get_cookies()               获得所有cookie信息
            get_cookie(name)            返回有特定name值得cookie信息
            add_cookie(cookie_dict)     添加cookie，必须有name和value值
            delete_cookie(name)         删除特定（部分）的cookie信息
            delete_all_cookies()        删除所有cookie信息
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.add_cookie({'name': 'key-012334556', 'value': 'value-908765446'})   # 手动添加cookie
cookies1 = driver.get_cookies()
print(cookies1)  # 通过打印信息可以看出cookie是以字典的形式进行存放的。
for cookie in cookies1:
    print('%s --> %s' % (cookie['name'], cookie['value']))  # 可以看到手工添加cookie成功
driver.delete_cookie('key-012334556')
driver.delete_all_cookies()     # 删除浏览器中所有的cookie信息
cookies2 = driver.get_cookies()
if cookies2:
    for cookie in cookies2:
        print('%s --> %s' % (cookie['name'], cookie['value']))  # 可以看到手工删除cookie成功
else:
    print('没有cookie！！！')
driver.close()


























