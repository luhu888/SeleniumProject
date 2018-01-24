# -*- coding: utf-8 -*-
# __author__=luhu
import unittest

from pip._vendor.distlib.compat import raw_input

from my_package.count import Count  # 从本地count.py文件中导入Count类

"""
        unittest的概念：test fixture,test suite,test case,test runner.
            test case
        一个TestCase 的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试
    前准备环境的搭建(setUp)，实现测试过程的代码(run)，以及测试后环境的还原(tearDown)。单元测试(unit
    test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个
    功能进行验证。
            test suite
        对一个功能的验证往往是需要多个测试用例的，可以把多个测试用例集合在一起执行，这就产生了测试
    套件TestSuite 的概念，它用来组装单个测试用例，而且TestSuite 也可以嵌套TestSuite。
    可以通过addTest 加载TestCase 到TestSuite 中，再返回一个TestSuite 实例。
            test runner
        TextTestRunner 是来执行测试用例的，其中的run(test)用来执行TestSuite/TestCase。测试的结果
    会保存到TextTestResult 实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
            test fixture
        对一个测试用例环境的搭建和销毁，是一个fixture，通过覆盖TestCase 的setUp()和tearDown()
    方法来实现。这个有什么用呢？比如说在这个测试用例中需要访问数据库，那么可以在setUp()中建立数
    据库连接以及进行一些初始化，在tearDown()中清除在数据库中产生的数据，然后关闭连接。注意tearDown
    的过程很重要，要为以后的TestCase 留下一个干净的环境。
"""


class TestCount(unittest.TestCase):    # 让所有执行测试的类都继承于TestCase类
    def setUp(self):     # 在setUp()方法中进行测试前的初始化工作
        print('加法测试开始')
        self.j = Count(2, 3)

    def test_add(self):
        self.add = self.j.add()
        self.assertEqual(self.add, 5)   # 断言，对Count类中add()方法返回值与预期值比较
        print('加法测试中。。。。')

    def tearDown(self):  # 在tearDown()方法中执行测试后的清除工作，没有可清理的工作就传一个pass
        print('加法测试结束')


"""
        在setUp()方法中要求用户输入一个数，在test_equal()中通过assertEqual()比较输入的数是否与
    10 的相等，如果不相等则输出msg 中定义的提示信息。
"""


class TestEqual(unittest.TestCase):
    def setUp(self):
        print('相等测试开始，请输入一个数字：')
        number = raw_input()
        self.number = number

    def test_equal(self):
        print('相等测试中。。。')
        self.assertEqual(self.number, 10, msg='你输入的是%s,不是10！！！' % self.number)

    def tearDown(self):
        print('相等测试结束！！！')


"""
        首先调用unittest 所提供的TestSuite()类，通过它下面的addTtest()方法来添加TestCount 类下面的
    test_add 测试方法。接着调用TextTestRunner()类，通过它下面的run()方法来运行suite 所组装的测试用
    例，执行结果如下。
"""
if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_add'))
    suite.addTest(TestEqual('test_equal'))

    # 执行测试集
    runner = unittest.TextTestRunner()
    runner.run(suite)




























