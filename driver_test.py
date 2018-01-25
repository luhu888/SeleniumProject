# -*- coding: utf-8 -*-
# __author__=luhu
import unittest
import my_test_case


def create_suite1():      # 构造自定义测试用例集1,定义test_case文件夹中所有以test开头的用例为测试用例集
    test_unit = unittest.TestSuite()
    test_dir = 'my_test_case'

    """
        start_dir ：要测试的模块名或测试用例目录。
        pattern='test*.py' ：表示用例文件名的匹配原则。星号“*”表示任意多个字符。
        top_level_dir=None：测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是放在多级目录
    中），默认为None。
        当测试用例多时，我们难免要将用例划分在不同层级的文件夹中，但这样discover()方法就不能同时读取
    到不同层级的测试用例，如果想被discover()读取执行非常简单，在目录下添加__init__.py 文件。
    """
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
            print(test_unit)
    return test_unit


if __name__ == '__main__':
    suite = create_suite1()
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # 手动单条添加测试用例集,可以添加来自不同目录层级的测试用例
    suite2 = unittest.TestSuite()

    # 添加my_test_case文件夹中test_selenium_unittest.py文件中MyTest类中的test_baidu测试用例
    test_case1 = my_test_case.test_selenium_unittest.MyTest('test_baidu')
    suite2.addTest(test_case1)

    runner2 = unittest.TextTestRunner()
    runner2.run(suite2)

"""
    单元测试也可以输出简单的测试报告，如下步骤：
        首先打开Windows 命令提示符，进入到.../test_project/目录下执行名命令：
            >Python all_test.py >> report/log.txt 2>&1
        Python all_test.py 通过Python 执行all_test 文件
        >>report/log.txt 将测试输出写入到report 目录下的log.txt 文件中
        file 2>&1 标准输出被重定向到文件file，然后错误输出也重定向到和标准输出一样，所以错误
    输出也写入文件file。
"""