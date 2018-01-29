# -*- coding: utf-8 -*-
# __author__=luhu
import sys       # 这样做并没有把直接定义在sys中的函数名称写入到当前符号表里，只是把模块sys的名字写到了那里。可以使用模块名称来访问函数
from base import fibonacci_serie   # Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
# from modname import *        # 把一个模块的所有内容全都导入到当前的命名空间也是可行的，这种声明不该被过多地使用

"""
    一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性
    来使该程序块仅在该模块自身运行时执行。每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
"""


if __name__ == '__main__':
    fib = fibonacci_serie.__name__
    sys_path = sys.path
    dir_name = dir(fibonacci_serie)
    # fibonacci_serie.fibonacci_series()
    print(fib)      # 查看模块中的方法名
    """
        sys.path 输出是一个列表，其中第一项是空串''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），
        亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。
        因此若像我一样在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。
        了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。
    """
    print(sys_path)
    print(dir_name)
    sys.ps1 = '...'
    print(sys.ps1)





































