# -*- coding: utf-8 -*-
# __author__=luhu
import time

files = file('luhu.txt', 'r')
strs = files.readlines()

try:
    for i in strs:
        print i
        time.sleep(1)
finally:    # 无论是否出现 异常，都会被执行的语句
    files.close()
    print '清理。。。关闭文件'