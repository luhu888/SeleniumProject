# -*- coding: utf-8 -*-
# __author__=luhu
"""
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
"""


def my_raise():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def my_error():     # 通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承
    try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
    finally:    # 定义清理行为，try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为
        print('无论是否有异常，我都执行！！！')


"""
    预定义的清理行为
    一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
    这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上
    关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
    下面这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭
"""


def my_predefine():   # predefine 预定义
    # for line in open("myfile.txt"):
    #     print(line, end="")
    # 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭

    with open("tmp/runoob.txt") as f:
        for line in f:
            print(line, end="")


if __name__ == '__main__':
    # my_raise()
    # my_error()
    my_predefine()


















































































































































