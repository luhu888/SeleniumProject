# -*- coding: utf-8 -*-
# __author__=luhu
import unittest

import time
from selenium import webdriver


class MyTest2(unittest.TestCase):
    def setUp(self):
        print '二级目录测试开始'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = 'https://www.baidu.com'

    def test_baidu2(self):
        print '测试中.....'
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(1)
        title = driver.title
        print title
        self.assertEqual(title, 'selenium_百度搜索')

    def tearDown(self):
        self.driver.quit()
        print '二级目录下测试结束'


if __name__ == '__main__':
    unittest.main()