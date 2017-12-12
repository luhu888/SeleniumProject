# -*- coding: utf-8 -*-
# __author__=luhu.txt
"""
  python是如何找到模块的，即python在执行import语句时，到底进行了哪些操作：
      1.创建一个新的，空的module对象（他可能包含多个module）
      2.把这个module对象插入sys.module中
      3.装载module的代码（如果需要，首先必须编译）
      4.执行新的module中对应的代码
      在执行第3步时，首先要找到module程序所在的位置，搜索的顺序是：
      当前路径（以及从当前目录指定的sys.path），然后是PythonPATh，然后是Python的安装设置相关的
  的默认路径。正因为存在这样的顺序，如果当前路径或PythonPATH中存在与标准module同样的module，则会覆盖
  标准module。也就是说，如果当前目录下存在xml.py，那么执行import xml时，导入的是当前目录下的module，
  而不是系统标准的xml。
      了解了这些，我们就可以先构建一个package，以普通module的方式导入，就可以直接访问次package中的
  各个module了，Python中的package必须包含一个__init.py__文件，用来导入需要使用的文件。
"""
import sys   # 跨目录模块的调用，需在跨目录的模块文件夹中新增一个__init__.py文件，导入你的py文件名
sys.path.append('\package')
from package import my_add
print my_add.my_add(4, 5)

