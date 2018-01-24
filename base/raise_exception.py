# -*- coding: utf-8 -*-
# __author__=luhu
"""
        抛出异常，对于print方法来说只能打印错误信息，Python中提供raise方法来抛出异常。其实用户输入什么
    样的信息与NameError之间没有什么关系，但我们可以使用raise自定义一些异常信息，这看上去比print更专业，
    需要注意的是raise只能使用Python中所提供的异常类，自定义的异常类不起作用。
"""
from pip._vendor.distlib.compat import raw_input

filename = raw_input('please input file name:')
if filename == 'hello':
    raise NameError('input file name error!')
