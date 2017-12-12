# -*- coding: utf-8 -*-
# __author__=luhu.txt
"""
    那么问题来了，我们一个操作会抛出什么类型的错误呢？
    异常的抛出机制：
        1.如果在运行时发生异常，解释器会查找相应的处理语句（称为handler）；
        2.要是在当前函数里没有找到的话，他就会将异常传递给上层的调用函数，看看那里能不能处理；
        3.如果在最外层（全局“main”）还是没有找到的话，解释器就会退出，同时打印traceback以便让用户找到错
        误产生的原因；
        注意：虽然大多数错误会导致异常，但一个异常不一定代表错误，有时他们只是一个警告，有时他们可能
        是一个终止信号，比如退出循环等。（在Python中所有的异常都继承于Exception，我们可以用它来接收所有的异常，但在
        Python2.5版本之后，所有的异常有了新的基类BaseException，Exception同样继承BaseException，所以我们
        也可以使用BaseException来接收所有的异常。）
    常见异常：
                    异常                       描述
                BaseException            新的所有异常类的基类
                Exception                所有的异常类的基类，但继承BaseException类
                AssertionError           assert断言语句失败
                AttributeError           试图访问一个对象没有属性
                IOError                  输入输出异常，试图打开一个不存在的文件（包括其他情况）时引进的错误
                NameError                使用一个还未赋值对象的变量
                IndexError               在使用序列中不存在的索引引发的错误
                IndentationError         语法错误，代码没有正确的对齐
                KeyboardInterrupt        Ctrl+C被按下，程序被强行终止
                TypeError                传入的对象类型与要求不符
                SyntaxError              Python代码逻辑语法出错，不能执行
"""
try:
    open('luhu.txt.txt', 'r')
except IOError:    # 捕捉异常
    print '出异常了！！！'


try:      # 更多的异常用法，与else结合使用
    test = '异常测试！！！'
    print test
except Exception, msg:
    print msg     # 打印报错信息
else:
    print '没有异常！！！'























